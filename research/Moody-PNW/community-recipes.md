# Community Recipes: Moody PNW / Dark Forest Editing

> Lightroom settings sourced from Reddit r/postprocessing, r/Lightroom, and YouTube tutorials.

---

## Recipe 1: RunNGunPhoto "Dark & Moody Forest" (Lightroom Mobile)

**Source**: Reddit r/postprocessing, Feb 2020 — 45 upvotes, verified settings.
**YouTube walkthrough**: `youtu.be/E6Ffh9BIWLE`
**Also**: Later variant (2023) for portrait-style forest look at `youtu.be/UixXPnsCsPk`

### Light Tab
- Exposure: -0.50
- Contrast: +35 to +50
- Highlights: -100 (maximizes detail)
- Shadows: +100 (maximizes detail)
- Whites: +25
- Blacks: -25
- Tone Curve: Strong S-curve, shadow point lifted ~0.75 stops (faded blacks)

### Color Tab
- Temperature: -10 (cooler)
- Tint: -5 (toward green)
- Saturation: -50
- HSL / Color Mix:
  - Red: Hue +20, Sat -30, Lum 0
  - Orange: Hue 0, Sat -10, Lum +80
  - Yellow: Hue 0, Sat -30, Lum 0
  - Green: Hue +50, Sat -80, Lum +40
  - Cyan: Hue +40, Sat -30, Lum +30
  - Blue: Hue -20, Sat -30, Lum +10
  - Purple: No change
  - Violet: No change

### Effects Tab
- Clarity: slightly down
- Dehaze: slightly up
- Split Tone: Green tint to highlights (+10 Sat max), purple/blue tint to shadows (+10 Sat max)
- Vignette: light

### Detail Tab
- Sharpening: +40 to 50, Radius 1.0 or lower

### Key observations
- The green hue shift (+50) pushes greens toward yellow/brown territory
- -80 green saturation crushes the "happy" green look
- Orange luminance +80 brightens earthy tones
- Lifted shadow point on tone curve creates that "faded" look
- Cool white balance + green tint is fundamental

---

## Recipe 2: thephlog "Dark & Moody Autumn Forest Edit"

**Source**: Reddit r/postprocessing, Feb 2020 — 981 upvotes (highest-voted moody forest post).
**YouTube**: `youtu.be/INCY0JGSJBs`

### Workflow

1. **Lens Corrections**: Remove chromatic aberration + lens distortion. Camera profile → Adobe Standard.

2. **Basic Adjustments**:
   - Drop Exposure further (started from already-dark RAW)
   - Raise Shadows significantly (preserves detail in dark areas while keeping overall dark feel)
   - Increase Whites slightly (adds separation between bright and dark)

3. **Local Adjustments**:
   - Radial filter on center: +Exposure, +Contrast, +Highlights (brighten focal area)
   - Radial filter on bottom center: subtle blue tint + highlights + clarity (atmospheric mystery)

4. **Color Grading**:
   - Split toning: warm tone on highlights
   - Calibration tab (critical!): Drop Blue Hue dramatically → turns greens into orange/red tones. Increase Blue Saturation.

5. **Nik Collection** (Color Efex Pro 4): Polarization effect to pull attention to center colors.

### Key observations
- Calibration tab is the secret weapon for shifting greens
- Radial gradients create focal glow in otherwise dark forest
- One commenter noted: "a little bit of dehaze but otherwise very nice"

---

## Recipe 3: Community Feedback Synthesis (r/postprocessing Mood Critique Threads)

**Sources**: Multiple critique threads with specific advice for achieving moody forest looks.

### Common themes from feedback on moody forest edits:

1. **"Lift the shadows a bit"** — consistent feedback across multiple posts. Dark moody doesn't mean crushed blacks — you need shadow detail.

2. **"Lower the greens"** — repeated advice to desaturate greens so foliage doesn't "stand out too much." Green desaturation is the #1 community signal.

3. **"The yellow channel needs to be toned down more than the green"** — yellow luminance is critical for the moody feel. Too-bright yellows kill the vibe.

4. **Split toning is essential** — greenish hue on highlights, but don't overdo it. Use subtle amounts.

5. **"Tone down saturation/vibrance"** — makes image look "sharp/noisy" otherwise.

6. **Fog/atmosphere post** (MitchGreenPhotos, Jan 2020):
   - Cool white balance
   - Bring up blacks (NOT crush them)
   - More midtone contrast
   - Soft light on brighter areas for fog glow

7. **From r/Lightroom "Dark and Moody in LR 2026" thread** (Feb 2026):
   - Start with histogram skewed left (darker image)
   - Pull down exposure and black point, raise white point
   - Adjust luminance sliders in HSL
   - Use radial gradient masks for focal brightness
   - Try Adobe built-in "Warm & Moody" + "Cinematic" presets layered
   - Landscape photographer "ExploreroftheLight": build in brightness selectively with radial masks

---

## Recipe 4: u/Nikon-D780 Settings (from Critique Thread)

**Source**: r/postprocessing comment, Jul 2021. Using "Ultralight-photo editor" but values translate to LR:
- Black level: -1
- Shadow level: +7
- Midtones: +4
- Highlights: +8
- White level: +4
- No saturation/hue/luminosity adjustments

Commenter's philosophy: "Raises shadow detail. Highlights the edge. The green foliage catches the viewer's eye, leading into the shadows — dark enough to add mystery, light enough to spark imagination."

---

## YouTube Tutorial References

| Tutorial | Creator | Focus |
|---|---|---|
| `youtu.be/E6Ffh9BIWLE` | RunNGunPhoto | Dark & Moody Forest — Lightroom Mobile (recipe #1 above) |
| `youtu.be/INCY0JGSJBs` | thephlog | Dark & Moody Autumn Forest — Lightroom Classic (recipe #2 above) |
| `youtu.be/UixXPnsCsPk` | RunNGunPhoto | Dark & Moody Forest Portrait Look (2023) |
| `youtu.be/OqrdskZDMnw` | Tasty-Statement | B&W Moody Forest Processing |
| `youtu.be/t8jK54oZHLs` | techrimon | Dark Moody Effect — Lightroom Mobile |

---

## Common Pattern: The Mood Slider "Formula"

Synthesizing all sources, the modal approach appears to be:

```
Exposure: -0.3 to -0.7
Contrast: +25 to +50
Highlights: -50 to -100
Shadows: +50 to +100
Whites: +15 to +35
Blacks: -15 to -30

Temperature: -5 to -15 (cool)
Tint: -3 to -10 (toward green)
Saturation: -30 to -60

Green Hue: +40 to +60 (shift toward yellow)
Green Sat: -60 to -90 (crush green)
Yellow Sat: -20 to -40
Orange Lum: +50 to +80 (earth tones pop)

Tone Curve: Lift shadow point (faded blacks) + mild S-curve
Split Toning: Green/teal highlights, cool blue/purple shadows
Vignette: -5 to -15
Dehaze: +5 to +15
```
