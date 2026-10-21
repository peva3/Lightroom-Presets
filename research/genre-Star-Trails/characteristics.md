# Star Trails Lightroom Preset — Characteristics

## Use Case
The Star Trails Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Star trail stacking and long-exposure night sky. Circular or linear star trails against dark sky. Foreground composition.

## Key Techniques
Higher Contrast (+35) and Clarity (+25) than MW — star trails need maximum line definition. Blue Sat +15 + Blue Lum -15 for deep rich sky. Aqua Sat +10 and Purple Sat +15 enhance varied star colors. Cool-on-cool Color Grading (shadows H250 S15, highlights H220 S5) creates monochromatic depth. |Vibrance−Saturation|=5. 18 attributes.

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
- **Defining traits checked:** Ex +0.3, Contrast +35, Highlights -50, Shadows +25, Whites +20, Blacks -15, Clarity +25, Dehaze +10, Vibrance +5; AquaSat +10, BlueSat +15, PurpleSat +15, BlueLum -15; shadow H250/S15, highlight H220/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. +35C and Clarity +25 for line definition, BlueSat +15/BlueLum -15 for a deep sky, Aqua +10/Purple +15 for star variety, cool-on-cool H250/H220 grade, Shadows +25/Blacks -15 balanced. No grain, NR at camera default.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI; long-exposure night practice.
- **Preset adjustments:** none
