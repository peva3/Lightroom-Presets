# Heavy NR

Noise reduction preset targeting heavy noise.
- Luminance Smoothing: 45
- Color Noise Reduction: 40
- Luminance Detail: 40

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** LuminanceSmoothing 45, ColorNoiseReduction 40, LuminanceNoiseReductionDetail 40. Ladder is monotonic across the family (Luminance 15 < 30 < 45 < 60; Color 20 < 30 < 40 < 50) with detail falling as smoothing rises -- the correct trade-off. Heavy step.
- **Sources:** Reference §6 (LuminanceSmoothing 0-100, ColorNoiseReduction default 25, LuminanceNoiseReductionDetail default 50); repo NR ladder.
- **Preset adjustments:** none
