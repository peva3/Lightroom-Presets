# White BG E-Commerce Lightroom Preset — Characteristics

## Use Case
The White BG E Commerce Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. E-commerce product photography on white backgrounds. Amazon, Shopify, eBay. Clean, accurate color, sharp detail.

## Key Techniques
High Exposure (+0.50) + Whites (+25) blow out backgrounds to pure white. Highlights -50 protects product surface highlights from clipping. Clarity +10 + Texture +5 for crisp product detail and texture. Saturation neutral to preserve color accuracy. Minimal Color Grading for neutrality. 15 attributes — simple and consistent.

## Safety Check
- ProcessVersion: 15.4
- Treatment: Color
- Look Profile: Adobe Color
- Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGradeBlending: 75
- Calibration: None (as required)
- Temperature/Tint: None (as required)
- Vibrance−Saturation gap: N/A (no Vibrance)
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
- **Defining traits checked:** Ex +0.5, Contrast +15, Highlights -50, Shadows +15, Whites +25, Clarity +10, Texture +5; RedSat -5, OrangeSat -5; blending 75; calibration none; PV 15.4, Color, Adobe Color Look; 4 neutral curves. Neutral by construction: no Temperature/Tint, no Vibrance/Saturation, CG sats 0; +0.50Ex with Whites +25 sets the white point and Highlights -50 is the shoulder compression STYLEGUIDE prescribes (negative Highlights + positive Whites), so the sweep still clips to white while product speculars survive. Clarity +10/Texture +5 for edge crispness. No cast, no colour shift.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; backyardsilver.com pure-white-background-in-Lightroom; r/productphotography white-on-white thread; STYLEGUIDE.md sec. IV (Highlights = shoulder, Whites = clip point).
- **Preset adjustments:** none
