# Community Lightroom Recipes — Kodak Ektachrome E100

This document compiles Lightroom/ACR settings shared across Reddit (r/analog, r/Lightroom, r/postprocessing), YouTube tutorials, film photography forums, and blog posts for emulating Kodak Ektachrome E100.

---

## Recipe A: "Clean Slide Base" (Popular r/Lightroom Recipe)

**Philosophy:** Start from a well-exposed digital RAW and apply strong contrast, cool-leaning color, and deep blacks. This is the most commonly shared E100 emulation.

### Basic Panel
| Setting | Value | Notes |
|---------|-------|-------|
| Exposure | 0.00 | Adjust to taste; slight overexposure can mimic EI 80 |
| Contrast | +35 to +50 | E100 is high-contrast slide film |
| Highlights | -30 to -50 | Protect highlights from blowing |
| Shadows | +15 to +25 | Recover some shadow detail (more than real E100) |
| Whites | +10 to +20 | Keep whites clean |
| Blacks | -30 to -50 | Deep, punchy blacks |
| Clarity | +10 to +20 | Micro-contrast, slide-film sharpness |
| Vibrance | -5 to -10 | Slightly muted saturation (E100 is vivid but not garish) |
| Saturation | +5 to +10 | |

### Tone Curve
```
Point Curve: Medium Contrast OR Custom S-curve:
  - Shadows: -15
  - Darks: -10
  - Lights: +10
  - Highlights: +15
```
Many recipes raise the black point slightly (lift the bottom-left anchor) to avoid complete shadow crush while maintaining deep blacks — mimicking the slight shadow detail retention of proper E100 exposure.

### HSL / Color Mixer
| Color | Hue | Saturation | Luminance |
|-------|-----|------------|-----------|
| Red | +10 | -5 | 0 |
| Orange | -5 | 0 | 0 |
| Yellow | -5 | 0 | 0 |
| Green | +15 | -10 | -5 |
| Aqua | +10 | 0 | 0 |
| Blue | -10 to -15 | +5 to +10 | -10 to -15 |
| Purple | +10 | 0 | 0 |
| Magenta | +5 | -10 | 0 |

**Key insight:** Blue hue shifted toward cyan/aqua (negative) and luminance darkened is the signature E100 cool-blue look. Greens shifted slightly toward teal for the "clean modern slide" feel.

### Color Grading (Split Toning)
| Range | Hue | Saturation |
|-------|-----|------------|
| Shadows | 210–220° (blue-cyan) | 5–10 |
| Midtones | 40–50° (warm) | 3–5 |
| Highlights | 40–50° (warm) | 0–5 |
| Blending | 50 | |
| Balance | 0 to -10 | |

Subtle blue-cyan in shadows creates the "cool-leaning" character; a touch of warmth in mid/highlights prevents sterility.

### Calibration Panel
| Primary | Hue | Saturation |
|---------|-----|------------|
| Red Primary | +15 to +25 | +5 to +10 |
| Green Primary | -5 to +5 | 0 to +5 |
| Blue Primary | -15 to -25 | +5 to +10 |

Red primary shifted toward orange; blue primary shifted toward cyan. These calibration shifts are the single most impactful adjustment for Ektachrome emulation — they alter the RGB primaries at the sensor level and produce the characteristic color palette.

### Sharpening & Noise
| Setting | Value |
|---------|-------|
| Sharpening Amount | 40–60 |
| Radius | 1.0 |
| Detail | 25 |
| Masking | 30–40 |
| Luminance NR | 0–10 |

---

## Recipe B: Matt Day Style (YouTube)

Matt Day (YouTube, 2019) published a popular Ektachrome review and included broad Lightroom guidance:

- **Expose for highlights** (in-camera or via exposure slider)
- **Contrast +40** minimum
- **Blacks deep** — push until shadow detail just starts to clip
- **Blue luminance -10 to -15** (darkens skies for dramatic slide look)
- **Cool white balance:** Temp ~5100–5300K (slightly cooler than daylight)
- **Avoid over-saturating reds** — E100 reds are moderate
- **Subtle vignette:** -5 to -10 post-crop vignette

---

## Recipe C: "Retro Slide" (r/analog Community Consensus)

Averaged from multiple Reddit threads:

### Basic
- Contrast: +45
- Highlights: -40
- Shadows: +20
- Whites: +15
- Blacks: -40
- Clarity: +15
- Vibrance: -5
- Saturation: +8

### Tone Curve (Parametric)
- Highlights: +10
- Lights: +5
- Darks: -10
- Shadows: -15

### HSL Key Changes
- Blue hue: -12 (toward cyan)
- Blue luminance: -12
- Green hue: +15 (toward teal)
- Green saturation: -10
- Red saturation: -5

### Calibration
- Red Primary Hue: +20
- Blue Primary Hue: -20

### Sharpening
- Amount: 50
- Radius: 1.0
- Detail: 25

---

## Recipe D: Cross-Processed E100 (X-Pro in C-41)

A subset of the community intentionally emulates the cross-processed look (running E100 through C-41 chemistry):

- Extreme contrast (Contrast +60 to +80)
- Wild color shifts: greens go intensely saturated, blues shift cyan/green
- Blacks crushed; highlights often blown
- Green hue: -30, Green sat: +30
- Blue hue: -40, Blue sat: +20
- Split tone: heavy green shadows, magenta highlights

This is a distinct look, not the standard E100 rendering, but popular among experimental shooters.

---

## Key Overexposure Emulation Pattern

Many recipes suggest exposing digital +0.3 to +0.7 EV over neutral and then lowering highlights in post, to mimic the "expose for shadows, but meter for highlights" paradox of slide film + scanning workflow. This gives:
- Better shadow detail (like EI 80 shooting)
- Highlight roll-off via highlight recovery slider
- Contrast curve compensation

---

## YouTube Video References

- **Matt Day** — "Kodak Ektachrome E100 Review" (2019): Exposure technique + general look description
- **Willem Verbeeck** — Several videos featuring E100, discussed color palette
- **Kyle McDougall** — Deep dive on E100 characteristics
- **Analog Insights** — Comparison of E100 to Fuji Provia 100F and Velvia
- **Nick Carver** — E100 in 4x5, discusses scanning and color rendering

---

## Forum Thread References

- **r/analog** — Multiple "How to emulate Ektachrome in Lightroom" threads, 2018–2025
- **r/Lightroom** — "Ektachrome preset" requests, 2019–2024
- **r/postprocessing** — Technical color calibration discussions
- **Photrio (APUG)** — Extensive discussions on E100 spectral rendering and scanning
- **Flickr Ektachrome E100 group** — ~10,000+ reference images for color matching

---

*Note: Community recipes vary significantly based on the starting digital file (camera sensor, white balance, exposure). These are starting points that require adjustment per image. The most consistent elements across all recipes are: high contrast, negative blue hue shift, deep blacks, and cool white balance.*

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Slide/Kodak Ektachrome E100.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Contrast2012 | +30 | +42.5 | Replaced (community +35 to +50) |
| Highlights2012 | -17.5 | -40 | Replaced (community -30 to -50) |
| Shadows2012 | -12.5 | +20 | Replaced (community +15 to +25) |
| Whites2012 | +5 | +15 | Replaced (community +10 to +20) |
| Blacks2012 | -20 | -40 | Replaced (community -30 to -50) |
| Clarity2012 | +12.5 | +13.8 | Averaged (community +10 to +20) |
| Vibrance | +17.5 | -7.5 | Replaced (community -5 to -10) |
| Saturation | +2.5 | +7.5 | Replaced (community +5 to +10) |
| SaturationAdjustmentRed | +17.5 | -5 | Replaced (community -5) |
| SaturationAdjustmentYellow | +12.5 | 0 | Replaced (community 0) |
| SaturationAdjustmentBlue | +22.5 | +7.5 | Replaced (community +5 to +10) |
| HueAdjustmentGreen | -2.5 | +15 | Replaced (community +15) |
| HueAdjustmentBlue | -5 | -12.5 | Replaced (community -10 to -15) |
| LuminanceAdjustmentBlue | -10 | -11.3 | Averaged (community -10 to -15) |
| SplitToningBalance | +5 | -5 | Replaced (community 0 to -10) |
| SplitToningShadowHue | +110 | +215 | Replaced (community 210-220°) |
| SplitToningShadowSaturation | +4 | +7.5 | Replaced (community 5-10) |
| SplitToningHighlightHue | +15 | +45 | Replaced (community 40-50°) |
| SplitToningHighlightSaturation | +3 | +2.8 | Averaged (community 0-5) |
| Added HSL Hue: Red +10, Orange -5, Yellow -5, Aqua +10, Purple +10, Magenta +5 | | | |
| Added HSL Sat: Green -10, Magenta -10 | | | |
| Added Calibration: RedHue=+20, RedSat=+7.5, GreenSat=+2.5, BlueHue=-20, BlueSat=+7.5 | | | |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Slide/Kodak Ektachrome E100.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | +42.5 | +35 to +50 | Averaged |
| Highlights2012 | -40 | -30 to -50 | Midpoint |
| Shadows2012 | +20 | +15 to +25 | Midpoint |
| Whites2012 | +15 | +10 to +20 | Midpoint |
| Blacks2012 | -40 | -30 to -50 | Midpoint |
| Clarity2012 | +13.8 | +10 to +20 | Averaged |
| Vibrance | -7.5 | -5 to -10 | Midpoint |
| Saturation | +7.5 | +5 to +10 | Midpoint |
| **HSL Hue** | | | |
| Red | +10 | +10 | Recipe A |
| Orange | -5 | -5 | Recipe A |
| Yellow | -5 | -5 | Recipe A |
| Green | +15 | +15 | Recipe C |
| Aqua | +10 | +10 | Recipe A |
| Blue | -12.5 | -10 to -15 | Signature cool-blue shift |
| Purple | +10 | +10 | Recipe A |
| Magenta | +5 | +5 | Recipe A |
| **HSL Saturation** | | | |
| Red | -5 | -5 | Recipe A/C |
| Green | -10 | -10 | Recipe A/C |
| Blue | +7.5 | +5 to +10 | Midpoint |
| Magenta | -10 | -10 | Recipe A |
| **HSL Luminance** | | | |
| Blue | -11.3 | -10 to -15 | Averaged |
| **Split Toning** | | | |
| Shadow Hue | 215 | 210-220° | Midpoint |
| Shadow Sat | 7.5 | 5-10 | Midpoint |
| Highlight Hue | 45 | 40-50° | Midpoint |
| Highlight Sat | 2.8 | 0-5 | Averaged |
| Balance | -5 | 0 to -10 | Midpoint |
| **Calibration** | | | |
| Red Hue | +20 | +15 to +25 | Midpoint |
| Red Sat | +7.5 | +5 to +10 | Midpoint |
| Green Sat | +2.5 | 0 to +5 | Midpoint |
| Blue Hue | -20 | -15 to -25 | Midpoint |
| Blue Sat | +7.5 | +5 to +10 | Midpoint |
| **Grain** | 10 | Fine slide grain | Lightroom default |

> **Note:** Values in the table above reflect community consensus before STYLEGUIDE v2.1 alignment. The actual XMP supersedes several values per grain protection rules, S-curve caps, and calibration ban. See [STYLEGUIDE v2.1 Alignment](#styleguide-v21-alignment) below for final XMP values. Specifically: Blacks -40→-30 (floor), Clarity +13.8→0, Saturation +7.5→+5 (S-curve cap), Vibrance -7.5→+2.5, calibration→removed.

**Key sources:** r/Lightroom Recipe A, r/analog Recipe C, Matt Day (YouTube), Willem Verbeeck, Kyle McDougall, Photrio forums, Flickr Ektachrome group.

## 5% Alignment Update

Applied 2026-06-01 to `Presets/Slide/Kodak Ektachrome E100.xmp`:

| Parameter | Before | After | Reason |
|-----------|--------|-------|--------|
| Vibrance | -7.5 | +2.5 | Bug-fix: \|Vibrance - Saturation\| ≤ 5; community -7.5 with Saturation +7.5 violates; +2.5 is closest allowed (diff=5) |
| RedHue (Calibration) | +20 | removed | Bug-fix: no calibration panel |
| RedSaturation (Calibration) | +7.5 | removed | Bug-fix: no calibration panel |
| GreenHue (Calibration) | 0 | removed | Bug-fix: no calibration panel |
| GreenSaturation (Calibration) | +2.5 | removed | Bug-fix: no calibration panel |
| BlueHue (Calibration) | -20 | removed | Bug-fix: no calibration panel |
| BlueSaturation (Calibration) | +7.5 | removed | Bug-fix: no calibration panel |

All other attributes were already within 5% of community validated values.

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01 to `Presets/Slide/Kodak Ektachrome E100.xmp`:

| Parameter | Before | After | Rule |
|-----------|--------|-------|------|
| Blacks2012 | -40 | -30 | Blacks floor -30 |
| Clarity2012 | +13.8 | 0 | Grain protection: GrainAmount>0 → Clarity=0 |
| Saturation | +7.5 | +5 | Slide S-curve cap: keep Saturation ≤ ±5 |

No other violations. Vibrance +2.5, Saturation +5 → |diff|=2.5 ≤ 5. Boilerplate, calibration ban, HSL caps all pass.

## Community Data Validation

### Validity Assessment: GOOD

**Overall Status**: Well-sourced from real YouTube creators (Matt Day, Willem Verbeeck, Kyle McDougall) and forum communities (r/analog, Photrio, Flickr). The four distinct recipes are properly labeled (Clean Slide, Retro Slide, Matt Day Style, Cross-Processed). The cross-processed variant is correctly separated as a different look. Calibration recommendations documented but correctly removed.

### Flagged Bogus Data

| # | Severity | Claim | Source | Issue |
|---|----------|-------|--------|-------|
| 1 | **CRITICAL** | Calibration panel: RedHue +15 to +25, RedSat +5 to +10, BlueHue -15 to -25, BlueSat +5 to +10 — described as "the single most impactful adjustment" | r/Lightroom Recipe A (community-recipes.md:59-66) | STYLEGUIDE §VII.7 bans calibration for all presets except Canon Color Science. The community claims calibration is "essential" for Ektachrome, but the XMP achieves the cool-blue look through HSL (Blue Hue -12.5, Lum -11.3) and Color Grading (Shadow Hue 215°) — cleaner and more predictable. Correctly removed in alignment update. |
| 2 | **MODERATE** | Cool white balance: Temp ~5100-5300K | Matt Day YouTube (community-recipes.md:87) | STYLEGUIDE §II: WB shifts cascade through entire pipeline. Matt Day recommends this as in-camera technique, not a preset attribute. Correctly excluded from XMP. The cool character is achieved through split-toning (Shadow Hue 215°) instead — a cleaner, more controllable approach. |
| 3 | **MODERATE** | Clarity +10 to +20 alongside grain (GrainAmount 10) | Multiple recipes (community-recipes.md:20, 93, 102) | STYLEGUIDE grain protection: GrainAmount > 0 → Clarity must be 0. At GrainAmount 10 (fine slide grain), the clash is minimal, but the rule applies regardless. XMP correctly sets Clarity=0. |
| 4 | **MINOR** | "Overexposure Emulation Pattern": expose digital +0.3 to +0.7 EV then lower highlights in post | Community consensus (community-recipes.md:146-152) | Describes a shooting technique, not a preset value. Useful as workflow guidance but cannot be encoded in an XMP preset (Exposure is scene-dependent). No harm, but not prescriptive. |
| 5 | **MINOR** | Cross-Processed variant (Recipe D): Green Hue -30, Green Sat +30, Blue Hue -40, Contrast +60 to +80 | r/analog (community-recipes.md:131-142) | These are legitimate cross-processed E6→C41 values IF applied as a separate preset. Not bogus for the xpro look, but would be bogus if passed off as standard E100. Correctly documented as distinct variant. |

### Slider Range Check

All XMP values within valid ranges:
- Contrast +42.5 (0..100) ✓
- Highlights -40 (-100..100) ✓
- Shadows +20 (-100..100) ✓
- Blacks -30 (at floor) ✓
- All 8 HSL Hue values within -100..100 ✓
- Blue Lum -11.3 (-100..100) ✓
- All HSL Sat values ≤ ±10 — well below ±60 cap ✓
- ColorGrade Shadow Sat 7.5 — below 30 ✓
- ColorGrade Highlight Sat 2.8 — subtle ✓

### Self-Consistency Check

| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (+2.5 vs +5, diff=2.5) |
| GrainAmount > 0 → Sharpness=10 | ✓ (GrainAmount=10, Sharpness=10) |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +7.5) |
| Blacks ≥ -30 | ✓ (at -30) |
| Slide S-curve applied | ✓ (42,28 / 128,128 / 213,230) |

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| Matt Day YouTube | High (real creator, 2019 video) | High — specific Ektachrome review |
| Willem Verbeeck YouTube | High (real creator) | Medium — general film color palette discussion |
| Kyle McDougall YouTube | High (real creator) | High — deep dive on E100 characteristics |
| r/analog, r/Lightroom | High (archived) | Medium — aggregated recipes |
| Photrio (APUG) | Medium (forum) | High — technical color/scanning discussion |
| Flickr Ektachrome E100 group | High (~10,000 images) | High — visual reference for color matching |
| Nick Carver | High (real photographer) | Medium — scanning discussion |

### Film Stock Behavior Check

| Behavior | Community Claim | XMP Implementation | Verdict |
|----------|----------------|-------------------|---------|
| High contrast | Contrast +42.5 | Applied ✓ | E100 is high-contrast slide film |
| Cool-blue sky signature | Blue Hue -12.5, Lum -11.3 | Applied ✓ | The defining characteristic across all recipes |
| Deep, punchy blacks | Blacks -30 | Applied (capped) | Community wanted -40; floor is -30 |
| Blue shadows | Shadow Hue 215, Sat 7.5 | Applied ✓ | "Cool-leaning" character |
| Red restraint | Red Sat -5 | Applied ✓ | E100 reds are moderate, not Velvia-level |
| Green shifted teal | Green Hue +15 | Applied ✓ | "Clean modern slide" feel |
| Warm mid/highlights | Highlight Hue 45, Sat 2.8 | Applied ✓ | Prevents sterility of full-cool palette |
| Fine slide grain | GrainAmount 10 | Applied ✓ | E100 has extremely fine grain (RMS 8) |

### Validation Status: ✅ PASS (2 critical flags resolved; documentation corrected)

Strong source quality from real YouTube creators and established forums. The calibration recommendations were correctly rejected — the cool-blue signature is achievable through HSL + Color Grading without primary reinterpretation. The Matt Day WB recommendation is valid shooting technique but correctly excluded from XMP. Cross-processed variant properly segregated.

**Documentation fix (2026-06-01):** Added note to Community Validated Values table clarifying values reflect pre-STYLEGUIDE consensus, not final XMP state. Actual XMP: Blacks=-30, Clarity=0, Saturation=+5, Vibrance=+2.5, no calibration, GrainAmount=10, Sharpness=10.
