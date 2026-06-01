# Fujifilm Eterna — Community Recipes

## Source: Fuji X Weekly (Eterna Summer recipe)

### Fuji Camera Recipe
```
Film Simulation: Eterna
Dynamic Range: DR200
Grain Effect: Strong, Small
Color Chrome Effect: Strong
Color Chrome Effect Blue: Strong
White Balance: Daylight, +3 Red, -7 Blue
Highlight: +2.5
Shadow: 0
Color: +4
Sharpness: -1
Noise Reduction: -4
Clarity: -3
ISO: Auto, up to ISO 6400
Exposure Compensation: +1/3 to +2/3 (typically)
```

### Fuji → Lightroom Translation
| Fuji Setting | LR Attribute | Value | Notes |
|---|---|---|---|
| H+2.5 | Highlights2012 | +25 | -2 to +4 → -20 to +40 (10/unit) |
| S0 | Shadows2012 | 0 | Inverted: 0→0 |
| Color+4 | Saturation | +15 | -4 to +4 → -20 to +20 (5/unit). Reduced to +15 for balance |
| Sharp-1 | Sharpness | 10 (capped) | Grain rule: max 10 |
| Clarity-3 | Clarity | 0 | Grain rule: Clarity=0 with grain |
| Grain Strong/Small | GrainAmount/Size | 35/15 | Weak→15, Strong→35; Small→15, Large→35 |
| Roughness≈50 | GrainFrequency | 50 | Standard roughness |
| DR200 | Exposure | -0.15 | Slight underexposure compensation |

### Key Design Decisions
1. **Saturation reduced from +20 to +15** — Fuji's Color+4 on Eterna base sim is already moderate; +20 in LR on neutral curve is aggressive
2. **Clarity set to 0** per STYLEGUIDE grain rule
3. **No WB** per STYLEGUIDE — warm cast via Color Grading (Shadow H40, Highlight H45)
4. **Negative Contrast (-10)** to maintain Eterna's signature low-contrast cinema look
5. **Vibrance matched to Saturation** (+12 vs +15, gap=3 ≤ 5)

### Eterna vs. Eterna Bleach Bypass
| Aspect | Eterna | Eterna Bleach Bypass |
|---|---|---|
| Contrast | Low (-10) | Very high (+55) |
| Saturation | Moderate (+15) | Heavily desaturated (-20) |
| Grain | Fine (Strong/Small) | Coarse (Strong/Medium) |
| Shadows | Open (0) | Crushed (-20) |
| Color cast | Warm golden | Metallic cool-warm |
| Category | Color-Negative | Creative |
