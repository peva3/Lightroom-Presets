# Light NR

Noise reduction preset targeting light noise.
- Luminance Smoothing: 15
- Color Noise Reduction: 20
- Luminance Detail: 60

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** LuminanceSmoothing 15, ColorNoiseReduction 20, LuminanceNoiseReductionDetail 60. Ladder is monotonic across the family (Luminance 15 < 30 < 45 < 60; Color 20 < 30 < 40 < 50) with detail falling as smoothing rises -- the correct trade-off. Lightest step.
- **Sources:** Reference §6 (LuminanceSmoothing 0-100, ColorNoiseReduction default 25, LuminanceNoiseReductionDetail default 50); repo NR ladder.
- **Preset adjustments:** none
