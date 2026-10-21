# Eye Enhance Lightroom Preset — Characteristics

## Use Case
The Eye Enhance Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Wildlife portraiture emphasizing eyes and facial detail. Big cats, birds of prey, primates. Catchlight and iris detail.

## Key Techniques
Milder overall treatment than Detail Pop — the eyes should be the most detailed element. Texture +10 + Clarity +10 for facial detail without overcooking. Red Sat +5 enhances eye color (many animals have red/orange in eyes). Blue Sat +5 for sky catchlights in eyes. Low Contrast (+10) preserves eye shadow detail. Orange Lum +5 subtly brightens fur around eyes. Minimal Color Grading. |Vibrance−Saturation|=3. 18 attributes.

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
- **Defining traits checked:** Ex +0.2, Contrast +10, Highlights -25, Shadows +15, Whites +5, Blacks -5, Clarity +10, Texture +10, Vibrance +8, Saturation +5; RedSat +5, GreenSat -10, BlueSat +5, OrangeLum +5; shadow H215/S3, highlight H43/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Wildlife portrait: milder than Detail Pop (Texture +10/Clarity +10), RedSat +5 for iris colour, BlueSat +5 for catchlights, Contrast +10 preserves eye shadow detail, OrangeLum +5 only.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. V.
- **Preset adjustments:** none
