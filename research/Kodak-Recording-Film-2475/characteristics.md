# Kodak Recording Film 2475 — Film Characteristics for Lightroom Presets

## Overview
Kodak Recording Film 2475 was an ultra-high-speed black-and-white negative film designed for surveillance and law enforcement applications. With an effective EI of 1000-4000 depending on development, it was one of the fastest films ever produced for general use. It was also used by some artistic photographers (notably for its extreme grain) before being discontinued. This document serves as a reference for creating a Lightroom preset that emulates Recording Film 2475.

## Key Characteristics
- **ISO**: 1000 (nominal), pushable to EI 4000+
- **Grain**: Extremely pronounced — massive, golf-ball grain structure
- **Sharpness**: Low — grain dominates over fine detail
- **Contrast**: Moderate to high — punchy, dramatic rendering
- **Spectral Sensitivity**: Extended red (super-panchromatic) — optimized for surveillance under varied lighting
- **Tonal Range**: Compressed — shadows block up quickly, highlights clip
- **Exposure Latitude**: Limited — designed for specific exposure scenarios
- **Development**: Processed in D-19, DK-50, or HC-110; push processing increases speed and grain dramatically

## Historical Context
- Originally designated "Kodak Linagraph Shellburst Film" (for military photography of artillery)
- Renamed 2475 Recording Film for surveillance and scientific applications
- Used extensively by law enforcement for nighttime surveillance
- Briefly adopted by art photographers in the 1970s for its extreme grain aesthetic
- Discontinued before 2000
- No direct replacement; Delta 3200 and T-Max 3200 are modern equivalents but with much finer grain

## Visual Signature
- Massive, overwhelming grain structure — golf ball-sized grain particles
- High contrast with dramatic deep blacks
- Extended red sensitivity lightens skin tones unnaturally
- Low sharpness — grain dominates over detail
- A gritty, documentary, surveillance aesthetic
- "Anti-beauty" film — the opposite of Panatomic-X
- Creates images that feel urgent, raw, and unfiltered

## Sources
- Kodak Publication F-31 (Recording Film 2475 datasheet)
- Law enforcement photography archives
- Community discussions on Photrio and Reddit r/analog
- Surveillance photography historical resources

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak T Max 3200](../Kodak-T-Max-3200/characteristics.md)
- [Kodak Tri X 400](../Kodak-Tri-X-400/characteristics.md)

## Validation Sweep 2026-10-21

- **Verdict:** minor drift
- **Defining traits checked:** EI 1000-4000 surveillance emulsion; the coarsest grain of any Kodak B&W ("golf-ball"); extended red / super-panchromatic; compressed tonal range where shadows block and highlights clip
- **Checked against XMP:** the defining trait is correct - GrainAmount 60 / GrainSize 55 / Roughness 75, coarser than T-Max 3200 (55/42/70); Contrast +25 (moderate-high); GrayMixerRed +25 / Blue -20 (extended red)
- **Sources:** research/Kodak-Recording-Film-2475 characteristics; published 2475 dev data (D-19 / DK-50 / HC-110); Photrio surveillance-film threads
- **Preset adjustments:** none
- **Note:** Drift: research describes a *compressed* range ("shadows block up quickly, highlights clip") but the tone panel expands it - Highlights -40, Shadows +20. Grain is the dominant defining trait and is right, so this is tonal drift, not a miss. Grain could plausibly sit a touch coarser still relative to TMZ.
