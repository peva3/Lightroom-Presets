# Warm Appetizing Food Lightroom Preset — Characteristics

## Use Case
The Warm Appetizing Food Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Restaurant, recipe, and food blog photography. Warm, inviting, makes food look hot and fresh. Works with breads, meats, golden-brown dishes.

## Key Techniques
Warm-dominant Color Grading: shadows H35 S12 + highlights H45 S10 envelop food in golden warmth. Red/Orange Sat +15 boost tomato, meat, and spice tones. Yellow Sat +10 enhances butter, cheese, bread crust. Texture +10 makes food surfaces tactile (bread crumb, sear marks). Green Sat -15 prevents garnish from stealing focus. |Vibrance−Saturation|=0. 18 attributes.

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
- **Defining traits checked:** Ex +0.2, Contrast +15, Highlights -25, Shadows +15, Whites +10, Blacks -10, Texture +10, Vibrance +10, Saturation +10; RedSat +15, OrangeSat +15, YellowSat +10, GreenSat -15, OrangeLum +10; shadow H35/S12, highlight H45/S10, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. The food brief done properly: H35/S12 shadow + H45/S10 highlight warmth, RedSat +15/OrangeSat +15 (protected, not clipped), YellowSat +10 for crust, Texture +10 for sear, GreenSat -15 so garnish does not steal focus.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI warm recipe (H45, Sat 5-10); food community recipes.
- **Preset adjustments:** none
