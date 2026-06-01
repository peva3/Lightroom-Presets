# Kodachrome 200 — Community Recipes

> Community emulation strategies from t3mujinpack and film forums. Warmer, grainier, action-oriented Kodachrome.

---

## t3mujinpack Reference (Primary Source)

**Source**: t3mujinpack — Kodachrome 200 Darktable .dtstyle profile

The t3mujinpack distinguishes Kodachrome 200 from K64 through four key differences:

1. **Warmer color balance**: White balance shifted warmer — the defining K200 characteristic
2. **Increased grain**: Grain values are significantly higher than K64, reflecting K200's RMS ~14-16
3. **Lower contrast**: The film's natural lower contrast (faster emulsion) is preserved
4. **Warmer reds**: Red hue shifted slightly more toward orange for the signature K200 warmth

### t3mujinpack Directional Values (Darktable → LR translation)

| Parameter | K64 Value | K200 Direction | Notes |
|-----------|-----------|---------------|-------|
| Contrast | +20 | +25 | Moderate (faster film = lower contrast, but K200 still slide film) |
| Highlights | -13.8 | -15 | Slightly more protection for action scenes |
| Grain Amount | 30 | 20 | K200 more grain than K64 (RMS 14-16 vs 10) |
| Grain Size | 25 | 25 | Similar grain character structure |
| Blue Hue | -10 | -5 | Less cyan shift — warmer blues |
| Blue Sat | +17.5 | +12.5 | Warmer, less saturated blues |
| Red Hue | +10 | +10 | Same warm bias as K64 |
| Red Sat | +20 | +15 | Slightly less (grainier film = less perceived sat) |
| Red Lum | -10 | -5 | Less deepening |
| Highlight tint | H50, Sat 7.5 | H50, Sat 7.5 | Same warm highlight |
| Shadow tint | H220, Sat 11.3 | H220, Sat 8 | Less cool shadow (warmer film) |
| Saturation | -5 | +5 | K200 was warmer/slightly more saturated overall |

---

## Sports & Wildlife Community

K200 was popular with sports and wildlife shooters who valued:
- The ability to shoot handheld at 1/500+ in daylight
- Kodachrome color accuracy for publication
- Acceptable grain that didn't detract from action subjects
- The warm palette suited outdoor portraiture and wildlife

From r/analog discussions of K200:
> "Kodachrome 200 was the slide film you grabbed when you needed speed. It wasn't as sharp as K25 or K64, but the grain was beautiful — structured, not noisy. It felt like a photograph, not a digital capture."

---

## Comparison with Kodachrome 64 (for preset builders)

| Element | Difference from K64 | Rationale |
|---------|-------------------|-----------|
| Grain Amount | 20 (vs 30) | More visible grain for 200-speed |
| Grain Size | 25 (same) | Similar structure to K64 |
| Blue Hue | -5 (vs -10) | Warmer blue rendering |
| Blue Sat | +12.5 (vs +17.5) | Less saturated blues |
| Red Sat | +15 (vs +20) | Slightly less for grainier look |
| Red Lum | -5 (vs -10) | Less deepening |
| Aqua Sat | +10 (vs +15) | Reduced |
| Shadow Sat | 8 (vs 11.3) | Less pronounced cool cast |
| Saturation | +5 (vs -5) | Warmer, more saturated overall |
| Contrast | +25 (vs +20) | Slightly higher |

---

## Sources

- t3mujinpack — Kodachrome 200 Darktable profile
- Eastman Kodak, Kodachrome 200 technical datasheet
- r/analog: "Kodachrome 200 — who shot it?", "K200 push processing"
- Sports Illustrated photo archive (1980s-90s)
- Kodachrome-64 research folder (family reference data)
