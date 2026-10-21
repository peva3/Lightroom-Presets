# Medium NR

Noise reduction preset targeting medium noise.
- Luminance Smoothing: 30
- Color Noise Reduction: 30
- Luminance Detail: 50

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** LuminanceSmoothing 30, ColorNoiseReduction 30, LuminanceNoiseReductionDetail 50. Ladder is monotonic across the family (Luminance 15 < 30 < 45 < 60; Color 20 < 30 < 40 < 50) with detail falling as smoothing rises -- the correct trade-off. Middle step.
- **Sources:** Reference §6 (LuminanceSmoothing 0-100, ColorNoiseReduction default 25, LuminanceNoiseReductionDetail default 50); repo NR ladder.
- **Preset adjustments:** none
