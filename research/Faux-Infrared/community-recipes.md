# Community Recipes — Faux Infrared in Lightroom

## Overview

Because real Kodak Aerochrome and HIE film are discontinued and prohibitively expensive (expired rolls sell for $100+), a thriving community has developed techniques to simulate the infrared look using Lightroom's B&W mixer, HSL panel, calibration sliders, and tone curves. The core principle: **brighten greens/yellows to simulate glowing foliage, darken blues/aquas to simulate dark IR skies.**

---

## Black & White Faux Infrared

### Method: B&W Mixer (Most Common)

This is the most reliable faux IR technique. The B&W panel in Lightroom lets you control the luminance of each color channel independently.

**Core settings (starting point):**

| Color Channel | Luminance Value | Purpose |
|--------------|----------------|---------|
| Red | +60 to +100 | Brightens warm-toned foliage |
| Orange | +50 to +80 | Brightens earthy tones, transitional vegetation |
| Yellow | +80 to +100 | Maximum leaf/grass luminance boost |
| Green | +80 to +100 | Primary foliage IR glow |
| Aqua | -30 to -60 | Darkens sky, water |
| Blue | -60 to -100 | Darkens sky dramatically (IR sky = black) |
| Purple | -30 to -60 | Darkens shadows, distant haze |
| Magenta | -20 to -40 | Subtle darkening |

**Complementary adjustments:**
- **Contrast:** +30 to +60 (IR is inherently contrasty)
- **Clarity:** +30 to +60 (enhances the Wood Effect texture)
- **Dehaze:** +15 to +40 (clears atmospheric haze, IR penetrates haze)
- **Exposure:** +0.3 to +1.0 (IR photos tend to be brighter)
- **Highlights:** -20 to -60 (recover bright foliage detail)
- **Shadows:** +20 to +40 (open up dark areas)
- **Whites:** +20 to +40 (push foliage to pure white)
- **Blacks:** -20 to -50 (deepen sky/shadows)

**Optional: Add halation/glow effect**
- **Sharpening:** Amount 40–80, Radius 1.0–1.5, Detail ~25
- Or use **Negative Clarity** locally (-20 to -40) with a radial filter on highlights
- Some users add a **Gaussian Blur** layer at ~5–10 px opacity in Photoshop to simulate HIE's anti-halation-less glow

### Method: HSL Desaturation (Less Common)

1. Set Treatment to B&W.
2. In HSL/Color panel (still works in B&W mode), push Green and Yellow luminance to +100.
3. Pull Blue luminance to -100.
4. Adjust Aqua similarly to darken skies.

### Reddit/Discussion Community Tips

From r/postprocessing, r/analog, r/infraredphotography:

- **"Green and yellow to +100, blues to -100"** is the universal starting mantra.
- **Use the Targeted Adjustment Tool** (TAT) in the B&W panel — click and drag UP on foliage, DOWN on sky.
- **HSL panel still matters in B&W** — the Luminance sliders in the B&W panel AND the HSL/Luminance sliders both affect the B&W mix. Some users prefer HSL because they can also adjust saturation before converting.
- **Graduated filter over sky:** -2 to -3 EV exposure, -100 blue luminance to get the dramatic dark sky IR look.
- **Orange/red filter emulation:** Before converting to B&W, apply a virtual red/orange filter via the calibration/profile to pre-shift colors for better separation.
- **Dehaze is critical** — IR film cuts through atmospheric haze. +20 to +50 dehaze is commonly recommended.

---

## Color (False-Color) Faux Infrared — Aerochrome Simulation

Simulating Aerochrome in Lightroom is harder because it requires channel remapping. Most successful approaches use HSL + Calibration.

### Method: HSL + Camera Calibration

**Step 1 — HSL Panel:**

| Slider | Hue | Saturation | Luminance |
|--------|-----|-----------|-----------|
| Red | +20 to +40 (toward magenta) | +20 to +40 | +30 to +60 |
| Orange | -20 to -40 (toward red) | +10 to +30 | +40 to +70 |
| Yellow | -30 to -60 (toward green) | -20 to -40 | +60 to +100 |
| Green | -60 to -100 (toward yellow) | -50 to -80 | +80 to +100 |
| Aqua | 0 to -20 | -30 to -60 | -40 to -80 |
| Blue | -10 to -30 | -40 to -80 | -60 to -100 |
| Purple | +30 to +60 (toward magenta) | -10 to +20 | -20 to -40 |
| Magenta | +40 to +80 (toward red) | +30 to +60 | +10 to +30 |

**Step 2 — Camera Calibration:**

| Slider | Value | Purpose |
|--------|-------|---------|
| Shadows Tint | +30 to +60 (toward green) | Shifts shadow color cast |
| Red Primary Hue | +40 to +80 (toward magenta) | Pushes reds toward Aerochrome pink/magenta |
| Red Primary Sat | +20 to +50 | Intensifies the false-color foliage |
| Green Primary Hue | -40 to -80 (toward yellow) | Shifts greens toward the Aerochrome red channel |
| Green Primary Sat | -20 to -40 | Reduces green intensity |
| Blue Primary Hue | +20 to +50 (toward purple) | Shifts blues toward cyan for sky separation |
| Blue Primary Sat | -20 to +20 | Adjust to taste |

**Step 3 — Tone Curve:**
- S-curve with lifted blacks (matte look common in film scans).
- Red channel: slight S-curve, lift shadows slightly.
- Green channel: reduce mid-tones (reduces residual green).
- Blue channel: slight boost in highlights (ensures sky isn't too dark).

**Step 4 — Split Toning:**
- Highlights: warm/peach tint (subtle, saturation 5–15).
- Shadows: cool blue/teal tint (saturation 10–25).
- This enhances the surreal color separation.

### Easier Alternative: Profile/Channel Swapping

Some users in Photoshop swap red/blue channels for instant false-color IR:
1. Open image in Photoshop.
2. Channel Mixer adjustment layer.
3. Red channel: Red = 0%, Blue = 100%.
4. Blue channel: Red = 100%, Blue = 0%.
5. Fine-tune in Lightroom afterward.

This approximates the Aerochrome spectral remapping (IR→red, red→green, green→blue).

---

## YouTube / Video Tutorial References

Popular YouTube channels that have covered faux infrared:
- **PIXimperfect** — Photoshop channel swap and IR simulation
- **Phlearn** — Infrared color grading
- **Peter McKinnon** — B&W infrared editing workflow
- **Jamie Windsor** — Film emulation including IR looks
- **Sean Tucker** — B&W processing with IR-style contrast

Search terms: `faux infrared lightroom`, `aerochrome lightroom tutorial`, `black and white infrared lightroom preset`, `false color infrared photoshop`.

---

## Quick-Reference Cheat Sheet

### B&W Faux IR (30-second recipe)
1. `V` key → B&W treatment
2. B&W Mixer: Green +100, Yellow +100, Blue -100, Aqua -80
3. Dehaze +30
4. Contrast +40
5. Clarity +40
6. Blacks -30

### Color Faux IR / Aerochrome (60-second recipe)
1. HSL: Green Hue -80, Green Sat -60, Green Lum +100
2. HSL: Blue Lum -80, Aqua Lum -60
3. HSL: Yellow Lum +80
4. Calibration: Red Primary Hue +60, Green Primary Hue -60
5. Calibration: Red Primary Sat +40
6. Dehaze +25, Contrast +20

### Best Source Images for Faux IR
- **Landscapes with deciduous trees** (conifers reflect less IR).
- **Bright midday sun** (maximum IR reflectance from foliage).
- **Blue sky with clouds** (clouds pop against dark IR sky).
- **Green grass, fields, meadows** (maximum IR bounce).
- **Water features** (water absorbs IR → goes black, striking contrast).
- **Avoid:** indoor, overcast/flat light, urban without vegetation, autumn/winter (dead leaves don't reflect IR as strongly).

---

## Sources
- Reddit communities: r/postprocessing, r/analog, r/infraredphotography
- YouTube tutorials (PIXimperfect, Phlearn, Jamie Windsor, Sean Tucker)
- Photography forum discussions (DPReview, Fred Miranda, Lightroom Queen Forums)
