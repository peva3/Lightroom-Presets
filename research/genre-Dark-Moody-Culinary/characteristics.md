# Dark Moody Culinary Lightroom Preset — Characteristics

## Use Case
The Dark Moody Culinary Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Dark, dramatic culinary photography. Wooden tables, dramatic side lighting, rustic dishes. Moody restaurant and chef portrait style.

## Key Techniques
Underexposure (-0.40) + strong Contrast (+25) create dramatic tonality. Blacks at -20 anchor shadows (within -30 safety floor). Red/Orange Sat +10 keep food colors present in the dark; everything else desaturated. Teal shadows (H220 S15) add moody cool depth. Light grain (Amount 15) for filmic texture without overwhelming food detail. Sharpness=10 protects grain. |Vibrance−Saturation|=3. 22 attributes — richest of the food presets.

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
- **Defining traits checked:** Ex -0.4, Contrast +25, Highlights -50, Shadows +10, Whites -5, Blacks -20, Vibrance -12, Saturation -15, Sharpness +10, Grain +15; RedSat +10, OrangeSat +10, YellowSat +5, GreenSat -30, BlueSat -20; shadow H220/S15, highlight H40/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Moody food: -0.40Ex, +25C, Blacks -20 anchors without crushing, Red/OrangeSat +10 keep food colour alive in shadow, Green/Blue pulled back, Grain 15 with Sharpness 10/Clarity 0/Texture 0 per grain rule.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VII (grain vs sharpening); research culinary recipes.
- **Preset adjustments:** none
