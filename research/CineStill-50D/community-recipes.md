# CineStill 50D — Lightroom Preset Settings & Recipes

## Source: Fuji X Weekly (extrapolated from CineStill 800T + Astia base)

### Fuji Camera Recipe (derived from Astia-based approach)
The CineStill 50D Lightroom preset community recipes compile settings from photographers worldwide. ```
Film Simulation: Astia
Dynamic Range: DR200
Highlight: -1
Shadow: 0
Color: -4
Noise Reduction: -4
Sharpening: 0
Clarity: -4
Grain Effect: Weak, Small
Color Chrome Effect: Strong
White Balance: 6800K, -5 Red, -3 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: +1/3 to +2/3 (typically)
```

### Fuji → Lightroom Translation
| Fuji Setting | LR Attribute | Value | Notes |
|---|---|---|---|
| H-1 | Highlights2012 | -10 | -2 to +4 → -20 to +40 (10/unit) |
| S0 | Shadows2012 | 0 | Inverted: 0→0 |
| Color-4 | Saturation | -20 | -4 to +4 → -20 to +20 (5/unit) |
| Sharp0 | Sharpness | 10 (capped) | Grain rule: max 10 |
| Clarity-4 | Clarity | 0 | Grain rule: Clarity=0 with grain |
| Grain Weak/Small | GrainAmount/Size | 15/15 | Weak→15, Strong→35; Small→15 |
| Roughness≈50 | GrainFrequency | 50 | Standard roughness |

### Halation Simulation Strategy
Halation (the red/orange glow around highlights when remjet is removed) cannot be directly simulated in LR sliders. This preset approximates it via:
1. **Warm highlight color grading** (Highlight H40/S8) — adds red/orange cast to the brightest tones
2. **Slight exposure boost** (+0.35) — pushes highlights into the warm grading zone
3. **Cool shadow grading** (Shadow H200/S5) — creates complementary contrast to warm highlights

### Key Design Decisions
1. **No WB** per STYLEGUIDE — warmth via Color Grading
2. **Clarity at 0** per grain rule — the Astia Clarity-4 suggestion is handled differently
3. **Vibrance -17**: Within 3 points of Saturation -20
4. **Minimal grain** (Amount 15): ISO 50 + Vision3 = finest grain. This is the primary differentiator from 800T
5. **Exposure +0.35**: ISO 50 sweet spot is slight overexposure (common practice with this stock)

### Distinction from CineStill 800T Preset
| Aspect | 50D | 800T (existing) |
|---|---|---|
| GrainAmount | 15 | 40 |
| GrainSize | 15 | 22.5 |
| Exposure | +0.35 | +0.75 |
| Contrast | +8 | +15 |
| Saturation | -20 (global) | Not set |
| Highlight Grade | H40/S8 (warm) | H50/S12.5 |
| Shadow Grade | H200/S5 (cool) | H210/S25 |
| Category | Color-Negative | Creative |
| Curve | Neutral | Cinematic |
| Blending | 50 | 75 |

---

## See Also

- [CineStill 50D — Film Characteristics](../CineStill-50D/characteristics.md)
- [CineStill 400D Lightroom Preset](../CineStill-400D/community-recipes.md)
- [Cinestill 800T Lightroom Preset](../Cinestill-800T/community-recipes.md)
- [Kodak Vision3 50D Lightroom Preset](../Kodak-Vision3-50D/community-recipes.md)
- [XMP Preset: CineStill 50D](../../Presets/Color-Negative/CineStill-50D.xmp)
