# Reset HSL

Resets all HSL/Color Mixer adjustments (Hue, Saturation, and Luminance for all 8 color channels) to 0. Does not affect other panels.

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** All 24 HSL hue/sat/lum attributes plus the 15 ColorGrade attributes are written to 0 with Blending back to 50, so no tint survives. Gap: the B&W mixer (GrayMixer*) lives in the same Color Mixer panel but is not zeroed, so a monochrome preset's mixer weights would survive this reset.
- **Sources:** Reference §4/§5/§9 default columns.
- **Preset adjustments:** none (gap recorded)

## Reset completeness fix (2026-10-21)

Added the eight `GrayMixer*` channels (Red, Orange, Yellow, Green, Aqua, Blue, Purple, Magenta) at 0. Lightroom's Color Mixer panel holds two independent sets of values — the HSL triplet and the Black & White mix — and resetting only `HueAdjustment*`, `SaturationAdjustment*` and `LuminanceAdjustment*` left a previous B&W mix intact when the image was later converted to monochrome. The preset now clears the whole panel, plus Color Grading as before.
