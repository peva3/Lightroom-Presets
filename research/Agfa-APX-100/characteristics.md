# Agfa APX 100 — Film Characteristics for Lightroom Presets

## Overview
Agfa APX 100 was a medium-speed, fine-grain black-and-white negative film. It was the most popular film in the Agfa APX line, offering a versatile combination of fine grain, good sharpness, and moderate contrast. Originally produced by Agfa-Gevaert; later revived under the AgfaPhoto APX branding by Lupus Imaging with a different emulsion. This document serves as a reference for creating a Lightroom preset that emulates APX 100.

## Key Characteristics
- **ISO**: 100 (nominal)
- **Grain**: Fine — smooth and consistent
- **Sharpness**: Good resolving power, clean edge definition
- **Contrast**: Moderate — slightly more than APX 25, less aggressive than APX 400
- **Tonal Range**: Smooth midtone transitions with good shadow detail
- **Development**: Popular with Rodinal, D-76, and XTOL; excellent push capacity to 200
- **Exposure Latitude**: Good — tolerates modest over/underexposure

## Historical Context
- The "Goldilocks" of the APX line — ISO 100 with fine grain and workable contrast
- Very popular in European markets alongside Agfa's color films
- Original Agfa-Gevaert emulsion discontinued 2005
- Current "AgfaPhoto APX 100" (Lupus Imaging) is a different film — reportedly Kentmere-based
- The original APX 100 remains a reference for classic fine-grain B&W

## Visual Signature
- Clean, natural rendering
- Moderate contrast with smooth highlight rolloff
- Characteristic Agfa tonal smoothness
- Grain is visible but unobtrusive — enough to remind you it's film
- Works well for portraiture, street photography, and general-purpose work

## Sources
- Agfa-Gevaert Technical Data Sheet (archived)
- t3mujinpack dtstyle data for Darktable emulation
- Photrio/APUG community archives

---

## See Also

For related Lightroom presets and film stock references:

- [Agfa APX 25](../Agfa-APX-25/characteristics.md)
- [Agfa APX 400](../Agfa-APX-400/characteristics.md)
- [Kodak Tri X 400](../Kodak-Tri-X-400/characteristics.md)

---

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** ISO 100, RMS granularity 9 and 150 lp/mm (Agfa datasheet) → "fine but visible" grain; moderate native contrast, *less* contrast than APX 400 and more than APX 25 (preset: Contrast +25 sits correctly between APX 25 +15 and APX 400 +25); standard panchromatic sensitivity. Drift: GrainAmount 25 is generous for an RMS 9 film (the APX 25 preset at 15 and Delta 100 at 15 are closer to their datasheets), and GrayMixer Red +30 is a strong warm bias for a film Agfa documents as evenly sensitised 400–650 nm — it is the largest red boost in the APX family even though APX 100 is the most "neutral" of the three. Neither is a defining-trait error; both read as house style.
- **Sources:** Agfa Professional black & white films technical data (mips.di.unimi.it archive, Agfa APX 25/100/400 spec table: APX 100 RMS 9.0, 150 lp/mm); Agfa APX data sheet reproductions on tmax100.com.
- **Preset adjustments:** none
