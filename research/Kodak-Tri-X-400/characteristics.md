# Kodak Tri-X 400 — Full Aesthetic Breakdown for Lightroom Presets

> The undisputed king of photojournalism B&W film. Distinctive grain pattern, crisp whites, aggressive mid-tones, legendary push behavior.

---

## Overview & Historical Context

Kodak Tri-X 400 is the most iconic black-and-white film ever made. Introduced in 35mm format in 1954 (and as sheet film in the 1940s), it has been the primary tool of photojournalists, documentary photographers, and street photographers for over 70 years. No other film stock has documented more history. This document serves as a reference for creating a Lightroom preset that emulates Tri X 400.

### Famous Photographers Who Used Tri-X

- **Henri Cartier-Bresson** — The "decisive moment" master
- **Sebastião Salgado** — Epic documentary projects (Workers, Genesis)
- **Daido Moriyama** — Japanese street photography, extreme grain aesthetic
- **Don McCullin** — Vietnam War photojournalism; pushed Tri-X to 1600+ routinely
- **Mary Ellen Mark** — Intimate documentary portraits
- **Bruce Davidson** — East 100th Street, Subway series
- **Garry Winogrand** — American street photography (shot Tri-X exclusively)
- **Josef Koudelka** — Gypsies, Invasion 68 (Prague)
- **Robert Frank** — The Americans (used Tri-X for many images)

---

## The "Woven" Grain Pattern: The Reticulation Controversy (565-point Reddit Thread Analysis)

### The Thread

In May 2024, u/drewsleyshoots posted to r/analog with the title:

> **"[Tri-X] anyone else get this weird 'woven' grain when using Tri-X?"**

This post received **563 points (98% upvoted)** and **33 comments**, making it one of the most-discussed Tri-X technical threads on Reddit.

### The Phenomenon

The OP described Tri-X scans that showed a **directional, cross-hatched "woven" texture** rather than the expected random "salt-and-pepper" grain. They noted: *"Rather than 'grains,' it looks like there's visible lines, almost a woven texture. I never experience this with HP5, or other B&W film stocks I've used."*

### Community Verdict: RETICULATION (Not Grain)

The top comment by u/treatbaby (363 points) identified this as **reticulation** — a physical distortion of the film emulsion caused by **harsh temperature changes during development**:

> *"Reticulation from harsh temperature changes during development."*

### Key Points from the Thread Discussion

1. **Reticulation ≠ Grain:** Reticulation is NOT grain. It is a physical cracking/wrinkling of the gelatin emulsion layer when the film experiences rapid temperature shifts (e.g., cold water stop bath after warm developer).

2. **Tri-X is NOT uniquely susceptible:** u/Jonathan-Reynolds, who tested film types for dev temperature in the 1990s, noted: *"I tested different film types for dev temperature in the nineties and found that Tri-X was no worse than other modern films."*

3. **The lab is often the culprit:** Multiple users reported reticulation from commercial labs using monobath developers (like Cinestill DF96) — these chemicals simplify B&W processing but can cause temperature shock issues.

4. **Monobath risk:** u/om-exe (57 points): *"Could also be that they're using a monobath, much more likely to happen than using one, and for lab black and white dev it can simplify things for them."*

5. **Real Tri-X grain is random, not directional:** Properly developed Tri-X produces a classic "salt-and-pepper" pattern — random, sharp-edged grains with distinct spacing. It should never look woven, crossed, or directional.

6. **User experience:** u/theSweetLou: *"I've gotten this reticulation 'grain pattern' when using Cinestill's DF96 monobath with TriX. I've heard from numerous people you aren't supposed to put TriX into monobath."*

### The Real Tri-X Grain Structure

When properly developed, Tri-X grain is:
- **Random distribution** (not directional/woven)
- **Sharp-edged** (not soft/fuzzy — this is what creates the "bite")
- **Variable size** — grain clumps in mid-tones, finer in highlights/shadows
- **"Salt and pepper"** — the classic description: sharp white and black specks against gray mid-tones
- **More pronounced than HP5+** — HP5 grain is often described as "smoother" or "softer" while Tri-X grain has "bite" or "edge"

---

## Contrast & Tonal Characteristics

### The "Long Toe, Straight Line" Curve

Tri-X's characteristic curve is legendary for its shape:
- **Long toe** (shadow region): Gradual transition from D-min, preserving shadow detail even in deep blacks. This is why Tri-X at box speed still has shadow detail — the toe is gentle.
- **Straight line** (mid-tones through highlights): Nearly linear response through Zones IV–VIII. This creates Tri-X's "honest" mid-tone rendering — no exaggerated compression or expansion.
- **Gentle shoulder** (extreme highlights): Roll-off is gradual, preserving highlight separation. Tri-X can handle 3–5 stops of overexposure without blocking up highlights.

### The "Aggressive Mid-Tones"

Tri-X's signature aesthetic stems from two factors working together:
1. The straight-line portion of the curve is steep (gamma ~0.65-0.80 depending on development) — contrast is "built in" to the mid-tones.
2. The toe and shoulder are gentle, meaning shadows and highlights both have "room" before they clip.

This combination means:
- **Mid-tones "pop"** — faces, textures, and textures at medium brightness have strong local contrast
- **Shadows stay open** — photojournalists could shoot in harsh light and still see detail in the shadows
- **Highlights don't blow out** — skin highlights, bright skies, and light sources retain separation

### Characteristic Zone Behaviors

| Zone | Density | Visual Appearance | Notes |
|------|---------|-------------------|-------|
| Zone I | 0.10–0.12 above D-min | Near-black with just-perceptible detail | Real speed closer to EI 250-320 |
| Zone II | 0.20–0.30 | Dark with visible detail | Shadow texture appears here |
| Zone III | 0.35–0.45 | Detailed shadows | Good texture detail |
| Zone IV | 0.55–0.65 | Dark mid-tones | Start of the "linear" response |
| Zone V | 0.70–0.85 | Middle gray | 18% reflectance point |
| Zone VI | 0.95–1.10 | Light mid-tones | Caucasian skin highlights |
| Zone VII | 1.15–1.30 | Bright with texture | Good highlight detail |
| Zone VIII | 1.35–1.50 | Bright with subtle texture | Approaching shoulder |
| Zone IX | 1.55–1.70 | Near-white with trace detail | Shoulder region |
| Zone X | 1.75+ | Paper white | D-max |

---

## Push Behavior: 800, 1600, 3200, and Beyond

### The "King of Push Processing"

Tri-X earned its reputation as THE pushable film during the Vietnam War era. Photojournalists routinely rated it at EI 800–1600 and pushed development to compensate. The combination of Tri-X + HC-110 + push became the standard for combat photography.

### Push by Stop: Detailed Characteristics

#### EI 800 (+1 Stop)

- **Grain:** Moderate increase. Still refined in 120, clearly visible in 35mm.
- **Contrast:** Moderate boost. Shadows begin to close down slightly.
- **Shadow detail:** Minimal loss. Zone II maintains some texture.
- **Ideal use:** Low-light street photography, overcast days, indoor available light.
- **Developer recommendations:** D-76 (8 min), HC-110 Dil B (6.5 min), XTOL (8.5 min).
- **Look:** "The sweet spot" — many photographers prefer EI 800 as their default Tri-X speed for the contrast boost.

#### EI 1600 (+2 Stops)

- **Grain:** Pronounced and characterful. This is THE classic "pushed Tri-X" look that defined photojournalism.
- **Contrast:** High. Blacks go deep, mid-tones are aggressive.
- **Shadow detail:** Significant loss. Zone II drops to near-black. Zone III becomes the new "textured shadow" zone.
- **Highlights:** Still retain separation thanks to the gentle shoulder.
- **Ideal use:** Night street photography, concerts, indoor available light, action/sports.
- **Developer recommendations:** HC-110 Dil B (9–10 min), Microphen (10–12 min), DD-X (10 min).
- **Look:** "Beautiful, gritty grain. Incredibly sharp — almost too sharp if you're not ready for it. Shadow detail holds surprisingly well. Looks honest. Looks real." (u/Primary_Resolve_2962, r/analog, 2025)

**From the 35mmc Bangkok Chinatown push test (November 2025):**
> *"Tri-X pushed +2 stops by my local lab produces excellent results — similar to what I get from Double-X rated at ISO 800. This is a success."*

#### EI 3200 (+3 Stops)

- **Grain:** Very heavy. Dominates the image texture. Grain becomes the primary aesthetic element.
- **Contrast:** Extremely high. Shadow region compresses dramatically.
- **Shadow detail:** Near-total loss. Zones I–II are completely black. Zone III has minimal texture.
- **Ideal use:** Extreme low light, deliberate aesthetic choice (grain as subject), desperation journalism.
- **Developer recommendations:** HC-110 Dil B (12–14 min), Rodinal 1:25 stand development (60–90 min).
- **Look:** Classic Vietnam War photojournalism aesthetic. Don McCullin's war photography signature look.

#### EI 6400–12800 (+4–5 Stops)

- **Documented on r/analog by u/provia (2019):** Tri-X at 12800 in HC-110 1:64 from syrup, 120 min development. Four inversions every 10 min. "Grain is there. Contrast is, too. But it works."
- **Grain:** Extreme. Image structure begins to break down.
- **Contrast:** Near-graphic. What remains of the image is starkly contrasted.
- **Ideal use:** Experimental. Not recommended for general photography.
- **Note:** This is well beyond Kodak's official recommendations and represents community "what if" experimentation.

---

## Tri-X 400 vs Ilford HP5+ 400 — The Definitive Comparison

These two films are the perennial rivals in the 400-speed B&W space. They are more alike than different, but the differences are meaningful to photographers who care about the "look."

### Side-by-Side Comparison

| Characteristic | Tri-X 400 | HP5+ | Winner |
|----------------|-----------|------|--------|
| **Grain pattern** | Sharp, "salt and pepper," random | Softer, "sandy," more uniform | Depends on taste |
| **Grain visibility** | More visible at all formats | Less visible, blends more | HP5 (if you want smooth) |
| **Shadow detail at box** | Good — real EI ~250-320 | Better — real EI ~320-400 | HP5 |
| **Mid-tone contrast** | High. Aggressive separation. | Lower. Flatter, smoother. | Tri-X (for punch) |
| **Highlight roll-off** | Gentle shoulder, preserves detail | Similar, slightly less forgiving | Tri-X (slightly) |
| **Push to 1600** | Grainy, contrasty, "honest" look | Smoother grain, crushed blacks | Tri-X (character); HP5 (clean) |
| **Skin tone rendering** | Crisp, every line visible | Softer, more flattering | HP5 (portraits); Tri-X (character) |
| **Red sensitivity** | Slightly extended — skin brightens | Standard panchromatic | Tri-X |
| **Film curl (drying)** | Significant — "Kodak curl" | Minimal — dries flat | HP5 |
| **Price (2024–2026)** | ~$10–12/roll (35mm) | ~$7–9/roll (35mm) | HP5 |
| **Archival stability** | Excellent — polyester base (120, 4×5) | Good — acetate base | Tri-X |
| **Push latitude** | Excellent to 1600, usable to 12800 | Excellent to 1600, usable to 6400 | Tie |

### Community Consensus (From Multiple Sources)

**From r/analog comparison by u/Primary_Resolve_2962 (2025):**

> **Tri-X 400 @ 1600:**
> - Beautiful, gritty grain
> - Incredibly sharp — almost too sharp if you're not ready for it
> - Shadow detail holds surprisingly well, even underexposed
> - Looks honest. Looks *real*
> - Renders skin, chrome, and concrete with equal respect
> - This is the go-to stock for high-contrast environments and industrial work

> **HP5+ @ 1600:**
> - Tons of contrast — blacks go straight to black
> - Grain is smoother than Tri-X, but less character-rich
> - Doesn't retain shadow detail as well when pushed
> - However, it's so flattering for portraits, especially for people with fine features or older skin
> - This is an easy shortcut for an old Hollywood look

**From 35mmc (Giacomo Cecot, November 2025):**

> *"Tri-X is a professional choice, considered sharp or very sharp by some, with fine yet pleasing grain and a great response to different light conditions without sacrificing tonal range and contrast."*
>
> *"HP5+ is a more affordable yet excellent value-for-money alternative with very similar characteristics, described by many as a workhorse that is a touch more forgiving than the TX 400, with a classic look and a tad larger grain."*

**Community Comments on 35mmc:**

- **Michael Murray (35mmc comment):** "HP5+ slightly flat at box speed, but love love love it +2 stops. Tri-X +2 is almost unfairly good with how dramatic, gritty, and contrasty it is."
- **Neal Wellons (35mmc comment):** "I like both films equally but shoot HP5+ because it dries flatter and is easier to scan."
- **Nick Orloff (35mmc comment):** "I prefer Tri-X for most subjects but find HP5 better if you need to push to 1600." (dissenting view)
- **Jeffery Luhn (35mmc comment):** "I have not used Tri-X 35mm often for over 45 years. It always seemed too grainy and unsharp for me." (noted that 120/4×5 Tri-X was acceptable)

### The "Character" Distinction

The most commonly cited difference across all communities:

- **Tri-X has "character"** — the grain is identifiable, the contrast curve has personality, the look is distinct. Photographers recognize Tri-X images.
- **HP5 has "versatility"** — smoother, more neutral, flatter at box speed, but capable of extreme contrast when pushed. Easier to bend to different looks, but less inherently distinctive.

---

## Developer Effects on Aesthetics

### D-76 / ID-11 (1:1)
- **The reference standard.** Balanced grain, good acutance, full speed.
- Produces the "classic" Tri-X look known to photojournalists from the 1960s–1980s.
- Grain: moderate and well-defined. Tonal range: full and smooth.
- Tri-X in D-76 1:1 at 6.75–9.75 min defines the "straight" Tri-X look.

### HC-110 (Dilution B)
- **The push developer.** Maximizes acutance (edge sharpness). Slightly lower real speed.
- Grain: sharper-edged, more "bite." Produces pronounced mid-tone contrast.
- The standard for Tri-X at 800–1600. Gives images a "crunchy" quality.
- Dilution H (1:63) used for semi-stand and extreme push development.

### Rodinal (1:50)
- **The grain enthusiast's developer.** Maximum edge effect. Enhanced grain.
- Grain: extremely visible, razor-sharp edges. Acutance: extreme.
- Real speed drops to ~200–250. Compensating development possible.
- r/analog comment: *"Tri-X in Rodinal (for the love of grain)"* — title of a post by u/PhotoGuy91 (2013)
- Not recommended for pushing (already grainy), excellent for structured, graphic compositions.

### XTOL (1:1)
- **The shadow detail developer.** Finest grain among common developers. Full speed to slightly enhanced.
- Produces clean, open shadows with excellent detail. More "modern" look.
- Matthew Bigwood (35mmc comment, 2025): *"I've used Tri-X and developed in Xtol which I think is a great combination."*
- Best for photographers who want Tri-X's contrast curve with finer grain and better shadows.

### Microphen
- **The speed-enhancing push developer.** Gains 1/3 to 2/3 stop real speed.
- Good for pushing to 1600+ while maintaining shadow detail.
- u/Primary_Resolve_2962 (r/analog, 2025) pushed Tri-X to 1600 in Microphen: "Beautiful, gritty grain. Incredibly sharp."

### Diafine (2-Bath)
- **The compensating developer.** Effective speed increase to ~650-800. Low grain for the speed.
- Produces a unique flat-but-detailed look. Works well for high-contrast scenes.
- Popular with street photographers who shoot unpredictably mixed lighting.

---

## Format-Specific Characteristics

### 35mm Tri-X

This is where Tri-X is most iconic and most recognizable. In 35mm:
- Grain is a **primary aesthetic element** — not a flaw
- The "salt-and-pepper" texture is visible even in small prints
- At ISO 400: noticeable but pleasant grain
- At ISO 800: grain becomes prominent
- At ISO 1600: grain dominates and defines the image
- Daido Moriyama's signature look — extreme grain, high contrast, Tri-X at 1600+ in 35mm

**Real-world resolution (35mm, D-76):**
- 50–60 lp/mm (high contrast target)
- About 6–8 megapixels of usable detail (with grain as artistic overlay)

### 120 (Medium Format) Tri-X

Tri-X in medium format is a fundamentally different film experience:
- Grain is **visible but refined** — present for texture but not dominant
- Tonal scale is smoother due to larger negative area
- At 6×6 (Hasselblad): visible grain at 11×14", fine at 8×10"
- At 6×7 (Mamiya/Pentax): grain visible at 16×20", nearly smooth at smaller sizes
- At 6×9: behaves almost like a fine-grain film

### 4×5 (Large Format) Tri-X

In large format, Tri-X is nearly grainless and behaves like a medium-speed film:
- Grain is invisible at normal print sizes
- The characteristic contrast curve is the main "Tri-X signature" — without the grain
- Ideal for contact printing (the original Tri-X format!)

---

## The "Tri-X Is Actually ISO 200" Community Debate

A long-running debate in the analog community revolves around Tri-X's "true" ISO speed.

### The Arguments

**The "Tri-X is ISO 200" camp (including many Zone System practitioners):**
- For full shadow detail (Zone I at 0.10 above D-min), Tri-X needs EI 200–250
- Kodak's published ISO 400 is based on the ISO standard, which allows less shadow detail than many photographers want
- Developing Tri-X at EI 200 and pulling development by 20–30% produces gorgeous, long-scale negatives with full shadow detail

**The "Tri-X is ISO 400" camp:**
- The ISO standard is the ISO standard — Tri-X is a 400-speed film
- At ISO 400 in standard development, shadows are perfectly acceptable for photojournalism/street photography
- Rating at 200 wastes a stop of speed that could get you a sharper, less motion-blurred image

**The "Tri-X is ISO 650–800" camp (Diafine users):**
- In speed-enhancing developers, Tri-X can genuinely achieve 650–800
- Diafine users regularly rate Tri-X at 800

### The Reality

Tri-X's real speed depends heavily on developer and development:
- **D-76 1:1, standard development:** ~EI 250–320 for full shadow detail
- **HC-110 Dil B, standard:** ~EI 250–320
- **XTOL 1:1:** ~EI 400–500
- **Microphen:** ~EI 500–650
- **Diafine:** ~EI 650–800

The debate persists because "Tri-X @ 200" and "Tri-X @ 400" both produce beautiful but different results — neither is "wrong."

---

## The "Tri-X for Portraits" Controversy

Some photographers love Tri-X for portraits; others avoid it.

**Pro-Tri-X for portraits (from community):**
- u/Primary_Resolve_2962 (r/analog, 2025): *"If you're shooting self-portraits, you will see every line in your face. But that's the point — it renders skin, chrome, and concrete with equal respect."*
- Portraits with "honest" rendering — Tri-X doesn't flatter, it documents
- Giacomo Cecot (35mmc, 2025): *"I would use this for portraits where the details matter, where I want to really see the eyes of the subject and possibly the wrinkles of an elderly person."*

**Anti-Tri-X for portraits (from community):**
- Jeffery Luhn (35mmc comment): Called Tri-X 35mm "too grainy and unsharp" even in HC-110 or D-76
- Many prefer HP5+ for portraits due to softer grain and smoother skin rendering
- r/analog post: "Tri-X 400 in HC110 = harsh grain for skin" (u/victorr_sun, 2016)

**The middle ground:**
- Tri-X in 120 format is universally praised for portrait work — grain is refined, tonal scale is beautiful
- Tri-X at EI 200 in XTOL produces smooth skin with rich detail
- The "problem" is primarily 35mm Tri-X at box speed or above, where grain becomes visible on skin

---

## Summary: The Tri-X "Look" in One Paragraph

Kodak Tri-X 400 produces images with **deep, open blacks**, **crisp, slightly warm whites**, and an **aggressive mid-tone contrast** that makes subjects "pop" from the frame. The grain is **random, sharp-edged, and character-rich** — not fine or smooth, but structured and identifiable — appearing as the classic **"salt and pepper" pattern** in mid-tones. When pushed to 1600 or beyond, the grain becomes **dominant, gritty, and dramatic** while surprisingly retaining highlight separation. The spectral sensitivity renders **skin slightly brighter than the eye perceives** (due to extended red sensitivity) and **dramatically darkens blue skies** — making even unfiltered Tri-X skies look dramatic. The film's **long straight-line curve with gentle toe and shoulder** means it handles extreme lighting conditions gracefully — underexposure yields gritty noir, overexposure yields smooth and creamy, and box speed delivers the definitive documentary B&W aesthetic that has defined photojournalism for seven decades. No other film combines this specific set of characteristics so completely: **sharpness with grain, contrast with latitude, honesty with beauty.**

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak T Max 3200](../Kodak-T-Max-3200/characteristics.md)
- [Kodak T Max 400](../Kodak-T-Max-400/characteristics.md)
