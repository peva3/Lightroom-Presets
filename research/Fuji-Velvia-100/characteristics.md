# Fuji Velvia 100 — Aesthetic Breakdown for Lightroom Presets

> Less extreme than Velvia 50, warmer, better skin tones. The most-used slide film by nature photographers in the 2000s.

---

## Core Identity

Velvia 100 (RVP100) was introduced in 2003 as Fujifilm's answer to the professional market's demand for a more versatile landscape slide film. While Velvia 50 was legendary for its extreme saturation and contrast, working pros needed something more practical: wider latitude, better skin tones, and finer grain. Velvia 100 delivered all three while retaining the iconic Velvia "pop." This document serves as a reference for creating a Lightroom preset that emulates Velvia 100.

The key differentiator from Velvia 50 is the yellow→red spectral shift. Velvia 50 pulls yellows aggressively toward orange/red — a "defect" that landscape photographers loved for golden-hour warmth. Velvia 100 is more neutral in its yellow rendering, producing more accurate warm tones. This makes it usable for portraits and commercial work where Velvia 50 made skin look ruddy/sunburned.

---

## Color Palette

### Greens — Rich But Not Hyper-Saturated
- Deep and lush but not the impossible emerald of Velvia 50
- More natural foliage rendering — forests feel real, not radioactive
- Slightly cooler green bias than Velvia 50 (less yellow-green in foliage)
- Maintains saturation into shadows better than consumer slide films

### Blues — Deep But Less Electric
- Strong sky blue with good separation from clouds
- Less cyan-suppressed than Velvia 50 — skies are blue-blue, not electric-blue
- Water rendered naturally with good shadow detail
- Cool but not artificial — the polarizer-like effect of Velvia 50 is toned down

### Reds & Warm Tones — Balanced, Portrait-Friendly
- Skins render warm but natural — *the* key Velvia 100 advantage over Velvia 50
- Golden-hour warmth is present but not artificially amplified
- Reds are rich without the magenta bias of Velvia 50
- Autumn foliage renders beautifully without oversaturation

### Neutrals — The Professional Difference
- White balance is more neutral than Velvia 50
- Grey tones are clean and accurate
- Less shadow color cast than Velvia 50

---

## Contrast & Dynamic Range

### Moderate-High Contrast
- Contrast is high (dMax ~3.5) but significantly lower than Velvia 50 (dMax ~3.8-4.0)
- Slightly wider exposure latitude — about ±¾ stop vs. Velvia 50's ±½ stop
- Shadows are deep but not crushed to black as aggressively
- Highlight rolloff is gentler than Velvia 50

### Grain & Sharpness
- **RMS 8**: Extremely fine grain (slightly finer than Velvia 50's RMS 9)
- **160 lines/mm resolving power**: Same outstanding resolution as Velvia 50
- **160 lp/mm**: Matches Velvia 50 in pure resolving power
- At normal viewing distances, grain is essentially invisible

---

## Practical Usage

Velvia 100 was the workhorse slide film of the 2000s:
- **Nature Photography**: Preferred over Velvia 50 for its wider latitude and better skin tones when people appeared in landscape scenes
- **Travel Photography**: The versatility made it ideal — one film for landscapes, street scenes, and environmental portraits
- **Wedding/Event**: Some pros used it for wedding details and environmental shots (not portraits — those went to Astia or Provia)
- **Publication**: Velvia 100 transparencies scanned better than Velvia 50 for magazine reproduction, having less extreme contrast

---

## Velvia 100 vs. Velvia 50

| Characteristic | Velvia 100 | Velvia 50 |
|---|---|---|
| Saturation | Very high | Extreme |
| Contrast | High (dMax ~3.5) | Very high (dMax ~3.8-4.0) |
| Yellow→Red shift | Mild, neutral | Aggressive, defining |
| Skin tones | Warm, usable | Ruddy, poor |
| Grain | RMS 8 (finer) | RMS 9 |
| Exposure latitude | ~±¾ stop | ~±½ stop |
| Golden-hour magic | Present but natural | Amplified beyond reality |
| Best use | All-round nature/travel | Specialized landscape |

---

## Digital Emulation Notes

The t3mujinpack reference approach: take Velvia 50's saturation and contrast profile, then:
1. Reduce overall contrast ~25% (less shadow crush, less highlight clip)
2. Moderate the yellow→red shift (key HSL difference from V50)
3. Increase orange luminance for better skin tones
4. Use slightly warmer highlight color grading vs. V50's cool shadow bias
5. Grain should be minimal — 5-10% of even Velvia 50 levels

---

## References

- Fujifilm Velvia 100 (RVP100) technical datasheet
- t3mujinpack — Velvia 100 profile reference
- Ken Rockwell, "Fuji Velvia 100 Review"
- r/analog community discussions — thousands of Velvia 100 images
- Nature photographers' consensus: Velvia 100 was the standard 2003-2015

---

## See Also

For related Lightroom presets and film stock references:

- [Fuji Velvia 50](../Fuji-Velvia-50/characteristics.md)
- [Fuji Astia 100F](../Fuji-Astia-100F/characteristics.md)
- [Fuji Provia 100F](../Fuji-Provia-100F/characteristics.md)
- [Fuji Provia 400F](../Fuji-Provia-400F/characteristics.md)
- [Fuji Provia 400X](../Fuji-Provia-400X/characteristics.md)
- [Fuji Sensia 100](../Fuji-Sensia-100/characteristics.md)
- [Fuji Fortia SP 50](../Fuji-Fortia-SP-50/characteristics.md)
- [Kodak Ektachrome E100](../Kodak-Ektachrome-E100/characteristics.md)
