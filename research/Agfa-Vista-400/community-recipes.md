# Agfa Vista 400 — Community Recipes & Lightroom Settings

## Overview

Agfa Vista 400 is emulated as a warmer, grainier, faster variant of Agfa Vista 200. The existing Vista 200 preset serves as the baseline, with values adjusted to reflect the ISO 400 stock's warmer color cast, more pronounced grain, and lower contrast.

## Reference: Existing Vista 200 Preset (Baseline)

The working Vista 200 values (see Vista 100 research for full table).

## Vista 400 Adjustments from Vista 200 Baseline

### Key Differences
- **Warmer**: Warmer overall tone, golden cast (anomalous in the Fuji-made Vista line)
- **More grain**: Increased by ~60% (ISO 400 vs 200)
- **Lower contrast**: Inherent to faster consumer emulsion
- **More red saturation**: Warm bias amplifies reds
- **Warm brown shadows**: Cooler blue shadow from 200 shifts warm

### Value Adjustments

| Attribute | Vista 200 | Vista 400 | Change | Rationale |
|---|---|---|---|---|
| Contrast2012 | +14 | +15 | +1 | Slight boost (offset speed contrast loss) |
| Highlights2012 | -11 | -8 | +3 | Less compression |
| Shadows2012 | +15 | +20 | +5 | More shadow lift |
| Whites2012 | +19 | +22 | +3 | Brighter whites |
| Blacks2012 | -15 | -18 | -3 | Deeper anchor |
| Saturation | +8 | +10 | +2 | Warmer/more sat |
| Vibrance | +12 | +14 | +2 | Gap=4 |
| SatAdjustmentRed | +28 | +30 | +2 | Strongest reds |
| SatAdjustmentBlue | +16 | +18 | +2 | More blue sat |
| SatAdjustmentYellow | +12 | +15 | +3 | Warmer yellows |
| SatAdjustmentOrange | +8 | +10 | +2 | Warmer skin |
| SatAdjustmentGreen | -5 | -8 | -3 | More muted greens |
| HueAdjustmentRed | -5 | -8 | -3 | More toward magenta |
| HueAdjustmentYellow | -5 | -8 | -3 | More toward orange |
| LuminanceAdjustmentRed | +10 | +10 | unchanged | |
| LuminanceAdjustmentBlue | +5 | +5 | unchanged | |
| ColorGradeShadowHue | 240 | 245 | +5 | Cooler shadow |
| ColorGradeHighlightHue | — | 50 | new | Golden highlights |
| ColorGradeHighlightSat | — | 5 | new | Subtle |
| GrainAmount | 21 | 33 | +12 | Grainier |
| GrainSize | 30 | 35 | +5 | Larger grain |
| GrainFrequency | 55 | 60 | +5 | Rougher |

## Core Emulation Philosophy

Vista 400 is the warm, fast consumer workhorse:
1. **Warm golden cast** — closer to Kodak than Fuji in temperature
2. **Moderate visible grain** — the price of ISO 400 speed
3. **Moderate consumer contrast** — lower than Vista 200
4. **Explosive primary reds** — the most saturated in the Vista line
5. **Warm brown shadows** — not the cool-green of Fuji consumer films

## Applied Lightroom Values

See XMP file for final applied values.

## Sources

- Existing Agfa Vista 200 preset (baseline reference)
- AgfaPhoto product documentation
- r/AnalogCommunity: Vista 400 discussions
- r/analog: Vista 400 image posts
- Japan Camera Hunter: Agfa Vista line overview
- Flickr: Agfa Vista 400 image samples
