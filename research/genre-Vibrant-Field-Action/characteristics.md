# Vibrant Field Action Lightroom Preset — Characteristics

## Use Case
The Vibrant Field Action Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Outdoor field sports — soccer, football, baseball, lacrosse, field hockey. Bright daylight, green fields, fast action.

## Key Techniques
Clarity +15 + Texture +10 for action detail — jersey numbers, facial expressions, ball tracking. Dehaze +10 cuts atmospheric haze for long-lens shots. Green Hue +15 shifts grass to natural olive; Green Sat only -5 (sports fields should look vibrant). Blue Sat +10 deepens sky. Yellow Sat +10 boosts uniforms and field markings. |Vibrance−Saturation|=2. 19 attributes.

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
- **Defining traits checked:** Ex +0.2, Contrast +20, Highlights -30, Shadows +20, Whites +15, Blacks -10, Clarity +15, Texture +10, Dehaze +10, Vibrance +12, Saturation +10; GreenHue +15, YellowSat +10, GreenSat -5, BlueSat +10; shadow H240/S5, highlight H43/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Field sport: Clarity +15/Texture +10 for jersey numbers, Dehaze +10 for long lenses, GreenHue +15 with GreenSat only -5 so turf stays vivid, BlueSat +10 sky, Vibrance 12/Saturation 10 (gap 2).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V.
- **Preset adjustments:** none

> **Validation Sweep 2026-10-21 — hue direction correction.** Lightroom's HSL hue axis runs Red → Orange → Yellow → Green → Aqua → Blue, so a *negative* Green Hue moves foliage toward yellow/olive and a *positive* value moves it toward cyan. The preset originally encoded this with the opposite sign; it now matches the olive/yellow-green shift described above.
