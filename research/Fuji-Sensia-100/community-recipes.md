# Fuji Sensia 100 — Community Lightroom Recipes

## Overview

Community recipes for Sensia 100 in Lightroom are scarce — the film was discontinued before the peak of the film emulation preset trend. Most references treat Sensia as a "warmer, slightly softer Provia" and suggest starting from Provia recipes with warmth and contrast adjustments.

## Derived Recipe (Based on Provia 100F + Consumer Characteristics)

Sensia's defining differences from Provia are warmer color balance and slightly lower contrast. The preset is built by starting from the Provia 100F recipe and adjusting for Sensia's consumer character.

### LR/XMP Implementation

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Basic Panel** | | |
| Contrast2012 | +15 | Lower contrast than Provia (+20) |
| Highlights2012 | -12.5 | Gentler highlight compression |
| Shadows2012 | -22.5 | Less shadow crush than Provia (-30) |
| Blacks2012 | -22.5 | Lighter black point (consumer film) |
| Whites2012 | +10 | Modest white point |
| Saturation | +5 | Slide S-curve cap |
| Vibrance | +3.8 | Subtle midtone warmth |
| **HSL Hue** | | |
| Red | +5 | Warm shift |
| Yellow | -5 | Toward orange (warmth) |
| **HSL Saturation** | | |
| Yellow | -5 | Restrain yellow |
| Green | -5 | Naturalize foliage |
| **HSL Luminance** | | |
| Orange | +7.5 | Creamy warm skin |
| **Color Grading** (Blending 75) | | |
| Shadow Hue/Sat | 50 / 5 | Warm shadow (not cool like Provia) |
| Highlight Hue/Sat | 45 / 5 | Warm-golden highlights |
| **Grain** | Amount 10, Size 15, Roughness 40 | Fine slide grain |
| **Detail** | Sharpness 10, Clarity 0, Texture 0 | Grain protection |

### StyleGuide Compliance
- Saturation +5 (Slide S-curve cap) ✓
- Vibrance within 5 of Saturation (|+3.8 - +5| = 1.2) ✓
- No Calibration ✓
- No Temperature/Tint ✓
- Grain→Sharpness=10, Clarity=Texture=Dehaze=0 ✓
- Blacks ≥ -30 (at -22.5) ✓
- HSL Sat ≤ ±60 (max +5) ✓
- Adobe Vivid Look block ✓
- Slide S-curve ✓

### Sources
- Derived from Provia 100F recipe with consumer film adjustments
- r/analog community — Sensia 100 characteristic descriptions
- Fuji X Weekly — Provia + warm shift methodology
