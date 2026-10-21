# Astro NR

Noise reduction preset targeting astro noise.
- Luminance Smoothing: 20
- Color Noise Reduction: 60
- Luminance Detail: 75

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** Preset is LuminanceSmoothing 20 / ColorNoiseReduction 60 / LuminanceNoiseReductionDetail 75: deliberately off the Light->Heavy ladder because night-sky noise is chroma-dominant and luminance smoothing is what eats stars (high colour NR, low luminance smoothing, high detail). The body text quoted 40/40/60 and has been aligned to the file.
- **Sources:** Reference §6; general astro-NR practice (chroma-dominant noise, star preservation).
- **Preset adjustments:** none (research text aligned to the preset)
