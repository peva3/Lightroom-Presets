# Fuji Superia 800 — Community Recipes & Lightroom Settings

## Overview

Fuji Superia 800 is the high-speed consumer film in the Superia lineup. This preset extrapolates from the established Superia 400 recipe, adding more grain, stronger green shadow cast, and the contrast profile of high-speed consumer film.

## Reference Recipe: Superia 400 (extrapolated for 800)

The Superia 400 Fuji X Weekly recipe provides the baseline:

**Superia 400 (X-Trans IV)**:
```
Film Simulation: Classic Negative
Grain Effect: Strong, Small
Color Chrome Effect: Off
Color Chrome FX Blue: Strong
White Balance: Auto, +3 Red & -5 Blue
Dynamic Range: DR400
Highlight: 0
Shadow: -1
Color: +4
Sharpness: -1
Clarity: -2
```

**Extrapolation to 800**:
- More grain (Strong → Strong+): Amount 38
- Larger grain (Small → Small-Medium): Size 33
- Less contrast (faster film): Contrast12 -5
- Stronger shadow cast: Shadow Hue more green
- Lower saturation: Color +4 → +3

## Fuji→Lightroom Translation (Extrapolated)

| Fuji Setting | Superia 400 | Superia 800 (extrap.) | Lightroom Attribute | Value |
|---|---|---|---|---|
| Grain Effect | Strong, Small | Strong+, Small-Med | GrainAmount | 38 |
| | | | GrainSize | 33 |
| | | | GrainFrequency | 55 |
| CCE | Off | Off | Vibrance | 0 (extra) |
| Highlight | 0 | -0.5 | Highlights2012 | -5 |
| Shadow | -1 | -0.5 | Shadows2012 | +5 (inverted) |
| Color | +4 | +3 | Saturation | +8 |
| Sharpness | -1 | -1 | Sharpness | 10 |

**STYLEGUIDE adjustments**:
- No WB (skip Auto +3R -5B)
- Vibrance matched to Saturation within 5: Vibrance +12, Saturation +8 (gap=4)
- DR400: extra Highlights -10 → total Highlights -15
- Grain protection: Sharpness = 10

## Core Emulation Philosophy

Superia 800 pushes the Fuji consumer formula to higher speed:
1. **Cool Fuji cast maintains at ISO 800** — notable achievement
2. **Moderate-to-prominent grain** — coarser than 400, finer than 1600
3. **Pronounced green shadow cast** — stronger than 400
4. **Magenta-red push preserved** but slightly desaturated
5. **Consumer contrast** — slightly less contrast than 400 (speed trade-off)

## Applied Lightroom Values

### Basic Panel
- Contrast: +20 (between 400's +15 and 1600's +28)
- Highlights: -25 (stronger compression for high speed)
- Shadows: +8
- Blacks: -5
- Whites: 0
- Saturation: +8
- Vibrance: +12 (gap=4)

### HSL / Color Mixer
- Red Sat: +10
- Red Hue: -10 (toward magenta — Fuji trait)
- Green Sat: +8 (Fuji consumer green)
- Blue Sat: +8 (Fuji consumer blue)
- Blue Hue: -5 (toward cyan)

### Color Grading (Blending 50)
- Shadow Hue: 140, Sat: 14 (pronounced green shadow)
- Highlight Hue: 40, Sat: 5 (subtle warmth)

### Grain
- Amount: 38, Size: 33, Frequency: 55

### Detail
- Sharpness: 10 (grain protection)

## Community Validated Values

| Attribute | Final Value | Source |
|---|---|---|
| Contrast2012 | +20 | Between Superia 400 + 1600 |
| Highlights2012 | -25 | H:-0.5 + DR400 |
| Shadows2012 | +8 | S:-0.5 inverted, tempered |
| Blacks2012 | -5 | High-speed shadow anchor |
| Saturation | +8 | Color+3 temper |
| Vibrance | +12 | Gap=4 |
| SaturationAdjustmentRed | +10 | Fuji consumer red |
| SaturationAdjustmentGreen | +8 | Fuji consumer green |
| SaturationAdjustmentBlue | +8 | Fuji consumer blue |
| HueAdjustmentRed | -10 | Toward magenta (Fuji) |
| HueAdjustmentBlue | -5 | Toward cyan |
| ColorGradeHighlightHue | 40 | Subtle warmth |
| ColorGradeHighlightSat | 5 | Subtle |
| ColorGradeShadowHue | 140 | Green shadow (stronger) |
| ColorGradeShadowSat | 14 | Pronounced shadow cast |
| GrainAmount | 38 | High-speed consumer |
| GrainSize | 33 | Medium-large |
| GrainFrequency | 55 | Consumer roughness |
| Sharpness | 10 | Grain protection |

## Sources

- Fuji X Weekly: Superia 400 recipe (baseline for extrapolation)
- Fuji X Weekly: Superia 1600 recipe data
- r/AnalogCommunity: Superia 800 discussion
- t3mujinpack: Fuji film simulation data
- Photrio: Superia 800 grain comparisons
- 35mmc.com: Fuji Superia line overview
