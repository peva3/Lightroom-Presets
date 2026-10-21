# M645 Medium Format — Look Characteristics

## Overview
The M645 Medium Format look is inspired by the tonal character of Mamiya 645 medium format camera systems. Medium format film (6x4.5cm negatives) produces a distinctive look characterized by smooth tonal transitions, gentle contrast, and a sense of depth that comes from the larger negative area.

## Key Characteristics
- **Format**: 6x4.5cm medium format (Mamiya 645 system)
- **Negative Size**: ~2.7x larger than 35mm (by area)
- **Depth of Field**: Shallower at equivalent apertures — contributes to subject separation
- **Tonal Transitions**: Smooth, creamy — the "medium format look"
- **Contrast**: Gentle, natural — larger negatives compress tones less aggressively
- **Grain**: Less apparent — the larger negative area means grain is less magnified
- **Sharpness**: Excellent detail rendering without harsh edge definition

## Mamiya 645 System
- Mamiya M645 (1975), M645 1000S, M645 Super, M645 Pro, M645 Pro TL
- 6x4.5cm format — 15-16 exposures per 120 roll
- Wide range of Mamiya-Sekor lenses known for their particular rendering
- The "645" format was designed as a compromise between 35mm convenience and 6x6/6x7 quality
- Popular with wedding, portrait, and fashion photographers through the 1980s-1990s

## Visual Signature
- Smooth, "creamy" tonal transitions between shadows and highlights
- Gentle contrast — not as punchy as 35mm
- Fine detail without harsh digital sharpness
- Natural depth and dimensionality from larger format
- Less grain at normal viewing sizes
- Colors (in original XMP) are desaturated with warmth and subtle green shifts

## Sources
- Archive-663/lightroomPresets GitHub repo (original M645.xmp reference)
- Mamiya camera system documentation
- Medium format photography community resources

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** generic 6x4.5 look (not a film stock) - smooth tonal transitions, gentle contrast, grain far less apparent than 35mm
- **Checked against XMP:** Contrast +15 (gentlest of the film presets), Highlights -20 / Shadows +20 (creamy transition), Blacks -20, GrainAmount 25 / GrainSize 25
- **Sources:** research/M645-Medium-Format characteristics; medium-format tonality consensus
- **Preset adjustments:** none
- **Note:** Judged against the format's tonal signature, not a datasheet. Grain 25 is above what a real 645 negative shows in print - it is a deliberate texture floor, not an error.
