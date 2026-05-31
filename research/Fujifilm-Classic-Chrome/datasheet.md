# Fujifilm Classic Chrome — Official Datasheet

> **Source:** Fujifilm X Stories, "Film Simulation CLASSIC CHROME" (June 10, 2014)  
> URL: https://fujifilm-x.com/global/stories/film-simulation-classic-chrome/

---

## Origin & Design Philosophy

### Built for Professionals, Not Based on Film

Classic Chrome is **not modelled on a real film stock**. It is the first Fujifilm Film Simulation designed from scratch — an original digital color science created in response to requests from professional photographers, particularly **photojournalists**.

Fuji's engineering team analyzed **hundreds of documentary-style images** to reverse-engineer what photojournalists want from a color profile. The conclusion: good documentary images let the photographer "tell the viewer a story" — the look should support narrative, not distract with vivid color.

### Name Meaning

The name "CLASSIC CHROME" evokes:
- The **ambience of vintage magazine/documentary photography**
- The look of **physical prints** (as opposed to screen-native images)
- A nostalgic but not gimmicky color palette

---

## Core Color Science

### Five Key Design Pillars (Fuji's Own Words)

1. **Low color saturation** — Colors are intentionally subdued across the board, but not "washed out." The tones remain full-bodied and rich even at lower saturation.

2. **Full-bodied tones** — Deep, weighty tonal reproduction. Shadows carry real weight and density. This is a high-contrast simulation at heart.

3. **Sky tone engineering** — The single most distinctive technical feature: **magenta is systematically removed from blue/sky tones**. Instead of a rich cyan-magenta sky, you get a cooler, more subdued, almost steely blue. This was the result of direct analysis of what made documentary skies look "documentary."

4. **Red-green chromatic rebalancing** — Classic Chrome applies specific hue and saturation shifts to reds and greens. Reds are controlled (warmer but less saturated), greens are shifted slightly toward yellow. This creates the "magazine editorial" color signature.

5. **Digital-first optimization** — Unlike earlier film sims designed with print in mind, Classic Chrome was tuned for LCD screen viewing in JPEG format, reflecting how modern documentary work is consumed.

---

## How It Maps to the X-Trans Sensor

- Classic Chrome is a **JPEG engine profile** applied at capture time by the X Processor image pipeline.
- It uses Fujifilm's X-Trans CFA (Color Filter Array) as the input, which provides a **6×6 pseudo-random RGB pattern** instead of a 2×2 Bayer pattern.
- The irregular pattern inherently reduces moiré and color aliasing, giving Classic Chrome's color shifts a cleaner, more "organic" starting point than Bayer sensors.
- In Lightroom, the **Camera Matching profile "Classic Chrome"** is an Adobe-engineered approximation — it gets close but does not perfectly reproduce the in-camera JPEG output. Adobe's profile is derived from profiling the camera's JPEG output and is not the original Fujifilm pipeline.

### Classic Chrome vs. Other Film Simulations (Fuji's Own Positioning)

| Simulation | Base Reference | Saturation | Contrast | Primary Use |
|---|---|---|---|---|
| **PROVIA** | Reversal film (slide) | Standard | Standard | All-purpose |
| **Velvia** | Reversal film (slide) | High | High | Landscape |
| **ASTIA** | Reversal film (slide) | Soft | Soft | Portraits |
| **PRO Neg. Std** | Negative film | Muted | Soft | Studio portraits |
| **PRO Neg. Hi** | Negative film | Muted | Higher | Fashion/editorial |
| **Classic Chrome** | **No film — original** | **Low-mid** | **Strong** | **Documentary/street** |
| **Classic Neg** | Color negative film | Low | Strong | Vintage snapshot |
| **ETERNA** | Cinema film | Very low | Very low | Video/cinematic |

---

## In-Camera Available Adjustments (Fuji System)

When using Classic Chrome in-camera, Fuji provides these additional controls that layer on top of the base sim:

| Parameter | Range | Default | Effect |
|---|---|---|---|
| Highlight Tone | -2 to +4 | 0 | Clips or recovers highlights |
| Shadow Tone | -2 to +4 | 0 | Deepens or lifts blacks |
| Color | -4 to +4 | 0 | Global saturation |
| Sharpness | -4 to +4 | 0 | Perceptual sharpening |
| Noise Reduction | -4 to +4 | 0 | JPEG NR strength |
| Grain Effect | Off / Weak / Strong | Off | Adds film-like grain (Small/Large) |
| Color Chrome Effect | Off / Weak / Strong | Off | Reduces luminance of saturated colors, increasing "color depth/density" |
| Color Chrome FX Blue | Off / Weak / Strong | Off | Applies Color Chrome Effect specifically to blue tones |
| White Balance Shift | R/B ±9 | 0 | Fine-tune color cast on A/B and G/M axes |
| Dynamic Range | DR100/DR200/DR400 | DR100 | Protects highlights (raises ISO floor) |

---

## Fujifilm's Own Verdict

> *"Images shot with CLASSIC CHROME generally have low color saturation and full-bodied tones. We were particularly struck by how tones in skies were reproduced... When the sky includes a hint of magenta, the resulting color is rich, but with CLASSIC CHROME we moved in a different direction and created new colors by removing the magenta component."*

> *"By combining CLASSIC CHROME with the camera's image quality control features (including shadow tones and highlight tones) to match the scene and emotion, users can achieve a broader creative range."*

---

## Technical Summary

- **Introduced:** June 2014 (with X-T1 firmware, later X100T)
- **Based on:** No reference film — original color science
- **Target user:** Photojournalists, documentary photographers, street photographers
- **Key characteristic:** Magenta removal from sky blues, controlled reds/greens, high contrast, low saturation
- **Sensor dependency:** X-Trans CMOS sensor pipeline (APS-C and GFX)
- **Lightroom equivalent:** Adobe "Camera Matching: CLASSIC CHROME" profile (approximation)
