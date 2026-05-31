# Community Recipes — Lightroom B&W Presets for Tri-X 400 Emulation

> Compiled from Reddit (r/Lightroom, r/analog, r/postprocessing, r/photography), YouTube tutorials, photography forums, and community blogs. These are community-developed settings — not official Kodak data.

---

## Recipe A: "Classic Tri-X at Box Speed" (D-76 Look)

Goal: Moderate grain, deep blacks, open shadows, strong mid-tone contrast. Emulates Tri-X at ISO 400 in D-76 1:1.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | 0 (adjust per image) |
| Contrast | +35 to +45 |
| Highlights | -15 |
| Shadows | +20 to +30 |
| Whites | +15 |
| Blacks | -25 to -35 |

### Tone Curve
```
Parametric:
  Highlights: -10
  Lights: +10
  Darks: -20
  Shadows: -5

Point Curve: Medium Contrast
```
Custom point curve (optional): Two-point S-curve with a slight lift in the deep shadows (crushed-but-not-blocked blacks).

### B&W Mix (HSL / Black & White)
| Color Channel | Value | Notes |
|---------------|-------|-------|
| Red | +25 to +35 | Lightens skin, darkens skies slightly |
| Orange | +15 to +25 | Key skin tone channel |
| Yellow | -10 to 0 | Preserves highlight separation |
| Green | -20 to -30 | Darkens foliage — Tri-X is panchromatic with red sensitivity |
| Aqua | 0 |
| Blue | -30 to -50 | Darkens skies — dramatic Tri-X sky look |
| Purple | 0 |
| Magenta | -10 to 0 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +20 to +35 |
| Dehaze | +5 to +15 |
| Texture | +10 to +20 |

### Grain (Critical for Tri-X emulation)
| Setting | Value | Notes |
|---------|-------|-------|
| Amount | 55 to 70 | Visible at 100% zoom on 24MP |
| Size | 35 to 45 | Tri-X grain is medium-coarse, not fine |
| Roughness | 65 to 80 | Key! High roughness creates "salt-and-pepper" texture |

### Vignette
| Setting | Value |
|---------|-------|
| Post-Crop Vignette | -10 to -15 |
| Midpoint | 35 |
| Feather | 50 |

---

## Recipe B: "Pushed Tri-X at 1600" (HC-110 Look)

Goal: Heavy, aggressive grain. Crushed blacks. High contrast with dramatic mid-tone separation. The classic 1970s war photographer / Daido Moriyama look.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | -0.3 to 0 |
| Contrast | +60 to +80 |
| Highlights | -30 |
| Shadows | +10 to +15 |
| Whites | +30 |
| Blacks | -40 to -55 |

### Tone Curve
```
Parametric:
  Highlights: -30
  Lights: +15
  Darks: -30
  Shadows: -15

Point Curve: Strong Contrast
```
Custom: Deep S-curve. Lift the toe slightly (RGB value ~8 at black), then steep drop.

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +30 |
| Orange | +20 |
| Yellow | -5 |
| Green | -35 |
| Aqua | 0 |
| Blue | -50 to -60 |
| Purple | -10 |
| Magenta | -10 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +40 to +60 |
| Dehaze | +15 to +25 |
| Texture | +20 to +30 |

### Grain (Heavy)
| Setting | Value |
|---------|-------|
| Amount | 75 to 100 |
| Size | 45 to 55 |
| Roughness | 80 to 95 |

### Vignette
| Setting | Value |
|---------|-------|
| Post-Crop Vignette | -20 to -30 |
| Midpoint | 25 |
| Feather | 40 |

---

## Recipe C: "Tri-X in Rodinal" (Maximal Grain/Acutance)

Goal: Pronounced grain with enhanced edge sharpness. Tri-X's true "grain texture" on full display. Favored by fine art / street photographers wanting aggressive texture.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | 0 |
| Contrast | +50 |
| Highlights | -20 |
| Shadows | +25 |
| Whites | +10 |
| Blacks | -30 |

### Tone Curve
- Strong S-curve with a sharp toe (blacks clip faster)
- Slightly lifted mid-point for more brightness in the mid-tones

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +20 |
| Orange | +15 |
| Yellow | -15 |
| Green | -25 |
| Blue | -40 |
| (Others at 0) |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +50 to +70 |
| Dehaze | +10 |
| Texture | +25 to +35 |

### Grain
| Setting | Value |
|---------|-------|
| Amount | 80 to 100 |
| Size | 40 to 50 |
| Roughness | 85 to 100 |

### Sharpening (Rodinal = high acutance)
| Setting | Value |
|---------|-------|
| Amount | 60 to 80 |
| Radius | 1.0 to 1.4 |
| Detail | 35 to 50 |
| Masking | 10 to 30 (to avoid sharpening grain in skies) |

---

## Recipe D: "Tri-X XP2 / Low Contrast Pull" (Tri-X @ 200)

Goal: Fine grain, long tonal scale, open shadows. Emulates Tri-X pulled to 200 in XTOL or D-76 1:3. Suitable for portraits with smoother skin.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | +0.3 to +0.5 |
| Contrast | +15 to +25 |
| Highlights | -25 |
| Shadows | +40 to +50 |
| Whites | +5 |
| Blacks | -15 to -20 |

### Tone Curve
- Gentle S-curve
- Shadow end NOT crushed — keep detail at RGB ~15

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +20 |
| Orange | +10 |
| Yellow | -10 |
| Green | -15 |
| Blue | -25 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +10 to +20 |
| Dehaze | +5 |
| Texture | +10 |

### Grain (Fine)
| Setting | Value |
|---------|-------|
| Amount | 30 to 45 |
| Size | 30 to 35 |
| Roughness | 50 to 60 |

---

## Recipe E: "Newspaper / Magazine Tri-X" (High-Contrast Repro)

Goal: Extremely punchy. Heavy black crush. The photojournalism look on newsprint.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +70 to +90 |
| Highlights | -40 |
| Shadows | -10 to -20 |
| Whites | +40 |
| Blacks | -60 |

### Tone Curve
- Aggressive S-curve
- Blacks at RGB 0-5 (full crush)
- Whites pushed to RGB 248+

### B&W Mix
- Heavy red/orange boost (+30 to +40)
- Blue heavy darken (-50 to -70)

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +60 to +80 |

### Grain
| Setting | Value |
|---------|-------|
| Amount | 70 to 90 |
| Size | 40 to 50 |
| Roughness | 75 to 90 |

---

## Key Insights from Community Research

### From Reddit (r/Lightroom, r/analog, r/postprocessing):

1. **"The B&W Mix is everything"** — Multiple Reddit threads emphasize that Tri-X's unique look comes from its spectral sensitivity (panchromatic with extended red). The red/orange channel boost is the single most important setting. Without it, B&W conversions look "generic."

2. **Grain roughness matters more than amount** — Lightroom's grain at 100 amount but 25 roughness looks like fine-grain Delta/T-Max, NOT Tri-X. Roughness at 70+ is essential for the "salt and pepper" character.

3. **Clarity is your friend, but don't overdo it** — Clarity above 60 produces "haloing" that looks digital, not like film edge sharpness (acutance). Use Clarity +30 to +45 and supplement with Texture for a more authentic "edge effect."

4. **The "woven grain" phenomenon on r/analog (565 points)** — A major thread discussed "woven" or "reticulated" grain pattern on Tri-X. Community consensus: this is RETICULATION from harsh temperature changes during development (specifically monobath developers or cold water stop), NOT inherent to Tri-X. Properly developed Tri-X has a random "salt and pepper" pattern, not a directional/reticulated one.

5. **"HP5 has smooth grain like sand, Tri-X has sharp grain like broken glass"** — Common community characterization from u/throwaway comment on r/analog.

### From YouTube:

Popular Tri-X emulation tutorials emphasize:
- Using the B&W Profile (not desaturation) as the foundation
- Heavy negative Blue and Cyan in the B&W mixer for dramatic skies
- Lightroom's built-in grain engine is considered "acceptable but not great" — many recommend using third-party grain overlays (like RNI or DxO FilmPack) for more authentic grain structure
- VSCO Film 01's Tri-X preset was widely considered the gold standard until discontinuation

### From Photography Forums:

- **FredMiranda.com** threads suggest Tri-X at EI 200-250 yields the "true" shadow detail, with the characteristic curve showing ~2 stops of underexposure latitude and 5+ stops overexposure latitude
- **Photrio (APUG)** consensus: D-76 1:1 at 9.75 min is the "reference standard" for Tri-X development against which all other developer/film combinations are judged
- **RangeFinderForum** recommendation: Pair Tri-X with a yellow filter (K2/Y48) for classic street photography look, or orange filter for dramatic skies
