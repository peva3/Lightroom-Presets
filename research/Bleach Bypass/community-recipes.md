# Bleach Bypass — Community Recipes

## STYLEGUIDE v2.1 Alignment
- **Fixed**: Blacks2012=0 → -50, ColorGradeBlending=75 → 50, HighlightSat=6.5 → 7.5 (STYLEGUIDE §X Bleach Bypass archetype recipe overrides Creative defaults)
- **Recipe conflict resolution**: STYLEGUIDE Bleach Bypass recipe explicitly specifies Clarity=+45, Dehaze=+20 WITH GrainAmount=41-45. The recipe overrides the general grain-protection rule (Clarity/Texture/Dehaze=0) because the chemical bleach bypass process inherently combines high contrast texture with grain.
- **Boilerplate verified**: ProcessVersion=15.4, Treatment=Color, Adobe Color Look, Cinematic curve
- **Hard bans clean**: No Calibration, no Temperature/Tint, HSL Sat all within ±60
- **Channel-specific desaturation**: 8 color channels individually desaturated (Red -30 through Magenta -40), contrast-driven rather than global Saturation
- **Color Grade**: Shadow H225 S10, Highlight H45 S7.5, Blending 50
- **Blacks2012=-50**: The STYLEGUIDE recipe specifies Blacks=-50 despite the general Creative default of 0. The heavy negative blacks anchor the high-contrast (+70) look.
