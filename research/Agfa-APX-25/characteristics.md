# Agfa APX 25 — Film Characteristics for Lightroom Presets

## Overview
Agfa APX 25 was an ultra-fine-grain, very low ISO black-and-white negative film produced by Agfa-Gevaert. It was renowned for its almost invisible grain structure, high sharpness, and exceptional enlarging capability. Discontinued in the early 2000s along with the rest of the APX line (later revived by Lupus Imaging as AgfaPhoto APX). This document serves as a reference for creating a Lightroom preset that emulates APX 25.

## Key Characteristics
- **ISO**: 25 (nominal)
- **Grain**: Virtually invisible — among the finest-grain B&W films ever produced
- **Sharpness**: Extremely high resolving power
- **Contrast**: Moderate; benefits from careful development for optimal tonality
- **Tonal Range**: Smooth, continuous tonality transitions; excellent micro-contrast
- **Spectral Sensitivity**: Ortho-panchromatic — slightly reduced red sensitivity compared to full panchromatic
- **Development**: Works well with Rodinal (classic pairing), Agfa Studional, D-76

## Historical Context
- Part of Agfa's APX line alongside APX 100 and APX 400
- Discontinued when AgfaPhoto ceased production (2005)
- Later rebranded versions surfaced under AgfaPhoto APX branding by Lupus Imaging (different emulsion)
- Original APX 25 is now a sought-after discontinued film
- Prized by landscape and fine-art photographers for extreme enlargements

## Visual Signature
- Creamy, smooth tonality with nearly zero visible grain
- Excellent for large-format-style results from 35mm
- High contrast capability with push processing
- Subtle, elegant rendering — the opposite of "gritty"
- Particularly beautiful in high-key and low-key scenes

## Sources
- Agfa-Gevaert Technical Data Sheet (archived)
- t3mujinpack dtstyle data for Darktable emulation
- Community forum archives (APUG/Photrio, rangefinderforum.com)

---

## See Also

For related Lightroom presets and film stock references:

- [Agfa APX 100](../Agfa-APX-100/characteristics.md)
- [Agfa APX 400](../Agfa-APX-400/characteristics.md)
- [Kodak Tri X 400](../Kodak-Tri-X-400/characteristics.md)

---

## Validation Sweep 2026-10-21
- **Verdict:** minor drift (research note itself needs correcting)
- **Defining traits checked:** ISO 25, RMS granularity 7.0 and 200 lp/mm — the finest-grained, highest-resolving APX (preset GrainAmount 15 / GrainSize 20 is the lowest of the APX trio, ordering correct); moderate-to-contrasty midtones with an early shoulder, i.e. rich midtone contrast plus soft highlights (preset: Contrast +15, Highlights −10, Blacks −20 — plausible); 7 µm emulsion layer. Correction to this folder: APX 25 is described above as "ortho-panchromatic / slightly reduced red", but Agfa's own spectrogram runs 400–650 nm like a true panchromatic film, and Photrio/photo.net comparisons note that *Efke 25* was the orthopanchromatic film while Agfapan APX 25 was true panchromatic. The preset's Red +25 / Blue −20 is therefore consistent with the film, not a bug.
- **Sources:** AGFAPAN APX 25 technical data sheet (tmax100.com PDF: RMS 7.0, 200 lp/mm, Refinal 6 min); Agfa Professional B&W technical data comparison table (APX 25 RMS 7, APX 100 RMS 9, APX 400 RMS 14); photo.net APX 25 vs APX 100 thread on curve shape and ortho-vs-pan sensitisation.
- **Preset adjustments:** none
