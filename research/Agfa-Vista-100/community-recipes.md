# Agfa Vista 100 — Community Recipes & Lightroom Settings

## Overview

Agfa Vista 100 is emulated as a cooler, finer-grain variant of Agfa Vista 200. The existing Vista 200 preset serves as the baseline, with values adjusted to reflect the ISO 100 stock's cooler color balance, finer grain structure, and higher contrast.

## Reference: Existing Vista 200 Preset (Baseline)

The working Vista 200 values:

| Attribute | Vista 200 Value |
|---|---|
| Contrast2012 | +14 |
| Highlights2012 | -11 |
| Shadows2012 | +15 |
| Whites2012 | +19 |
| Blacks2012 | -15 |
| Saturation | +8 |
| Vibrance | +12 |
| SaturationAdjustmentRed | +28 |
| SaturationAdjustmentBlue | +16 |
| SaturationAdjustmentYellow | +12 |
| SaturationAdjustmentOrange | +8 |
| SaturationAdjustmentGreen | -5 |
| HueAdjustmentRed | -5 |
| HueAdjustmentGreen | +5 |
| HueAdjustmentYellow | -5 |
| HueAdjustmentBlue | -5 |
| LuminanceAdjustmentRed | +10 |
| LuminanceAdjustmentBlue | +5 |
| ColorGradeShadowHue | 240 |
| ColorGradeShadowSat | 5 |
| GrainAmount | 21 |
| GrainSize | 30 |
| GrainFrequency | 55 |

## Vista 100 Adjustments from Vista 200 Baseline

### Key Differences
- **Cooler**: Lower temperature character, more neutral whites (-2 Saturation on warm channels)
- **Finer grain**: Reduced grain by ~40% (ISO 100 vs 200)
- **Higher contrast**: Consumer slower film = higher inherent contrast
- **Slightly less red saturation**: Cooler rendering reduces red punch
- **Neutral-cool shadow**: Blue shadow instead of warm

### Value Adjustments

| Attribute | Vista 200 | Vista 100 | Change | Rationale |
|---|---|---|---|---|
| Contrast2012 | +14 | +18 | +4 | Higher contrast (slower film) |
| Highlights2012 | -11 | -15 | -4 | More highlight protection |
| Shadows2012 | +15 | +10 | -5 | Less shadow lift (higher contrast) |
| Whites2012 | +19 | +15 | -4 | Moderated |
| Blacks2012 | -15 | -10 | +5 | Less deep anchor |
| Saturation | +8 | +5 | -3 | Cooler = less global sat |
| Vibrance | +12 | +8 | -4 | Gap from Saturation = 3 |
| SatAdjustmentRed | +28 | +22 | -6 | Cooler reds |
| SatAdjustmentBlue | +16 | +12 | -4 | Cooler overall |
| SatAdjustmentYellow | +12 | +8 | -4 | Less yellow warmth |
| SatAdjustmentOrange | +8 | +5 | -3 | Less warm skin |
| LuminanceAdjustmentRed | +10 | +5 | -5 | Less red pop |
| LuminanceAdjustmentBlue | +3 | +3 | unchanged | |
| ColorGradeShadowHue | 240 | 245 | +5 | Slightly cooler shadow |
| GrainAmount | 21 | 12 | -9 | Finer grain |
| GrainSize | 30 | 18 | -12 | Finer grain |
| GrainFrequency | 55 | 50 | -5 | Slightly smoother |

## Core Emulation Philosophy

Vista 100 is the cool, clean Agfa consumer film:
1. **Cooler neutral balance** — clean whites, no cream cast
2. **Very fine grain** — consumer ISO 100 with tight grain structure
3. **Higher contrast** than Vista 200 — inherent to slower emulsion
4. **Strong primaries** — reds and blues pop (Vista family trait)
5. **Cool shadows** — blue-leaning, not warm brown

## Applied Lightroom Values

See XMP file for final applied values.

## Sources

- Existing Agfa Vista 200 preset (baseline reference)
- AgfaPhoto product documentation
- r/AnalogCommunity: Vista 100 discussions
- Japan Camera Hunter: Agfa Vista line overview
- Photrio: Consumer ISO 100 film comparisons
- Flickr: Agfa Vista 100 image samples
