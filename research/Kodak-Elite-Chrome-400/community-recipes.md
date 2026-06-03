# Kodak Elite Chrome 400 — Community Lightroom Recipes

## Overview

Elite Chrome 400 recipes are essentially non-existent in the community — the film was a consumer product discontinued before the digital era's film emulation trend. The t3mujinpack reference provides the primary source data.

## t3mujinpack Reference (Primary Source)

The t3mujinpack treats Elite Chrome 400 as a warm, moderate-contrast, consumer-grade 400-speed slide film — the Kodak consumer counterpart to Fuji Sensia but at higher speed.

### LR/XMP Implementation

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +25 | Moderate consumer-slide contrast |
| Highlights2012 | -17.5 | Moderate highlight compression |
| Shadows2012 | -20 | Moderate shadow depth |
| Blacks2012 | -25 | Consumer slide blacks |
| Whites2012 | +10 | Modest white point |
| Saturation | +5 | Slide S-curve cap |
| **HSL Hue** | | |
| Yellow | -5 | Slight warm shift (toward orange) |
| **HSL Saturation** | | |
| Green | -5 | Naturalize foliage (consumer palette) |
| Yellow | +5 | Subtle golden warmth |
| **HSL Luminance** | | |
| Orange | +7.5 | Creamy warm skin |
| Blue | -7.5 | Subtle sky depth |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 50 / 7.5 | Warm shadows (consumer palette) |
| Highlight Hue/Sat | 45 / 5 | Warm-golden highlights |
| **Grain** | Amount 20, Size 25, Roughness 45 | 400-speed consumer slide grain |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- No Vibrance (avoids gap issue) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks ≥ -30 (at -25) ✓
- HSL Sat ≤ ±60 (max +5) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- t3mujinpack — Elite Chrome 400 profile
- Kodak Elite Chrome 400 datasheet
- Sensia 100 recipe (consumer slide baseline)
- Provia 400X recipe (400-speed slide baseline)

---

## See Also

- [Kodak Elite Chrome 400 — Film Characteristics](../Kodak-Elite-Chrome-400/characteristics.md)
- [Kodak Ektachrome 400X Lightroom Preset](../Kodak-Ektachrome-400X/community-recipes.md)
- [Kodak Ektachrome E100 Lightroom Preset](../Kodak-Ektachrome-E100/community-recipes.md)
- [XMP Preset: Kodak Elite Chrome 400](../../Presets/Slide/Kodak Elite Chrome 400.xmp)
