# Dreamy Maternity Lightroom Preset — Characteristics

## Use Case
The Dreamy Maternity Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Maternity golden hour and outdoor lifestyle sessions. Ethereal, warm without being orange. Soft skin rendering.

## Key Techniques
Mild positive Exposure (+0.40) with negative Contrast (-10) for soft compression. Negative Clarity (-8) and Texture (-5) smooth skin organically. Warm shadows (H45 S8) + warm highlights (H40 S5) create golden envelope. Green desaturation (-20) and hue shift (+15) push foliage toward golden-olive. Just 18 attributes — structured, simple. |Vibrance−Saturation|=2.

## Safety Check
- ProcessVersion: 15.4
- Treatment: Color
- Look Profile: Adobe Color
- Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGradeBlending: 75
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: Checked — within ±5
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
- **Defining traits checked:** Ex +0.4, Contrast -10, Highlights -35, Shadows +30, Whites +10, Blacks +10, Clarity -8, Texture -5, Vibrance -3, Saturation -5; GreenHue +15, YellowSat -10, GreenSat -20, OrangeLum +12; shadow H45/S8, highlight H40/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Ethereal maternity: +0.40Ex, -10C, Clarity -8/Texture -5 smooth skin without plastic, warm H45/H40 envelope at 5-8%, OrangeLum +12 with no orange sat push.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI; research maternity/portrait recipes.
- **Preset adjustments:** none

> **Validation Sweep 2026-10-21 — hue direction correction.** Lightroom's HSL hue axis runs Red → Orange → Yellow → Green → Aqua → Blue, so a *negative* Green Hue moves foliage toward yellow/olive and a *positive* value moves it toward cyan. The preset originally encoded this with the opposite sign; it now matches the olive/yellow-green shift described above.
