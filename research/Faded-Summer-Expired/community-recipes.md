# Community Recipes — Lightroom Settings for Expired Film Looks

> Sourced from Reddit (r/analog, r/postprocessing, r/Lightroom), YouTube tutorials, and photography forums. These are community-shared starting points for emulating the "Faded Summer / Expired Film" aesthetic.

---

## Core Principle: The 15-Year Attic Rule

The aesthetic we're emulating: cheap consumer color negative film (think Kodak Gold 200, Fuji Superia 400, or generic drugstore film) stored in a hot attic for 10–15 years, then shot with **+2 stops of overexposure**. The combination of heat degradation and deliberate overexposure produces a distinct look:

- Washed-out, milky shadows (base fog from heat)
- Extreme warmth / yellow-brown color cast (dye coupler degradation)
- Greens shift toward yellow-brown
- Blues become muted and teal-leaning
- Overall low contrast with lifted blacks
- Visible grain increase

---

## Recipe 1: "Attic Gold" — Reddit r/postprocessing Classic

The most-circulated recipe on r/postprocessing and r/analog for the heat-damaged expired look:

### Lightroom Classic Settings

**Basic Panel:**
| Parameter | Value | Notes |
|-----------|-------|-------|
| Exposure | +0.70 to +1.33 | Simulate +2 stops overexposure; adjust to taste |
| Contrast | -30 to -50 | Kill contrast; expired film loses contrast |
| Highlights | -60 to -80 | Recover blown skies |
| Shadows | +40 to +60 | Lift shadows into the base fog zone |
| Whites | +15 to +25 | Keep some brilliance |
| Blacks | +35 to +55 | **Key move**: clipped blacks are the giveaway; lift them significantly |

**Tone Curve:**
- Lift the black point: drag the bottom-left point up to roughly (0, 12-18%) on the Y axis
- Slight S-curve flattened: midtones slightly pulled down, highlights pulled up gently
- Alternative: add three points and create a gentle fade at both ends

**HSL / Color Panel:**
| Channel | Hue | Saturation | Luminance |
|---------|-----|------------|-----------|
| Red | +10 | -10 | +5 |
| Orange | -5 | -15 | +10 |
| Yellow | -15 | -15 | +5 |
| Green | **+30 to +50** | **-30 to -50** | -10 |
| Aqua | +15 | -20 | 0 |
| Blue | -10 | -20 | +5 |
| Purple | 0 | -20 | 0 |
| Magenta | +10 | -15 | 0 |

> The green-to-yellow shift (+30 to +50 on Green Hue) is the signature move. This pushes green foliage toward the yellow-brown spectrum that heat-damaged film produces.

**Color Grading (Split Toning):**
| Region | Hue | Saturation |
|--------|-----|------------|
| Shadows | 45–55 (warm yellow-orange) | 15–25 |
| Midtones | 35–45 (golden) | 10–15 |
| Highlights | 40–50 (warm) | 5–10 |

**Effects Panel:**
| Parameter | Value | Notes |
|-----------|-------|-------|
| Grain Amount | 40–60 | Expired film has pronounced grain |
| Grain Size | 35–50 | Larger than fresh film due to clumping |
| Grain Roughness | 60–80 | Rough, irregular grain pattern |
| Vignette Amount | -10 to -18 | Subtle edge darkening |
| Vignette Midpoint | 40–50 | |

**Calibration Panel (Critical for the "look"):**
| Channel | Hue | Saturation |
|---------|-----|------------|
| Red Primary | -10 | -5 |
| Green Primary | **+25** | -15 |
| Blue Primary | +10 | -10 |

> Pushing Green Primary Hue right is the secret sauce many Reddit users swear by—it shifts the entire green response toward the yellow-brown zone that defines heat-degraded color film.

---

## Recipe 2: "Sun-bleached Superia" — YouTube Tutorial Consensus

Derived from multiple YouTube tutorials focusing on the "left in a hot car for 5 summers" look:

### Lightroom Classic Settings

**Basic Panel:**
| Parameter | Value |
|-----------|-------|
| Temperature | +15 to +25 (warm it up) |
| Tint | -5 to +5 (slightly green for Superia base) |
| Exposure | +0.50 to +1.00 |
| Contrast | -20 to -40 |
| Highlights | -50 to -70 |
| Shadows | +30 to +50 |
| Whites | +10 to +20 |
| Blacks | +30 to +50 |

**Key Modification — Radial Filters:**
Add multiple radial filters to simulate uneven heat damage:
- Filter 1 (center): slight warmth + low contrast
- Filter 2 (edges): more warmth, more fade, stronger vignette
- Filter 3 (random placement): simulate "hot spot" damage with extreme warmth and exposure bump

**Grain Overlay Technique (advanced):**
Some YouTubers recommend adding a real scanned grain plate as a layer in Photoshop on Overlay/Soft Light mode at 15–30% opacity for maximum authenticity.

---

## Recipe 3: "Faded Summer" — r/Lightroom Community Preset

A minimal, highly-shared recipe that focuses on the faded, warm, low-contrast core:

**Lightroom Settings (concise):**
```
Exposure: +1.00
Contrast: -35
Highlights: -65
Shadows: +45
Whites: 0
Blacks: +40

Tone Curve:
  Blacks lifted to 15% (fade)
  Mild S-curve

Temperature: +12
Vignette: -15

HSL Green: Hue +35, Sat -35
HSL Yellow: Sat -20, Lum +15
HSL Blue: Sat -25, Lum +10

Split Tone:
  Shadows: Hue 55, Sat 20
  Highlights: Hue 45, Sat 10

Grain: 50/35/65
Calibration Green Primary: Hue +25, Sat -10
```

---

## Recipe 4: "Heat-Baked Kodak Gold" — Forum Deep Dive

From photography forums discussing the specific look of Kodak Gold 200 expired 2005–2010:

### Known Kodak Gold Aging Characteristics
- Gold 200 shifts strongly toward yellow-orange as it ages
- Blue sky → cyan/teal; Red → orange; Green → yellow-brown
- Base fog appears as a warm, reddish-brown veil over the entire image
- Grain becomes clumpy compared to fresh

### Recipe
| Setting | Value |
|---------|-------|
| WB Temp | 6200–7000K |
| WB Tint | -5 to +10 |
| Exposure | +0.85 |
| Contrast | -40 |
| Tone Curve | Lift blacks to ~18%, slight mid-tone dip |
| HSL Green Hue | +40 |
| HSL Green Sat | -40 |
| HSL Aqua Sat | -30 |
| HSL Blue Sat | -20 |
| HSL Blue Hue | +5 (toward cyan) |
| Split Tone Shadows | 50/20 |
| Split Tone Highlights | 42/12 |
| Grain | 55/40/70 |
| Post-Crop Vignette | -22, Midpoint 45, Feather 80 |

---

## Recipe 5: "Generic Drugstore Film Left in Attic" — Maximum Degradation

This recipe pushes everything further for the most extreme "baked" look:

**Basic:**
| Parameter | Value |
|-----------|-------|
| Exposure | +1.00 to +1.50 |
| Contrast | -50 |
| Highlights | -80 |
| Shadows | +70 |
| Blacks | +60 |
| Dehaze | -15 to -25 (adds atmospheric haze/fog) |

**HSL — Aggressive Color Shifts:**
| Channel | Hue | Sat | Lum |
|---------|-----|-----|-----|
| Red | 0 | -20 | 0 |
| Orange | -10 | -20 | +5 |
| Yellow | -20 | -25 | +10 |
| Green | **+60** | -50 | -10 |
| Aqua | +20 | -30 | 0 |
| Blue | -15 | -30 | +10 |
| Purple | -10 | -30 | 0 |
| Magenta | 0 | -25 | 0 |

**Optional:**
- Add a Graduated Filter from the bottom at +0.30 exposure and +15 temp to simulate uneven light leak damage
- Desaturate edges slightly via a radial filter inverted

---

## Photoshop / Capture One Equivalents

### Photoshop Actions (from r/postprocessing)
1. **Faded Film Action**: Curves adjustment layer lifting black point to RGB 25,25,25 → add Solid Color layer of #CC8800 at 10% opacity on Soft Light → add grain layer
2. **Color Shift Layer**: Selective Color adjustment: Greens → reduce Cyan +40%, increase Yellow +60%; Neutrals → increase Yellow +10%

### Capture One Settings (from Phase One forums)
- Base Characteristics: set to "Linear Response" for flat starting point
- Levels: lift black output to ~25
- Color Balance: Master → add warmth; Shadows → push toward orange (~45)
- Color Editor: Green hue +25°, Saturation -30; Blue hue -10°, Saturation -20
- Grain: 40 Impact, 50 Granularity (Silver Rich type)

---

## Community Wisdom & Tips

### From r/analog:
- "The key to nailing the expired film look is that blacks should NEVER be black. There's no true black on expired color neg film — it's all brown or dark green."
- "Don't just add warmth globally. The shadows should be warm/muddy, but highlights can be neutral or slightly cool. That contrast in white balance is what sells it."
- "Overexposing 2 stops on fresh film doesn't look like expired film. The base fog from heat is what creates the milky, low-contrast shadows. Lifting blacks in the tone curve is the single most important move."

### From r/postprocessing:
- "Add your grain LAST, after all color adjustments. Expired film grain sits ON TOP of the color shifts, not underneath them."
- "Don't use the Dehaze slider negative — it looks digital. Lift blacks with the tone curve instead."
- "The Calibration panel is underrated. Green Primary right, Blue Primary left. That alone gets you 70% there."

### From YouTube comments:
- "Use reference images. Find actual expired film scans on r/analog and color-pick from them to dial in your white balance."
- "The vignette should be warm-toned, not just dark. Use the Color Grading tool to tint the vignette area warm."
- "Film grain in Lightroom isn't great. Some pros export to Photoshop and use real scanned film grain overlays for the most authentic look."

---

## Quick-Start Card

If you only remember five things:

1. **Lift blacks to 30-55** (Tone Curve or Blacks slider) — the base fog effect
2. **Green Hue +30 to +50, Green Saturation -30 to -50** — the signature color shift
3. **Temperature +10 to +25** — overall warmth
4. **Contrast -30 to -50** — flatten the image
5. **Grain 40-60, Roughness 60-80** — the texture of decay

Combine these five moves and you have the foundation. Layer on HSL tweaks to specific colors based on which film stock you're emulating.
