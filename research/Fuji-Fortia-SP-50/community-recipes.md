# Fuji Fortia SP 50 — Community Lightroom Recipes

## Overview

Fortia SP 50 is among the rarest slide films ever produced — community recipes are essentially non-existent. The t3mujinpack reference provides the only structured emulation data. This preset is built by taking Velvia 50's recipe and amplifying saturation, hue shifts, and contrast to Fortia SP's "beyond Velvia" level.

## t3mujinpack Reference (Primary Source)

The t3mujinpack treats Fortia SP as Velvia 50 with the saturation, contrast, and warmth dialed beyond normal limits.

### LR/XMP Implementation

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +45 | Higher contrast than Velvia (+40) |
| Highlights2012 | -70 | Aggressive highlight protection |
| Shadows2012 | -35 | Deep shadow crush |
| Blacks2012 | -30 | At slide floor |
| Whites2012 | +17.5 | Bright pop |
| Saturation | +5 | Slide S-curve cap |
| **HSL Hue** (Velvia + enhanced shifts) | | |
| Red | +20 | Strong red→orange warmth |
| Orange | -15 | Pull toward red |
| Yellow | -22.5 | Strong yellow→orange (signature move) |
| Green | +27.5 | Deep emerald green |
| Aqua | +17.5 | Push to blue |
| Blue | -10 | Slight cyan shift |
| Purple | +17.5 | Warm purples |
| Magenta | +12.5 | Warm magentas |
| **HSL Saturation** (Beyond Velvia levels) | | |
| Red | +30 | Hyper-saturated reds |
| Orange | +25 | Intense warm tones |
| Yellow | +15 | Golden saturation |
| Green | +42 | Maximum green intensity |
| Aqua | -20 | Suppress cyan (purer greens/blues) |
| Blue | +32 | Deep polarized skies |
| Purple | +20 | Flower intensity |
| Magenta | +25 | Magenta pop |
| **HSL Luminance** | | |
| Green | -17.5 | Deepen foliage |
| Aqua | -17.5 | Darken cyan/skies |
| Blue | -25 | Deep dark blue skies |
| Orange | +7.5 | Bright warm tones |
| Yellow | +7.5 | Luminous golds |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 230 / 12.5 | Strong cool-blue shadows |
| Highlight Hue/Sat | 50 / 10 | Strong warm-golden highlights |
| Balance | -5 | Shadow bias |
| **Grain** | Amount 5, Size 15, Roughness 40 | ISO 50 = ultra-fine grain |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### Key Differences from Velvia 50
| Parameter | Velvia 50 | Fortia SP 50 | Reason |
|-----------|-----------|--------------|--------|
| Contrast2012 | +40 | +45 | Higher contrast |
| Highlights2012 | -65 | -70 | More highlight protection |
| Shadows2012 | -30 | -35 | More shadow crush |
| HueAdjustmentRed | +15 | +20 | Stronger warm shift |
| HueAdjustmentOrange | -10 | -15 | Stronger shift |
| HueAdjustmentYellow | -17.5 | -22.5 | Stronger yellow→orange |
| SaturationAdjustmentGreen | +35 | +42 | Beyond Velvia green |
| SaturationAdjustmentRed | +22.5 | +30 | Beyond Velvia red |
| SaturationAdjustmentBlue | +26.3 | +32 | Beyond Velvia blue |
| ColorGradeShadowSat | 10 | 12.5 | Stronger shadow cooling |
| ColorGradeHighlightSat | 7.5 | 10 | Stronger highlight warming |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- No Vibrance (avoids gap issue) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks -30 (at floor) ✓
- HSL Sat ≤ ±60 (max +42, well within cap) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- t3mujinpack — Fortia SP 50 profile
- Velvia 50 community recipe (baseline)
- r/analog — rare Fortia SP images

---

## See Also

- [Fuji Fortia SP 50 — Film Characteristics](../Fuji-Fortia-SP-50/characteristics.md)
- [Fuji Velvia 50 Lightroom Preset](../Fuji-Velvia-50/community-recipes.md)
- [Fuji Velvia 100 Lightroom Preset](../Fuji-Velvia-100/community-recipes.md)
- [Fuji Astia 100F Lightroom Preset](../Fuji-Astia-100F/community-recipes.md)
- [XMP Preset: Fuji Fortia SP 50](../../Presets/Slide/Fuji Fortia SP 50.xmp)
