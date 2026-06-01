# Fuji Provia 100F — Community Lightroom Recipes

## Fuji X Weekly Recipe (Primary Source)

The Fuji X Weekly community has developed in-camera recipes for Fuji X/GFX cameras that emulate Provia's slide film look. The parameters below represent the Fuji→Lightroom translation using the standard mapping.

### Fuji X Weekly Parameters
| Parameter | Value | LR Translation |
|-----------|-------|----------------|
| Film Simulation | Classic Chrome | Adobe Vivid (Slide) |
| DR | DR400 | Highlights extra -5 |
| Highlight | -1 | Highlights2012 -15 (incl DR400) |
| Shadow | +3 | Shadows2012 -30 (inverted) |
| Color | +4 | Saturation +5 (S-curve cap) |
| Noise Reduction | -4 | NR -4 |
| Sharpness | -1 | Sharpness 10 (grain cap) |
| Clarity | -3 | Clarity 0 (grain rule) |
| Grain | Weak / Small | GrainAmount 10, GrainSize 15 |
| Color Chrome Effect | Strong | Vibrance +5 |
| Color Chrome FX Blue | Strong | Extra blue channel boost |
| WB Shift | Day -2R +5B | Cool-leaning balance |

### LR/XMP Implementation (Final Values)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +20 | Moderate slide contrast |
| Highlights2012 | -15 | H-1 + DR400 (-5) |
| Shadows2012 | -30 | S+3 inverted |
| Blacks2012 | -25 | Deep slide blacks (above -30 floor) |
| Whites2012 | +12.5 | Clean whites |
| Saturation | +5 | Color+4 capped (S-curve rule) |
| Vibrance | +5 | CCE Strong |
| **HSL Hue** | | |
| Blue | -5 | Slight cyan shift (Provia blue) |
| **HSL Saturation** | | |
| Green | -5 | Naturalize foliage |
| Blue | +5 | Subtle sky boost |
| **HSL Luminance** | | |
| Blue | -10 | Deeper skies |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 220 / 6.3 | Cool-blue shadows |
| Highlight Hue/Sat | 45 / 3.8 | Subtle warm highlights |
| **Grain** | Amount 10, Size 15, Roughness 40 | Weak/Small (slide = fine grain) |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- Vibrance within 5 of Saturation (diff=0) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks ≥ -30 (at -25) ✓
- HSL Sat ≤ ±60 (max +5) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- Fuji X Weekly (fujixweekly.com): Provia 100F recipe
- r/analog, r/Lightroom community discussions
- Fujifilm RDP III datasheet
