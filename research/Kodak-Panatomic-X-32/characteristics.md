# Kodak Panatomic-X 32 — Film Characteristics for Lightroom Presets

## Overview
Kodak Panatomic-X was an ultra-fine-grain, slow-speed black-and-white negative film (ISO 32). Introduced in 1933 and discontinued in 1987, it achieved legendary status among fine-art photographers for its virtually invisible grain, exceptional sharpness, and long tonal scale. Ansel Adams used it for many of his most famous works. This document serves as a reference for creating a Lightroom preset that emulates Panatomic X 32.

## Key Characteristics
- **ISO**: 32 (nominal), often shot at 25-50
- **Grain**: Ultra-fine — essentially grainless at normal viewing distances
- **Sharpness**: Exceptional — among the sharpest general-purpose B&W films ever made
- **Contrast**: Low to moderate — long, smooth tonal scale with excellent shadow/highlight separation
- **Tonal Range**: Extremely wide — 10+ zones achievable with careful development
- **Spectral Sensitivity**: Ortho-panchromatic (slightly reduced red sensitivity compared to modern pan films)
- **Development**: Popular in D-76 1:1, Microdol-X, Rodinal; benefits from dilute developers for maximum sharpness
- **Exposure Latitude**: Very wide — forgiving of underexposure and overexposure

## Historical Context
- Introduced 1933, discontinued 1987 — 54-year production run
- The choice of Ansel Adams, Edward Weston, and many f/64 group members
- USDA aerial photography standard for decades due to its resolution
- Eventually replaced by T-Max 100 (1986) which offered finer grain but different tonality
- Remains one of the most mourned discontinued films in analog photography

## Visual Signature
- Creamy, smooth midtones with exquisite detail
- Shadows that hold detail without blocking up
- Highlights that roll off gently without harsh clipping
- Grain is essentially invisible in prints up to 16x20"
- A "painterly" quality that digital still struggles to replicate
- Skin tones render naturally with slight brightness — excellent portrait film

## Sources
- Kodak Publication F-4018 (Panatomic-X Professional Film datasheet)
- Ansel Adams, *The Negative* (1981)
- Photrio/APUG community archives
- t3mujinpack Darktable reference data

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak Plus X 125](../Kodak-Plus-X-125/characteristics.md)
- [Kodak T Max 100](../Kodak-T-Max-100/characteristics.md)

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** ultra-fine grain with very high resolving power; medium-to-high contrast; long smooth tonal scale; disputed spectral signature
- **Checked against XMP:** GrainAmount 10 / GrainSize 15 (essentially grainless), Contrast +12 (medium), Blacks -15, Highlights -10 / Shadows +12 (gentle shoulder and toe), GrayMixerRed +15 / Blue -25
- **Sources:** Analog.Cafe "The Atomic Film" ("panchromatic emulsion and extended red sensitivity"); Alex Luyckx Panatomic-X review; Photo.net / Photrio fine-grain comparisons
- **Preset adjustments:** none
- **Note:** Research CONFLICT: this file calls Panatomic-X "ortho-panchromatic (slightly reduced red)", which would imply darker reds and lighter skies - the XMP does the opposite. Three independent external sources describe it as *extended* red, which supports Red +15 / Blue -25, so the XMP was left alone and the unsourced research line is flagged instead.
