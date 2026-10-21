# Court Action Indoor Lightroom Preset — Characteristics

## Use Case
The Court Action Indoor Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Indoor court sports — basketball, volleyball, gymnastics. Artificial lighting, fast motion, mixed color temperatures.

## Key Techniques
Exposure +0.35 compensates for typical indoor dimness. Contrast +25 + Clarity +20 for action definition. Shadow lift +25 reveals detail on darker side of athletes. Texture +10 for uniform and skin detail. Light orange/red desaturation (-5) calms sodium-vapor arena light casts on skin. Cool shadow split (H225 S8) adds crisp indoor depth. |Vibrance−Saturation|=0. 17 attributes.

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
- **Defining traits checked:** Ex +0.35, Contrast +25, Highlights -35, Shadows +25, Whites +10, Blacks -10, Clarity +20, Texture +10, Vibrance +5, Saturation +5; RedSat -5, OrangeSat -5, GreenSat -5; shadow H225/S8, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Indoor sport: +0.35Ex, +25C, Clarity +20/Texture +10 for action detail, Shadows +25 opens the shaded side of athletes, Red/OrangeSat -5 calms sodium-vapour spill; no WB override (arena lighting is per-venue).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; Sports/venue editing practice; STYLEGUIDE.md sec. V.
- **Preset adjustments:** none
