# Ektachrome 100G — Community Recipes

> Community emulation strategies from t3mujinpack and film forums. Finer grain, cooler, more neutral than current E100.

---

## t3mujinpack Reference (Primary Source)

**Source**: t3mujinpack — Ektachrome 100G Darktable .dtstyle profile

The t3mujinpack treats E100G as a professional-neutral slide film — minimal adjustments, high fidelity. From the .dtstyle data:

1. **Neutral baseline**: Fewer HSL adjustments than any other slide film profile — E100G was about accuracy, not character
2. **Cooler highlight tint**: Slightly cool highlights (the "blue neutral" look)
3. **Finer grain**: Grain values are lower than current E100 or E100VS — RMS 8 quality
4. **Subtle blue boost**: A modest blue/aqua saturation increase — the defining color move
5. **Minimal hue shifts**: Almost no hue adjustments — the film itself was neutral

### t3mujinpack Directional Values (Darktable → LR translation)

| Parameter | Value/Direction | Notes |
|-----------|----------------|-------|
| Contrast | +20 | Moderate — slide film contrast without drama |
| Highlights | -15 | Standard highlight protection |
| Shadows | -15 | Moderate shadow depth |
| Blacks | -25 | Clean blacks, not crushed |
| Whites | -5 | Slight highlight compression |
| Saturation | +3 | Very subtle global saturation |
| Red Hue | +5 | Slight warmth in reds |
| Green Hue | +10 | Slide-film green shift |
| Blue Hue | -5 | Subtle warmth in skies |
| Red Sat | +5 | Minimal boost |
| Aqua Sat | +5 | Clean aqua for skies |
| Blue Sat | +7.5 | Clean deep blue (no Kodachrome drama) |
| Red Lum | -5 | Slight density |
| Blue Lum | -5 | Minor sky darkening |
| Grain | Amount 5, Size 15 | RMS 8 = nearly invisible |
| Highlight tint | H40, Sat 5 | Slightly cool highlight |
| Shadow tint | H215, Sat 5 | Clean blue shadow |
| Blending | 75 | Clean color separation |

---

## Commercial Photography Community

E100G was the slide film of choice for:
- **Catalog photography**: Clothing, products, furniture — color accuracy was mandatory
- **Architectural photography**: Clean whites, accurate greys, controlled blues
- **Food photography**: True-to-life color rendering
- **Reproduction work**: Art documentation, museum archives

Photographers prized E100G for its "blank canvas" quality — it didn't impose a look. The film stayed out of the way and let the subject speak.

---

## Comparison with Current E100 (for preset builders)

| Element | E100G | Current E100 | Difference |
|---------|-------|-------------|------------|
| Grain | Finer (RMS 8) | Coarser (RMS ~11) | Lower grain, finer texture |
| Color balance | Neutral-cool | Neutral-warm | Cooler, more clinical |
| Blue rendering | Warm blue | Clean blue | Subtly warmer blue |
| Skin tones | Cool, accurate | Warm, flattering | Less flattering, more accurate |
| Saturation | +3 | Similar | Slightly lower |
| Professional vs. Consumer | Professional standard | Enthusiast market | E100G was for pro workflows |

---

## Key Preset Design Principles

1. **Accuracy over character**: This is not a "look" film — it's a baseline
2. **Minimal adjustments**: Fewer than 15 attributes total (the closest to the originals' philosophy)
3. **Fine grain**: RMS 8 means essentially grain-free at normal viewing
4. **Cool advantage**: The slightly cool neutral is the defining difference from current E100
5. **Clean color separation**: Color grading at Blending 75 for crisp shadow/highlight divide

---

## Sources

- t3mujinpack — Ektachrome 100G Darktable profile
- Kodak Ektachrome E100G technical datasheet (2001)
- Photo.net forums: "E100G vs. Provia 100F" commercial comparison
- Rangefinderforum.com: "E100G — the last pro Ektachrome"
- fujixweekly.com — E100 recipes for reference direction
