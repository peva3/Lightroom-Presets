#!/usr/bin/env python3
"""Generate 65 film variant + video format XMP presets from existing parent presets."""

import os, re, uuid, copy, random
random.seed(42)

# ── XML namespaces ──────────────────────────────────────────────────
NS = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'crs': 'http://ns.adobe.com/camera-raw-settings/1.0/',
}
CINEMATIC_CURVE = ["0, 20", "64, 55", "128, 128", "192, 196", "255, 235"]
SLIDE_CURVE = ["0, 0", "42, 28", "128, 128", "213, 230", "255, 255"]
NEUTRAL_CURVE = ["0, 0", "255, 255"]

def parse_xmp(path):
    """Parse an XMP file and return (desc_attrs, child_elements_as_strings)."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    # Extract all crs: prefixed attributes from the rdf:Description line
    desc_match = re.search(r'<rdf:Description\s+([^>]+)>', raw)
    attrs = {}
    if desc_match:
        attr_str = desc_match.group(1)
        for m in re.finditer(r'crs:(\w+)="([^"]*)"', attr_str):
            attrs[m.group(1)] = m.group(2)
    
    # Extract inner XML (Name, Group, Look, ToneCurves)
    inner = re.search(r'(<crs:Name>.*?)(</rdf:Description>)', raw, re.DOTALL)
    inner_xml = inner.group(1) if inner else ""
    
    return attrs, inner_xml, raw

def build_xmp(attrs, inner_xml, group, curve_points):
    """Build a complete XMP file string from attributes and inner XML."""
    # Build new UUID
    new_uuid = str(uuid.uuid4()).replace('-', '').upper()[:32]
    while len(new_uuid) < 32:
        new_uuid += "0"
    attrs["UUID"] = new_uuid
    
    # Build attribute string
    attr_parts = []
    for k, v in attrs.items():
        attr_parts.append(f'crs:{k}="{v}"')
    
    # Ensure mandatory attrs
    mandatory = {
        "PresetType": "Normal",
        "Cluster": "",
        "SupportsAmount": "True",
        "SupportsColor": "True",
        "SupportsMonochrome": "True",
        "SupportsHighDynamicRange": "True",
        "SupportsNormalDynamicRange": "True",
        "SupportsSceneReferred": "True",
        "SupportsOutputReferred": "True",
        "RequiresRenditionBehavior": "True",
        "HasSettings": "True",
    }
    for k, v in mandatory.items():
        if k not in attrs:
            attr_parts.insert(0, f'crs:{k}="{v}"')
    
    attr_str = " ".join(attr_parts)
    
    # Determine Look block
    treatment = attrs.get("Treatment", "Color")
    if treatment == "Monochrome":
        look_name = "Adobe Monochrome"
        look_uuid = "0C09521111114111B1115456789ABCDE"
        look_mono = "True"
    else:
        # Check if this is a Slide preset
        if "Vivid" in attrs.get("Name", "") or group == "Slide":
            look_name = "Adobe Vivid"
            look_uuid = "EA1DE074F188405965EF399C72C221D9"
        else:
            look_name = "Adobe Color"
            look_uuid = "B952C21111114111B1115456789ABCDE"
        look_mono = "False"
    
    # Update Group and Name in inner XML
    name = attrs.get("Name", "Unnamed")
    inner_updated = inner_xml
    
    # Replace existing Name element content
    inner_updated = re.sub(
        r'<rdf:li xml:lang="x-default">.*?</rdf:li>',
        f'<rdf:li xml:lang="x-default">{name}</rdf:li>',
        inner_updated,
        count=1
    )
    
    # Replace Group element content (2nd occurrence)
    inner_updated = re.sub(
        r'(<crs:Group>\s*<rdf:Alt>\s*<rdf:li xml:lang="x-default">).*?(</rdf:li>)',
        f'\\1{group}\\2',
        inner_updated
    )
    
    # Build tone curves
    curve_names = ["", "Red", "Green", "Blue"]
    curve_xml = ""
    for suffix in curve_names:
        tag = f"ToneCurvePV2012{suffix}"
        seq_items = "".join(f'<rdf:li>{pt}</rdf:li>' for pt in curve_points)
        curve_xml += f'<crs:{tag}><rdf:Seq>{seq_items}</rdf:Seq></crs:{tag}>'
    
    xmp = f'''<x:xmpmeta xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00">
 <rdf:RDF>
 
 <rdf:Description rdf:about="" {attr_str}>
 <crs:Name>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">{name}</rdf:li>
 </rdf:Alt>
 </crs:Name>
 <crs:Group>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">{group}</rdf:li>
 </rdf:Alt>
 </crs:Group>
 <crs:Look>
 
 
 <rdf:Description crs:Name="{look_name}" crs:Amount="1.000000" crs:UUID="{look_uuid}" crs:SupportsAmount="True" crs:SupportsMonochrome="{look_mono}" crs:SupportsOutputReferred="True">
 <crs:Group>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">Profiles</rdf:li>
 </rdf:Alt>
 </crs:Group>
 </rdf:Description>
 </crs:Look>
 {curve_xml}</rdf:Description>
 </rdf:RDF>
</x:xmpmeta>'''
    return xmp

def read_preset(path):
    """Read parent XMP and return parsed attrs."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    attrs = {}
    for m in re.finditer(r'crs:(\w+)="([^"]*)"', raw):
        attrs[m.group(1)] = m.group(2)
    return attrs

def safe_float(v, default=0.0):
    """Parse float safely."""
    try:
        return float(v)
    except (ValueError, TypeError):
        return default

def fmt(v):
    """Format a float to minimal decimal places."""
    if isinstance(v, (int, float)):
        if v == int(v):
            return str(int(v))
        return f"{v:.1f}" if v == round(v, 1) else f"{v:.2f}"
    return str(v)

def adjust(base_val, delta):
    """Add delta to a value (numeric string or number)."""
    v = safe_float(base_val)
    return fmt(v + delta)

def clamp_sat(v):
    """Clamp HSL sat to ±60."""
    val = safe_float(v)
    return fmt(max(-60.0, min(60.0, val)))

def sat_adjust(base_val, delta):
    """Adjust saturation with ±60 cap."""
    v = safe_float(base_val) + delta
    return fmt(max(-60.0, min(60.0, v)))

# ── Parent preset paths ──────────────────────────────────────────────
COLOR_NEG = "/app/lr-presets/Presets/Color-Negative"
BW = "/app/lr-presets/Presets/Black-White"
CREATIVE = "/app/lr-presets/Presets/Creative"
SLIDE = "/app/lr-presets/Presets/Slide"
VIDEO_DIR = "/app/lr-presets/Presets/Video"

# ── PUSHED +1 STOP ───────────────────────────────────────────────────
def make_pushed_1(parent_path, target_name):
    """+1 stop push: more contrast, bigger grain, more saturation."""
    attrs = read_preset(parent_path)
    
    # Basic panel: contrast up, shadows down, blacks down
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], +15)
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], -10)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], -10)
    if "Blacks2012" in attrs:
        new_blacks = max(-30.0, safe_float(attrs["Blacks2012"]) - 8)
        attrs["Blacks2012"] = fmt(new_blacks)
    if "Exposure2012" in attrs:
        attrs["Exposure2012"] = adjust(attrs["Exposure2012"], -0.15)
    
    # Grain: bigger, rougher, more
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], +15)
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], +8)
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], +10)
    if "GrainRoughness" in attrs:
        attrs["GrainRoughness"] = adjust(attrs["GrainRoughness"], +10)
    
    # Saturation bump
    if "Saturation" in attrs:
        attrs["Saturation"] = adjust(attrs["Saturation"], +5)
    
    # Ensure grain safety rules
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

def make_pushed_2(parent_path, target_name):
    """+2 stop push: extreme contrast, heavy grain, aggressive saturation."""
    attrs = read_preset(parent_path)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], +28)
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], -20)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], -20)
    if "Blacks2012" in attrs:
        attrs["Blacks2012"] = fmt(max(-30.0, safe_float(attrs["Blacks2012"]) - 15))
    if "Exposure2012" in attrs:
        attrs["Exposure2012"] = adjust(attrs["Exposure2012"], -0.35)
    if "Whites2012" in attrs:
        attrs["Whites2012"] = adjust(attrs["Whites2012"], +10)
    
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], +28)
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], +15)
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], +15)
    if "GrainRoughness" in attrs:
        attrs["GrainRoughness"] = adjust(attrs["GrainRoughness"], +20)
    
    if "Saturation" in attrs:
        attrs["Saturation"] = adjust(attrs["Saturation"], +10)
    
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── PULLED -1 STOP ───────────────────────────────────────────────────
def make_pulled_1(parent_path, target_name):
    """-1 stop pull: lower contrast, finer grain, desaturated."""
    attrs = read_preset(parent_path)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -15)
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], +15)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], +15)
    if "Blacks2012" in attrs:
        attrs["Blacks2012"] = adjust(attrs["Blacks2012"], +10)
    if "Exposure2012" in attrs:
        attrs["Exposure2012"] = adjust(attrs["Exposure2012"], +0.30)
    if "Whites2012" in attrs:
        attrs["Whites2012"] = adjust(attrs["Whites2012"], -5)
    
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -12)
        if safe_float(attrs["GrainAmount"]) < 5:
            attrs["GrainAmount"] = "5"
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], -8)
        if safe_float(attrs["GrainSize"]) < 10:
            attrs["GrainSize"] = "10"
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], -10)
    if "GrainRoughness" in attrs:
        attrs["GrainRoughness"] = adjust(attrs["GrainRoughness"], -10)
    
    if "Saturation" in attrs:
        attrs["Saturation"] = adjust(attrs["Saturation"], -5)
    
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── EXPIRED ──────────────────────────────────────────────────────────
def make_expired(parent_path, target_name, years):
    """Expired film: faded contrast, color shifts, heavy grain, lifted blacks."""
    attrs = read_preset(parent_path)
    extreme = (years >= 30)
    mult = 1.5 if extreme else 1.0
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -12 * mult)
    if "Blacks2012" in attrs:
        attrs["Blacks2012"] = adjust(attrs["Blacks2012"], +12 * mult)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], +10 * mult)
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], +15 * mult)
    if "Whites2012" in attrs:
        attrs["Whites2012"] = adjust(attrs["Whites2012"], -15 * mult)
    
    # Color shifts toward magenta/green (expired film hallmark)
    # Tint shift toward magenta
    attrs["ColorGradeBalance"] = adjust(attrs.get("ColorGradeBalance", "0"), +15 * mult)
    
    # Shift shadow color toward green/magenta
    if "ColorGradeShadowHue" in attrs:
        attrs["ColorGradeShadowHue"] = adjust(attrs["ColorGradeShadowHue"], -30 * mult)
    if "ColorGradeShadowSat" in attrs:
        attrs["ColorGradeShadowSat"] = adjust(attrs["ColorGradeShadowSat"], +8 * mult)
    
    # Reduce saturation globally
    if "Saturation" in attrs:
        attrs["Saturation"] = adjust(attrs["Saturation"], -10 * mult)
    
    # Heavy base fog grain
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], +22 * mult)
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], +12 * mult)
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], +15 * mult)
    if "GrainRoughness" in attrs:
        attrs["GrainRoughness"] = adjust(attrs["GrainRoughness"], +18 * mult)
    
    # Fade specific hues
    if "SaturationAdjustmentGreen" in attrs:
        attrs["SaturationAdjustmentGreen"] = sat_adjust(attrs["SaturationAdjustmentGreen"], -10 * mult)
    if "SaturationAdjustmentBlue" in attrs:
        attrs["SaturationAdjustmentBlue"] = sat_adjust(attrs["SaturationAdjustmentBlue"], -10 * mult)
    
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── SCANNER VARIANTS ─────────────────────────────────────────────────
def make_noritsu(parent_path, target_name):
    """Noritsu scanner: warmer, more contrasty, more saturated."""
    attrs = read_preset(parent_path)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], +8)
    if "Saturation" in attrs:
        attrs["Saturation"] = adjust(attrs["Saturation"], +8)
    
    # Noritsu warmth: shift color grade toward warm
    attrs["ColorGradeHighlightHue"] = adjust(attrs.get("ColorGradeHighlightHue", "45"), +5)
    attrs["ColorGradeHighlightSat"] = adjust(attrs.get("ColorGradeHighlightSat", "5"), +5)
    attrs["ColorGradeShadowHue"] = adjust(attrs.get("ColorGradeShadowHue", "210"), -5)
    attrs["ColorGradeBalance"] = adjust(attrs.get("ColorGradeBalance", "0"), +10)
    
    # Slightly more grain visible from scanning
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], +5)
    
    return attrs

def make_frontier(parent_path, target_name):
    """Frontier scanner: cooler, cyan shadows, less contrast."""
    attrs = read_preset(parent_path)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -5)
    
    # Frontier cool/cyan bias
    attrs["ColorGradeShadowHue"] = adjust(attrs.get("ColorGradeShadowHue", "210"), +15)
    attrs["ColorGradeShadowSat"] = adjust(attrs.get("ColorGradeShadowSat", "8"), +5)
    attrs["ColorGradeBalance"] = adjust(attrs.get("ColorGradeBalance", "0"), -10)
    
    # Slightly softer grain
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], -5)
    
    return attrs

# ── FORMAT VARIANTS ──────────────────────────────────────────────────
def make_120(parent_path, target_name):
    """Medium format 120: finer grain, smoother tonality."""
    attrs = read_preset(parent_path)
    
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -10)
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], -8)
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], -5)
    
    # Slightly smoother contrast
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -3)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], +5)
    
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

def make_4x5(parent_path, target_name):
    """Large format 4x5: ultra-fine grain, smoothest tonality."""
    attrs = read_preset(parent_path)
    
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -18)
        if safe_float(attrs["GrainAmount"]) < 3:
            attrs["GrainAmount"] = "3"
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], -12)
        if safe_float(attrs["GrainSize"]) < 8:
            attrs["GrainSize"] = "8"
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], -10)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -5)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], +8)
    
    if "GrainAmount" in attrs:
        attrs["Sharpness"] = "10"
        attrs["Clarity2012"] = "0"
        attrs["Dehaze"] = "0"
        attrs["Texture"] = "0"
        attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── DARKROOM TONING (B&W) ───────────────────────────────────────────
def make_bw_tone(target_name, highlight_hue, highlight_sat, shadow_hue, shadow_sat, balance):
    """B&W toning preset: split-tone effect via ColorGrade wheels."""
    attrs = {
        "Treatment": "Monochrome",
        "ProcessVersion": "15.4",
        "ConvertToGrayscale": "True",
        "Sharpness": "10",
        "LuminanceSmoothing": "0",
        "Blacks2012": "-20",
        "Contrast2012": "+20",
        "Highlights2012": "-15",
        "Shadows2012": "+15",
        "Whites2012": "+10",
        "Texture": "0",
        "Clarity2012": "0",
        "Dehaze": "0",
        "GrainAmount": "35",
        "GrainSize": "25",
        "GrainFrequency": "50",
        "GrayMixerRed": "+20",
        "GrayMixerOrange": "+15",
        "GrayMixerYellow": "+5",
        "GrayMixerGreen": "-10",
        "GrayMixerAqua": "-15",
        "GrayMixerBlue": "-25",
        "GrayMixerPurple": "-5",
        "GrayMixerMagenta": "0",
        "ColorGradeMidtoneHue": "0",
        "ColorGradeMidtoneSat": "0",
        "ColorGradeMidtoneLum": "0",
        "ColorGradeHighlightHue": highlight_hue,
        "ColorGradeHighlightSat": highlight_sat,
        "ColorGradeHighlightLum": "0",
        "ColorGradeShadowHue": shadow_hue,
        "ColorGradeShadowSat": shadow_sat,
        "ColorGradeShadowLum": "0",
        "ColorGradeGlobalHue": "0",
        "ColorGradeGlobalSat": "0",
        "ColorGradeGlobalLum": "0",
        "ColorGradeBlending": "50",
        "ColorGradeBalance": balance,
    }
    return attrs

# ── DEVELOPMENT VARIANTS (B&W) ───────────────────────────────────────
def make_dev_variant(parent_path, target_name, grain_delta, size_delta, roughness_delta, contrast_delta, shadow_delta, highlights_delta):
    """Development variant: change grain structure and contrast."""
    attrs = read_preset(parent_path)
    
    if "GrainAmount" in attrs:
        attrs["GrainAmount"] = adjust(attrs["GrainAmount"], grain_delta)
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], size_delta)
    if "GrainFrequency" in attrs:
        attrs["GrainFrequency"] = adjust(attrs["GrainFrequency"], roughness_delta)
    if "GrainRoughness" in attrs:
        attrs["GrainRoughness"] = adjust(attrs["GrainRoughness"], roughness_delta)
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], contrast_delta)
    if "Shadows2012" in attrs:
        attrs["Shadows2012"] = adjust(attrs["Shadows2012"], shadow_delta)
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], highlights_delta)
    
    attrs["Sharpness"] = "10"
    attrs["Clarity2012"] = "0"
    attrs["Dehaze"] = "0"
    attrs["Texture"] = "0"
    attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── PRINT EMULATION ──────────────────────────────────────────────────
def make_ra4_print(target_name):
    """RA-4 Color Print: slight warmth, lifted blacks, print contrast."""
    attrs = {
        "Treatment": "Color",
        "ProcessVersion": "15.4",
        "Sharpness": "10",
        "LuminanceSmoothing": "0",
        "Blacks2012": "+10",
        "Contrast2012": "+18",
        "Exposure2012": "+0.15",
        "Highlights2012": "-35",
        "Shadows2012": "+25",
        "Whites2012": "-5",
        "Texture": "0",
        "Clarity2012": "0",
        "Dehaze": "0",
        "GrainAmount": "15",
        "GrainSize": "20",
        "GrainFrequency": "50",
        "Saturation": "-3",
        "Vibrance": "-1",
        "HueAdjustmentRed": "+5",
        "HueAdjustmentOrange": "-3",
        "HueAdjustmentYellow": "-5",
        "HueAdjustmentGreen": "+10",
        "SaturationAdjustmentRed": "+5",
        "SaturationAdjustmentOrange": "+5",
        "SaturationAdjustmentGreen": "-10",
        "SaturationAdjustmentBlue": "-5",
        "LuminanceAdjustmentOrange": "+5",
        "ColorGradeMidtoneHue": "0",
        "ColorGradeMidtoneSat": "0",
        "ColorGradeMidtoneLum": "0",
        "ColorGradeHighlightHue": "45",
        "ColorGradeHighlightSat": "8",
        "ColorGradeHighlightLum": "0",
        "ColorGradeShadowHue": "50",
        "ColorGradeShadowSat": "5",
        "ColorGradeShadowLum": "0",
        "ColorGradeGlobalHue": "0",
        "ColorGradeGlobalSat": "0",
        "ColorGradeGlobalLum": "0",
        "ColorGradeBlending": "50",
        "ColorGradeBalance": "+10",
    }
    return attrs

def make_ilford_warmtone(target_name):
    """Ilford Multigrade Warmtone: warm-toned B&W paper emulation."""
    attrs = {
        "Treatment": "Monochrome",
        "ProcessVersion": "15.4",
        "ConvertToGrayscale": "True",
        "Sharpness": "10",
        "LuminanceSmoothing": "0",
        "Blacks2012": "-15",
        "Contrast2012": "+15",
        "Highlights2012": "-10",
        "Shadows2012": "+10",
        "Whites2012": "+5",
        "Texture": "0",
        "Clarity2012": "0",
        "Dehaze": "0",
        "GrainAmount": "25",
        "GrainSize": "20",
        "GrainFrequency": "45",
        "GrayMixerRed": "+15",
        "GrayMixerOrange": "+12",
        "GrayMixerYellow": "+8",
        "GrayMixerGreen": "-8",
        "GrayMixerAqua": "-10",
        "GrayMixerBlue": "-20",
        "GrayMixerPurple": "0",
        "GrayMixerMagenta": "0",
        "ColorGradeMidtoneHue": "0",
        "ColorGradeMidtoneSat": "0",
        "ColorGradeMidtoneLum": "0",
        "ColorGradeHighlightHue": "40",
        "ColorGradeHighlightSat": "15",
        "ColorGradeHighlightLum": "0",
        "ColorGradeShadowHue": "35",
        "ColorGradeShadowSat": "12",
        "ColorGradeShadowLum": "0",
        "ColorGradeGlobalHue": "0",
        "ColorGradeGlobalSat": "0",
        "ColorGradeGlobalLum": "0",
        "ColorGradeBlending": "50",
        "ColorGradeBalance": "+20",
    }
    return attrs

def make_c_print(target_name):
    """C-Print (Chromogenic Color Print): RA-4 paper look with more pop."""
    attrs = {
        "Treatment": "Color",
        "ProcessVersion": "15.4",
        "Sharpness": "10",
        "LuminanceSmoothing": "0",
        "Blacks2012": "-5",
        "Contrast2012": "+25",
        "Exposure2012": "+0.10",
        "Highlights2012": "-30",
        "Shadows2012": "+20",
        "Whites2012": "+10",
        "Texture": "0",
        "Clarity2012": "0",
        "Dehaze": "0",
        "GrainAmount": "20",
        "GrainSize": "22",
        "GrainFrequency": "50",
        "Saturation": "+5",
        "Vibrance": "+5",
        "HueAdjustmentRed": "+5",
        "HueAdjustmentGreen": "+10",
        "HueAdjustmentBlue": "-5",
        "SaturationAdjustmentRed": "+10",
        "SaturationAdjustmentOrange": "+8",
        "SaturationAdjustmentGreen": "+5",
        "SaturationAdjustmentBlue": "+10",
        "LuminanceAdjustmentOrange": "+8",
        "ColorGradeMidtoneHue": "0",
        "ColorGradeMidtoneSat": "0",
        "ColorGradeMidtoneLum": "0",
        "ColorGradeHighlightHue": "45",
        "ColorGradeHighlightSat": "5",
        "ColorGradeHighlightLum": "0",
        "ColorGradeShadowHue": "210",
        "ColorGradeShadowSat": "5",
        "ColorGradeShadowLum": "0",
        "ColorGradeGlobalHue": "0",
        "ColorGradeGlobalSat": "0",
        "ColorGradeGlobalLum": "0",
        "ColorGradeBlending": "50",
        "ColorGradeBalance": "0",
    }
    return attrs

# ── CINE VARIANTS ────────────────────────────────────────────────────
def make_vision3_500t(parent_path, target_name):
    """Vision3 500T: tungsten-balanced cine film, cooler cast, higher contrast."""
    attrs = read_preset(parent_path)
    
    # 500T is faster, tungsten balanced
    attrs["GrainAmount"] = adjust(attrs.get("GrainAmount", "21"), +10)
    attrs["GrainSize"] = adjust(attrs.get("GrainSize", "30"), +5)
    attrs["Contrast2012"] = adjust(attrs.get("Contrast2012", "31"), +5)
    attrs["Exposure2012"] = adjust(attrs.get("Exposure2012", "0.23"), -0.10)
    
    # Tungsten balance: cooler
    attrs["ColorGradeHighlightHue"] = adjust(attrs.get("ColorGradeHighlightHue", "45"), -10)
    attrs["ColorGradeShadowHue"] = adjust(attrs.get("ColorGradeShadowHue", "210"), +10)
    attrs["ColorGradeBalance"] = adjust(attrs.get("ColorGradeBalance", "10"), -8)
    
    # Blue channel responds differently in tungsten film
    attrs["SaturationAdjustmentBlue"] = adjust(attrs.get("SaturationAdjustmentBlue", "0"), +8)
    
    attrs["Sharpness"] = "10"
    attrs["Clarity2012"] = "0"
    attrs["Dehaze"] = "0"
    attrs["Texture"] = "0"
    attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── VIDEO LUT VARIANTS ───────────────────────────────────────────────
def make_video_variant(parent_path, target_name):
    """Convert a stills preset to video-grade: wider DR, cinematic curve, softer grain."""
    attrs = read_preset(parent_path)
    
    # Strip calibration (never in presets — except some creative ones have exceptions)
    calib_keys = ['RedHue', 'RedSaturation', 'GreenHue', 'GreenSaturation', 
                  'BlueHue', 'BlueSaturation', 'ShadowTint', 'Temperature', 'Tint',
                  'CalibrationRedHue', 'CalibrationRedSat', 'CalibrationGreenHue',
                  'CalibrationGreenSat', 'CalibrationBlueHue', 'CalibrationBlueSat']
    for k in calib_keys:
        attrs.pop(k, None)
    
    # Video-specific adjustments
    # Slightly lift blacks for Rec.709 safety
    if "Blacks2012" in attrs:
        current = safe_float(attrs["Blacks2012"])
        if current < -15:
            attrs["Blacks2012"] = fmt(current + 10)
        elif current < 0:
            attrs["Blacks2012"] = fmt(current + 5)
        else:
            attrs["Blacks2012"] = fmt(current)
    
    # Reduce contrast slightly for wider DR video
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -5)
    
    # Slightly more highlight protection for video's lower DR
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], -8)
    
    # Reduce grain for video (grain aliases on video codecs)
    if "GrainAmount" in attrs:
        grain = safe_float(attrs["GrainAmount"])
        if grain > 30:
            attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -15)
        elif grain > 15:
            attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -8)
        else:
            attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -3)
        if safe_float(attrs["GrainAmount"]) < 5:
            attrs["GrainAmount"] = "5"
    
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], -5)
    
    # Ensure safety
    attrs["Sharpness"] = "10"
    attrs["Clarity2012"] = "0"
    attrs["Dehaze"] = "0"
    attrs["Texture"] = "0"
    attrs["LuminanceSmoothing"] = "0"
    
    return attrs

def make_video_bw_variant(parent_path, target_name):
    """Convert B&W stills preset to video-grade."""
    attrs = read_preset(parent_path)
    
    # Strip calibration
    calib_keys = ['RedHue', 'RedSaturation', 'GreenHue', 'GreenSaturation', 
                  'BlueHue', 'BlueSaturation', 'ShadowTint', 'Temperature', 'Tint',
                  'CalibrationRedHue', 'CalibrationRedSat', 'CalibrationGreenHue',
                  'CalibrationGreenSat', 'CalibrationBlueHue', 'CalibrationBlueSat']
    for k in calib_keys:
        attrs.pop(k, None)
    
    if "Blacks2012" in attrs:
        current = safe_float(attrs["Blacks2012"])
        if current < -15:
            attrs["Blacks2012"] = fmt(current + 10)
    
    if "Contrast2012" in attrs:
        attrs["Contrast2012"] = adjust(attrs["Contrast2012"], -5)
    
    if "Highlights2012" in attrs:
        attrs["Highlights2012"] = adjust(attrs["Highlights2012"], -5)
    
    if "GrainAmount" in attrs:
        grain = safe_float(attrs["GrainAmount"])
        if grain > 30:
            attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -12)
        elif grain > 15:
            attrs["GrainAmount"] = adjust(attrs["GrainAmount"], -8)
        if safe_float(attrs["GrainAmount"]) < 5:
            attrs["GrainAmount"] = "5"
    
    if "GrainSize" in attrs:
        attrs["GrainSize"] = adjust(attrs["GrainSize"], -5)
    
    attrs["Sharpness"] = "10"
    attrs["Clarity2012"] = "0"
    attrs["Dehaze"] = "0"
    attrs["Texture"] = "0"
    attrs["LuminanceSmoothing"] = "0"
    
    return attrs

# ── WRITE PRESET ─────────────────────────────────────────────────────
def write_preset(out_path, attrs, target_name, group, curve_points=None):
    """Write a single XMP preset file."""
    attrs["Name"] = target_name
    
    # Fix any leftover numeric formatting issues (e.g. "- -30.0")
    for k, v in list(attrs.items()):
        if isinstance(v, str) and v.startswith("- -") or v.startswith("+ +"):
            attrs[k] = v.replace("- -", "-").replace("+ +", "+")
    
    # Generate UUID
    attrs["UUID"] = str(uuid.uuid4()).replace('-', '').upper()[:32]
    while len(attrs["UUID"]) < 32:
        attrs["UUID"] += "0"
    
    # Build attribute string
    attr_parts = []
    for k, v in attrs.items():
        attr_parts.append(f'crs:{k}="{v}"')
    
    # Ensure mandatory attribute presence
    mandatory = {
        "PresetType": "Normal",
        "Cluster": "",
        "SupportsAmount": "True",
        "SupportsColor": "True",
        "SupportsMonochrome": "True",
        "SupportsHighDynamicRange": "True",
        "SupportsNormalDynamicRange": "True",
        "SupportsSceneReferred": "True",
        "SupportsOutputReferred": "True",
        "RequiresRenditionBehavior": "True",
        "HasSettings": "True",
    }
    for k, v in mandatory.items():
        if k not in attrs:
            attr_parts.insert(0, f'crs:{k}="{v}"')
    
    attr_str = " ".join(attr_parts)
    
    # Determine Look block
    treatment = attrs.get("Treatment", "Color")
    if treatment == "Monochrome":
        look_name = "Adobe Monochrome"
        look_uuid = "0C09521111114111B1115456789ABCDE"
        look_mono = "True"
    else:
        look_name = "Adobe Color"
        look_uuid = "B952C21111114111B1115456789ABCDE"
        look_mono = "False"
    
    # Determine curve
    if curve_points is None:
        if group == "Creative" or group == "Video":
            curve_points = CINEMATIC_CURVE
        elif group == "Slide":
            curve_points = SLIDE_CURVE
        else:
            curve_points = NEUTRAL_CURVE
    
    # Build tone curves
    curve_xml = ""
    for suffix in ["", "Red", "Green", "Blue"]:
        tag = f"ToneCurvePV2012{suffix}"
        seq_items = "".join(f'<rdf:li>{pt}</rdf:li>' for pt in curve_points)
        curve_xml += f'<crs:{tag}><rdf:Seq>{seq_items}</rdf:Seq></crs:{tag}>'
    
    xmp = f'''<x:xmpmeta xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00">
 <rdf:RDF>
 
 <rdf:Description rdf:about="" {attr_str}>
 <crs:Name>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">{target_name}</rdf:li>
 </rdf:Alt>
 </crs:Name>
 <crs:Group>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">{group}</rdf:li>
 </rdf:Alt>
 </crs:Group>
 <crs:Look>
 
 
 <rdf:Description crs:Name="{look_name}" crs:Amount="1.000000" crs:UUID="{look_uuid}" crs:SupportsAmount="True" crs:SupportsMonochrome="{look_mono}" crs:SupportsOutputReferred="True">
 <crs:Group>
 <rdf:Alt>
 <rdf:li xml:lang="x-default">Profiles</rdf:li>
 </rdf:Alt>
 </crs:Group>
 </rdf:Description>
 </crs:Look>
 {curve_xml}</rdf:Description>
 </rdf:RDF>
</x:xmpmeta>'''
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xmp)

# ═══════════════════════════════════════════════════════════════════════
# MAIN GENERATION
# ═══════════════════════════════════════════════════════════════════════

presets_created = []

# ── 1. PUSHED +1 STOPS (10) ─────────────────────────────────────────
pushed_1 = [
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 +1", "Color Negative", make_pushed_1),
    (f"{COLOR_NEG}/Kodak Portra 800.xmp", "Kodak Portra 800 +1", "Color Negative", make_pushed_1),
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 +1", "Color Negative", make_pushed_1),
    (f"{COLOR_NEG}/Kodak Ektar 100.xmp", "Kodak Ektar 100 +1", "Color Negative", make_pushed_1),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 +1", "Black White", make_pushed_1),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus +1", "Black White", make_pushed_1),
    (f"{COLOR_NEG}/Kodak Ultramax 400.xmp", "Kodak Ultramax 400 +1", "Color Negative", make_pushed_1),
    (f"{COLOR_NEG}/Fuji Superia X-TRA 400.xmp", "Fuji Superia X-TRA 400 +1", "Color Negative", make_pushed_1),
]
# Delta 3200 +2 and T-Max 3200 +2 go in pushed_2 list, but they're named +2 so let's put them in pushed_1 with stronger params
# Actually: Delta 3200+2 and T-Max 3200+2 are called "+2" in the spec, so let's use pushed_2 for them
# But they should still be counted among the 10 pushed+1 list...
# Let me re-read: "Pushed +1 Stops (10): ... Delta 3200+2, T-Max 3200+2..."
# These are still +2 versions but included in this category. Let me use make_pushed_1 but with extra push
pushed_1_extra = [
    (f"{BW}/Ilford Delta 3200.xmp", "Ilford Delta 3200 +2", "Black White", make_pushed_2),
    (f"{BW}/Kodak T-Max 3200.xmp", "Kodak T-Max 3200 +2", "Black White", make_pushed_2),
]

for parent, name, group, func in pushed_1:
    attrs = func(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

for parent, name, group, func in pushed_1_extra:
    attrs = func(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 2. PUSHED +2 STOPS (5) ──────────────────────────────────────────
pushed_2 = [
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 +2", "Color Negative"),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 +2", "Black White"),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus +2", "Black White"),
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 +2", "Color Negative"),
    (f"{COLOR_NEG}/Kodak Ultramax 400.xmp", "Kodak Ultramax 400 +2", "Color Negative"),
]
for parent, name, group in pushed_2:
    attrs = make_pushed_2(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 3. PULLED -1 STOP (4) ───────────────────────────────────────────
pulled_1 = [
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 -1", "Color Negative"),
    (f"{COLOR_NEG}/Kodak Portra 800.xmp", "Kodak Portra 800 -1", "Color Negative"),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus -1", "Black White"),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 -1", "Black White"),
]
for parent, name, group in pulled_1:
    attrs = make_pulled_1(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 4. EXPIRED (5) ──────────────────────────────────────────────────
expired = [
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 Expired 10yr", "Color Negative", 10),
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 Expired 30yr", "Color Negative", 30),
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 Expired", "Color Negative", 15),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 Expired", "Black White", 15),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus Expired", "Black White", 15),
]
for parent, name, group, years in expired:
    attrs = make_expired(parent, name, years)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 5. SCANNER VARIANTS (3) ─────────────────────────────────────────
scanner = [
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 Noritsu", "Color Negative", make_noritsu),
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Kodak Gold 200 Frontier", "Color Negative", make_frontier),
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 Noritsu", "Color Negative", make_noritsu),
]
for parent, name, group, func in scanner:
    attrs = func(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 6. FORMAT VARIANTS (3) ──────────────────────────────────────────
format_variants = [
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 120", "Color Negative", make_120),
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Kodak Portra 400 4x5", "Color Negative", make_4x5),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 120", "Black White", make_120),
]
for parent, name, group, func in format_variants:
    attrs = func(parent, name)
    out = f"/app/lr-presets/Presets/{group.replace(' ', '-')}/{name}.xmp"
    write_preset(out, attrs, name, group)
    presets_created.append(name)

# ── 7. DARKROOM TONING (5) ──────────────────────────────────────────
toning = [
    ("Sepia Tone", "35", "18", "25", "12", "+25"),
    ("Selenium Tone", "275", "12", "250", "8", "-10"),
    ("Gold Tone", "230", "10", "220", "8", "-5"),
    ("Copper Tone", "20", "15", "15", "12", "+20"),
    ("Split Warm-Cool", "45", "15", "220", "12", "0"),
]
for name, hh, hs, sh, ss, bal in toning:
    attrs = make_bw_tone(name, hh, hs, sh, ss, bal)
    out = f"{BW}/{name}.xmp"
    write_preset(out, attrs, name, "Black White", curve_points=NEUTRAL_CURVE)
    presets_created.append(name)

# ── 8. DEVELOPMENT (5) ──────────────────────────────────────────────
dev = [
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 Rodinal", +15, +8, +15, +10, -5, -10),
    (f"{BW}/Kodak Tri-X 400.xmp", "Kodak Tri-X 400 HC-110", +5, +3, +5, -5, +5, +5),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus DD-X", -10, -8, -8, -5, +5, +5),
    (f"{BW}/Ilford HP5 Plus.xmp", "Ilford HP5 Plus Stand Dev", -5, 0, -5, -15, +15, +10),
    (f"{BW}/Ilford Delta 3200.xmp", "Ilford Delta 3200 Microphen", +10, +8, +10, +8, -8, -5),
]
for parent, name, gd, sd, rd, cd, shd, hld in dev:
    attrs = make_dev_variant(parent, name, gd, sd, rd, cd, shd, hld)
    out = f"{BW}/{name}.xmp"
    write_preset(out, attrs, name, "Black White", curve_points=NEUTRAL_CURVE)
    presets_created.append(name)

# ── 9. PRINT EMULATION (3) ──────────────────────────────────────────
print_presets = [
    ("RA-4 Color Print", "Color Negative", make_ra4_print, NEUTRAL_CURVE),
    ("Ilford MG Warmtone", "Black White", make_ilford_warmtone, NEUTRAL_CURVE),
    ("C-Print", "Color Negative", make_c_print, NEUTRAL_CURVE),
]
for name, group, func, curve in print_presets:
    attrs = func(name)
    # Tighten vibrance-saturation gap
    if "Vibrance" in attrs and "Saturation" in attrs:
        vib = safe_float(attrs["Vibrance"])
        sat = safe_float(attrs["Saturation"])
        if abs(vib - sat) > 5:
            attrs["Vibrance"] = fmt(max(sat - 5, min(sat + 5, vib)))
    dir_name = group.replace(" ", "-")
    out = f"/app/lr-presets/Presets/{dir_name}/{name}.xmp"
    write_preset(out, attrs, name, group, curve_points=curve)
    presets_created.append(name)

# ── 10. CINE VARIANTS (2) ───────────────────────────────────────────
cine = [
    (f"{COLOR_NEG}/Kodak Vision3 250D.xmp", "Kodak Vision3 250D ECN-2", "Color Negative", None),
]
# 250D ECN-2 is essentially the existing Vision3 250D with ECN-2 in name
attrs = read_preset(cine[0][0])
# Add slight ECN-2 process characteristics (slightly flatter, additive grain from remjet removal)
attrs["Contrast2012"] = adjust(attrs.get("Contrast2012", "31"), -3)
attrs["GrainAmount"] = adjust(attrs.get("GrainAmount", "21"), +3)
attrs["Sharpness"] = "10"
attrs["Clarity2012"] = "0"
attrs["Dehaze"] = "0"
attrs["Texture"] = "0"
attrs["LuminanceSmoothing"] = "0"
out = f"{COLOR_NEG}/Kodak Vision3 250D ECN-2.xmp"
write_preset(out, attrs, "Kodak Vision3 250D ECN-2", "Color Negative", curve_points=NEUTRAL_CURVE)
presets_created.append("Kodak Vision3 250D ECN-2")

# 500T ECN-2
attrs_500t = make_vision3_500t(f"{COLOR_NEG}/Kodak Vision3 250D.xmp", "Kodak Vision3 500T ECN-2")
out = f"{COLOR_NEG}/Kodak Vision3 500T ECN-2.xmp"
write_preset(out, attrs_500t, "Kodak Vision3 500T ECN-2", "Color Negative", curve_points=NEUTRAL_CURVE)
presets_created.append("Kodak Vision3 500T ECN-2")

# ── 11. VIDEO LUT CROSS-FORMAT (20) ──────────────────────────────────
video_presets = [
    # Film-based video presets
    (f"{COLOR_NEG}/Kodak Portra 400.xmp", "Portra 400 Video", make_video_variant),
    (f"{COLOR_NEG}/Kodak Gold 200.xmp", "Gold 200 Video", make_video_variant),
    (f"{COLOR_NEG}/Kodak Ektar 100.xmp", "Ektar 100 Video", make_video_variant),
    (f"{CREATIVE}/Cinestill 800T.xmp", "Cinestill 800T Video", make_video_variant),
    (f"{CREATIVE}/Cinematic Teal and Orange.xmp", "Teal & Orange Cinematic Video", make_video_variant),
    (f"{CREATIVE}/Cyberpunk Neon City.xmp", "Cyberpunk Neon Video", make_video_variant),
    (f"{CREATIVE}/Moody PNW.xmp", "Moody PNW Video", make_video_variant),
    (f"{CREATIVE}/Bleach Bypass.xmp", "Bleach Bypass Video", make_video_variant),
    (f"{CREATIVE}/1980s VHS Synthwave.xmp", "VHS Synthwave Video", make_video_variant),
    (f"{CREATIVE}/Wong Kar-Wai 80s Hong Kong.xmp", "WKW Hong Kong Video", make_video_variant),
    (f"{SLIDE}/Kodachrome 64.xmp", "Kodachrome 64 Video", make_video_variant),
    (f"{SLIDE}/Fuji Velvia 50.xmp", "Velvia 50 Video", make_video_variant),
    (f"{BW}/Kodak Tri-X 400.xmp", "Tri-X 400 Video", make_video_bw_variant),
    # Additional creative video presets
    (f"{CREATIVE}/Wes Anderson Pastel.xmp", "Wes Anderson Pastel Video", make_video_variant),
    (f"{CREATIVE}/Kodak Aerochrome.xmp", "Kodak Aerochrome Video", make_video_variant),
    (f"{CREATIVE}/Cinematic Dream Look.xmp", "Cinematic Dream Look Video", make_video_variant),
    (f"{CREATIVE}/Cross-Processed Velvia.xmp", "Cross-Processed Velvia Video", make_video_variant),
    (f"{CREATIVE}/Polaroid SX-70.xmp", "Polaroid SX-70 Video", make_video_variant),
    (f"{CREATIVE}/Super 8 Home Movie.xmp", "Super 8 Home Movie Video", make_video_variant),
    (f"{CREATIVE}/Pastel Anime Aethereal.xmp", "Pastel Anime Aethereal Video", make_video_variant),
]

for parent, name, func in video_presets:
    attrs = func(parent, name)
    out = f"{VIDEO_DIR}/{name}.xmp"
    # For Slide-based video presets, use slide curve; for B&W, neutral; else cinematic
    curve = CINEMATIC_CURVE
    if "SLIDE" in parent.upper() or "Velvia" in name or "Kodachrome" in name:
        curve = SLIDE_CURVE
    elif "BW" in parent or "Tri-X" in name:
        curve = NEUTRAL_CURVE
    
    write_preset(out, attrs, name, "Video", curve_points=curve)
    presets_created.append(name)

# ── VERIFY & REPORT ──────────────────────────────────────────────────
print(f"\n=== PRESETS CREATED: {len(presets_created)} ===\n")
for i, name in enumerate(presets_created, 1):
    print(f"  {i:3d}. {name}")

# Count by category
cats = {}
for p in presets_created:
    if "Video" in p:
        c = "Video"
    elif any(kw in p for kw in ["Tri-X", "HP5", "Delta", "T-Max", "Sepia", "Selenium", "Gold Tone", "Copper", "Split Warm", "Rodinal", "HC-110", "DD-X", "Stand Dev", "Microphen", "Ilford MG"]):
        c = "Black White"
    elif "Vision3" in p or "Portra" in p or "Gold" in p or "Ektar" in p or "Ultramax" in p or "Superia" in p or "RA-4" in p or "C-Print" in p:
        c = "Color Negative"
    else:
        c = "Other"
    cats[c] = cats.get(c, 0) + 1

print(f"\nBy category:")
for c, n in sorted(cats.items()):
    print(f"  {c}: {n}")
