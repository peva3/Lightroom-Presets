# Fujifilm Nostalgic Negative — Lightroom Preset Settings & Recipes

## Source: Fuji X Weekly (Nostalgic Air recipe)

### Fuji Camera Recipe
```
Film Simulation: Nostalgic Negative
Grain Effect: Strong, Small
Color Chrome Effect: Off
Color Chrome Effect Blue: Off
White Balance: Auto, +5 Red, -1 Blue
Dynamic Range: DR100
Highlight: -1
Shadow: 0
Color: +4
Sharpness: -2
Noise Reduction: -4
Clarity: -3
ISO: Auto, up to ISO 6400
Exposure Compensation: 0 to +2/3 (typically)
```

### Fuji → Lightroom Translation
| Fuji Setting | LR Attribute | Value | Notes |
|---|---|---|---|
| H-1 | Highlights2012 | -10 | -2 to +4 → -20 to +40 (10/unit) |
| S0 | Shadows2012 | 0 | Inverted: 0→0 |
| Color+4 | Saturation | +15 | Reduced from +20 for balance |
| Sharp-2 | Sharpness | 5 | Grain rule: max 10. Sharp-2 → 5 in LR |
| Clarity-3 | Clarity | 0 | Grain rule: Clarity=0 with grain |
| Grain Strong/Small | GrainAmount/Size | 35/15 | Weak→15, Strong→35; Small→15, Large→35 |
| Roughness≈50 | GrainFrequency | 50 | Standard roughness |

### Key Design Decisions
1. **Amber cast via Color Grading, not WB**: STYLEGUIDE prohibits WB in presets. Shadow H40/S12 + Highlight H45/S8 creates the warm amber-green character
2. **Green Hue +10**: Shifts greens toward yellow-olive for the amber-green photo album aesthetic
3. **Saturation +15 (not +20)**: Fuji's Color+4 on Nostalgic Neg already has a strong amber boost; +20 in LR with neutral curve would oversaturate
4. **Vibrance +12**: Within 3 points of Saturation +15 per the Vib-Sat gap rule
5. **Blacks at +10**: Gentle black point for the vintage print aesthetic — never crushed
6. **Contrast -5**: Soft tonal transitions characteristic of aged photo prints

### Related Fuji X Weekly Recipes
- **Nostalgic Print** (higher contrast variant): H0/S+1/Color+3/Sharp-1
- **Nostalgic Summer** (brighter variant): H-2/S+1/Color+2/Sharp-1/Clarity-2
- **1970s Summer** (Kodak Instamatic inspired): Nostalgic Neg + warm WB + very low contrast

---

## See Also

- [Fujifilm Nostalgic Negative — Film Characteristics](../Fujifilm-Nostalgic-Negative/characteristics.md)
- [Fujifilm Classic Negative Lightroom Preset](../Fujifilm-Classic-Negative/community-recipes.md)
- [Fujifilm Pro 400H Lightroom Preset](../Fujifilm-Pro-400H/community-recipes.md)
- [Fuji Astia 100F Lightroom Preset](../Fuji-Astia-100F/community-recipes.md)
