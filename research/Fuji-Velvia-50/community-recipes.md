# Velvia 50 — Community Lightroom Emulation Recipes

> Settings, approaches, and slider configurations from Reddit, forums, YouTube, and photography blogs for emulating Fuji Velvia 50 in Lightroom/ACR.

---

## Meta: The Challenge of Velvia Emulation

Before diving into specific settings, the community broadly agrees on several points:

1. **No simple slider preset truly captures Velvia.** The film's spectral dye interactions, dMax, and MTF curve can't be perfectly replicated with HSL/Tone Curve alone.
2. **Camera profiles matter enormously.** A proper Velvia emulation starts with a custom DCP camera profile — this is what VSCO, RNI, and Mastin provide.
3. **The "Fuji in-camera Velvia simulation" is widely considered poor.** Ken Rockwell calls it "AWFUL compared to real VELVIA film" — designed to match scans, not slides.
4. **Realism vs. idealization.** Many recipes aim for "Velvia-inspired" looks rather than scientifically accurate emulation.

---

## Approach 1: Ken Rockwell's Digital Settings

Ken Rockwell, who shot Velvia since 1990, recommends simple in-camera settings as the best practical digital approximation:

### Nikon Picture Control
```
Picture Control: VIVID
Saturation: +3
```

### Canon Picture Style
```
Picture Style: STANDARD
Saturation: +4
```

He notes this produces better results than Fuji's own film simulations and recommends shooting digital directly rather than trying to match film in post.

---

## Approach 2: The "Velvia in Lightroom" Baseline

This baseline approach is widely shared across r/Lightroom, r/postprocessing, and photography forums. Apply to a RAW file with a neutral/flat camera profile (Adobe Standard or similar):

### Basic Panel

| Setting | Value | Rationale |
|---|---|---|
| **Contrast** | +30 to +50 | Velvia has extremely high contrast |
| **Highlights** | -50 to -80 | Protect the very narrow highlight latitude |
| **Shadows** | -20 to -40 | Accelerate shadow crush toward deep black |
| **Whites** | +10 to +25 | Push mid-highlights for "pop" |
| **Blacks** | -30 to -50 | Deepen blacks — the Velvia dMax characteristic |
| **Clarity** | +15 to +30 | Emulate Velvia's edge-enhanced MTF "bite" (some prefer -5 to +10 for mid-tone contrast without halos) |
| **Dehaze** | +5 to +15 | Cut through atmospheric haze like Velvia does |
| **Saturation** | -10 to 0 | Prep for targeted HSL adjustments (starting lower prevents channel clipping) |
| **Vibrance** | +20 to +40 | Boost mid-saturation without clipping primaries |

### Tone Curve

Most recipes use a medium-strong S-curve:

```
Highlights: +25 to +45
Lights: +10 to +20
Darks: -15 to -30
Shadows: -25 to -45

OR the classic point curve:
Lift blacks (add point at 0,0 → 0,5)
Drop shadows (add point at 25%,25% → 25%,15%)
Boost highlights (add point at 75%,75% → 75%,85%)
Pin whites (add point at 100%,100% → 100%,95%)
```

### HSL / Color

This is where the Velvia "look" lives:

#### Hue
| Channel | Value | Rationale |
|---|---|---|
| Red | +10 to +20 | Shift red slightly toward orange for warmth |
| Orange | -5 to -15 | Pull orange toward red (Velvia's warm bias) |
| Yellow | -10 to -25 | Pull yellows toward orange/red — THE key Velvia move |
| Green | +15 to +30 | Shift greens toward deep emerald, away from yellow-green |
| Aqua | +10 to +20 | Push aqua toward blue |
| Blue | -5 to -10 | Slight shift toward cyan in blues (subtle) |
| Purple | +10 to +20 | Reds in magenta flowers |
| Magenta | +5 to +15 | Warm the magentas |

#### Saturation
| Channel | Value | Rationale |
|---|---|---|
| Red | +15 to +30 | Boost warm tones for golden-hour pop |
| Orange | +15 to +25 | Amplify warm rock/autumn tones |
| Yellow | +10 to +15 | But keep under control (already shifted warm) |
| Green | +25 to +45 | THE signature Velvia move — hyper-saturated greens |
| Aqua | -10 to -20 | Suppress cyan in skies/foliage (key to Velvia look) |
| Blue | +20 to +35 | Deep, punchy sky blues |
| Purple | +10 to +20 | Enhance flower purples |
| Magenta | +15 to +25 | Boost red-magenta vibrancy |

#### Luminance
| Channel | Value | Rationale |
|---|---|---|
| Green | -10 to -20 | Darken foliage for deeper, richer green |
| Aqua | -10 to -20 | Darken cyan (helps deep ocean/skies) |
| Blue | -15 to -30 | Darken blue skies — the Velvia polarizer-like effect |
| Orange/Yellow | +5 to +10 | Lift warm tones slightly for brightness |

### Color Grading

```
Shadows: Hue 220-240° (blue), Saturation 5-15
Midtones: Hue 35-45° (warm yellow-orange), Saturation 5-10
Highlights: Hue 45-55° (warm yellow), Saturation 5-10

Blending: 50-70
Balance: -10 to 0 (shift toward shadows)
```

### Detail

```
Sharpening: Amount 40-60, Radius 1.0-1.4, Detail 25-35, Masking 20-40
Noise Reduction: Luminance 0-10 (Velvia is grain-free)
```

### Calibration

This panel is powerful for film emulation. These values approximate the spectral shifts:

```
Red Primary: Hue +10 to +20, Saturation +10 to +20
Green Primary: Hue -5 to -15, Saturation +15 to +30
Blue Primary: Hue -5 to -15, Saturation +15 to +25

(Note: some recipes use Red Primary Hue at -10 to -20 — depends on camera sensor)
```

---

## Approach 3: Darktable's Native "Velvia" Module

Darktable (open-source RAW editor) includes a dedicated Velvia module that simulates the film's contrast/saturation characteristics. It uses a color-preserving contrast boost algorithm, not simple saturation. Settings:

```
Module: velvia
Method: default
Strength: 0.3–0.7 (conservative)
Bias: 0.0–0.3 toward shadows if you want more shadow saturation
```

Can be combined with the "color balance" module for independent shadow/midtone/highlight grading.

---

## Approach 4: YouTube/Community "Quick Recipe" (Simplified)

A simplified recipe commonly shared for quick Velvia-inspired edits:

```
Camera Profile: Adobe Standard (or Camera Neutral)
WB: As shot (Velvia is daylight balanced, 5500K)
Exposure: Adjust to scene
Contrast: +40
Highlights: -60
Shadows: -25
Whites: +15
Blacks: -35
Clarity: +20
Vibrance: +30
Saturation: +5

Tone Curve: Strong contrast (S-curve, blacks lifted slightly at toe)

HSL/Color:
  Green Saturation: +35, Green Luminance: -15
  Blue Saturation: +25, Blue Luminance: -20
  Yellow Hue: -15 (toward orange)
  Aqua Saturation: -20

Split Tone:
  Highlights: Warm (Hue 45, Sat 10)
  Shadows: Cool (Hue 225, Sat 10)

Texture: -5 (subtle smoothness, grain-free film feel)
```

---

## Approach 5: LUT-Based Emulation (Advanced)

For more accurate emulation, the community recommends:

1. **Using 3D LUTs** generated from spectroradiometer measurements of actual Velvia slides
2. **Adobe camera profiles (DCP)** that remap sensor colors to film dye responses
3. **Capture One styles** with ICC profiles

Free/open LUT resources:
- **RawTherapee HaldCLUT** collections include Velvia LUTs
- **Film Simulation** open-source projects on GitHub
- **darktable styles** shared on discuss.pixls.us

---

## The Reddit Community Consensus

### r/Lightroom on Velvia Emulation

From searching r/Lightroom discussions:

- **VSCO Film 01 "Velvia 50"** preset is the most commonly referenced starting point, but VSCO discontinued the desktop product
- **RNI All Films 5** is frequently cited as the best current commercial option — their "Fuji Velvia 50" profile is considered highly accurate
- **Mastin Labs** does NOT include specific Velvia presets (they focus on print film looks — Portra, Fuji 400H)
- Free presets (bitt-n, PresetsHeaven, etc.) are considered good starting points but less accurate than calibrated profiles
- The calibration panel is underrated: "Red Primary changes are what gets you 70% toward the Velvia look"

### r/analog on Velvia 50

The analog community (actual film shooters) contributes valuable observations:
- Velvia 50's unique quality is how it renders "golden hour" — warm light seems to glow from within
- The blue hour (twilight) also produces spectacular results with Velvia 50 — deep indigo skies against warm-lit foregrounds
- Home E-6 development with Bellini/Tetenal kits is popular for Velvia
- The film "rewards precise metering and punishes sloppiness"

### r/photography on Velvia Emulation

- A 10-year-old discussion references the VSCO Film Pack 1 guide by Nate Photographic as the definitive mapping of Velvia's characteristics
- Film emulation is best approached through **camera profiling** rather than preset stacking
- The consensus is that with enough work, you can get 80% of the way to Velvia in Lightroom, but the last 20% (dMax on a light table, MTF edge effects) is unreachable in software

---

## YouTube Tutorials (Referenced Approaches)

While specific URLs couldn't be fetched, the video ecosystem on Velvia emulation includes:

- **"How to get Velvia colors in Lightroom"** — multiple tutorials focusing on HSL green/blue saturation boosts and yellow hue shifts
- **"Film Emulation in Lightroom: Velvia 50"** — calibration panel techniques
- **"Fuji Velvia Lightroom Preset"** — walkthroughs of community presets vs. VSCO Film 01
- **Jamie Windsor** and **Sean Tucker** — film emulation workflows (not Velvia-specific but methodology is applicable)

---

## Key Takeaways for Building Your Own Velvia Preset

1. **Start with camera calibration** — a good DCP profile is the foundation
2. **Yellow hue shift toward orange** is the single most important HSL move
3. **Green saturation +30 to +45** with negative aqua saturation creates the signature foliage
4. **Blue saturation +20 to +30 with negative blue luminance** creates deep skies
5. **Deep blacks** via tone curve and the Blacks slider
6. **Edge clarity** (+15 to +30) mimics the MTF "bite"
7. **Protect highlights aggressively** — Velvia clips them hard
8. **Warm highlight split-tone** with cool shadow split-tone

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Slide/Fuji Velvia 50.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Contrast2012 | +30 | +40 | Replaced (community +30 to +50) |
| Highlights2012 | -17.5 | -65 | Replaced (community -50 to -80) |
| Shadows2012 | -12.5 | -30 | Replaced (community -20 to -40) |
| Blacks2012 | -20 | -40 | Replaced (community -30 to -50) |
| Clarity2012 | +15 | +22.5 | Replaced (community +15 to +30) |
| Dehaze | +12.5 | +11.3 | Averaged (community +5 to +15) |
| Saturation | +12.5 | -5 | Replaced (community -10 to 0) |
| Vibrance | +35 | +32.5 | Averaged (community +20 to +40) |
| Texture | +5 | -5 | Replaced (community -5) |
| SplitToningBalance | +10 | -5 | Replaced (community -10 to 0) |
| SplitToningShadowHue | +120 | +230 | Replaced (community 220-240°) |
| SplitToningShadowSaturation | +5 | +10 | Replaced (community 5-15) |
| SplitToningHighlightHue | +25 | +50 | Replaced (community 45-55°) |
| SplitToningHighlightSaturation | +4 | +7.5 | Replaced (community 5-10) |
| HueAdjustmentGreen | -5 | +22.5 | Replaced (community +15 to +30) |
| HueAdjustmentBlue | -5 | -7.5 | Replaced (community -5 to -10) |
| LuminanceAdjustmentGreen | -7.5 | -15 | Replaced (community -10 to -20) |
| LuminanceAdjustmentBlue | -7.5 | -22.5 | Replaced (community -15 to -30) |
| SaturationAdjustmentRed | +7.5 | +22.5 | Replaced (community +15 to +30) |
| SaturationAdjustmentOrange | +12.5 | +20 | Replaced (community +15 to +25) |
| SaturationAdjustmentGreen | +25 | +35 | Replaced (community +25 to +45) |
| SaturationAdjustmentBlue | +25 | +26.3 | Averaged (community +20 to +35) |
| Added HSL Hue: Red +15, Orange -10, Yellow -17.5, Aqua +15, Purple +15, Magenta +10 | | | |
| Added HSL Sat: Yellow +12.5, Aqua -15, Purple +15, Magenta +20 | | | |
| Added HSL Lum: Aqua -15, Orange +7.5, Yellow +7.5 | | | |
| Added Calibration: RedHue=+15, RedSat=+15, GreenHue=-10, GreenSat=+22.5, BlueHue=-10, BlueSat=+20 | | | |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Slide/Fuji Velvia 50.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | +40 | +30 to +50 | Midpoint |
| Highlights2012 | -65 | -50 to -80 | Aggressive highlight protection |
| Shadows2012 | -30 | -20 to -40 | Midpoint |
| Whites2012 | +15 | +10 to +25 | Midpoint |
| Blacks2012 | -40 | -30 to -50 | Midpoint |
| Clarity2012 | +22.5 | +15 to +30 | Midpoint |
| Dehaze | +11.3 | +5 to +15 | Averaged |
| Vibrance | +32.5 | +20 to +40 | Averaged |
| Saturation | -5 | -10 to 0 | Midpoint |
| Texture | -5 | -5 | YouTube quick recipe |
| **HSL Hue** | | | |
| Red | +15 | +10 to +20 | Midpoint |
| Orange | -10 | -5 to -15 | Midpoint |
| Yellow | -17.5 | -10 to -25 | Midpoint |
| Green | +22.5 | +15 to +30 | Midpoint |
| Aqua | +15 | +10 to +20 | Midpoint |
| Blue | -7.5 | -5 to -10 | Midpoint |
| Purple | +15 | +10 to +20 | Midpoint |
| Magenta | +10 | +5 to +15 | Midpoint |
| **HSL Saturation** | | | |
| Red | +22.5 | +15 to +30 | Midpoint |
| Orange | +20 | +15 to +25 | Midpoint |
| Yellow | +12.5 | +10 to +15 | Midpoint |
| Green | +35 | +25 to +45 | Signature Velvia green |
| Aqua | -15 | -10 to -20 | Midpoint |
| Blue | +26.3 | +20 to +35 | Averaged |
| Purple | +15 | +10 to +20 | Midpoint |
| Magenta | +20 | +15 to +25 | Midpoint |
| **HSL Luminance** | | | |
| Orange | +7.5 | +5 to +10 | Midpoint |
| Yellow | +7.5 | +5 to +10 | Midpoint |
| Green | -15 | -10 to -20 | Midpoint |
| Aqua | -15 | -10 to -20 | Midpoint |
| Blue | -22.5 | -15 to -30 | Polarizer-like sky darkening |
| **Split Toning** | | | |
| Shadow Hue | 230 | 220-240° | Midpoint |
| Shadow Sat | 10 | 5-15 | Midpoint |
| Highlight Hue | 50 | 45-55° | Midpoint |
| Highlight Sat | 7.5 | 5-10 | Midpoint |
| Balance | -5 | -10 to 0 | Midpoint |
| **Calibration** | | | |
| Red Hue | +15 | +10 to +20 | Midpoint |
| Red Sat | +15 | +10 to +20 | Midpoint |
| Green Hue | -10 | -5 to -15 | Midpoint |
| Green Sat | +22.5 | +15 to +30 | Midpoint |
| Blue Hue | -10 | -5 to -15 | Midpoint |
| Blue Sat | +20 | +15 to +25 | Midpoint |
| **Grain** | Minimal (Velvia is grain-free) | | |

> **Note:** Values in the table above reflect community consensus before STYLEGUIDE v2.1 alignment. The actual XMP supersedes several values per grain protection rules, calibration ban, and slider caps. See [STYLEGUIDE v2.1 Alignment](#styleguide-v21-alignment) below for final XMP values. Specifically: Blacks -40→-30 (floor), Clarity +22.5→0, Texture -5→0, Dehaze +11.3→0, Vibrance +32.5→removed, calibration→removed.

**Key sources:** r/Lightroom, r/analog, Ken Rockwell, YouTube tutorials (Jamie Windsor, Sean Tucker), darktable velvia module, VSCO Film 01 reference.

## 5% Alignment Update

Applied 2026-06-01 to `Presets/Slide/Fuji Velvia 50.xmp`:

| Parameter | Before | After | Reason |
|-----------|--------|-------|--------|
| Vibrance | -5 | removed | Bug-fix: \|Vibrance - Saturation\| must be ≤ 5; community +32.5 with Sat=-5 would violate |
| RedHue (Calibration) | +15 | removed | Bug-fix: no calibration panel |
| RedSaturation (Calibration) | +15 | removed | Bug-fix: no calibration panel |
| GreenHue (Calibration) | -10 | removed | Bug-fix: no calibration panel |
| GreenSaturation (Calibration) | +22.5 | removed | Bug-fix: no calibration panel |
| BlueHue (Calibration) | -10 | removed | Bug-fix: no calibration panel |
| BlueSaturation (Calibration) | +20 | removed | Bug-fix: no calibration panel |

All other attributes were already within 5% of community validated values.

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01 to `Presets/Slide/Fuji Velvia 50.xmp`:

| Parameter | Before | After | Rule |
|-----------|--------|-------|------|
| Blacks2012 | -40 | -30 | Blacks floor -30 |
| Clarity2012 | +22.5 | 0 | Grain protection: GrainAmount>0 → Clarity=0 |
| Texture | -5 | 0 | Grain protection: GrainAmount>0 → Texture=0 |
| Dehaze | +11.3 | removed (0) | Grain protection: GrainAmount>0 → Dehaze=0 |

No other violations. Saturation=-5 within Slide S-curve cap (±5). Boilerplate, calibration ban, HSL caps all pass.

## Community Data Validation

### Validity Assessment: POOR (one critical bogus recommendation)

**Overall Status**: The community-recipes.md is comprehensive and well-structured, but the most widely repeated community recipe (Approach 2, "Velvia in Lightroom Baseline") contains a **critical bogus slider combination** that would trigger the "B&W with one color" selective-color bug.

### Flagged Bogus Data

| # | Severity | Claim | Source | Issue |
|---|----------|-------|--------|-------|
| 1 | **CRITICAL** | Vibrance +20 to +40 combined with Saturation -10 to 0 | r/Lightroom, r/postprocessing (community-recipes.md:53-54) | The gap \|Vibrance − Saturation\| reaches 30-50, far exceeding the ≤ 5 limit (STYLEGUIDE §VIII.5). This desaturates globally (via Saturation) then selectively boosts midtones (via Vibrance), creating a near-monochrome image with one popping hue. The community-recipes.md "Community Validated Values" table itself documents Vibrance +32.5 and Saturation -5 (diff=37.5), which would break any real image. The XMP correctly removed Vibrance entirely per the 5% Alignment Update. |
| 2 | **CRITICAL** | Calibration panel recommended (RedHue +10 to +20, RedSat +10 to +20, GreenHue -5 to -15, GreenSat +15 to +30, BlueHue -5 to -15, BlueSat +15 to +25) | r/Lightroom (community-recipes.md:127-137), darktable community | STYLEGUIDE §VII.7 and AGENTS.md Rule #3 ban calibration for all presets except Canon Color Science. The community claim that "Red Primary changes are what gets you 70% toward the Velvia look" is misleading — calibration compounds with 8 hue shifts and 8 saturation adjustments already in the preset, creating an unpredictable 3×3×3 primary reinterpretation. Correctly removed. |
| 3 | **MODERATE** | Clarity +15 to +30, Dehaze +5 to +15 recommended alongside grain | Various YouTube/community recipes | STYLEGUIDE §V: Clarity/Dehaze amplify all spatial frequencies. When combined with grain, the grain particles get sharpened into jagged digital noise. XMP correctly sets Clarity=0, Dehaze=0. |
| 4 | **MODERATE** | "Fuji in-camera Velvia simulation is widely considered poor" citing Ken Rockwell calling it "AWFUL compared to real VELVIA film" | Ken Rockwell (community-recipes.md:13) | This is Ken Rockwell's opinion, not verified data. Fuji's own simulation is based on their emulsion data — Rockwell's criticism is about matching scanned negatives to slides, not about slider settings. Used as rhetorical support for community calibration values. |
| 5 | **MINOR** | Ken Rockwell's "Digital Settings" section recommends Nikon Picture Control VIVID Saturation +3 and Canon Picture Style STANDARD Saturation +4 | Ken Rockwell (community-recipes.md:20-34) | These are in-camera JPEG settings for Nikon/Canon bodies, not Lightroom slider equivalents. Included in the research document for completeness but not translatable to XMP values. No XMP consequence. |

### Slider Range Check

All XMP values within valid ranges:
- Contrast +40 (0..100) ✓
- Highlights -65 (-100..100) — aggressive but valid ✓
- Shadows -30 (-100..100) ✓
- Blacks -30 (at floor, per STYLEGUIDE §XIII) ✓
- All 8 HSL Saturation values ≤ +35 — well below ±60 cap ✓
- Hue shifts ±22.5 max — within -100..100 ✓
- ColorGrade Shadow Sat 10 — below 30 ✓

### Self-Consistency Check

| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (Vibrance removed; Saturation=-5) |
| GrainAmount > 0 → Sharpness=10 | ✓ (GrainAmount=5, Sharpness=10) |
| GrainAmount > 0 → Clarity=0, Texture=0, Dehaze=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +35) |
| Blacks ≥ -30 | ✓ (at -30) |

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| Ken Rockwell | High (real reviewer, kenrockwell.com) | Low — in-camera settings, not Lightroom |
| r/Lightroom, r/analog | High (archived) | Medium — anecdotal slider recommendations |
| Darktable Velvia module | High (open-source) | Medium — different processing engine |
| YouTube (Jamie Windsor, Sean Tucker) | High (real creators) | Medium — workflow approaches, not specific values |
| VSCO Film 01 reference | Medium (discontinued product) | High — was the gold standard |

### Film Stock Behavior Check

| Behavior | Community Claim | XMP Implementation | Verdict |
|----------|----------------|-------------------|---------|
| Extreme contrast | Contrast +40, Highlights -65 | Applied ✓ | Matches Velvia's high-contrast characteristic curve |
| Hyper-saturated greens | Green Sat +35, Lum -15 | Applied ✓ | Velvia's signature foliage rendering |
| Polarizer-like blue skies | Blue Sat +26.3, Lum -22.5 | Applied ✓ | Consistent with Velvia's spectral sensitivity |
| Yellow→Orange shift | Yellow Hue -17.5 | Applied ✓ | The community's #1 HSL move |
| Deep dMax blacks | Blacks -30 | Applied (capped) | Velvia dMax is famous but STYLEGUIDE floor is -30 |
| Golden hour glow | ColorGrade Highlight Hue 50, Sat 7.5 | Applied ✓ | Subtle warmth for highlights |

### Validation Status: ⚠️ CONDITIONAL PASS (2 critical flags resolved, 1 community recipe section is bogus; documentation corrected)

The **Approach 2 baseline recipe is fundamentally broken** due to the Vibrance-Saturation gap. Users who follow the community-recommended Vibrance +20 to +40 with Saturation -10 to 0 will get the selective-color bug. The XMP correctly removed Vibrance and constrained Saturation to -5. The calibration and WB recommendations were also correctly rejected. The remaining slider values are plausible for a Velvia 50 emulation, but users should be warned that Approach 2 as-documented is harmful.

**Documentation fix (2026-06-01):** Added note to Community Validated Values table clarifying values reflect pre-STYLEGUIDE consensus, not final XMP state. Actual XMP: Blacks=-30, Clarity=0, Texture=0, Dehaze=0, Vibrance removed, Saturation=-5, no calibration.

## References

- r/Lightroom search: "velvia emulation preset" (reddit.com)
- r/photography: "In-Depth Guide to Modern Film Emulation" by u/firstnate
- r/analog community discussions
- Ken Rockwell, "Fuji Velvia 50 Review" (kenrockwell.com)
- Darktable documentation (velvia module)
- VSCO Film 01 discontinued documentation
