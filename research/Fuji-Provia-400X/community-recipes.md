# Fuji Provia 400X — Community Lightroom Recipes

## Overview

Provia 400X recipes are rare in the community — the film was produced in limited quantities and discontinued early. The t3mujinpack reference pack includes Provia 400X as a distinct profile, serving as the primary source for this preset.

## t3mujinpack Reference (Primary Source)

The t3mujinpack profiles capture the Provia 400X look as a higher-speed variant of Provia 100F with marginally less saturation, slightly higher contrast, and visible but fine grain structure.

### LR/XMP Implementation

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +22.5 | Slightly higher than Provia 100F (+20) |
| Highlights2012 | -20 | 400-speed highlight compression |
| Shadows2012 | -25 | Deep slide shadows |
| Blacks2012 | -27.5 | Near the -30 floor (slide dMax) |
| Whites2012 | +12.5 | Clean whites |
| Saturation | +5 | Slide S-curve cap |
| **HSL Hue** | | |
| Blue | -5 | Provia-family cool-blue shift |
| **HSL Saturation** | | |
| Green | -5 | Naturalize foliage |
| Blue | +3.8 | Subtle sky depth (less than 100F +5) |
| **HSL Luminance** | | |
| Blue | -10 | Deep slide-film skies |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 220 / 6.3 | Cool-blue shadows (Provia family) |
| Highlight Hue/Sat | 45 / 3.8 | Subtle warm highlights |
| **Grain** | Amount 20, Size 20, Roughness 40 | 400-speed slide grain |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### Key Differences from Provia 100F
| Parameter | Provia 100F | Provia 400X | Reason |
|-----------|-------------|-------------|--------|
| Contrast2012 | +20 | +22.5 | Higher-speed = higher contrast |
| Highlights2012 | -15 | -20 | More highlight compression |
| GrainAmount | 10 | 20 | 400 vs 100 speed grain |
| GrainSize | 15 | 20 | Larger grain at higher ISO |
| SaturationAdjustmentBlue | +5 | +3.8 | Slightly less saturation |
| Vibrance | +5 | (removed) | No CCE on 400X recipe |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- No Vibrance (no Vibrance-Saturation gap issue) ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks ≥ -30 (at -27.5) ✓
- HSL Sat ≤ ±60 (max +5) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- t3mujinpack — Provia 400X profile
- Fujifilm Provia 400X technical datasheet

---

## See Also

- [Fuji Provia 400X — Film Characteristics](../Fuji-Provia-400X/characteristics.md)
- [Fuji Velvia 50 Lightroom Preset](../Fuji-Velvia-50/community-recipes.md)
- [Fuji Velvia 100 Lightroom Preset](../Fuji-Velvia-100/community-recipes.md)
- [Fuji Astia 100F Lightroom Preset](../Fuji-Astia-100F/community-recipes.md)
- [XMP Preset: Fuji Provia 400X](../../Presets/Slide/Fuji Provia 400X.xmp)
