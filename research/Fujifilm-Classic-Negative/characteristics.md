# Classic Negative — Full Aesthetic Breakdown for Lightroom Presets

## Executive Summary

Classic Negative is Fujifilm's digital emulation of **consumer-grade Fujicolor Superia negative film**, designed to reproduce the look of developed prints from the 1990s and early 2000s. It is characterized by a **very muted palette**, **cyan-green shifted shadows**, **magenta-biased highlights**, and **hard contrast**. The aesthetic is deliberately "unbalanced" — warm midtones with a cool overall cast — creating a nostalgic, lo-fi character that evokes family photo albums and one-hour photo lab prints. This document serves as a reference for creating a Lightroom preset that emulates Classic Negative.

---

## 1. Overall Color Palette

### Primary Characteristics:
- **Very muted, lower saturation than Classic Chrome** (approximately 25-35% less saturation on reds/yellows)
- **Warm midtones but cool overall balance** — the warmth in the middle tones is offset by the cool shadow bias
- **Desaturated reds and yellows** — the warm colors are intentionally dulled
- **Deep rich greens but muted** — greens have density but lack vibrance
- **Cyan/teal-leaning blues** — skies and blue objects shift toward aqua
- **Magenta-leaning highlights** — bright areas carry a subtle pinkish cast

### The "FujiColor Superia" Identity:
Fuji X Weekly (Ritchie Roesch) has confirmed that Classic Negative is "closely modeled after Fujifilm's Superia line of films." The Superia films were consumer-grade color negative films with Fuji's proprietary 4th Color Layer Technology, designed to produce pleasing prints under a wide range of conditions — particularly the mixed lighting of family snapshots.

---

## 2. Shadow Character — THE DEFINING FEATURE

### Green-Shifted Shadows:
The single most distinctive characteristic of Classic Negative is the **cyan-green bias in shadow areas**. This comes from:

1. **Dye cross-talk in consumer negative film:** When consumer film sits in a camera for extended periods (common for family cameras), the different color dye layers interact chemically, producing a color cast. The cyan-forming layer and yellow-forming layer interaction produces a greenish shadow bias.

2. **Color contrast with highlights:** The green shadows are complemented by magenta highlights (complementary colors), creating the "color contrast" Fuji describes.

### What This Means Practically:
- **Black objects will have a subtle green/cyan tint**
- **Dark areas of images feel cooler than midtones**
- **Shadow detail is retained but colored**
- **This is NOT simply a global white balance shift** — it affects only the shadow tonal range

### Lightroom Implementation Note:
This cannot be achieved with just the Temperature/Tint sliders. It requires:
- **Split toning:** Green/cyan cast added to shadows via the Color Grading panel
- **Tone curve:** Per-channel curves (particularly blue channel lift in shadows)
- **Calibration panel:** Blue primary shift toward cyan

---

## 3. Highlight Character

### Magenta-Highlight Bias:
Highlights have a subtle **magenta/pinkish cast**. This is the complementary partner to the green shadows. Consumer negative film's highlight areas naturally developed this warm-pink quality.

### Highlight Hardness:
Unlike Classic Chrome's soft highlight roll-off, Classic Negative maintains harder highlight transitions. Overexposed areas don't gracefully bloom — they hit a harder ceiling. This contributes to the "hard contrast" description.

### Practical Effect:
- White objects in sun look slightly warm/pink
- Sky highlights carry a subtle warmth
- Flash-lit subjects have a warmer highlight quality

---

## 4. Midtone Character

### Warm Midtones:
Despite the overall cool shadow bias, midtones actually carry **warmth**. This creates the "unbalanced" feel Fuji describes — midtones feel warm while shadows feel cool.

### Colorful Midtones:
Fuji specifically states Classic Negative is "colorful even in the midtones." This means:
- Midtone saturation is maintained even while overall saturation is low
- There's tonal separation in the mid-range that gives colors presence
- Not flat — there's micro-contrast in midtones

---

## 5. Key Color Channel Behaviors

### Reds → Orange
- Reds are significantly desaturated
- Hue shifts from true red toward orange-red
- Red objects (stop signs, red clothing, red flowers) appear more muted and warm
- In some recipes, reds can appear almost brown
- **HSL in Lightroom:** Red hue +15 to +25, Red saturation -15 to -30

### Yellows → Desaturated Warm
- Yellows lose significant saturation
- They maintain warmth but become duller
- Golden hour light becomes more amber than bright gold
- **HSL in Lightroom:** Yellow saturation -20 to -35, Yellow hue 0 to +10

### Greens → Deep, Rich, Muted
- Greens have depth and density but lack vibrance
- Shift slightly toward yellow-green
- Foliage looks like 90s vacation photos — dark green, substantial but not "punchy"
- **HSL in Lightroom:** Green hue +10 to +20, Green saturation -10 to -20, Green luminance -5 to -15

### Blues → Cyan/Teal
- Blues shift cooler toward cyan
- Sky blues become more aqua
- This ties into the overall green shadow cast
- **HSL in Lightroom:** Blue hue -10 to -20, Blue saturation -5 to -15

### Aquas → Cyan
- Aquas become more distinctly cyan
- Important for the shadow color bias
- **HSL in Lightroom:** Aqua hue +5 to +15, Aqua saturation -10 to -20

### Skin Tones → Warm Amber
- Skin tones get a warm, slightly amber cast
- Not unflattering but noticeably warm
- Shadow skin tones pick up the green bias, creating a complex look
- Reggie's Superia was specifically designed to handle diverse skin tones well

---

## 6. Tone Curve Characteristics

### Overall Shape: Hard S-Curve

```
Highlights: Hard shoulder (minimal roll-off)
    |
Midtones: Steep transition (high midtone contrast)
    |
Shadows: Deep crush with green color bias
```

### Specifics:
- **Black point:** Lowered (deeper blacks) — not lifted like Classic Chrome
- **Shadow transition:** Rapid descent into shadows
- **Midtone contrast:** Elevated — separation in the mid-gray range
- **Highlight transition:** Harder/shorter roll-off than Classic Chrome
- **White point:** Maintained but with magenta tint

### Compared to Classic Chrome:
Classic Negative has a steeper S-curve throughout. Everything is more contrasty. Classic Chrome's defining feature is its soft highlight shoulder — Classic Negative's defining feature is its hard shadow with green cast.

---

## 7. Exposure Behavior

### Distinctive Exposure-Dependent Look:
Fuji X Weekly notes that Classic Negative's exposure "affects how the pictures are rendered, similar to how Superia film behaves to overexposure and underexposure."

**Underexposure:**
- Cyan-green shadow bias becomes more prominent
- Colors become more muted overall
- Contrast increases
- Shadows become heavier

**Optimal Exposure:**
- Balanced warm midtones with cool shadow character
- Colors have presence despite being muted

**Overexposure:**
- Pastel quality emerges
- Magenta highlight bias strengthens
- Colors become lighter/airier
- Some recipes recommend +2/3 to +1 exposure compensation

---

## 8. The 90s Japanese Documentary Aesthetic

### Why Classic Negative Feels Like 90s Documentary:
The specific combination of:
1. **Cyan-green shadows** (common in consumer negative film processing)
2. **Magenta highlights** (complementary color contrast)
3. **Muted reds** (consumer film's weaker red response)
4. **Deep, rich greens** (consumer film's strong green response)
5. **Hard contrast** (point-and-shoot cameras, direct flash)

...creates what the photographic community calls the "90s Japanese documentary aesthetic." This is the look of:
- Hiromix's snapshot photography
- 90s Japanese street fashion magazines
- Daido Moriyama's color work
- Family vacation photos from the era

### Why It's Different from 90s American Snapshot Aesthetic:
The Japanese/Western consumer film look differed slightly:
- **Japanese (Fuji Superia):** More green shadow bias, cooler overall, cyan cast
- **American (Kodak Gold):** More yellow warmth, golden highlights, warmer overall

Classic Negative specifically captures the **Japanese/Fuji interpretation** of consumer film.

---

## 9. Grain Behavior

Classic Negative is specifically noted by Fuji as working "well with grain." The film simulation was designed with grain in mind because:

- Consumer negative film inherently had more grain than professional film
- 90s point-and-shoot cameras with small apertures and fast film produced visible grain
- Disposable camera aesthetics include noticeable grain

### In-Camera:
Most community recipes use **Strong, Large** grain settings. This contributes to the lo-fi, analog character.

### In Lightroom:
Grain settings should be:
- **Amount:** 25-45 (moderate to heavy)
- **Size:** 35-50 (larger grain for analog feel)
- **Roughness:** 50-70 (visible texture)

---

## 10. Lightroom Emulation Strategy

### Summary of Key Adjustments Needed:

| Panel | Adjustment | Purpose |
|---|---|---|
| **Basic** | Contrast +10 to +20 | Harder contrast than neutral |
| **Basic** | Highlights -10 to -30 | Prevent clipping, control magenta highlight |
| **Basic** | Shadows +10 to +20 | Lift shadows slightly while keeping green cast |
| **Tone Curve** | S-curve with harder shoulders | Hard contrast character |
| **HSL / Red** | Hue +15 to +25, Sat -15 to -30 | Red → Orange, desaturated |
| **HSL / Orange** | Sat -5 to -15 | Mute skin warmth slightly |
| **HSL / Yellow** | Sat -20 to -35 | Significant yellow desaturation |
| **HSL / Green** | Hue +10 to +20, Sat -10 to -20, Lum -5 to -15 | Deepen and mute greens |
| **HSL / Aqua** | Hue +5 to +15, Sat -10 to -20 | Cyan shift |
| **HSL / Blue** | Hue -10 to -20, Sat -5 to -15 | Blue → Cyan shift |
| **Color Grading → Shadows** | Hue: 140-180 (green/cyan), Sat: 10-20 | THE KEY ADJUSTMENT — green shadow cast |
| **Color Grading → Highlights** | Hue: 320-340 (magenta), Sat: 5-10 | Subtle magenta highlight |
| **Calibration → Red Primary** | Hue +10, Sat -10 | Warm shift, less red saturation |
| **Calibration → Green Primary** | Hue +10 to +15, Sat -10 | Green toward yellow-green |
| **Calibration → Blue Primary** | Hue -10 to -20, Sat -5 to -10 | Blue toward cyan, less saturation |
| **Effects → Grain** | Amount 30-45, Size 35-50, Roughness 50-70 | Analog grain |
| **WB** | Slightly warm (5500-6000K), Tint -5 to -10 (green) | Warm-green base |

### Critical Adjustments (non-negotiable for the look):
1. **Green/cyan shadow cast** (Color Grading shadows or calibration)
2. **Red → Orange hue shift + heavy red desaturation**
3. **Yellow desaturation** (major contributor to the muted palette)
4. **Blue → Cyan shift**
5. **Harder contrast S-curve**
6. **Heavy grain**

### Optional Enhancements:
- Negative Clarity (-10 to -20) for lo-fi softness
- Slight vignette for consumer camera feel
- Negative Dehaze (-5 to -10) for atmosphere

---

## 11. Reference Look Description

When you look at a Classic Negative image, you should see:

- Shadows that are not black but **dark green/cyan**
- Highlights that are not pure white but slightly **warm pink**
- Reds that look **orange-brownish** and muted
- Skies that are **teal/aqua** instead of pure blue
- Greens that are **dark, rich, olive-leaning**
- Overall palette that feels **subdued but colorful**, not gray/monochrome
- A **nostalgic**, slightly melancholic feel
- The texture of **analog grain**
- A look that says "this could be a print from 1997"

---

## 12. Sources & References

1. **Fujifilm Official:** https://fujifilm-x.com/global/products/film-simulation/classic-neg/
2. **Fuji X Weekly (Ritchie Roesch):** https://fujixweekly.com/
3. **Fuji X Weekly - 90s Film Look:** https://fujixweekly.com/2023/07/19/getting-that-90s-film-look-with-fujifilm-cameras/
4. **Fuji X Weekly - Favorite Classic Neg Recipes:** https://fujixweekly.com/2024/03/20/my-15-favorite-film-simulation-recipes-that-use-classic-negative/
5. **Fuji X Weekly - Classic Neg Everyday:** https://fujixweekly.com/2025/02/24/classic-negative-is-perfect-for-everyday-moments-and-vacation-snapshots/
6. **Reddit r/fujifilm - Classic Cuban Negative Recipe:** https://old.reddit.com/r/fujifilm/comments/1c4j7ut/
7. **Reddit r/Lumix - Lightroom Recreation:** https://old.reddit.com/r/Lumix/comments/1d0p8f8/
8. **Fuji X Weekly - Reggie's Superia:** https://fujixweekly.com/2026/03/12/reggies-superia-a-fujifilm-recipe-for-x-trans-iv-v-cameras/
9. **Fuji X Weekly - Classic Amber:** https://fujixweekly.com/2025/11/01/classic-amber-fujifilm-x-t5-x-trans-v-film-simulation-recipe/

---

## See Also

For related Lightroom presets and film stock references:

- [Fujifilm Classic Chrome](../Fujifilm-Classic-Chrome/characteristics.md)
- [Fujifilm Pro 400H](../Fujifilm-Pro-400H/characteristics.md)
- [Fujifilm Nostalgic Negative](../Fujifilm-Nostalgic-Negative/characteristics.md)
- [Fuji Superia XTRA 400](../Fuji-Superia-XTRA-400/characteristics.md)
