# Kodak ColorPlus 200 — Community Recipes & Lightroom Settings

## Overview

Kodak ColorPlus 200 is emulated using Fuji X Weekly's Kodak Emulsion in-camera recipe as the primary reference, cross-referenced with community knowledge about ColorPlus's warm/golden consumer film character.

## Primary Reference: Fuji X Weekly "Kodak Emulsion" Recipe

Source: Fuji X Weekly community

```
Film Simulation: Classic Chrome
Grain Effect: Strong, Large
Color Chrome Effect: Off
Color Chrome FX Blue: Off
White Balance: Shade, -2 Red & +2 Blue
Dynamic Range: DR400
Highlight: -2
Shadow: -2
Color: +3
Sharpness: 0
Noise Reduction: -4
Clarity: -3
```

## Fuji→Lightroom Translation

Per project Fuji→LR mapping:

| Fuji Setting | Value | Lightroom Attribute | Value |
|---|---|---|---|
| Film Sim: Classic Chrome | — | Look | Adobe Color |
| Grain: Strong, Large | — | GrainAmount, GrainSize | 35, 35 |
| Grain Roughness | — | GrainFrequency | 50 |
| DR400 | — | Highlights2012 (extra) | -10 |
| Highlight: -2 | — | Highlights2012 | -20 |
| Shadow: -2 | — | Shadows2012 | +20 (inverted) |
| Color: +3 | — | Saturation | +15 → tempered to +10 |
| Clarity: -3 | — | Clarity2012 | -30 → 0 (grain protection) |

**STYLEGUIDE adjustments**:
- Clarity forced to 0 when GrainAmount > 0
- Sharpness forced to 10 when GrainAmount > 0
- No WB adjustments (per STYLEGUIDE "no WB unless defining")
- Vibrance matched within 5 of Saturation

## Core Emulation Philosophy

ColorPlus 200 sits between Gold 200 and basic consumer film:
1. **Warm consumer character** — golden-yellow midtone bias
2. **Muted compared to Gold** — less saturation, more subtle overall
3. **Brown/warm shadows** — not the teal-cyan of Gold 200
4. **Visible consumer grain** — moderate, organic, slightly irregular
5. **Budget film soul** — unpretentious, forgiving, nostalgic

## Applied Lightroom Values

### Basic Panel
- Contrast: +10 (moderate consumer punch)
- Highlights: -30 (recipe -20 + DR400 -10)
- Shadows: +20 (recipe -2 inverted)
- Blacks: -5 (gentle anchor)
- Whites: 0
- Saturation: +10
- Vibrance: +12 (gap = 2)

### HSL / Color Mixer
- Red Sat: +8 (warm tone boost)
- Orange Sat: +5
- Yellow Sat: +8 (golden cast)
- Yellow Hue: -5 (toward gold/orange)
- Green Sat: -5 (muted greens)
- Green Hue: +5 (less blue-green)
- Blue Sat: -8 (muted skies)

### Color Grading (Blending 50)
- Shadow Hue: 40, Sat: 8 (warm brown shadows)
- Highlight Hue: 45, Sat: 10 (golden highlights)

### Grain
- Amount: 35, Size: 35, Frequency: 50 (Strong/Large consumer)

### Detail
- Sharpness: 10 (grain protection rule)

## Community Validated Values

Final XMP values, cross-referenced from Fuji X Weekly Kodak Emulsion recipe and ColorPlus 200 community knowledge:

| Attribute | Final Value | Source |
|---|---|---|
| Contrast2012 | +10 | Consumer film baseline |
| Highlights2012 | -30 | H:-2 + DR400 |
| Shadows2012 | +20 | S:-2 inverted |
| Blacks2012 | -5 | Gentle anchor |
| Saturation | +10 | Color+3 tempered |
| Vibrance | +12 | Within 5 of Saturation |
| SaturationAdjustmentRed | +8 | Warm reds |
| SaturationAdjustmentOrange | +5 | Warm skin |
| SaturationAdjustmentYellow | +8 | Golden cast |
| SaturationAdjustmentGreen | -5 | Muted greens |
| SaturationAdjustmentBlue | -8 | Muted skies |
| HueAdjustmentYellow | -5 | Toward gold |
| HueAdjustmentGreen | +5 | Away from blue-green |
| ColorGradeHighlightHue | 45 | Golden highlights |
| ColorGradeHighlightSat | 10 | Moderate warmth |
| ColorGradeShadowHue | 40 | Warm brown shadows |
| ColorGradeShadowSat | 8 | Moderate shadow warmth |
| GrainAmount | 35 | Strong (recipe) |
| GrainSize | 35 | Large (recipe) |
| GrainFrequency | 50 | Consumer roughness |
| Sharpness | 10 | Grain protection |

## Sources

- Fuji X Weekly: Kodak Emulsion recipe (fujixweekly.com)
- r/AnalogCommunity: Gold 200 vs ColorPlus 200 comparison threads
- Photrio: Consumer film side-by-side tests
- Kodak Alaris: ColorPlus 200 technical specifications
- 35mmc.com: Budget film roundups
