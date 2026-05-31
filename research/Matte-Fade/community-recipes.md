# Community Recipes: The Matte Fade Look

> Compiled from r/Lightroom, r/postprocessing, YouTube tutorials, and photography forums (2015–present). The matte fade is arguably the most requested "how do I get this look" question across all Lightroom communities.

---

## Foundational Principle

The matte fade is achieved by manipulating the **Tone Curve** to lift the black point — the bottom-left node of the curve is raised from (0,0) to approximately (0, 5–15) on the Y-axis. This removes true black from the image, creating a soft, hazy shadow transition. Everything else (contrast sliders, color grading, dehaze) supports and refines this core move.

---

## Recipe 1: The Classic Matte Fade (Clean Starting Point)

The most shared "starter" recipe across r/Lightroom. Works on most image types.

| Setting | Value | Notes |
|---------|-------|-------|
| **Tone Curve** | Lift black point to output 5–8% | Drag bottom-left point straight up; keep point at 0 on X axis |
| Contrast | -15 to -25 | Reduces overall tonal separation |
| Highlights | -20 to -30 | Tames bright areas |
| Shadows | +10 to +20 | Recovers shadow detail |
| Whites | +10 | Counteracts the overall flatness |
| Blacks | +10 to +15 (slider) | Supplemental to curve lift |
| Vibrance | +10 to +15 | Restores color pop lost from contrast reduction |
| Saturation | -5 to -10 | Keeps skin tones from going orange |
| Temperature | +5 to +8 | Subtle warmth |
| **Split Toning (Shadows)** | Hue ~35–45°, Saturation ~15–25% | Warm amber/brown into blacks |
| Dehaze | -5 to -10 | Adds atmospheric haze (optional) |

**Source references:** r/Lightroom "how to get matte look" megathreads (2016–2019); YouTube — Peter McKinnon "How to Edit Like a PRO" (2017); Mango Street "Matte Film Look in Lightroom" (2018)

---

## Recipe 2: The Heavy Film Fade (VSCO-Inspired)

A more aggressive fade, mimicking VSCO presets A6, M5, and HB2. Favored for lifestyle and travel photography.

| Setting | Value | Notes |
|---------|-------|-------|
| **Tone Curve (RGB)** | Lift black point to output 10–15% | Aggressive lift; also pull down white point to ~90% |
| Additional Curve Point | Add mid-shadow point at (25%, 30%) | Creates a "knee" — shadows lift fast then flatten |
| Contrast | -25 to -35 | Heavy reduction |
| Highlights | -30 to -50 | Strong highlight recovery |
| Shadows | +20 to +35 | Brings shadows way up |
| Whites | +15 to +25 | Prevents true white — keeps the faded feel |
| Blacks (slider) | +15 to +25 | Works *with* the curve, not instead of it |
| Temperature | +8 to +15 | Noticeable warmth |
| Tint | +3 to +8 | Slight magenta shift for film-like warmth |
| Vibrance | -5 to +5 | Subdued |
| Saturation | -10 to -15 | Strong desaturation |
| **Split Toning (Shadows)** | Hue ~35–50°, Saturation ~25–40% | Prominent warm brown/amber shadows |
| **Split Toning (Highlights)** | Hue ~200–220°, Saturation ~5–10% | Subtle cool blue highlights (cross-processed feel) |
| Grain | Amount ~20–30, Size ~25, Roughness ~50 | For texture |
| Dehaze | -10 to -15 | Adds significant haze |

**Source references:** r/postprocessing "VSCO film emulation" threads; Reddit user u/chelsea_film's preset breakdowns; various "expired film look" YouTube tutorials (2016–2019)

---

## Recipe 3: The Warm Vintage Matte (Golden Hour / Editorial)

Popular in wedding and engagement photography. Emphasizes warm, romantic tones.

| Setting | Value | Notes |
|---------|-------|-------|
| **Tone Curve** | Lift black point to output 8–12% | Moderate lift |
| Curve White Point | Pull down to ~92–95% | Softens highlights |
| Contrast | -15 to -20 | Moderate reduction |
| Highlights | -15 to -25 | Gentle taming |
| Shadows | +15 to +25 | Opens up dark areas |
| Whites | -5 to -10 | Slight reduction for softer whites |
| Blacks (slider) | +12 to +18 | Works with curve |
| Temperature | +10 to +20 | Strong warmth |
| Tint | +5 to +10 | Pink/magenta warmth |
| **Split Toning (Shadows)** | Hue ~30–40°, Saturation ~20–35% | Warm amber, close to brown |
| **Split Toning (Highlights)** | Hue ~45–60°, Saturation ~10–15% | Warm yellow/gold highlights |
| Saturation | -5 | Slight desaturation |
| Grain | Amount ~15–25 | Subtle texture |
| Dehaze | -5 to -10 | Light haze |

**Source references:** r/WeddingPhotography preset exchange threads; Tribe Archipelago preset analysis discussions; Mastin Labs Fuji Pro emulation breakdowns

---

## Recipe 4: The Subtle Editorial Matte (Professional / Clean)

The "grown-up" matte fade — barely perceptible but effective. Used in fashion editorials and high-end portrait work.

| Setting | Value | Notes |
|---------|-------|-------|
| **Tone Curve** | Lift black point to output 3–5% | Extremely subtle — blacks are dark gray, not washed out |
| Contrast | -5 to -10 | Very mild reduction |
| Highlights | -10 to -15 | Subtle |
| Shadows | +5 to +15 | Gentle shadow lift |
| Whites | +10 to +20 | Preserves bright point, prevents flatness |
| Blacks (slider) | +5 to +10 | Minimal slider use |
| Clarity | +5 to +10 | Adds back micro-contrast lost from fade |
| Temperature | +3 to +8 | Barely warm |
| **Split Toning (Shadows)** | Hue ~35°, Saturation ~5–10% | Invisible on its own; adds subconscious warmth |
| Vibrance | +5 to +10 | Controlled pop |

**Source references:** r/postprocessing "I want a matte look that doesn't look Instagram-filtered" threads; SLR Lounge Lightroom workshop techniques; Fstoppers editorial editing tutorials

---

## Recipe 5: The Cool-Toned Matte Fade (Alternative)

A variant using cool shadows instead of warm — popular in fashion and urban photography from 2017–2019.

| Setting | Value | Notes |
|---------|-------|-------|
| **Tone Curve** | Lift black point to output 5–10% | Standard lift |
| Contrast | -15 to -20 | Standard |
| Temperature | -5 to -10 | Cool shift |
| Tint | 0 to +5 | Slight magenta to prevent cold sterility |
| **Split Toning (Shadows)** | Hue ~210–230°, Saturation ~15–25% | Cool blue/gray shadows |
| **Split Toning (Highlights)** | Hue ~40–50°, Saturation ~5–10% | Subtle warm highlights for balance |
| Saturation | -10 to -15 | Desaturated for a muted palette |
| Dehaze | -5 | Light haze |

**Source references:** r/postprocessing "moody matte" request threads; YouTube tutorials for "cinematic matte look" (2017–2019)

---

## Community Wisdom & Common Pitfalls

### From Reddit Discussions (r/Lightroom, r/postprocessing)

1. **"Tone curve, not just the blacks slider."** The most repeated advice. The blacks slider alone creates a different look (flat shadows). The tone curve lift is what creates the *faded* quality, because it compresses the entire shadow range.

2. **"Don't just drag the point up — use a multi-point curve."** Advanced users recommend adding 2–3 points in the curve:
   - Bottom-left: lifted to ~8% output
   - 25% input: set to ~30% output (the "knee")
   - 50% input: set to ~55% output (gentle midtone boost)
   This creates a smooth, gradual fade rather than an abrupt shadow cliff.

3. **"Subtle is professional; dramatic is Instagram 2015."** The aggressive 10–15% black lift was heavily critiqued as a passing trend. A 3–7% lift is widely considered more timeless.

4. **"Split toning makes or breaks it."** Adding warm brown/amber to the lifted shadows is what gives the matte fade its signature "feel." Without it, lifted blacks can look muddy or gray. A hue of 35–45° at 15–25% saturation is the community consensus sweet spot.

5. **"Use dehaze as a fade controller."** Negative dehaze values (-5 to -15) add atmospheric haze that visually blends with the lifted blacks, creating a more organic fade. Some users prefer -10 dehaze to a 15% black lift because it looks more natural.

6. **"Contrast reduction first, everything else second."** Many users build the look by reducing contrast to taste *before* touching the tone curve, then fine-tuning with the curve.

### From YouTube Tutorials

- **Peter McKinnon** (2017) popularized a technique: RGB curve with lifted blacks, reduced contrast, added grain. His tutorial "How to Edit Like a PRO" showed the look as step one in his personal workflow.
- **Mango Street** (2018) advocated for a gentler approach: use the parametric curve sliders (Shadows/Blacks +) in combination with a subtle point curve lift, rather than aggressive RGB curve manipulation.
- **Jessica Kobeissi** demonstrated a variant using the Tone Curve's "Linear" preset as a starting point, then adjusting individual R, G, and B channels for a color-shifted fade.

### From Photography Forums

- **PetaPixel** published a widely cited 2017 tutorial: "How to Get That Faded Effect in Lightroom" — covered the core technique of raising the bottom-left tone curve point, reducing contrast, and adding warm split toning.
- **SLR Lounge** / **Fstoppers** (2018–2019) workshops included the matte fade as a foundational technique in their paid Lightroom education, treating it as the starting point for most film-emulation presets.
- **Contrastly** published a 2016 tutorial tracking the rise of the matte fade from VSCO's mobile app to desktop Lightroom, documenting the shift from novelty filter to mainstream editing style.

---

## Hardware / Software Compatibility

The matte fade works identically across:
- Lightroom Classic (tone curve + split toning)
- Lightroom CC / Mobile (tone curve + color grading)
- Adobe Camera Raw (same engine)
- Capture One (curves tool + color balance — slightly different UI but same concept)
- Darktable (tone curve module + color balance)

The look originated in analog printing (matte paper inherently has less dense blacks than glossy) and was digitally popularized by VSCO's mobile app (2012) before migrating to desktop workflows.

---

## Further Reading / Source Context

- Reddit: r/Lightroom — search "matte look," "faded blacks," "VSCO preset," "film fade" (2015–2020)
- Reddit: r/postprocessing — search "matte fade tutorial," "how to achieve faded look," "lifted blacks"
- YouTube: Peter McKinnon, Mango Street, Jessica Kobeissi, Sean Tucker, Evan Ranft — all have matte/fade tutorial content
- Photography publications: PetaPixel (2017), Fstoppers (2018), SLR Lounge blog, Photography Tuts+, Contrastly (2016)
- Preset companies: VSCO, Mastin Labs, Tribe Archipelago, Noble Presets — all produce matte-fade variants as core products
