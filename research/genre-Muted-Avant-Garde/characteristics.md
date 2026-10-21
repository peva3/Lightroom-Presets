# Muted Avant-Garde Lightroom Preset — Characteristics

## Use Case
The Muted Avant Garde Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Avant-garde and conceptual fashion. Near-monochrome with subtle blue depth. Works on fashion films, art projects, alternative editorials.

## Key Techniques
Heavy global desaturation (-30) + heavy channel desaturation (Green -50, Blue -30, Yellow -30) create near-monochrome base. Blue/violet shadow split (H250 S10) is the one surviving color — gives the look its eerie cool signature. |Vibrance−Saturation|=5 (exactly at the safety limit). Contrast +20 provides structure that desaturation would otherwise flatten. Clarity +10 adds art-film texture. 18 attributes — desaturation is the hero, everything else supports.

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
- **Defining traits checked:** Ex -0.25, Contrast +20, Highlights -40, Shadows +15, Whites +5, Blacks -10, Clarity +10, Vibrance -25, Saturation -30; RedSat -20, OrangeSat -25, YellowSat -30, GreenSat -50, BlueSat -30; shadow H250/S10, highlight H35/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Near-monochrome: Saturation -30 with GreenSat -50/BlueSat -30/YellowSat -30, single blue-violet shadow signature H250/S10, +20C to keep structure. Vibrance -25/Saturation -30 (gap 5) - the desaturation is the brief, not the selective-colour bug.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VIII.5 (Vibrance-Saturation gap).
- **Preset adjustments:** none
