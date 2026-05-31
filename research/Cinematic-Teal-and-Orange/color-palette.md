# Color Palette — Teal & Orange

## Complementary Positioning

The Teal & Orange palette is built on **near-complementary** hues on a standard 360° color wheel:

```
        Orange (30°)
           /\
          /  \
         /    \
        /      \
       /  SKIN  \
      /   ZONE   \
     /            \
    /              \
 Green (120°) ----+---- Red (0°/360°)
    \              /
     \            /
      \   TEAL   /
       \  ZONE  /
        \      /
         \    /
          \  /
           \/
        Cyan/Teal (195°)
```

## Hue Angle Targets

| Element | Hue Angle | Lightroom HSL Position | Notes |
|---|---|---|---|
| **Orange Highlights** | 25°–40° | Between Orange and Yellow sliders | Push yellows toward orange |
| **Teal Shadows** | 185°–210° | Between Aqua and Blue sliders | True teal, not pure cyan |
| **Skin Tone** | 15°–30° | Orange/Red boundary | MUST protect from shift |
| **Sky** | 200°–220° | Blue slider | Natural blue pushed teal |
| **Foliage** | 50°–80° | Yellow/Green boundary | Desaturated; pushed yellow |
| **Fire/Explosions** | 20°–35° | Orange primary | Already orange, just saturated |

## Split Complementary Breakdown

Teal & Orange isn't a pure two-color palette — it's a **split-complementary** scheme in practice:

```
Primary:     Orange (30°)
Complement:  Teal (210°)

Split tones:
  Shadows  → Teal-Cyan (195°–215°)  
  Midtones → Preserved / slightly warm
  Highlights → Amber-Orange (25°–40°)
```

### Why Split Rather Than Pure Complementary?

Pure complementary (exactly 180° apart) creates the "clown vomit" effect — maximum chromatic tension that's uncomfortable to watch for extended periods. The split approach:
- Warms the teal slightly (closer to cyan than true teal) to feel cool but not electric
- Warms the orange slightly (closer to amber than red-orange) to feel golden rather than radioactive
- Keeps the midtones relatively neutral as a visual "rest zone"

## The 2383-Inspired Gamut

Kodak 2383 print film has a specific color gamut that's narrower than Rec.709 in some areas and wider in others:

### 2383 Color Bias Map
```
Film Negative (wide gamut)
       ↓
2383 Print Stock (compressed gamut with bias)
       ↓
Projected Image

Color shifts in 2383:
  Blue → Cyan-Teal (warm blues don't exist on 2383)
  Yellow → Amber-Orange (lemon yellows become golden)  
  Green → Olive/Warm Green (cool greens die)
  Red → Orange-Red (pure red survives but warms)
  Magenta → Red-Orange (magenta shifts warm)
```

This means the 2383 "look" naturally:
1. **Eliminates cool greens** — foliage becomes warm or desaturated
2. **Converts pure blues to teal** — skies, shadows, water all shift cyan
3. **Amplifies warm tones** — any warmth becomes more saturated
4. **Crushed blacks** — shadow detail rolls off into teal-black

## Typical RGB Parade Values for Teal/Orange

A "correct" teal/orange grade on scopes:

### Shadows (IRE 0–20)
```
Red:   ~5-10 IRE (suppressed)
Green: ~10-20 IRE (elevated for teal)
Blue:  ~15-25 IRE (elevated for teal)
→ Green + Blue > Red = Teal shadow cast
```

### Midtones (IRE 40–60)
```
Red:   ~45-55 IRE (equalized)
Green: ~40-55 IRE (equalized)
Blue:  ~40-50 IRE (slightly suppressed for warmth)
→ Red slightly elevated over Blue = warm bias at midtones
```

### Highlights (IRE 80–100)
```
Red:   ~85-95 IRE (elevated)
Green: ~80-90 IRE (elevated)
Blue:  ~70-80 IRE (suppressed)
→ Red + Green > Blue = Orange-Yellow highlight cast
```

## HSB/HSV Values

| Element | H (Hue) | S (Saturation) | B (Brightness) |
|---|---|---|---|
| Teal Shadow | 190–200° | 25–45% | 10–30% |
| Neutral Midtone | 30–40° | 10–20% | 40–60% |
| Orange Highlight | 25–35° | 40–70% | 70–95% |
| Skin (lit side) | 18–28° | 35–55% | 60–85% |
| Skin (shadow side) | 20–30° | 15–30% | 25–45% |

## Hex Color References

```
Teal Shadow:        #0A4A5E  (deep teal)
Teal Shadow (lift): #1A5A6E  (milky teal)
Orange Highlight:   #D4782A  (amber-orange)
Orange Peak:        #E8943A  (golden-orange)
Skin Protected:     #D4956A  (natural skin tone)
Neutral Mid:        #8A7A6A  (warm gray)
Teal Sky:           #4A8A9E  (cinematic sky)
Crushed Black:      #051A24  (near-black teal)
```

## Common Variations

### "Bayhem" (Michael Bay Extreme)
- Contrast: Very high
- Teal saturation: 60–80% (pushed to unnatural levels)
- Orange saturation: 70–90%
- Skin tones: Secondary correction to prevent total orange takeover
- Blacks: Fully crushed with strong cyan tint
- Overall: Hot, aggressive, maximum color contrast

### "Blockbuster Warm" (Conservative)
- Contrast: Medium-high
- Teal saturation: 20–35%
- Orange saturation: 30–50%
- Skin tones: Natural with slight warmth
- Blacks: Slightly lifted, subtle teal
- Overall: Warm and inviting, teal is barely perceptible

### "Cyberpunk Teal" (Blue-Shifted)
- Contrast: High  
- Teal saturation: 50–70%
- Orange: De-emphasized, shifted to magenta/pink highlights
- Shadows: Deep blue-cyan
- Skin: Pulled toward magenta rather than orange
- Overall: Blue/cyan dominant, orange is accent

### "Vintage Teal/Orange" (Desaturated)
- Contrast: Low
- Teal saturation: 15–25% (muted)
- Orange saturation: 20–30% (muted)
- Blacks: Lifted with warm cast (no teal blacks)
- Overall grain and halation added
- Mimics 1970s film stock with modern color sensibilities
