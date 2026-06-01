# Fuji Superia 100 — Community Recipes & Lightroom Settings

## Overview

Fuji Superia 100 is emulated using Fuji X Weekly's in-camera recipe as the primary reference, mapped to Lightroom per the project's Fuji→LR translation table.

## Primary Reference: Fuji X Weekly Recipe

Source: Fuji X Weekly community

```
Film Simulation: Classic Negative
Grain Effect: Weak, Small
Color Chrome Effect: Strong
Color Chrome FX Blue: Weak
White Balance: Daylight, 0 Red & -1 Blue
Dynamic Range: Auto
Highlight: -1
Shadow: -2
Color: +1
Sharpness: -2
Noise Reduction: -4
Clarity: -2
Exposure Compensation: +1/3 to +2/3
```

## Fuji→Lightroom Translation

Per project Fuji→LR mapping:

| Fuji Setting | Value | Lightroom Attribute | Value |
|---|---|---|---|
| Film Sim: Classic Negative | — | Look | Adobe Color |
| Grain: Weak, Small | — | GrainAmount, GrainSize | 15, 15 |
| Grain Roughness | — | GrainFrequency | 50 |
| Color Chrome Effect: Strong | — | Vibrance | +5 |
| Highlight: -1 | — | Highlights2012 | -10 |
| Shadow: -2 | — | Shadows2012 | +20 (inverted) |
| Color: +1 | — | Saturation | +5 |
| Sharpness: -2 | — | Sharpness | 5 (map: -4 to +4 → 0 to 20) |
| Clarity: -2 | — | Clarity2012 | -20 → 0 (grain protection) |
| Exp +1/3 to +2/3 | — | Exposure2012 | +0.50 |

**STYLEGUIDE adjustments**:
- Clarity forced to 0 when GrainAmount > 0
- No WB adjustments (0R -1B skipped per STYLEGUIDE)
- Vibrance (+5) within 5 of Saturation (+5): gap = 0

## Core Emulation Philosophy

Superia 100 is the fine-grain Fuji consumer film:
1. **Cool-neutral Fuji cast** — clean whites, slightly cool
2. **Fine grain** — barely visible, tight
3. **Subtle green shadow** — the Fuji family trait, less pronounced
4. **Magenta-red push** — the characteristic Fuji red rendering
5. **Higher contrast** than faster Superia films — inherent to slower emulsions

## Applied Lightroom Values

### Basic Panel
- Exposure: +0.50 (recipe +1/3 to +2/3)
- Contrast: +8 (consumer moderate)
- Highlights: -10 (H:-1)
- Shadows: +20 (S:-2 inverted)
- Blacks: -5
- Whites: 0
- Saturation: +5
- Vibrance: +5 (CCE Strong; gap=0)

### HSL / Color Mixer
- Red Sat: +5
- Red Hue: -5 (toward magenta — Fuji trait)
- Green Sat: +5 (Fuji consumer green)
- Blue Sat: +5 (Fuji consumer blue)
- Blue Hue: -3 (toward cyan)

### Color Grading (Blending 50)
- Shadow Hue: 140, Sat: 8 (green shadow cast)
- Highlight Hue: 35, Sat: 5 (subtle warmth)

### Grain
- Amount: 15, Size: 15, Frequency: 50 (Weak/Small)

### Detail
- Sharpness: 5 (Sharpness -2 mapped, below 10 = grain-safe)

## Community Validated Values

Final XMP values, cross-referenced from Fuji X Weekly Superia 100 recipe:

| Attribute | Final Value | Source |
|---|---|---|
| Exposure2012 | +0.50 | Recipe +1/3 to +2/3 |
| Contrast2012 | +8 | Consumer film baseline |
| Highlights2012 | -10 | H:-1 |
| Shadows2012 | +20 | S:-2 inverted |
| Blacks2012 | -5 | Gentle anchor |
| Saturation | +5 | Color +1 |
| Vibrance | +5 | CCE Strong; gap=0 |
| SaturationAdjustmentRed | +5 | Fuji consumer red |
| SaturationAdjustmentGreen | +5 | Fuji consumer green |
| SaturationAdjustmentBlue | +5 | Fuji consumer blue |
| HueAdjustmentRed | -5 | Toward magenta (Fuji) |
| HueAdjustmentBlue | -3 | Toward cyan |
| ColorGradeHighlightHue | 35 | Subtle warm highlight |
| ColorGradeHighlightSat | 5 | Subtle |
| ColorGradeShadowHue | 140 | Green shadow (Fuji trait) |
| ColorGradeShadowSat | 8 | Moderate shadow cast |
| GrainAmount | 15 | Weak (recipe) |
| GrainSize | 15 | Small (recipe) |
| GrainFrequency | 50 | Standard consumer roughness |
| Sharpness | 5 | Sharpness -2 mapped |

## Sources

- Fuji X Weekly: Superia 100 recipe (fujixweekly.com)
- t3mujinpack: Fuji film simulation data
- r/AnalogCommunity: Superia 100 discussion
- r/FujifilmSimulations: Superia recipe community
- Fujifilm Superia product line documentation
