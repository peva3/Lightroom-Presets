# Vibrant Color Pop — Community Recipes

## Source
Cinemora Presets: https://cinemorapresets.com/color-pop-lightroom-presets

## Published Slider Values (Source)
Exposure: +0.15 | Contrast: +10 | Highlights: -20 | Shadows: +12 | Whites: +5 | Blacks: -8 | Vibrance: +35 | Saturation: +12 | Clarity: +8

## STYLEGUIDE Adjustment
Source Vibrance +35 / Saturation +12 gap = 23, exceeding the |Vibrance-Saturation| ≤ 5 rule. This gap would create the "selective-color" bug (near-monochrome with one popping hue). Fixed by raising Saturation to +30 to match Vibrance within 5 points, preserving the "maximum color impact" intent while preventing the bug.

## Description
Vibrant Color Pop preset. The most saturated preset in the collection, designed to make colors vivid and punchy while maintaining skin tone protection via Vibrance bias. High saturation + vibrance for maximum color impact. Moderate clarity for color definition. Gentle contrast to avoid crushing saturated tones. HSL boosts across red, orange, yellow, and blue for full-spectrum color enhancement.

## XMP Translation Notes
- No WB (color pop, not WB-dependent)
- Blacks -8 from source → Blacks 0 (double-fade prevention)
- Sat adjusted to +30 (from +12) to match Vib +35 within 5-point rule
- HSL boosts across warm + blue channels for full-spectrum pop
- ColorGrade: cool shadows + warm highlights for color contrast
