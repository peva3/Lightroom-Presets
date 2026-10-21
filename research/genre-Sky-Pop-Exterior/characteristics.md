# Sky Pop Exterior Lightroom Preset — Characteristics

## Use Case
The Sky Pop Exterior Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Real estate exterior shots where sky and curb appeal matter. Blue sky enhancement with natural ground colors.

## Key Techniques
Blue Sat +20 + Blue Lum -10 deepen sky without cyan cast. Aqua Sat +15 gives graduated sky richness. Dehaze +10 cuts atmospheric haze for crisp rooflines. Green Sat -10 prevents lawn from going nuclear. Highlights -40 protects cloud detail. |Vibrance−Saturation|=0. 17 attributes.

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
- **Defining traits checked:** Ex +0.15, Contrast +15, Highlights -40, Shadows +15, Whites +10, Blacks -10, Dehaze +10, Vibrance +5, Saturation +5; GreenSat -10, AquaSat +15, BlueSat +20, BlueLum -10; shadow H230/S8, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Exterior real estate: BlueSat +20 and BlueLum -10 deepen sky without cyan, AquaSat +15 for gradient, Dehaze +10 for rooflines, GreenSat -10 saves lawns, Highlights -40 holds cloud detail.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; Imagen AI real-estate guide; STYLEGUIDE.md sec. VI.
- **Preset adjustments:** none
