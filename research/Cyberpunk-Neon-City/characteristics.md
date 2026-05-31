# Characteristics — Cyberpunk Neon City Aesthetic Breakdown

> A comprehensive analysis of the visual language, color theory, and technical qualities that define the Cyberpunk Neon City aesthetic in photography and film.

---

## 1. The Core Palette: Magenta/Cyan Neon

The cyberpunk neon city look is fundamentally a **complementary color scheme** built on:

### Primary Axis
- **Magenta / Hot Pink / Purple** — The dominant neon color. Represents synthetic life, holographic advertisement, the feminine-coded artificial (Joi in BR2049), and digital consciousness.
- **Cyan / Teal / Electric Blue** — The shadow and accent color. Represents technology, cold corporate power, rain-soaked streets, and the omnipresent digital infrastructure.

### The Physics Behind the Palette
This magenta-cyan pairing is not arbitrary:
- **Sodium vapor streetlights** (orange/amber) dominated real cities when Blade Runner was conceived. The cyberpunk aesthetic *inverts* this: orange is suppressed, magenta is heightened.
- **LED and neon signage** naturally produces these spectral colors when photographed at night.
- The **complementary contrast** between cyan (~180°) and magenta (~300°) on the color wheel creates maximum visual tension — the fundamental "unease" of the cyberpunk world.

### The Absence of Natural Color
A defining characteristic is **what is removed**:
- **Green** is nearly eliminated. Foliage doesn't exist in the cyberpunk city. Green is the color of nature, life, and the organic — antithetical to the synthetic world.
- **Yellow** is crushed toward orange or eliminated. Warm, "cozy" tones are suppressed.
- **Natural skin tones** are shifted toward cool/cyan or warm/magenta depending on lighting context.

---

## 2. Green Elimination

### Why Green Must Die

Green is the color of:
- Chlorophyll / plant life / nature
- Health and vitality
- The "normal" world outside the cyberpunk dystopia

The cyberpunk genre posits a world where nature has been destroyed or marginalized. Eliminating green from the color palette reinforces:
- Environmental collapse (the world outside the city is wasteland)
- Synthetic replacement of the organic (replicants, holograms, AI)
- The triumph of the artificial

### How Green Is Eliminated in Post-Production

| Technique | Implementation |
|-----------|---------------|
| HSL Hue Shift | Shift green hues toward cyan (160-180°) or toward yellow (50-60°) |
| HSL Saturation | Desaturate green channel to -80 to -100 |
| Calibration | Shift green primary hue toward cyan/blue, reduce saturation |
| Split Toning | Overwhelm any residual green with cyan shadows + magenta highlights |
| LUT Application | Apply a teal/orange or magenta/cyan LUT that remaps greens |

---

## 3. High Clarity and Dehaze — The "Crunch"

### Clarity (Micro-Contrast)

Clarity enhances midtone contrast at a local level, which creates:

| Effect | Aesthetic Purpose |
|--------|------------------|
| Texture in concrete/steel | Emphasizes the brutalist, decaying architecture |
| Edge definition on neon | Makes neon signs appear to "cut through" the darkness |
| Skin texture | Makes faces look weathered, tired, cyberpunk-noir |
| Wet surface detail | Enhances rain-slicked pavement reflections |
| Light blooming | High clarity + dehaze creates a "glow halo" around point light sources |

Typical clarity values: **+40 to +70**

### Dehaze

Dehaze was originally designed to remove atmospheric haze, but in cyberpunk grading it serves a dual purpose:

1. **Removes real haze/fog** — Sharpens the image, increases perceived clarity
2. **Creates neon glow blooming** — When combined with high clarity, dehaze at +30 to +60 produces a characteristic "bloom" effect around bright lights against dark backgrounds

The combination of high clarity + high dehaze creates the **signature "crunchy" cyberpunk texture** that distinguishes it from smooth cinematic grading.

---

## 4. Crushed Blacks and Lifted Shadows

### The Noir Foundation

Cyberpunk inherits its lighting language from **film noir**:
- Deep, crushed blacks (absolute black at ~5-15 IRE rather than 0)
- Shadows that obscure detail — mystery and danger in the darkness
- Low-key lighting with pools of colored neon light
- Strong chiaroscuro (light/dark contrast)

### Tone Curve Shape

```
Blacks:   Lifted to ~8-12 on a 0-255 scale (matte shadow look)
Shadows:  Steep curve for contrast in the shadow-to-midtone transition
Midtones: Neutral to slightly bright (where neon lives)
Highlights: Rolled off smoothly (no hard clipping on neon signs)
Whites:   Compressed below 245 to avoid digital clipping
```

The **"RGB tone curve trick"** used by many cyberpunk editors: Crush each channel's black point individually, then lift the combined RGB curve shadow point. This creates rich color in the deep shadows rather than pure black.

---

## 5. The Color Temperature Paradox

Cyberpunk images often have a **split color temperature**:
- **Global white balance**: Tinted toward cool (3800-4500K) with magenta tint (+20 to +40)
- **Local warm accents**: Radial/brush adjustments on neon signs at 5500-6500K for contrast

This creates the sensation of a cold, hostile environment punctuated by artificial warmth — heat that comes from technology, not from the sun or fire.

---

## 6. Texture and Surface Quality

### Wetness
- Rain-soaked streets are practically mandatory
- Wet surfaces create specular reflections that double the neon presence
- Puddles create mirror-like secondary light sources
- Condensation on windows diffuses light beautifully

### Atmospheric Particles
- Smoke, steam, fog — anything that catches light and creates volumetric rays
- Particulate matter (smog, dust) catches colored light and creates depth
- The air itself should feel "thick" and polluted

### Surface Materials
- Concrete, steel, glass — brutalist materials
- Holographic surfaces (glass with colored reflections)
- Glossy wet pavement
- Corrugated metal, industrial grates

---

## 7. Compositional Conventions

- **Verticality**: The city is layered — ground level (trash, decay), mid-level (neon, commerce), upper level (corporate spires, flying vehicles)
- **Framing within framing**: Windows, doorways, alleyways — the city as a series of nested boxes
- **Leading lines**: Neon signs create natural leading lines into the frame
- **Negative space**: Large areas of dark shadow punctuated by small, brilliant neon elements
- **Scale**: Tiny human figures against massive architecture — the individual vs. the system

---

## 8. The Emotional Register

The cyberpunk neon city aesthetic is not purely visual — it carries specific emotional coding:

| Element | Emotion |
|---------|---------|
| Magenta/pink neon | Artificial desire, holographic intimacy, the synthetic feminine |
| Cyan/teal neon | Cold corporate power, surveillance, technocratic control |
| Crushed blacks | Mystery, danger, the unknown |
| High clarity | Hyper-reality, sensory overload, the inability to "see softly" |
| Green absence | Ecological grief, the death of nature |
| Wet surfaces | Melancholy, tears, the city weeping |
| Vertical scale | Alienation, powerlessness, the individual dwarfed by capital |

---

## 9. Technical Pitfalls (What NOT To Do)

| Mistake | Why It Fails |
|---------|-------------|
| Over-saturation | Turns image into cartoon — neon should glow but not be garish |
| Too much clarity | Creates halos around edges, looks like bad HDR |
| Forgetting skin tones | If people are in frame, maintain natural skin while grading around it |
| Killing ALL warm tones | Some warmth (especially in highlights) provides contrast to the cool shadows |
| Uniform color wash | Use local adjustments — the whole image shouldn't be one flat magenta/cyan wash |
| Ignoring luminance | Saturated color with no luminance variation looks flat — boost luminance on key neon colors |

---

## 10. The Evolution of the Look

### Blade Runner (1982)
- More amber/gold in the palette alongside cyan
- Practical lighting (actual neon tubes, not CGI)
- Softer contrast than modern interpretations
- Smoke and rain as primary atmospheric elements
- Jordan Cronenweth's cinematography: shafts of light cutting through volumetric atmosphere

### Blade Runner 2049 (2017)
- More extreme color separation (orange Vegas, cyan LA, white Wallace Corp)
- Higher clarity, sharper digital look
- Expanded palette: toxic yellow, radiation orange, sterile white
- Roger Deakins' cinematography: controlled, architectural lighting

### Cyberpunk 2077 (2020, CD Projekt Red)
- Maximum saturation variant — pushed magenta/yellow/cyan to video game extremes
- Holographic overlays and UI elements integrated into the world
- Daytime cyberpunk (not all night — harsh overcast with neon accents)

### Modern Instagram/TikTok Interpretation
- Even more extreme clarity/dehaze
- Teal/orange split toning hybridized with magenta accents
- Often combined with "glow" / "bloom" / "diffusion" filters
