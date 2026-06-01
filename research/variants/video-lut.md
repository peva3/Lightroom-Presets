# Video LUT Cross-Format Presets

## Purpose
These XMP presets serve as reference for .cube LUT generation. Each is a color-grade-optimized version of a top film/creative preset, adjusted for video's lower dynamic range, Rec.709 color space constraints, and grain aliasing on codecs.

## Video-Specific Adjustments
- Blacks lifted (floor ≥ -15 for Rec.709 safety)
- Contrast reduced -5 (wider apparent DR)
- Highlights pulled -8 harder (video clips earlier)
- Grain reduced: -8 to -15 Amount, -5 Size (avoids codec aliasing)
- Calibration and Temperature/Tint stripped (video color pipelines handle WB differently)
- Cinematic tone curve applied

## Presets (20)

### Film-Based Video (13)
- Portra 400 Video, Gold 200 Video, Ektar 100 Video
- Cinestill 800T Video
- Kodachrome 64 Video, Velvia 50 Video
- Tri-X 400 Video

### Creative-Based Video (7)
- Teal & Orange Cinematic Video, Cyberpunk Neon Video
- Moody PNW Video, Bleach Bypass Video
- VHS Synthwave Video, WKW Hong Kong Video
- Wes Anderson Pastel Video, Kodak Aerochrome Video
- Cinematic Dream Look Video, Cross-Processed Velvia Video
- Polaroid SX-70 Video, Super 8 Home Movie Video
- Pastel Anime Aethereal Video
