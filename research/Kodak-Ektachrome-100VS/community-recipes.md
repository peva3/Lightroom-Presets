# Kodak Ektachrome 100VS — Community Lightroom Recipes

## Overview

E100VS recipes build on standard E100 emulation with enhanced saturation, warmer color grading, and higher contrast. The t3mujinpack reference provides the primary source data for the VS variant.

## t3mujinpack Reference (Primary Source)

The t3mujinpack distinguishes E100VS from standard E100 through increased saturation across red, green, and blue channels, a warmer highlight bias, and stronger overall contrast.

### LR/XMP Implementation

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +45 | High impact (matches standard E100) |
| Highlights2012 | -45 | Strong shoulder roll-off |
| Shadows2012 | -15 | Less crush than Velvia (VS is vivid but not extreme) |
| Blacks2012 | -30 | Deep slide blacks (at floor) |
| Whites2012 | +15 | Clean, bright whites |
| Saturation | +5 | Slide S-curve cap |
| **HSL Hue** (inherited from E100 + tweaks) | | |
| Red | +10 | Warm red shift |
| Orange | -5 | Pull toward red |
| Yellow | -5 | Slight warm shift |
| Green | +15 | Toward teal (E100 signature) |
| Aqua | +10 | Push toward blue |
| Blue | -12.5 | Signature cool-cyan blue |
| Purple | +10 | Warm purples |
| Magenta | +5 | Subtle warmth |
| **HSL Saturation** (VS = boosted) | | |
| Red | +7.5 | Warmer reds than standard E100 (-5) |
| Green | +7.5 | Boosted greens (standard E100 -10) |
| Blue | +15 | Deeper skies than E100 (+7.5) |
| Yellow | +7.5 | Golden-hour pop |
| Magenta | -5 | Control magenta (skin protection) |
| **HSL Luminance** | | |
| Blue | -12.5 | Deep dramatic skies |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 215 / 10 | Cool-cyan shadows (stronger than E100) |
| Highlight Hue/Sat | 50 / 5 | Warm-golden highlights (warmer than E100 45) |
| Balance | -5 | Slight shadow bias |
| **Grain** | Amount 10, Size 25, Roughness 40 | Fine slide grain |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### Key Differences from Standard E100
| Parameter | E100 | E100VS | Reason |
|-----------|------|--------|--------|
| SaturationAdjustmentRed | -5 | +7.5 | VS = vivid reds |
| SaturationAdjustmentGreen | -10 | +7.5 | VS = saturated greens |
| SaturationAdjustmentBlue | +7.5 | +15 | VS = deeper blues |
| ColorGradeHighlightHue | 45 | 50 | Warmer highlights |
| ColorGradeShadowSat | 7.5 | 10 | Stronger shadow color |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- No Vibrance (avoids gap issue) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks -30 (at floor) ✓
- HSL Sat ≤ ±60 (max +15) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- t3mujinpack — E100VS profile
- Kodak Ektachrome E100VS datasheet
- Ektachrome family comparison research

---

## See Also

- [Kodak Ektachrome 100VS — Film Characteristics](../Kodak-Ektachrome-100VS/characteristics.md)
- [Kodak Ektachrome E100 Lightroom Preset](../Kodak-Ektachrome-E100/community-recipes.md)
- [Kodak Ektachrome 320T Lightroom Preset](../Kodak-Ektachrome-320T/community-recipes.md)
- [Kodak Ektachrome 64 Lightroom Preset](../Kodak-Ektachrome-64/community-recipes.md)
- [XMP Preset: Kodak Ektachrome 100VS](../../Presets/Slide/Kodak Ektachrome 100VS.xmp)
