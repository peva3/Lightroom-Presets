# Stage Lighting Lightroom Preset — Characteristics

## Use Case
The Stage Lighting Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Concert and live performance photography. Stage LED lighting, spotlights, haze. Dramatic, colorful, high-energy.

## Key Techniques
High Contrast (+30) + strong Clarity (+25) for stage drama and musician detail. Dehaze +15 cuts through stage haze for sharp spotlight beams. Blue Sat +10 and Magenta Sat +10 enhance common concert lighting colors. Green Sat -20 removes ugly green cast from fluorescent stage backlights. Teal/orange split (H225 S15 shadows, H42 S12 highlights) enhances the natural concert color contrast. |Vibrance−Saturation|=3. 20 attributes.

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
- **Defining traits checked:** Ex +0.25, Contrast +30, Highlights -50, Shadows +15, Whites +10, Blacks -15, Clarity +25, Dehaze +15, Vibrance +5, Saturation +8; GreenSat -20, BlueSat +10, MagentaSat +10; shadow H225/S15, highlight H42/S12, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Concert: +30C/Clarity +25 for performers, Dehaze +15 for beams, BlueSat +10/MagentaSat +10 for LED palettes, GreenSat -20 kills fluorescent backlight, H225/H42 split, Highlights -50 protects spotlights.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V/VI.
- **Preset adjustments:** none
