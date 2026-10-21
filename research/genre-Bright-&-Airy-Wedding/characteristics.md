# Bright & Airy Wedding Lightroom Preset — Characteristics

## Use Case
The Bright & Airy Wedding Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. High-key wedding photography — getting-ready, ceremony, detail shots. Designed for soft natural light and white-dominant scenes.

## Key Techniques
Lifted blacks (+15) + negative Contrast (-15) compress tonal range for pastel airiness. Negative Clarity (-10) and Texture (-5) create soft bloom. Green hue shift (+20) pushes foliage toward mint; blue desaturation (-20) softens sky. Aqua luminance boost (+35) adds ethereal glow. Minimal Color Grading for subtle warmth in highlights, cool in shadows (blending 75 for clean separation).

## Safety Check
- ProcessVersion: 15.4
- Treatment: Color
- Look Profile: Adobe Color
- Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGradeBlending: 75
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: N/A (no Vibrance)
- HSL Sat max: Within ±60
- Blacks floor: ≥ -30
- Grain protection: N/A (no grain)

## See Also

- [Genre Presets](../../docs/genre.md)
- [Mobile Presets](../../docs/mobile.md)
- [Seasonal Presets](../../docs/seasonal.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Ex +0.5, Contrast -15, Highlights -40, Shadows +35, Whites +15, Blacks +15, Clarity -10, Texture -5, Saturation -5; GreenHue +20, YellowSat -10, GreenSat -30, BlueSat -20, OrangeLum +10, AquaLum +35; shadow H210/S4, highlight H45/S4, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. High-key wedding: +0.50Ex/-15C with Blacks +15 and Clarity/Texture negative reads airy not washed; OrangeLum +10 lifts skin with no orange sat push; cool/tan split at 4% sat.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI skin-safe rule; research WEDDING community recipes (Mastin Labs/Bright & Airy).
- **Preset adjustments:** none
