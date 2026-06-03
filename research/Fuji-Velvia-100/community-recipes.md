# Fuji Velvia 100 — Lightroom Preset Settings & Recipes

> Community emulation strategies from t3mujinpack, Reddit, and film forums. Less extreme than Velvia 50, warmer, with usable skin tones.

---

## t3mujinpack Reference (Primary Source)

**Source**: t3mujinpack — Fuji Velvia 100 Darktable .dtstyle profile

The t3mujinpack treats Velvia 100 as a distinct profile from Velvia 50 — not simply "Velvia 50 with saturation turned down." Key differences in the .dtstyle data:

1. **Lower contrast**: Shadow compression is gentler, highlight protection less aggressive
2. **Yellow rendering more neutral**: The yellow→red shift is moderated significantly
3. **Better skin tones**: Orange luminance is elevated relative to Velvia 50, and orange saturation is reduced
4. **Warmer overall balance**: The highlight color grade shifts warm (golden) rather than cool-neutral
5. **Finer grain profile**: Grain values are set lower than Velvia 50

### t3mujinpack Directional Values (Darktable → LR translation)

| Parameter | Direction | Notes |
|-----------|-----------|-------|
| Contrast | +25 to +35 | High but below V50 (+40) |
| Highlights | -35 to -45 | Wider latitude than V50 (-65) |
| Shadows | -15 to -20 | Less crush than V50 (-30) |
| Blacks | -25 to -30 | Deep but not extreme |
| Red Hue | +10 to +15 | Slight orange bias |
| Yellow Hue | -5 to -15 | Less aggressive than V50 (-17.5) |
| Green Hue | +10 to +20 | Cooler greens than V50 |
| Blue Hue | -5 | Subtle cyan shift |
| Green Sat | +20 to +30 | Rich but below V50 (+35) |
| Blue Sat | +15 to +25 | Punchy but conservative |
| Red Sat | +10 to +15 | Natural vs. V50's +22.5 |
| Green Lum | -10 to -15 | Plant density |
| Blue Lum | -10 to -20 | Sky depth |
| Orange Lum | +5 to +10 | Key for skin tones |
| ColorGrade Highlight | Hue 45-55, Sat 5-10 | Warm golden glow |
| ColorGrade Shadow | Hue 215-225, Sat 8-12 | Cool blue separation |

---

## Community Consensus

### r/Lightroom on Velvia 100 vs. 50

- Velvia 100 is preferred for presets that need to work on **people + landscape** — V50 makes skin unusable
- The "nature photographer's sweet spot" — enough pop for landscapes, enough restraint for environmental portraits
- Often cited as the missing link between Velvia 50 (too extreme) and Provia (too neutral)
- Community mostly uses VSCO Film 01's "Velvia 100" profile as reference, or RNI All Films 5

### r/analog Shooters

- Velvia 100 is still produced and widely available (unlike many films in this collection)
- Home E-6 development is straightforward with modern kits
- Real Velvia 100 shooters note the film handles mixed lighting better than V50
- The slightly cooler green rendering is actually more accurate to reality than V50's hyper-green

---

## Calibration Caveats

The community frequently recommends calibration panel values for Velvia emulation. All calibration values have been **excluded** per STYLEGUIDE rules (no calibration except Canon Color Science). The t3mujinpack's directional color shifts inform HSL values directly instead.

---

## Key Differences from Velvia 50 (reference for preset builders)

| Element | Velvia 50 | Velvia 100 | Delta |
|---------|-----------|------------|-------|
| Contrast | +40 | +30 | -10 |
| Highlights | -65 | -40 | +25 (less aggressive) |
| Shadows | -30 | -15 | +15 (less crush) |
| Yellow Hue | -17.5 | -10 | +7.5 (more neutral) |
| Green Sat | +35 | +25 | -10 |
| Red Sat | +22.5 | +12.5 | -10 |
| Orange Sat | +20 | +12.5 | -7.5 |
| Orange Lum | +7.5 | +5 | -2.5 |
| Grain | 5/15/50 | 5/15/50 | Same (both fine-grain) |
| ColorGrade Highlight | Hue 50, Sat 7.5 | Hue 50, Sat 5 | -2.5 (more subtle) |

---

## Sources

- t3mujinpack — Fuji Velvia 100 Darktable profile
- r/Lightroom: "Velvia 100 vs 50 for presets", "Landscape presets with skin tones"
- r/analog: Velvia 100 user discussions and sample images
- VSCO Film 01 Velvia 100 (discontinued reference)
- RNI All Films 5 — Fuji Velvia 100 profile
- Ken Rockwell, "Fuji Velvia 100 Review"

---

## See Also

- [Fuji Velvia 100 — Film Characteristics](../Fuji-Velvia-100/characteristics.md)
- [Fuji Velvia 50 Lightroom Preset](../Fuji-Velvia-50/community-recipes.md)
- [Fuji Astia 100F Lightroom Preset](../Fuji-Astia-100F/community-recipes.md)
- [Fuji Provia 100F Lightroom Preset](../Fuji-Provia-100F/community-recipes.md)
- [XMP Preset: Fuji Velvia 100](../../Presets/Slide/Fuji Velvia 100.xmp)
