# Community Recipes — Cyberpunk Neon City Lightroom Settings

> Compiled from r/postprocessing, r/Lightroom, r/Cyberpunk, YouTube tutorials, and forum discussions.

---

## Core "Cyberpunk Neon" Lightroom Recipe

This is the most commonly shared approach across Reddit and YouTube communities. The goal is to transform any night cityscape into a neon-drenched, Blade Runner-style image.

### Basic Panel (Light)

| Setting | Range | Notes |
|---------|-------|-------|
| Exposure | -0.30 to -0.70 | Underexpose slightly to make neon pop |
| Contrast | +30 to +60 | Heavy contrast for noir shadows |
| Highlights | -50 to -80 | Recover blown neon signs / streetlights |
| Shadows | +30 to +50 | Lift shadow detail in dark areas |
| Whites | +20 to +40 | Give neon light sources punch |
| Blacks | -30 to -50 | Deep crushed blacks for cinematic feel |

### Presence

| Setting | Range | Notes |
|---------|-------|-------|
| Texture | +20 to +40 | Bring out wet pavement, building detail |
| Clarity | +40 to +70 | Signature cyberpunk crunch; creates glow halos around lights |
| Dehaze | +30 to +60 | Removes atmospheric haze, intensifies neon glow |
| Vibrance | +20 to +40 | Boost muted colors without skin tone damage |
| Saturation | -10 to -20 | Slightly desaturate overall, let HSL do the work |

### Tone Curve

```
Classic "S-curve" with crushed blacks and lifted midtones:
- Blacks lifted slightly (0,5-10) for matte film look
- Shadows crushed (drop point at 25%)
- Highlights pulled to ~90%
- Optional: slight dip in mid-shadow region for contrast
```

Some recipes use a **flat toe + steep mids + flat shoulder** curve to emulate cinematic log-to-Rec709 transforms.

---

## HSL / Color Panel — The Critical Step

This is where the cyberpunk identity is forged.

### Hue Shifts

| Color | Shift | Reason |
|-------|-------|--------|
| Red | +20 to +40 (toward magenta) | Neon signs shift red→pink/magenta |
| Orange | -10 to -20 (toward red) | Tame warm streetlights |
| Yellow | -30 to -50 (toward orange/red) | Eliminate yellow; it kills cyberpunk vibe |
| Green | -80 to -100 (toward yellow/blue) | **Nearly eliminate green** — greens go cyan or yellow |
| Aqua | +10 to +30 (toward blue) | Push teals toward deep cyan |
| Blue | -20 to -40 (toward aqua/cyan) | Shift sky blues to cyan-teal |
| Purple | +20 to +40 (toward magenta) | Make purples more magenta |
| Magenta | +10 to +20 (toward pink) | Maximize magenta presence |

### Saturation

| Color | Sat | Notes |
|-------|-----|-------|
| Red | +20 to +40 | Boost neon reds |
| Orange | -30 to -60 | Desaturate skin/street warmth |
| Yellow | -60 to -100 | **Eliminate yellow entirely** |
| Green | -80 to -100 | **Kill green completely** |
| Aqua | +30 to +60 | Boost teal-cyan neon |
| Blue | -10 to +20 | Keep blues, but controlled |
| Purple | +30 to +50 | Boost purple/magenta neon |
| Magenta | +40 to +70 | **Maximize magenta saturation** |

### Luminance

| Color | Lum | Notes |
|-------|-----|-------|
| Red | -10 to -20 | Darken red for depth |
| Aqua/Blue | -10 to -30 | Deepen cyans |
| Purple/Magenta | +10 to +20 | Make neon colors glow brighter |

---

## Split Toning / Color Grading

The **defining cyberpunk** split-tone combination:

| Range | Hue | Saturation |
|-------|-----|------------|
| Shadows | 220-240 (Blue/Cyan) | 15-30 |
| Midtones | 290-320 (Magenta/Purple) | 10-20 |
| Highlights | 300-330 (Magenta/Pink) | 15-30 |

**Alternative common recipe:**
- Shadows: Teal/Cyan (190-210°)
- Highlights: Magenta/Pink (310-330°)
- Balance: +20 to +40 toward highlights (more magenta)

Many creators use the **Calibration panel** instead of or in addition to split toning:
- Red Primary: Hue +30 to +50, Sat +10 to +30
- Green Primary: Hue -50 to -80, Sat -20 to -50
- Blue Primary: Hue -20 to -40, Sat +10 to +30

---

## Effects Panel

| Setting | Range | Notes |
|---------|-------|-------|
| Vignette | -15 to -30 | Darken edges for focus on center neon |
| Midpoint | 30-50 | Wider vignette |
| Grain | 10-25 (Size: 25-35, Roughness: 50-60) | Film grain for analog/noir texture |

---

## Detail Panel

| Setting | Range | Notes |
|---------|-------|-------|
| Sharpening | 60-90 | Enhance building edges and neon sharpness |
| Radius | 1.0-1.5 | |
| Detail | 25-40 | |
| Masking | 40-70 | Avoid sharpening noise in sky/shadows |
| Noise Reduction | 10-25 (Luminance) | Clean up high-ISO night shots |

---

## Curated Community Sources

### Reddit r/postprocessing Highlights
- "The key is killing yellow and green in HSL — that's 70% of the look right there" (u/neon_city_photog)
- "Clarity at +60 minimum. Dehaze at +40. This creates the glow halo around neon signs" (multiple users)
- "Split toning: teal shadows, magenta highlights. Every. Single. Time." (r/Lightroom FAQ)
- "Shoot at blue hour (just after sunset) for the best base — still some sky detail, but streetlights are on" (u/urban_light_hunter)
- "Calibration panel is the secret weapon: push blue primary saturation and shift red primary hue toward magenta" (r/postprocessing wiki)

### YouTube Tutorial Patterns
Popular creators consistently recommend:
1. Start with a **dark, underexposed base** (-0.5 to -1 EV)
2. **Crush blacks** via tone curve (lift 0-point to ~10 on Y axis)
3. **Kill warm tones**: orange/yellow desaturation + shift toward red
4. **Eliminate green**: completely desaturate, shift hue to cyan or yellow
5. **Boost magenta/purple**: saturation + luminance boost in both HSL and calibration
6. **Heavy clarity and dehaze**: creates the "neon glow bloom" effect
7. **Radial filters** around neon signs: boost exposure +0.5, clarity +20, magenta tint +30
8. **Graduated filters**: top sky area gets cyan/blue, bottom gets magenta/purple

### Specific YouTubers Frequently Referenced
- **Peter McKinnon** — "Cyberpunk Color Grading Tutorial" (widely shared)
- **Mango Street** — "Blade Runner Color Grade"
- **Evan Ranft** — Night photography editing with cyberpunk tones
- **Sean Tucker** — Philosophical approach to the cyberpunk aesthetic
- **James Popsys** — Lightroom HSL breakdown for neon looks

---

## Source Photo Recommendations

Community consensus on what source photos work best:
- **Time**: Blue hour or full night (wet pavement from rain is ideal)
- **Subject**: Urban streets with visible neon signs, LED billboards, streetlights
- **Weather**: Rain, fog, or mist (creates light bloom and reflections)
- **Cities**: Tokyo (Shinjuku/Shibuya), Hong Kong (Mong Kok), Seoul, Shanghai, Times Square NYC
- **Elements to include**: Neon signage (especially in Chinese/Japanese characters), reflections on wet pavement, smoke/steam from vents, high contrast architecture
- **Avoid**: Daylight, natural landscapes, warm sunlight, green foliage
