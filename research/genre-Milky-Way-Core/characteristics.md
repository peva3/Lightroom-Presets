# Milky Way Core Lightroom Preset — Characteristics

## Use Case
The Milky Way Core Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Milky Way core astrophotography. Enhancing dust lanes, star color, and galactic structure. Dark sky locations.

## Key Techniques
High Contrast (+30) + Dehaze (+15) for MW dust lane definition. Clarity +20 sharpens cloud structure without star-trailing. Purple Sat +20 + Magenta Sat +15 enhance the natural purple/magenta in the galactic core. Blue Lum -10 deepens night sky. Green Sat -20 removes airglow green cast. Shadow lift (+40) recovers foreground. |Vibrance−Saturation|=5 (at limit, needed for MW color pop). 20 attributes.

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
- **Verdict:** minor drift
- **Defining traits checked:** Ex +0.4, Contrast +30, Highlights -60, Shadows +40, Whites +25, Blacks -20, Clarity +20, Dehaze +15, Vibrance +10, Saturation +5; GreenSat -20, BlueSat +15, PurpleSat +20, MagentaSat +15, BlueLum -10; shadow H260/S10, highlight H40/S8, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Astro core: Shadows +40 lifts, Blacks -20 keeps sky dark without full crush, Highlights -60 protects the core, Dehaze +15/Clarity +20 for dust lanes, Blue +15/Purple +20/Magenta +15 preserve star colour, no grain added. Two drifts from current astro practice: Clarity +20 creates star halos where -5 to -15 is the refined default, and luminance NR is left untouched (absent = camera default), which is noisy at ISO 3200+. Advisory only; contrast is the preset's intent.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; photographylife.com/how-to-edit-milky-way-lightroom; jonnorrisphoto.com Milky Way editing workflow.
- **Preset adjustments:** none
