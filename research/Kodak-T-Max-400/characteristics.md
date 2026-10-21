# Kodak T-Max 400 — Film Characteristics for Lightroom Presets

## Overview
Kodak T-Max 400 is a medium-speed T-grain (tabular grain) black-and-white negative film introduced in 1986 alongside T-Max 100. Updated in 2007 for improved sharpness and finer grain. It uses flat, plate-like silver halide crystals for higher efficiency than traditional cubic-grain films. This document serves as a reference for creating a Lightroom preset that emulates T Max 400.

## Key Characteristics
- **ISO**: 400 (nominal)
- **Grain**: Fine for a 400-speed film — significantly finer than Tri-X 400
- **Sharpness**: Very high resolving power; T-Max films were marketed as the sharpest B&W films available
- **Contrast**: Moderate to moderately high
- **Tonal Range**: Clean, linear; good highlight and shadow detail
- **Development**: Benefits from T-Max or T-Max RS developer; precise processing matters more than with traditional films
- **Exposure Latitude**: Good, but less forgiving than HP5+ or Tri-X for underexposure

## Historical Context
- Introduced 1986, updated 2007
- Popular with photographers who want ISO 400 speed with visual quality closer to an ISO 100 film
- The T-Max vs Tri-X debate defined an era of B&W film photography
- Used extensively in photojournalism, wedding, and commercial work

## Visual Signature
- Clean and precise — avoids the "gritty" look of traditional films
- Fine grain at 400 speed
- Neutral tonality with good separation across the full range
- Slightly cooler/lower-contrast shadow character than Tri-X
- Popular for portraiture where some grain texture is desired without the full grit of Tri-X

## Comparison to Tri-X 400
- T-Max 400 has noticeably finer grain
- T-Max 400 has a cleaner, less "vintage" look
- Tri-X has more forgiving exposure latitude
- Tri-X has more pronounced grain and "character"
- Both are excellent 400-speed films — choice is aesthetic preference

## Sources
- Kodak Alaris Technical Data Sheet (F-4043)
- Fuji X Weekly (Thomas Schwab, Anders Lindborg, Ritchie Roesch recipe, August 2020)

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak T Max 100](../Kodak-T-Max-100/characteristics.md)
- [Kodak T Max 3200](../Kodak-T-Max-3200/characteristics.md)
- [Kodak Tri X 400](../Kodak-Tri-X-400/characteristics.md)
- [Kodak Plus X 125](../Kodak-Plus-X-125/characteristics.md)

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** fine grain for a 400 (significantly finer than Tri-X); moderate-to-moderately-high contrast; slightly cooler and lower-contrast shadow character than Tri-X
- **Checked against XMP:** GrainAmount 35 vs Tri-X 55, GrainSize 28 vs 35, Contrast +30 vs Tri-X +35, Shadows +20 (cooler, more open shadows), GrayMixerRed +35 / Blue -35
- **Sources:** Kodak T-Max 400 datasheet; research/Kodak-T-Max-400 characteristics; Tri-X vs T-Max 400 community comparisons
- **Preset adjustments:** none
