# Cinestill 800T — Community Recipes (Lightroom Emulation)

## Overview

Emulating Cinestill 800T in Lightroom requires two separate components:
1. **Color & tone settings** — achievable in Lightroom alone
2. **Red halation effect** — requires Photoshop, a halation brush, or external overlays

The most thorough public recipe comes from **Joe D'Agostino** (2020 blog post), with specific panel-by-panel settings. Many YouTube tutorials and preset packs build upon similar principles.

---

## Joe D'Agostino's Public Recipe (2020)

The most detailed free public recipe. Published on his blog under "Recreating Cinestill 800T for Lightroom."

### Shooting Prep (in-camera)
- Shoot slightly underexposed (protect highlights)
- In-camera WB: 2800–3200K
- Best results with night scenes containing point light sources

### Basic Panel
| Setting | Value |
|---|---|
| WB Temp | 2850 K (starting point) |
| Tint | Adjust gently — strong shifts with small movements |
| Exposure | +0.50 to +1.00 (recover from underexposure) |
| Contrast | +10 to +20 |
| Highlights | -60 to -80 (slam down hard) |
| Shadows | +40 to +60 (pulls filmic red tones from shadows) |
| Whites | -20 to -40 (soften highlight bite) |
| Blacks | -10 to -20 |

### Tone Curve (Parametric)
- S-curve with lifted tail on darks for subtle matte look
- "Flip up the tail on the darks for a subtle matte look if you like that style"

### RGB Curves (Point Curve)
Joe emphasizes copying his exact RGB curve shapes:

**Red channel**: S-curve — lift shadows slightly, pull highlights down
**Green channel**: Similar S-curve — more neutral midtones
**Blue channel**: Most aggressive curve — significant shadow lifting (adds blue/teal to shadows), moderate highlight suppression

The key insight: **shadows in Cinestill scans shift from blue → teal → green → even red tones** in deep blacks. The RGB curves create these cross-channel transitions.

### HSL Panel
Joe provides exact numeric values (screenshots shown but not all numbers transcribed — see original post):
- **Reds**: Saturation boosted moderately
- **Oranges**: Hue shifted toward red, saturation moderately boosted
- **Yellows**: Minimal adjustment
- **Greens**: Hue shifted toward teal
- **Aquas**: Saturation boosted, luminance adjusted
- **Blues**: Luminance darkened for richer night skies
- **Purples/Magentas**: Moderate adjustments

### Split Toning
| Setting | Value |
|---|---|
| Highlights Hue | Cool/warm balanced (near 50) |
| Highlights Saturation | Low (~10–15) |
| Shadows Hue | Teal/blue zone (~200–220) |
| Shadows Saturation | Moderate (~20–30) |
| Balance | Adjust from center as needed |

### Calibration Panel
Input exact values from the calibration tab:
- Red Primary: Shift hue toward orange, moderate saturation adjustment
- Green Primary: Shift hue toward teal, slight saturation increase
- Blue Primary: Shift hue, saturation adjustment
(This creates the base "film matrix" color transform)

### Effects
- **Grain**: Add to taste (35mm style, Amount ~30–50, Size ~25, Roughness ~50)
- **Vignette**: Subtle (-5 to -10)
- **Dehaze**: Slightly negative (~ -5 to -10) for glow
- **Clarity**: Slightly negative (~ -5 to -10)

### Halation (post-Lightroom)
Joe notes: "its very hard to achieve in Lightroom." His solutions:
1. **Black Pro Mist filter** (1/4 strength, Tiffen brand) — in-camera diffusion creates highlight bloom
2. **Halation brush** — included in his paid preset pack for Lightroom
3. **Photoshop** — for the most control

---

## PresetsStore Free Preset Recipe (2021)

Published as a step-by-step tutorial at presetsstore.com. Approach:

### Light Correction
1. Create matte style via tone curves
2. Standard exposure/highlights/shadows adjustments
3. Negative dehaze and clarity for softness
4. Add grain

### Color Correction
1. Warm yellow tint to shadows
2. Cool blue tint to midtones
3. Overall filmic, retro color scheme

### Preset Available
- Free DNG download (mobile app compatible)
- Paid XMP version available with 3 variations

---

## Common Community Patterns (r/postprocessing, YouTube)

From Reddit's r/postprocessing thread on Cinestill 800T emulation (2024):

### Key Challenges Identified
- **Halation is the hardest part** — most community members agree true halation requires Photoshop or dehancer-like plugins
- Many users report spending **1–2 years** trying to get satisfactory Cinestill emulation
- Davinci Resolve users often find better results via Dehancer or FilmConvert plugins

### Approaches That Work
1. **Start with Vision3 500T base** (the Kodak film) rather than trying to emulate Cinestill directly — then add halation separately
2. **Use Dehancer plugin** (paid) — has dedicated Cinestill 800T profile with halation simulation
3. **RGB curves are critical** — the cross-channel shadow color transitions define the look more than any single adjustment
4. **In-camera WB matters** — starting at ~2800–3200K in-camera reduces post-processing work

### Free LUT Resources
- **Lutmix.com**: Free Cinestill 800T LUTs — color style only, no halation
- **PSD Stack**: Free Cinestill 800 preset for Photoshop
- **t3mujinpack (GitHub)**: Open-source Darktable presets including Cinestill film emulation

---

## YouTube Tutorial References

1. "How to Create the CineStill 400D/800T Look in Lightroom Classic" — Step-by-step Lightroom tutorial
2. Jamie Windsor's "JW Lightroom Presets 4 — Cinestill" — Detailed before/after walkthrough with Photoshop halation action
3. Multiple creators on YouTube demonstrate halation creation via:
   - Layer masks + red glow brushes in Photoshop
   - Blend-if on highlights + gaussian blur + red color overlay
   - Dedicated halation plugins

---

## Dehancer Plugin (Professional Solution)

The most accurate digital emulation mentioned repeatedly in community discussions:
- Has dedicated Cinestill 800T profile
- Models halation physically (simulates light reflection through film base)
- Supports Davinci Resolve, Premiere, Final Cut, Photoshop (paid plugin)
- Price: ~$199–399 depending on license tier

---

## Sources
- Joe D'Agostino Photography Blog: "Recreating Cinestill 800T for Lightroom" (March 2020)
- r/postprocessing: "Cinestill 800T Emulation" thread (2024)
- PresetsStore: "CineStill 800T | Free Lightroom Preset" tutorial
- Lutmix.com: Cinestill 800T free LUTs
- PSD Stack: Free Cinestill 800 Preset
- t3mujinpack GitHub: Darktable film emulation presets
- YouTube: Multiple Lightroom Classic Cinestill tutorials
