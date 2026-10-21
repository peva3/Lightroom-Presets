# Zone Focus B&W Lightroom Preset — Characteristics

## Use Case
The Zone Focus B&W Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. Classic B&W street photography. Zone focus shooting, decisive moment capture, urban documentary. The 'Tri-X pushed to 1600' look.

## Key Techniques
B&W mixer is the hero: Red +25 lightens skin/faces, Orange +15 brightens skin, Green -20 darkens foliage for depth, Blue -25 creates dramatic dark skies. Contrast +35 for bold tonal separation. Blacks at -25 (within -30 floor) for deep shadows that 'go black deliberately.' Grain Amount 45, Size 30, Roughness 60 for pushed-Tri-X character. Sharpness=10 per grain rule. Neutral tone curve per B&W convention. Adobe Monochrome Look profile. 19 attributes.

## Safety Check
- ProcessVersion: 15.4
- Treatment: Monochrome
- Look Profile: Adobe Monochrome
- Curve: Neutral (0,0 → 255,255)
- ColorGradeBlending: 50
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: N/A (B&W)
- HSL Sat max: Within ±60
- Blacks floor: ≥ -30
- Grain protection: Sharpness=10, Clarity=0, Texture=0, Dehaze=0

## See Also

- [Genre Presets](../../docs/genre.md)
- [Mobile Presets](../../docs/mobile.md)
- [Seasonal Presets](../../docs/seasonal.md)
- [All Lightroom Preset Categories](../../docs/index.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Ex +0.1, Contrast +35, Highlights -30, Shadows +20, Whites +10, Blacks -25, Sharpness +10, Grain +45; HSL all zero; blending 50; calibration none; PV 15.4, Monochrome, Adobe Monochrome Look; 4 neutral curves. Pushed-Tri-X: ConvertToGrayscale=True, Adobe Monochrome Look, GrayMixer Red +25/Orange +15 (skin), Green -20/Blue -25 (foliage/sky), +35C, Blacks -25, Grain 45/30/60 with Sharpness 10 and Clarity/Texture 0.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VII/IX; B&W mixer practice.
- **Preset adjustments:** none
