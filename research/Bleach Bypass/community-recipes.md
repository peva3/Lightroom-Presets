# Bleach Bypass — Community Recipes

## STYLEGUIDE v2.1 Alignment
- **Fixed**: Blacks2012=0 → -50, ColorGradeBlending=75 → 50, HighlightSat=6.5 → 7.5 (STYLEGUIDE §X Bleach Bypass archetype recipe overrides Creative defaults)
- **Recipe conflict resolution**: STYLEGUIDE Bleach Bypass recipe explicitly specifies Clarity=+45, Dehaze=+20 WITH GrainAmount=41-45. The recipe overrides the general grain-protection rule (Clarity/Texture/Dehaze=0) because the chemical bleach bypass process inherently combines high contrast texture with grain.
- **Boilerplate verified**: ProcessVersion=15.4, Treatment=Color, Adobe Color Look, Cinematic curve
- **Hard bans clean**: No Calibration, no Temperature/Tint, HSL Sat all within ±60
- **Channel-specific desaturation**: 8 color channels individually desaturated (Red -30 through Magenta -40), contrast-driven rather than global Saturation
- **Color Grade**: Shadow H225 S10, Highlight H45 S7.5, Blending 50
- **Blacks2012=-50**: The STYLEGUIDE recipe specifies Blacks=-50 despite the general Creative default of 0. The heavy negative blacks anchor the high-contrast (+70) look.

## Validation Sweep 2026-10-21
- **Verdict:** accurate (aligned to this file's own recipe)
- **Defining traits checked:** (1) contrast explosion — Contrast +70, Highlights -65, Shadows -40, Whites +15, Clarity +45, Dehaze +20; (2) silver-wash desaturation, channel-specific rather than global — Red -30, Orange -25, Yellow -35, Green -40, Aqua -45, Blue -20, Purple -35, Magenta -40 with no global Saturation; (3) inky blacks — Blacks now -50, plus Grain 41.25/40/60 for silver grain.
- **Doc/file divergence found:** this file described Blacks -50, Blending 50 and HighlightSat 7.5 but the XMP still carried -30 / 75 / 6.5. Applied the documented recipe so file and research agree; the -50 black is what separates bleach bypass from "contrasty preset".
- **Sources:** Kodak "Processing Techniques" (retained silver raises contrast, lowers saturation, deepens shadows); ASC "Soup du Jour" / Seven CCE & Saving Private Ryan ENR; lowepost SPR case study (Dale Grahn); finalcolor.com ("maroons and blues tend to go black"); STYLEGUIDE §X Bleach Bypass.
- **Preset adjustments:** Blacks2012 -30 → -50; ColorGradeBlending 75 → 50; ColorGradeHighlightSat 6.5 → 7.5.
