# Kodachrome 25 — Community Recipes

> Community emulation strategies from t3mujinpack and film forums. Finer grain, cooler, sharper than K64.

---

## t3mujinpack Reference (Primary Source)

**Source**: t3mujinpack — Kodachrome 25 Darktable .dtstyle profile

The t3mujinpack treats Kodachrome 25 as a derivative of Kodachrome 64 with key modifications. From the .dtstyle data:

1. **Cooler white balance**: Slightly cooler color temperature than K64, giving the characteristic K25 "cool precision"
2. **Finer grain profile**: Grain values are lower than even K64 — K25 had genuinely invisible grain at normal magnifications
3. **Higher microcontrast**: The sharpness advantage is emulated through tone curve microcontrast, not digital sharpening
4. **Cleaner blues**: Blue saturation is slightly higher than K64 with more cyan bias
5. **Tighter reds**: Red saturation is slightly lower than K64, but red purity is higher (less orange shift)

### t3mujinpack Directional Values (Darktable → LR translation)

| Parameter | K64 Value | K25 Direction | Notes |
|-----------|-----------|---------------|-------|
| Contrast | +20 | +25 | Higher (lower speed film) |
| Highlights | -13.8 | -10 | Slightly less compression |
| Blues | Hue -10, Sat +17.5, Lum -15 | Hue -15, Sat +20, Lum -15 | Deeper, more cyan |
| Reds | Hue +10, Sat +20, Lum -10 | Hue +5, Sat +10, Lum -5 | Cleaner, less saturated |
| Shadow tint | 220°, Sat 11.3 | 225°, Sat 8 | Cooler shadow cast |
| Highlight tint | 50°, Sat 7.5 | 45°, Sat 5 | Cooler highlights |
| Grain | Amount 30, Size 25 | Amount 5, Size 15 | K25's RMS 8 = near-invisible |
| Saturation | -5 | 0 | Neutral vs K64's slight desaturation |

---

## Landscape Photography Community

### National Geographic Era

K25 was the film of choice for National Geographic landscape photographers from the 1960s through the 1980s. The combination of Kodachrome color + lowest possible grain was essential for large-format reproduction in the magazine's high-quality printing. Photogs noted:

- K25 skies were "the cleanest blue you could put on a page"
- Detail in rock and earth textures was unmatched
- The slow speed forced deliberate composition — tripod, cable release, careful metering

### Ansel Adams & Color

Adams's color work (often overlooked in favor of his B&W) was predominantly on Kodachrome. His approach: expose for the highlights, let shadows fall where they may — the opposite of his B&W Zone System. K25's high contrast suited this approach because the deep blacks created strong graphic compositions against saturated color.

### Galen Rowell — Pre-Velvia

Before Velvia 50 launched in 1990, Rowell shot Kodachrome 25 extensively. His famous mountain photography of the 1970s-80s was on K25. When he switched to Velvia in the 1990s, he noted the warmer palette and higher saturation as improvements for his style, but acknowledged K25's superior sharpness and grain structure.

---

## Comparison with Kodachrome 64 (for preset builders)

| Element | Difference from K64 | Rationale |
|---------|-------------------|-----------|
| Grain | Much finer (5 vs 30) | RMS 8 vs 10 |
| Contrast | Slightly higher (+25 vs +20) | Lower-speed films are contrastier |
| Blue Hue | More cyan (-15 vs -10) | Cooler spectral sensitivity |
| Blue Sat | Higher (+20 vs +17.5) | Purer cyan dye at slow speed |
| Red Hue | More neutral (+5 vs +10) | Less orange bias |
| Red Sat | Lower (+10 vs +20) | Cleaner, more precise reds |
| Highlight tint | Cooler (H45 vs H50) | Overall cooler balance |
| Shadow tint | Cooler (H225 vs H220) | More pronounced cool shadow |
| Saturation | 0 vs -5 | No global desaturation needed |

---

## Sources

- t3mujinpack — Kodachrome 25 Darktable profile
- Eastman Kodak, Kodachrome 25 technical datasheet
- Ansel Adams color photography bibliography
- National Geographic photographic archive (K25 era)
- Galen Rowell mountain photography (pre-1990 K25 work)
- Kodachrome-64 research folder (family reference data)
