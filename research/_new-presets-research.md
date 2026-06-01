# New Presets Research — Wayback Machine Findings
## Date: 2026-06-01

---

## SOURCES SEARCHED

| Source | Method | Status |
|--------|--------|--------|
| old.reddit.com/r/Lightroom | Wayback CDX + snapshot | BLOCKED — robots.txt |
| old.reddit.com/r/postprocessing | Wayback CDX + snapshot | BLOCKED — robots.txt |
| old.reddit.com/r/analog | Wayback CDX + snapshot | BLOCKED — robots.txt |
| fredmiranda.com/forum | Wayback CDX | NO RESULTS |
| photrio.com/forum | Wayback CDX | NO RESULTS |
| dpreview.com/forums | Wayback CDX | NO RESULTS |
| **fujixweekly.com** | Wayback CDX + snapshot | **SUCCESS — recipes found** |
| Broad web (* wildcard) | Wayback CDX | 403 — rate limited |

Reddit's robots.txt blocks Wayback Machine from archiving /comments/* and /search pages, so Reddit sources are unavailable. Photography forums returned no matching CDX entries for these film stocks. Fuji X Weekly was the only productive source.

---

## B&W FILM STOCKS — FINDINGS

### 1. Ilford Pan F Plus 50 — FOUND!

**Source:** Fuji X Weekly (archived 2024-01-03)
**URL:** https://web.archive.org/web/20240103165333/https://fujixweekly.com/2022/01/02/fujifilm-x100v-film-simulation-recipe-ilford-pan-f-plus-50/
**Author:** Anders Lindborg, modified by Ritchie Roesch
**Camera base:** Fujifilm X-Trans IV (X100V)

**Fuji camera recipe:**
```
Monochrome (standard, no filter)
Dynamic Range: DR100
Highlight: 0
Shadow: +1
Noise Reduction: -4
Sharpening: 0
Clarity: +2
Grain Effect: Weak, Large
Color Chrome Effect: Off
Color Chrome Effect Blue: Off
White Balance: Daylight, +1 Red & -6 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: -1/3 to +1/3 (typically)
```

**Anders' original version:** Shadow +2, Clarity 0, Sharpness +1, NR -3

**Characteristics noted:**
- Low-ISO, contrasty, sharp, detailed, fine-grain B&W negative
- WB shift used to model spectral sensitivity bump
- "Really soft light recommended for portraits"
- "High contrast with a really classic black and white look, emphasis on the black"
- Good in controlled lighting/studio

**Lightroom translation notes:**
- Set Treatment to Monochrome
- Sharpness should be LOW (≤10) since grain is active
- Contrast: high shadows + clarity for punch
- WB shift on B&W affects grey rendering of specific colors — since this is monochrome in LR, this translates to the B&W mix

---

### 2. Ilford Delta (Push-Process / 3200) — FOUND!

**Source:** Fuji X Weekly (archived 2023-09-29)
**URL:** https://web.archive.org/web/20230929073610/https://fujixweekly.com/2020/04/24/not-my-fujifilm-x-t30-ilford-delta-push-process-film-simulation-recipe/
**Author:** K. Adam Christensen + Ritchie Roesch
**Camera base:** Fujifilm X-Trans III (X-T30)

**Fuji camera recipe:**
```
Monochrome (+Y, +R, +G)
Dynamic Range: DR400
Highlight: 0
Shadow: +3
Grain: Strong
Color Chrome Effect: Off
Toning: 0
Sharpening: -3
Noise Reduction: -4
ISO: 12800 (can go down to 3200)
Exposure Compensation: +1/3 to +2/3 (typically)
```

**Characteristics noted:**
- Delta 3200 is actually ISO 1000 with "built-in" push-processing
- Without Large grain (X-T30 limitation), resembles Delta 400 pushed ~1.5 stops
- Extremely high ISO recipe — very grainy, contrasty
- Monochrome filters: Yellow + Red + Green (boosted sensitivity across spectrum)

**Lightroom translation notes:**
- Massive grain, very high contrast
- Shadow +3 = very crushed blacks
- The Y+R+G filter stack means broad spectral sensitivity (less filtering)
- Low Sharpness, low NR

---

### 3. Ilford HP5 Plus 400 — FOUND! (reference)

**Source:** Fuji X Weekly (archived 2023-12-06)
**URL:** https://web.archive.org/web/20231206072405/https://fujixweekly.com/2018/12/01/my-fujifilm-x100f-ilford-hp5-plus-film-simulation-recipe/
**Camera base:** Fujifilm X-Trans III (X100F)

**Fuji camera recipe:**
```
Acros (Acros+Y, Acros+R, Acros+G)
Dynamic Range: DR200
Highlight: +4
Shadow: +2
Noise Reduction: -3
Sharpening: 0
Grain Effect: Strong
ISO: Auto up to ISO 6400
Exposure Compensation: 0 (typically)
```

**Characteristics:**
- HP5 vs Delta 400: HP5 has a hair less contrast, more exposure latitude, more forgiving
- Highlight +4 to prevent clipping
- Acros has built-in grain that increases with ISO

**FP4 inference from HP5:** FP4 Plus 125 would be finer grain, lower base ISO, perhaps slightly more contrast than HP5. Reduce grain to Weak, baseline contrast slightly higher.

---

### 4. Ilford Delta 100 — NOT FOUND (extrapolation available)

No direct recipe on Fuji X Weekly. The Delta Push-Process recipe exists for 3200. Delta 100 would be:
- Much finer grain than Delta 3200
- High sharpness, high contrast (tabular-grain film)
- Baseline: between Pan F (finer grain) and HP5 (more grain)
- From the HP5 article: Ritchie notes "Ilford Delta 100 was my go-to for fine-grain"

**Extrapolation approach:** Start from HP5 recipe, reduce grain, increase contrast slightly, sharpen more. Pan F recipe is closest starting point but Pan F has more contrast.

---

### 5. Ilford FP4 Plus 125 — NOT FOUND

No recipe on Fuji X Weekly. FP4 is a traditional-grain (non-tabular) 125 ISO film with:
- Moderate contrast, fine grain for traditional emulsion
- Wide exposure latitude
- Classic mid-century look

**Extrapolation approach:** Similar grain to Pan F but lower contrast. Start from HP5 recipe, reduce ISO, moderate contrast.

---

### 6. Kodak Double-X 5222 — NOT FOUND

No recipe on Fuji X Weekly. Eastman Double-X is a cinema B&W negative film (ISO 250 daylight, 200 tungsten) used in classic Hollywood films like Schindler's List, Casino Royale. Characteristics:
- Classic cubic-grain structure
- Rich midtones, moderate contrast
- Somewhat gritty grain structure (not modern tabular-grain smooth)
- Excellent latitude

---

### 7. Fomapan 100/200/400 — NOT FOUND

No recipes on Fuji X Weekly. Fomapan is a Czech traditional-grain B&W film family:
- Fomapan 100: Classic look, moderate contrast, traditional grain
- Fomapan 200: More versatile, good tonal range
- Fomapan 400: Higher grain, slightly muddy shadows
- Known for "retro" rendering and strong grain character

---

### 8. Fuji Neopan 400 — NOT FOUND

Fuji X Weekly has a Neopan Acros rumor post but NO Neopan 400 recipe. Neopan 400 (discontinued) was a cubic-grain B&W film:
- Fine grain for 400 speed
- Good sharpness with wide tonal range
- Slightly softer contrast than Tri-X
- Popular for street photography in Japan

The Neopan Acros recipes exist on FWX (Acros is the successor).

---

## COLOR FILM STOCKS — FINDINGS

### 9. Fujicolor Pro 160NS — FOUND! (7 recipes)

**Source:** Fuji X Weekly (archived 2023-09-29)
**URL:** https://web.archive.org/web/20230929170824/https://fujixweekly.com/2021/05/24/a-different-approach-7-new-fujicolor-pro-160ns-film-simulation-recipes-yes-7/
**Author:** Anders Lindborg
**Camera base:** Fujifilm X-Trans III (X-T3)

**Box Speed recipe:**
```
PRO Neg. Hi
Dynamic Range: DR400
Highlight: 0
Shadow: 0
Color: 0
Color Chrome Effect: Off
Grain: Weak
Noise Reduction: -4
Sharpness: -3
White Balance: Daylight, 0 Red & 0 Blue
ISO: Auto up to ISO 6400
Exposure Compensation: 0 to +2/3 (typically)
```

**Pull/Push variants:**
| Variant | HL | SH | Color | Sharp | Notes |
|---------|-----|-----|-------|-------|-------|
| Pulled -2 | -2 | -1 | -1 | -3 | Bright sun |
| Pulled -1 | -1 | -1 | 0 | -3 | Sun |
| Box Speed | 0 | 0 | 0 | -3 | Normal |
| Pushed +1 | +1 | 0 | 0 | -3 | Some shade |
| Pushed +2 | +2 | 0 | +1 | -3 | Shade/clouds |
| Pushed +3 | +2 | +1 | +2 | -3 | Dull |
| Pushed +4 | +3 | +2 | +3 | -4 | Very dull |

**Characteristics:**
- Professional color negative film (successor to NPS 160)
- Very natural skin tones, modest saturation
- Wide exposure latitude
- Designed for portrait and wedding work
- The push/pull approach emulates film's exposure flexibility

**Lightroom translation notes:**
- Base recipe is very neutral — this film is about subtlety
- PRO Neg. Hi = Neutral color profile in LR terms
- DR400 = lifted shadows, compressed highlights (Tone Curve)
- The push/pull system is about adapting contrast to lighting conditions

---

### 10. Fujicolor Superia 100 — FOUND!

**Source:** Fuji X Weekly (archived 2024-03-15)
**URL:** https://web.archive.org/web/20240315041451/https://fujixweekly.com/2020/06/09/fujifilm-x100v-film-simulation-recipe-fujicolor-superia-100/
**Camera base:** Fujifilm X-Trans IV (X100V)

**Fuji camera recipe:**
```
Classic Negative
Dynamic Range: DR-Auto
Highlight: -1
Shadow: -2
Color: +1
Noise Reduction: -4
Sharpening: -2
Clarity: -2
Grain Effect: Weak, Small
Color Chrome Effect: Strong
Color Chrome Effect Blue: Weak
White Balance: Daylight, 0 Red & -1 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: +1/3 to +2/3 (typically)
```

**Characteristics:**
- Consumer-grade color negative (1998-2009)
- Replaced Super G Plus 100
- "Family snapshot" nostalgic aesthetic
- Low contrast, but not too low — good all-rounder
- The new Classic Negative film simulation is modeled directly on Superia
- Classic Neg has a distinctive color palette shift

**Lightroom translation notes:**
- Classic Negative is Fujifilm's built-in Superia emulation
- Low contrast (HL -1, SH -2), slight clarity reduction softens
- CCE:Strong = enhanced red/green saturation in highlights
- CCEB:Weak = slight blue desaturation in highlights
- This is essentially what "Classic Negative" on Fuji cameras does

---

### 11. Lomography Color 100 — FOUND! (aka Kodak Pro Image 100 / Gold 100)

**Source:** Fuji X Weekly (archived 2023-06-06)
**URL:** https://web.archive.org/web/20230606124942/https://fujixweekly.com/2019/10/31/my-fujifilm-x-t30-lomography-color-100-film-simulation-setting/
**Camera base:** Fujifilm X-Trans III (X-T30)

**Fuji camera recipe:**
```
Velvia
Dynamic Range: DR400
Highlight: +1
Shadow: +1
Color: -3
Noise Reduction: -4
Sharpening: +1
Grain Effect: Weak
Color Chrome Effect: Weak
White Balance: Cloudy/Shade, -3 Red & +7 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: +1/3 to +2/3
```

**CRITICAL FINDING:** The article explicitly states Lomography Color 100 is **rebadged Kodak Gold 100 and/or Kodak Pro Image 100** (and possibly Ektar 100). So this recipe gives us Pro Image 100 and ColorPlus 200 (Gold 100/200 family) base values!

**Characteristics:**
- Lomography Color 100 uses Velvia as base (NOT Classic Neg)
- Heavy WB shift: Cloudy/Shade with -3R +7B (warm + blue)
- Very desaturated (-3 Color on already-saturated Velvia = normal-ish)
- CCE:Weak boosts red tones modestly
- Hi-Fi low-fi hybrid aesthetic

**Lightroom translation notes:**
- This recipe effectively gives us Pro Image 100 base values
- Velvia + Color -3 = moderate saturation
- The Cloudy WB + color shift is the defining character
- Gold 200 / ColorPlus 200 would use similar WB + CCE settings with different base

---

### 12. Kodak ColorPlus 200 — NOT FOUND DIRECTLY (extrapolation available)

No direct recipe on Fuji X Weekly. ColorPlus 200 is Kodak's budget consumer color negative:
- Warm cast, moderate contrast, moderate saturation
- Very similar to Gold 200 family
- Based on Lomography Color 100 = Gold 100/Pro Image 100 family

**Extrapolation approach:** Start from Superia 100 base with warmer WB shift, slightly higher contrast. Or use Lomography Color 100 recipe as starting point with adjustments for 200 speed (more grain, slightly different color).

---

### 13. Kodak Pro Image 100 — EXTRAPOLATION from Lomography Color 100

Pro Image 100 is rebadged as Lomography Color 100. See finding #11 above.
- Designed for tropical/warm climates
- Natural skin tones, moderate contrast
- Consumer-grade but consistent results

---

### 14. CineStill 50D — NOT FOUND (800T found, extrapolation available)

Fuji X Weekly has CineStill 800T recipes but NOT 50D. 50D characteristics:
- Kodak Vision3 50D cinema film with remjet removed
- ISO 50 daylight-balanced
- Extremely fine grain, wide dynamic range
- Natural colors with slight warmth
- Halation effects in highlights (cinestill signature)
- Much lower contrast than 800T, finer grain

**Extrapolation approach:** CineStill 800T recipe adjusted for daylight balance, reduced grain, lower ISO, different WB. The CineStill 800T recipes are on FWX.

---

### 15. Lomography Metropolis — NOT FOUND

No recipe on Fuji X Weekly. Metropolis characteristics:
- Desaturated, high-contrast color negative (ISO 100-400)
- Muted greens, strong blues, muted skin tones
- Urban/gritty aesthetic
- A comment on the Lomography Color 100 post (from Nicolas, Nov 2019) links to DPReview sample gallery

**Extrapolation approach:** Desaturate globally, boost contrast, cool WB, selective desaturation of greens and skin tones.

---

### 16. Lomography Turquoise — NOT FOUND

No recipe on Fuji X Weekly. LomoChrome Turquoise characteristics:
- Extreme color shift film — blues become turquoise, reds become deeper
- Very saturated, otherworldly color palette
- Contrasty with crushed blacks
- ISO 100-400

---

## ADDITIONAL REFERENCE RECIPES FOUND (for contextual values)

### Fujicolor Superia 800 (X-Trans III)
URL: fujixweekly.com/2018/02/03/my-fujifilm-x100f-fujicolor-superia-800-film-simulation-recipe-pro-neg-std/
(Not fetched — present in CDX for reference)

### Kodak Ektar 100 (X-Trans III)
URL: fujixweekly.com/2018/06/16/my-fujifilm-x100f-kodak-ektar-100-film-simulation-recipe/
(Not fetched — already in collection)

### Fujifilm Acros (X-Trans III)
URL: fujixweekly.com/2017/08/27/my-fujifilm-x100f-acros-film-simulation-recipe/
(Not fetched — already in collection)

---

## SUMMARY TABLE

| Film Stock | Status | Closest Recipe Available | Viable? |
|-----------|--------|-------------------------|---------|
| Ilford Delta 100 | NOT FOUND | Delta Push-Process + HP5 extrapolation | Yes — extrapolate |
| Ilford FP4 Plus 125 | NOT FOUND | HP5 recipe adjusted for 125 | Yes — extrapolate |
| **Ilford Pan F Plus 50** | **FOUND** | FWX direct recipe | **YES** |
| Fomapan 100/200/400 | NOT FOUND | HP5/Delta recipes + Czech grain profile | Weak |
| Kodak Double-X 5222 | NOT FOUND | HP5 + cinema characteristics | Weak |
| Fuji Neopan 400 | NOT FOUND | Acros recipe + Tri-X soft contrast | Yes — extrapolate |
| Kodak ColorPlus 200 | NOT FOUND | Lomography Color 100 family | Yes — family relation |
| **Kodak Pro Image 100** | **EXTRAPOLATED** | Lomography Color 100 = Pro Image 100 | **YES** |
| **Fujicolor Pro 160NS** | **FOUND** | FWX direct recipe (7 variants) | **YES** |
| **Fujifilm Superia 100** | **FOUND** | FWX direct recipe | **YES** |
| CineStill 50D | NOT FOUND | 800T recipe adjusted | Yes — extrapolate |
| Lomography Metropolis | NOT FOUND | None | Weak |
| Lomography Turquoise | NOT FOUND | None | Weak |

---

## KEY OBSERVATIONS FOR LIGHTROOM TRANSLATION

1. **Fuji film simulations map to LR profiles:**
   - Classic Negative → Adobe Color or custom profile
   - PRO Neg. Hi → Adobe Standard/Neutral
   - Velvia → Adobe Vivid
   - Monochrome/Acros → Monochrome treatment

2. **WB shift affects grey rendering in B&W:** Pan F recipe uses +1R/-6B shift in B&W to emulate spectral sensitivity — in LR, use B&W Mix panel instead.

3. **Push/pull system** (Pro 160NS) adapts contrast to light — a useful framework for any film emulation preset.

4. **Grain + Clarity interaction:** When Clarity is used, reduce Sharpness. FWX consistently uses negative Sharpness when Clarity is non-zero.

5. **Lomography Color 100 = Pro Image 100 = Gold 100:** The rebadging finding gives us a reference recipe for the Kodak consumer film family.
