# Lomography Metropolis — Community Recipes

## Source: Fuji X Weekly (extrapolated from Eterna Bleach Bypass base)

### Fuji Camera Recipe (derived)
```
Film Simulation: Eterna Bleach Bypass
Dynamic Range: DR200
Highlight: +1
Shadow: +2.5
Color: -2
Noise Reduction: -4
Sharpening: -1
Clarity: +4
Grain Effect: Strong, Small
Color Chrome Effect: Strong
Color Chrome Effect Blue: Strong
White Balance: Auto, +1 Red, -7 Blue
ISO: Auto, up to ISO 6400
```

### Fuji → Lightroom Translation
| Fuji Setting | LR Attribute | Value | Notes |
|---|---|---|---|
| H+1 | Highlights2012 | +10 | -2 to +4 → -20 to +40 (10/unit) |
| S+2.5 | Shadows2012 | -25 | Inverted: +2 to +4 → +20 to -40 |
| Color-2 | Saturation | -10 | -4 to +4 → -20 to +20 (5/unit) |
| Sharp-1 | Sharpness | 10 (capped) | Grain rule: max 10 |
| Clarity+4 | Clarity | 0 | Grain rule: Clarity=0 with grain |
| Grain Strong/Small | GrainAmount/Size | 35/15 | Weak→15, Strong→35; Small→15, Large→35 |
| Roughness≈50 | GrainFrequency | 50 | Standard roughness |

### Key Design Decisions
1. **Clarity set to 0** per STYLEGUIDE grain rule — Fuji's Clarity operates differently from LR's
2. **No WB adjustment** per STYLEGUIDE rule — warm cast achieved via Color Grading instead
3. **Sharpness capped at 10** to prevent grain particle sharpening
4. **Desaturation via global Saturation + target HSL** for the "almost B&W" character
5. **Blacks anchored at 0** per Creative category double-fade prevention rule

### Alternative Community Approaches
- Some recipes use Classic Negative as base sim instead of Eterna Bleach Bypass
- Portra 400 + heavy desaturation + contrast boost is an alternative base
- CineStill 800T profile with desaturation is used by some preset packs
