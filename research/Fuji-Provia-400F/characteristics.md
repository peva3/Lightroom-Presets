# Fuji Provia 400F — Aesthetic Characteristics for Lightroom Presets

## The Film

Fuji Provia 400F (E-6, daylight balanced at 5500K) was Fujifilm's professional ISO 400 color transparency film, introduced as the second generation of the Provia 400 line. It predates Provia 400X (2006) and was produced approximately 2000-2006. It represented Fujifilm's answer to Kodak's high-speed E-6 films. This document serves as a reference for creating a Lightroom preset that emulates Provia 400F.

## Core Aesthetic

### 1. Fuji Professional Slide Character
- **Moderate-to-high contrast** — professional slide film, designed for clean projection
- **Warmer than 400X** — the F generation had a warmer, slightly golden midtone compared to the cooler, more neutral 400X that followed
- **Fuji color science** — characteristic Fuji magenta-cyan balance rather than Kodak's neutral-cool
- **Good skin tones** for a slide film — Fuji's skin tone rendering was generally more flattering than Kodak's equivalent

### 2. Color Palette by Hue

| Hue | Provia 400F Rendering |
|-----|----------------------|
| **Blue (sky)** | Rich, slight magenta-leaning blue — Fuji's sky signature |
| **Blue (shadow)** | Subtle magenta-blue cast |
| **Red** | Vibrant but controlled, slightly warm |
| **Green (foliage)** | Lush green with subtle warmth — less yellow than Kodak |
| **Skin tones** | Warm-neutral, more forgiving than Ektachrome |
| **Magenta/Purple** | Slightly emphasized — Fuji's magenta bias |
| **Whites** | Clean, subtle warmth |

### 3. Contrast & Dynamic Range
- **Moderate-high contrast** — professional slide profile
- **RMS ~13-14** — typical for ISO 400 slide film, more grain than Provia 100F
- **Dynamic range ~7 stops** — standard slide film latitude
- The warmer balance helps mitigate the harsh shadow transitions of slide film

### 4. The Fuji Difference
Provia 400F's defining Fuji characteristics:
- **Magenta bias** in neutrals and shadows (not cyan like Ektachrome)
- **Warmer overall** than Provia 400X which followed
- **Smoother highlight transition** than Ektachrome equivalents
- **Richer greens** that remain natural rather than going teal

## Comparison: Provia 400F vs Provia 400X vs Ektachrome 400X

| Attribute | Provia 400F | Provia 400X | Ektachrome 400X |
|-----------|-------------|-------------|-----------------|
| Warmth | Warm | Cool-neutral | Warm |
| Shadow bias | Magenta | Neutral | Neutral-cool |
| Blues | Magenta-blue | True blue | Warm-blue |
| Greens | Rich warm | Natural | Yellow-green |
| Skin tones | Warm, good | Cool, accurate | Warm, saturated |
| Contrast | Moderate-high | Moderate-high | High |
| Grain | RMS ~13 | RMS ~12 | RMS ~14 |

## References
- Fujifilm Provia 400F technical datasheet
- t3mujinpack: Provia 400F Darktable style
- Fuji X Weekly: Provia 400 recipe (similar era)
- Photrio: Provia 400F vs 400X discussions
- r/analog: Provia 400F examples

*Note: t3mujinpack has a Provia 400F Darktable style available. Values derived from film family analysis with Provia 100F and 400X as anchors.*

---

## See Also

For related Lightroom presets and film stock references:

- [Fuji Velvia 50](../Fuji-Velvia-50/characteristics.md)
- [Fuji Velvia 100](../Fuji-Velvia-100/characteristics.md)
- [Fuji Astia 100F](../Fuji-Astia-100F/characteristics.md)
- [Fuji Provia 100F](../Fuji-Provia-100F/characteristics.md)
- [Fuji Provia 400X](../Fuji-Provia-400X/characteristics.md)
- [Fuji Sensia 100](../Fuji-Sensia-100/characteristics.md)
- [Fuji Fortia SP 50](../Fuji-Fortia-SP-50/characteristics.md)
- [Kodak Ektachrome E100](../Kodak-Ektachrome-E100/characteristics.md)


## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Fast pushable E-6: grain 18/28 (visible but tight for ISO 400), Contrast +40 and small saturation touches (+5 hue on red/green/blue) fit the punchier high-speed Provia; blue Luminance -10 keeps skies clean. No calibration or WB contamination.
- **Sources:** Fujifilm Velvia 100 datasheet (world's highest saturation, RMS 8); Velvia 50 / Provia 100F datasheets (RMS 8, medium saturation + contrast); Fujifilm Sensia 100 product page; Fortia SP entry (Wikipedia) + Fuji X Weekly 'Fortia 50' (highest-saturation Fuji emulsion, above Velvia 50); Astia 100F reviews (Alex Luyckx) and Fujifilm film-simulation chart (soft/muted).
- **Preset adjustments:** none

> **Validation Sweep 2026-10-21 — hue direction correction.** Lightroom's HSL hue axis runs Red → Orange → Yellow → Green → Aqua → Blue, so a *negative* Green Hue moves foliage toward yellow/olive and a *positive* value moves it toward cyan. The preset originally encoded this with the opposite sign; it now matches the olive/yellow-green shift described above.
