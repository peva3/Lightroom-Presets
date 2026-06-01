# Cyberpunk Neon City — Community Recipes

## STYLEGUIDE v2.1 Alignment
- **Fixed**: Blacks2012=0 → -40, ColorGradeBlending=75 → 70 (STYLEGUIDE §X Cyberpunk/Blade Runner recipe)
- **Fixed**: Removed Texture=+30 (recipe does not include Texture; grain protection would require 0 anyway with GrainAmount>0)
- **Fixed**: Added Vibrance=-15 to close |Vibrance−Saturation| gap (was 15, now 0)
- **Fixed**: Grain updated to recipe values: Amount=45 (was 17.5), Size=40 (was 30), Frequency=65 (was 55)
- **Fixed**: Removed 16 extra HSL attributes not in recipe (Aqua, Blue, Magenta, Orange, Purple, Red adjustments). STYLEGUIDE recipe specifies only: Green H-90/S-60 (capped from S-90), Yellow S-60 (capped from S-80), Magenta S+55.
- **SAT CAPS APPLIED**: Green Sat -60 and Yellow Sat -60 are at the ±60 system safety cap. The STYLEGUIDE recipe specifies S-90 and S-80 raw values, but Commandment #6 mandates ±60 max to prevent channel destruction + demosaic artifact amplification.
- **Boilerplate verified**: ProcessVersion=15.4, Treatment=Color, Adobe Color Look, Cinematic curve
- **Hard bans clean**: No Calibration, no Temperature/Tint
- **Color Grade**: Shadow H230 S22.5, Highlight H315 S22.5, Blending 70, Balance +30
- **Clarity/Dehaze kept per recipe**: Clarity=+55 and Dehaze=+45 are explicitly specified in the STYLEGUIDE Cyberpunk recipe alongside GrainAmount=45 — the recipe overrides the general grain-protection rule (this is an intentional creative choice for the cyberpunk aesthetic)
