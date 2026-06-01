# Fuji Superia 200 — Community Recipes & Lightroom Settings

## Overview

Fuji Superia 200 sits between Superia 100 and 400 in the Fuji consumer lineup. This preset is derived from the Superia 100 Fuji X Weekly recipe, adjusted toward Superia 400 characteristics to capture the "middle child" balance of the 200-speed emulsion.

## Reference Recipe: Fuji X Weekly Superia 100 (adapted)

The Superia 100 recipe provides the baseline; values are interpolated between 100 and 400 characteristics:

- **From Superia 100**: Classic Negative base, fine grain, cool-neutral balance, moderate contrast
- **Toward Superia 400**: More grain, warmer midtones, stronger green shadow, more saturation

## Fuji→Lightroom Translation (Interpolated)

| Fuji Setting | 100 Value | 200 Value (interpolated) | 400 Value |
|---|---|---|---|
| Grain Effect | Weak, Small | Weak-Medium, Small-Medium | Strong, Small |
| Color Chrome Effect | Strong | Weak | Off |
| Highlight | -1 | -1.5 | 0 |
| Shadow | -2 | -1.5 | -1 |
| Color | +1 | +2 | +4 |
| Sharpness | -2 | -1 | -1 |
| Clarity | -2 | -1 | -2 |

### Lightroom Mapping for Superia 200

| Fuji Setting | Lightroom Attribute | Value |
|---|---|---|
| Grain | GrainAmount | 23 |
| Grain | GrainSize | 22 |
| Grain | GrainFrequency | 50 |
| CCE Weak | Vibrance | +2 (interpolated) |
| Highlight -1.5 | Highlights2012 | -15 |
| Shadow -1.5 | Shadows2012 | +15 (inverted) |
| Color +2 | Saturation | +10 |
| Sharpness -1 | Sharpness | 7.5 → 8 |

## Core Emulation Philosophy

Superia 200 balances the lineup:
1. **Cool-neutral Fuji cast** — warmer than 100, cooler than 400
2. **Fine-to-moderate grain** — present but not distracting
3. **Moderate green shadow** — less than 400, more than 100
4. **Magenta-red push** at moderate intensity
5. **Consumer contrast** — between 100 (high) and 400 (moderate)

## Applied Lightroom Values

### Basic Panel
- Exposure: +0.40 (between 100's +0.50 and 400's 0)
- Contrast: +12 (between 100's +8 and 400's +15)
- Highlights: -15 (interpolated)
- Shadows: +18 (interpolated)
- Blacks: -2 (between -5 and +5)
- Whites: 0
- Saturation: +8
- Vibrance: +10 (gap=2)

### HSL / Color Mixer
- Red Sat: +8
- Red Hue: -7 (toward magenta — between 100's -5 and 400's -10)
- Green Sat: +5 (Fuji consumer green)
- Blue Sat: +3
- Blue Hue: -4 (toward cyan)

### Color Grading (Blending 50)
- Shadow Hue: 135, Sat: 12 (moderate green shadow)
- Highlight Hue: 38, Sat: 5 (subtle warmth)

### Grain
- Amount: 23, Size: 22, Frequency: 50

### Detail
- Sharpness: 8 (between 5 and 10)

## Community Validated Values

| Attribute | Final Value | Source |
|---|---|---|
| Exposure2012 | +0.40 | Interpolated from 100+400 |
| Contrast2012 | +12 | Between 100+400 consumer baseline |
| Highlights2012 | -15 | H:-1.5 interpolated |
| Shadows2012 | +18 | S:-1.5 inverted interpolated |
| Blacks2012 | -2 | Gentle midpoint |
| Saturation | +8 | Color+2 interpolated |
| Vibrance | +10 | CCE interpolation; gap=2 |
| SaturationAdjustmentRed | +8 | Fuji consumer red |
| SaturationAdjustmentGreen | +5 | Fuji consumer green |
| SaturationAdjustmentBlue | +3 | Fuji consumer blue |
| HueAdjustmentRed | -7 | Toward magenta (Fuji) |
| HueAdjustmentBlue | -4 | Toward cyan |
| ColorGradeHighlightHue | 38 | Interpolated warmth |
| ColorGradeHighlightSat | 5 | Subtle |
| ColorGradeShadowHue | 135 | Green shadow (Fuji trait) |
| ColorGradeShadowSat | 12 | Between 100 and 400 |
| GrainAmount | 23 | Between 15+31 |
| GrainSize | 22 | Between 15+28 |
| GrainFrequency | 50 | Consumer roughness |
| Sharpness | 8 | Between 5+10 |

## Sources

- Fuji X Weekly: Superia 100 recipe (baseline reference)
- Fuji X Weekly: Superia 400 recipe (upper reference)
- t3mujinpack: Fuji film simulation data
- r/AnalogCommunity: Superia 200 discussion threads
- Fujifilm Superia product line documentation
