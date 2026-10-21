# Epic Landscape Lightroom Preset — Characteristics

## Use Case
The Epic Landscape Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Grand aerial landscapes — mountain ranges, coastlines, forests from above. Epic scale, vibrant colors, dramatic light.

## Key Techniques
Strong Contrast (+25) + Dehaze (+10) + Clarity (+15) for epic landscape structure. Blue Sat +15 for sky drama; Yellow Sat +10 for golden-hour warmth. Green Hue +15 + Green Sat -15 naturalize vast forest/field expanses. Cool-on-warm Color Grading (shadows H230 S8, highlights H43 S8) adds cinematic depth. |Vibrance−Saturation|=0. 20 attributes.

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
- **Defining traits checked:** Ex +0.2, Contrast +25, Highlights -45, Shadows +25, Whites +15, Blacks -10, Clarity +15, Dehaze +10, Vibrance +10, Saturation +10; GreenHue +15, YellowSat +10, GreenSat -15, AquaSat +5, BlueSat +15; shadow H230/S8, highlight H43/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. +25C, Highlights -45, Dehaze +10, Clarity +15 for scale; BlueSat +15 for sky, GreenSat -15 to stop forest mush; Vibrance 10/Saturation 10 (gap 0).
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. IV/V; landscape community recipes.
- **Preset adjustments:** none
