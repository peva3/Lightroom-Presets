# Bleach Bypass — Chemical Process Datasheet

## Overview

**Bleach bypass** (also known as **skip bleach**, **silver retention**, or in Japanese: **銀残し / gin-nokoshi**) is a photochemical film processing technique where the bleaching stage is partially or fully omitted during color film development. This causes metallic silver crystals to be retained in the emulsion alongside the color dye layers, producing a black-and-white image superimposed on the color image.

**First use:** *Her Brother* (1960), directed by Kon Ichikawa, cinematography by Kazuo Miyagawa (a former chemist who invented the process). Miyagawa was inspired by Oswald Morris's dye-transfer Technicolor work on John Huston's *Moby-Dick* (1956).

**Western rediscovery:** Roger Deakins's use on all release prints for *Nineteen Eighty-Four* (1984).

---

## Standard Color Film Processing (ECN-2 / FCP)

Normal color negative (ECN-2) or color print (FCP) development follows this sequence:

```
1. Color Developer (CD-3 for ECN-2, CD-4 for C-41)
   → Forms color dye clouds + metallic silver image
2. Stop Bath
   → Halts development
3. Wash
4. Bleach (Ferricyanide or persulfate)
   → Converts metallic silver back to silver halide
5. Wash
6. Fixer
   → Removes all silver halide, leaving only color dyes
7. Final Wash
8. Stabilizer
```

The bleach step converts metallic silver (the black-and-white latent image) into silver halide, which is then dissolved away by the fixer. In normal processing, **no silver remains in the final image** — only the color dye clouds.

---

## Bleach Bypass Process

In bleach bypass, the bleach step is **skipped entirely** or **greatly shortened**:

```
1. Color Developer
2. Stop Bath
3. Wash
4. [BLEACH — SKIPPED]
5. Fixer
   → Removes undeveloped silver halide only
6. Final Wash
```

The key chemical consequence: **metallic silver that formed the image during color development is never removed.** It remains embedded in all three emulsion layers alongside the cyan, magenta, and yellow dye clouds.

---

## What Happens Physically in the Emulsion

### In normal processing:
- Color developer reduces exposed silver halide grains to metallic silver
- Couplers in each layer form cyan, magenta, and yellow dyes at the development sites
- Bleach rehalogenizes the metallic silver → fixer removes it
- **Result:** pure dye image

### In bleach bypass:
- The metallic silver is **never rehalogenized and never removed**
- Each dye layer retains its silver image
- The silver adds **density proportionally to exposure** (more in highlights, less in shadows)
- **Result:** dye image + silver image superimposed

This effectively creates a **black-and-white silver image overlaid on the color dye image**, producing:

| Property | Effect |
|----------|--------|
| **Contrast** | Dramatically increased (silver adds density to midtones and highlights) |
| **Blacks** | Deeper, richer (silver density in shadows) |
| **Saturation** | Severely reduced (the neutral-density silver "grays out" the color dyes) |
| **Grain** | Amplified (silver grain is retained alongside dye clouds) |
| **Exposure latitude** | Reduced (highlights blow out faster, shadows crush faster) |
| **Sharpness** | Apparent increase (silver edge contrast) |

---

## Where Bleach Bypass Can Be Applied

The effect varies significantly depending on **which generation** it's applied to:

### 1. On Camera Original Negative (OCN)
- **Effect:** Hotter highlights, more grain (camera negative has large silver grains)
- **Used by:** Janusz Kamiński on *Minority Report* (high-speed Fuji negative)
- Roger Deakins on *Jarhead*, *The Assassination of Jesse James* (partial skip-bleach on negative, then DI)
- **Risk:** No protection element exists — the look is "baked in"

### 2. On Interpositive (IP) / Intermediate
- **Effect:** Moderate contrast increase, moderate grain
- **Lower risk** — original negative is unaltered

### 3. On Internegative (IN)
- **Effect:** Moderate contrast increase, finer grain (internegative stock has very low ASA / fine grain)
- **Most common for theatrical release** — cost-effective, insurance-friendly

### 4. On Release Print (FCP)
- **Effect:** Deepest blacks, finest grain (print stock has smallest silver grains)
- **Maximum impact on blacks and shadow density**
- **Expensive** — applied to every single print

---

## Proprietary Variants (Controlled Silver Retention)

Full skip bleach can be too extreme. Labs developed partial / controlled processes:

### Technicolor ENR (Erhöhte Normalentwicklung / "Enhanced Normal Development")
- **NOT** simply a shortened bleach time
- Adds **extra B&W developer tanks** in the FCP line between bleach and fix
- After bleach rehalogenizes the silver, a black-and-white positive developer (D97) redevelops a controlled percentage back to metallic silver
- **Controlled via IR densitometer reading:** ENR level (e.g., ENR 50, ENR 100)
- Maximum ENR (~100 IR) is roughly **half** the strength of full skip bleach (~230 IR)
- **Used on:** *Seven* (Darius Khondji), *War of the Worlds* (Spielberg/Kamiński)

### Technicolor OZ Process
- Proprietary variant; details are trade secrets
- Named after *The Wizard of Oz*

### Deluxe ACE (Adjustable Contrast Enhancement)
- Similar to ENR — partial silver redevelopment
- Used a separate B&W developer bath

### Deluxe CCE (Custom Contrast Enhancement)
- Another Deluxe proprietary variant
- Relationship to ACE not publicly documented

### Partial Skip Bleach (Shortened Bleach Time)
- Film runs through only a fraction of normal bleach racks (e.g., ~1/5 of normal bleach time)
- According to Kodak: **95% of bleaching occurs in the first 30 seconds**
- Partial bleach bypass on camera negative is extremely difficult to control
- Requires extensive testing per batch; no set AIM density
- **Practical only on print stock (ECP)** with slower-acting bleaches

---

## Visual Results by Processing Stage

From David Mullen ASC (cinematography.com, May 2025):

> "Skip bleach on a negative makes the highlights hotter rather than the shadows darker, and it adds a lot more grain because camera negative silver grains are larger than the silver grains in intermediate and print stock, which are very low ASA."

| Stage | Highlights | Shadows | Grain | Blacks |
|-------|-----------|---------|-------|--------|
| Camera Negative | **Blown out** | Moderate crush | **Heaviest grain** | Moderate |
| Interpositive/Internegative | Moderate | Moderate | Fine grain | Deep |
| Release Print | Controlled | **Deepest blacks** | Finest grain | **Maximum** |

---

## Key Chemical Details

### Bleach Chemistry
- Traditional: Potassium ferricyanide (Farmer's Reducer principle)
- Modern ECN-2: Ammonium persulfate with accelerators
- ECN-2 bleach is **highly active** — very fast rehalogenization
- Makes partial bleach bypass extremely difficult on negative

### Fixer
- Removes undeveloped silver halide only
- Does NOT remove metallic silver (that's the bleach's job)
- In bleach bypass, the fixer leaves metallic silver intact

### Silver Grain Size Hierarchy
1. **Camera negative** (largest grains, ~ASA 50–500)
2. **Intermediate stock** (very fine grain, ~ASA <1)
3. **Print stock** (finest grain, ~ASA <1)

---

## AHU Layer and Modern Stocks (2025+)

Kodak's newer Vision3 stocks are replacing the traditional remjet backing with an **AHU (Anti-Halation Undercoat)** layer that:

- Contains silver that is normally converted in bleach and washed off in fix
- In bleach bypass, the AHU silver is **also retained**
- May interfere with proper scanning of the negative
- Makes traditional bleach bypass on new ECN-2 stocks "tricky" if not pointless

---

## Exposure Compensation

When shooting for bleach bypass:

| Processing Stage | Recommended Compensation |
|------------------|-------------------------|
| Camera negative bleach bypass | **Overexpose by 1 stop** (rate 500T at 250 EI) to keep midpoint |
| Internegative bleach bypass | Same — +1 stop to compensate for silver density |
| Print bleach bypass | No camera compensation needed (adjusted in printing) |

---

## Sources

- Wikipedia: Bleach bypass
- David Mullen ASC, cinematography.com forum threads (May 2025, July 2022)
- Robert Houllahan (Cinelab), cinematography.com (July 2022)
- Ludwig Hagelstein, cinematography.com (July 2022)
- ASC "Soup du Jour: Bleach Bypass" (November 1998)
- Alexis Van Hurkman, *Color Correction Look Book* (Peachpit Press, 2013), Chapter 2
