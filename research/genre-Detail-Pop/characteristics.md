# Detail Pop Lightroom Preset — Characteristics

## Use Case
The Detail Pop Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Wildlife photography — birds, mammals, reptiles. Fur, feather, and scale detail. Natural habitat backgrounds.

## Key Techniques
Texture +15 + Clarity +15 is the detail duo — fur and feather structure pops. Green Hue +10 + Green Sat -15 naturalize foliage backgrounds without distracting from subject. Orange Sat +10 + Yellow Sat +10 enhance animal coat colors and golden-hour rim light. Blue Sat +10 for sky backgrounds. Subtle Dehaze +5 for distance clarity. |Vibrance−Saturation|=2. 20 attributes.

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
- **Defining traits checked:** Ex +0.15, Contrast +15, Highlights -30, Shadows +20, Whites +10, Blacks -10, Clarity +15, Texture +15, Dehaze +5, Vibrance +12, Saturation +10; GreenHue +10, OrangeSat +10, YellowSat +10, GreenSat -15, BlueSat +10; shadow H220/S5, highlight H43/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Wildlife: Texture +15/Clarity +15 is the detail duo, GreenSat -15 naturalises habitat, Orange/YellowSat +10 lift coat and rim light, Dehaze +5 only. Vibrance +12 vs Saturation +10 (gap 2) safe.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V safety caps; research wildlife recipes.
- **Preset adjustments:** none
