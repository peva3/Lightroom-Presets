# McCurry Kodachrome — Characteristics

## Film Background
Kodachrome 64 (introduced 1974, third era) was actually a B&W film with color dyes added during the K-14 development process. It is the most difficult film to scan accurately, often producing a blue cast. McCurry's "last roll" slides were scanned by Richard Jackson, a leading Kodachrome scanning expert.

## Key Aesthetic
- Properly-scanned Kodachrome aesthetic (not projected-slide look)
- Warm, saturated reds and skin tones
- Subtle cool shadow bias (scan artifact, not projection artifact)
- Narrow dynamic range requiring careful exposure
- Best results at ISO ≤ 1600
- Classic Chrome base gives Kodak-like warm neutrality

## XMP Translation
- No WB (the 5900K Classic Chrome rendering is profile-based, not slider-based)
- Neutral Highlights/Shadows (recipe uses H:0/S:0)
- Subtle grain (Weak/Small → Amount 20, Size 22)
- Modest saturation (Color +2 → Sat +12)
- Warm highlight + cool shadow ColorGrade for Kodachrome scan aesthetic
- Orange luminance boost for skin warmth

## STYLEGUIDE Compliance
- No Calibration ✓
- No WB (not defining; Classic Chrome profile handles color) ✓
- |Vibrance - Saturation| = 2 ≤ 5 ✓
- HSL ≤ ±60 ✓
- Grain → Sharpness=10, LuminanceSmoothing=0 ✓
- Tone Curve: Cinematic Creative ✓
- ColorGradeBlending: 75 ✓
