# Fuji Neopan 400 — Film Characteristics for Lightroom Presets

## Overview
Fuji Neopan 400 was a traditional-cubic-grain black-and-white negative film from Fujifilm. It was part of Fuji's Neopan B&W line alongside Neopan 100 Acros and Neopan 1600. Unlike Acros (which used Fuji's Super Fine-Σ grain technology), Neopan 400 used conventional grain structure for a more classic B&W look. This document serves as a reference for creating a Lightroom preset that emulates Neopan 400.

## Key Characteristics
- **ISO**: 400 (nominal)
- **Grain**: Pronounced — traditional cubic grain with visible texture
- **Sharpness**: Good resolving power; not as sharp as Acros but with more character
- **Contrast**: Moderate to moderately high
- **Tonal Range**: Good separation across the full range with rich midtones
- **Development**: Works well with standard developers; good push capacity
- **Spectral Sensitivity**: Slightly different from Kodak films — Fuji's own spectral dye sensitization

## Historical Context
- Part of Fuji's Neopan B&W family
- Positioned as Fuji's answer to Kodak Tri-X and Ilford HP5+
- Discontinued — only Neopan 100 Acros II remains in production (as of 2024)
- Less documented in English-language community compared to Kodak/Ilford equivalents
- Had a strong following in Japan and among photographers who preferred the Fuji B&W tonal signature

## Visual Signature
- Traditional B&W grain structure — visible, organic texture
- Slightly different tonal curve from Kodak — more neutral midtones, less "yellow-filtered" character
- Fuji's spectral sensitivity gives subtly different luminance rendering of colors
- Pronounced grain adds character — similar in spirit to Tri-X
- Works well for documentary, street, and reportage photography

## Sources
- Fujifilm Professional Data Guide (archived)
- t3mujinpack dtstyle data (Neopan/Acros family reference)
- Community forum discussions (Photrio, rangefinderforum.com)

---

## See Also

For related Lightroom presets and film stock references:

- [Fuji Neopan 1600](../Fuji-Neopan-1600/characteristics.md)
- [Kodak Tri X 400](../Kodak-Tri-X-400/characteristics.md)

---

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** ISO 400 traditional cubic grain, "pronounced, similar in spirit to Tri-X" — preset GrainAmount 50 / GrainSize 35 vs Tri-X 55/35 and T-Max 400 35/28: correctly placed between T-grain and Tri-X. Moderate-to-moderately-high contrast (+30) and rich midtones are consistent. Drift: GrayMixer Red +35 / Blue −40 is the most extreme warm-cool split in the B&W set (Tri-X is +30/−40), while this folder describes Neopan 400 as having "more neutral midtones, less yellow-filtered character" than Kodak — a ±35 red push is the opposite of the documented Fuji signature. Tonal register is still correct, so no edit.
- **Sources:** Fujifilm Professional Data Guide (Neopan 400, via 125px.com techdocs) and t3mujinpack Neopan reference cited here; California Creeks B&W table (traditional Neopan 400/1600 emulsions, RMS 16 for 1600); Tri-X 400 baseline in this repo for grain scale.
- **Preset adjustments:** none
