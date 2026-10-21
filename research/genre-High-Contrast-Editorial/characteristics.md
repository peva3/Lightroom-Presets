# High Contrast Editorial Lightroom Preset — Characteristics

## Use Case
The High Contrast Editorial Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. High-fashion editorial photography. Studio and location fashion, runway, lookbooks. Bold, dramatic, unapologetic contrast.

## Key Techniques
High Contrast (+40) is the defining move — fashion editorial wants punch. Clarity +15 adds structural crunch for clothing textures (leather, denim, sequins). Cool shadows (H230 S18) create that signature fashion blue-black. Desaturated greens/oranges keep focus on garments not environment. Light grain (Amount 15) for magazine-print texture. Sharpness=10 per grain rule. |Vibrance−Saturation|=2. 22 attributes — richer than average but each slider has purpose.

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
- Grain protection: Sharpness=10, Clarity=0, Texture=0, Dehaze=0

## See Also

- [Genre Presets](../../docs/genre.md)
- [Mobile Presets](../../docs/mobile.md)
- [Seasonal Presets](../../docs/seasonal.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Ex -0.15, Contrast +40, Highlights -45, Shadows +10, Whites +10, Blacks -20, Vibrance -8, Saturation -10, Sharpness +10, Grain +15; OrangeSat -10, YellowSat -10, GreenSat -25, BlueSat -10; shadow H230/S18, highlight H38/S10, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Fashion: +40C, Blacks -20, cool H230/S18 shadows, OrangeSat -10 so garments lead, Grain 15 with Sharpness 10 and Clarity/Texture/Dehaze 0. Docs drift: characteristics.md claims Clarity +15, which the file (correctly) does not carry - grain and clarity must not coexist.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VII/IX (grain vs sharpening, audit note).
- **Preset adjustments:** none
