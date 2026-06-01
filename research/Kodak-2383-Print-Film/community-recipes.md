# Kodak 2383 Print Film — Community Recipes

## Source
ACES 2383 PFE Reference Data: https://github.com/ampas/aces-dev

## ACES 2383 Print Film Emulation (PFE) Reference
Kodak Vision Color Print Film 2383 is the #1 cinema print film used for theatrical release prints. The ACES Print Film Emulation (PFE) transform mathematically models this film's characteristics.

### Print Film Density Characteristics (2383)
- **White Point**: warm, ~D55-D60 (cinema projector lamps are ~5400K with warm shift)
- **Shadow Tint**: cool cyan-green (complementary to warm highlights, the defining "print film look")
- **Contrast**: aggressive S-curve with distinct toe and shoulder rolloffs
- **Saturation**: subtractive behavior — peaks in midtones (~25-65% luminance), rolls off near black and white
- **Black Density**: deep, rich with subtle detail retention (not clipped)
- **Gamut**: slightly compressed vs scene-referred digital; gentle roll-off at gamut boundary

### Standard 2383 Print Density Curve (Status M)
D-min: ~0.10 (deep blacks with slight density)
Mid-scale gamma: ~2.8-3.2 (aggressive contrast)
D-max: ~3.2-3.5 (dense blacks)

## XMP Translation
The ACES 2383 look is translated to LR sliders:
1. Warm WB (D60 → Temperature 5800, Tint +5)
2. Aggressive S-curve Tone Curve (deeper toe/shoulder than standard cinematic)
3. Cool cyan-green shadow Color Grading (H180/S20)
4. Warm highlight Color Grading (H42/S12)
5. Subtractive saturation (Saturation -5, selective HSL)
6. Dense blacks with smooth toe
