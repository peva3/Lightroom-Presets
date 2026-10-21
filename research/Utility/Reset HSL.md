# Reset HSL

Resets all HSL/Color Mixer adjustments (Hue, Saturation, and Luminance for all 8 color channels) to 0. Does not affect other panels.

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** All 24 HSL hue/sat/lum attributes plus the 15 ColorGrade attributes are written to 0 with Blending back to 50, so no tint survives. Gap: the B&W mixer (GrayMixer*) lives in the same Color Mixer panel but is not zeroed, so a monochrome preset's mixer weights would survive this reset.
- **Sources:** Reference §4/§5/§9 default columns.
- **Preset adjustments:** none (gap recorded)
