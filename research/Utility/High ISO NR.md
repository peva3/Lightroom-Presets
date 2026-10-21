# High ISO NR

Noise reduction preset targeting high noise.
- Luminance Smoothing: 60
- Color Noise Reduction: 50
- Luminance Detail: 35

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** LuminanceSmoothing 60, ColorNoiseReduction 50, LuminanceNoiseReductionDetail 35. Ladder is monotonic across the family (Luminance 15 < 30 < 45 < 60; Color 20 < 30 < 40 < 50) with detail falling as smoothing rises -- the correct trade-off. Top step, detail reduced to 35.
- **Sources:** Reference §6 (LuminanceSmoothing 0-100, ColorNoiseReduction default 25, LuminanceNoiseReductionDetail default 50); repo NR ladder.
- **Preset adjustments:** none
