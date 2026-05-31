# Cross-Processed E-6 → C-41: Chemical Datasheet

## Process Summary

**Cross-processing (Xpro)** is the deliberate processing of photographic film in a chemical solution intended for a different film type. The most common form is processing **E-6 slide (reversal) film in C-41 color negative chemistry**.

## E-6 vs C-41: Why the Chemistry Matters

### Normal E-6 Processing (3-bath or 6-bath)
1. **First Developer (BW developer)** — reduces exposed silver halide to metallic silver, creating a negative silver image in each layer
2. **Reversal Bath / Fogging** — chemically fogs the remaining unexposed silver halide (or exposes to light in older processes)
3. **Color Developer** — develops the fogged silver halide AND activates dye couplers in each emulsion layer to form cyan, magenta, and yellow dyes
4. **Bleach** — converts all metallic silver back to silver halide
5. **Fixer** — removes all silver halide, leaving only dye images
6. **Final Wash & Stabilizer**

Result: A **positive** (slide) image on transparent base — what you see is what you shot.

### Normal C-41 Processing
1. **Color Developer** — develops exposed silver halide AND simultaneously activates dye couplers to form dyes in each layer
2. **Bleach** — converts metallic silver to silver halide
3. **Fixer** — removes all silver, leaving only dye
4. **Wash & Stabilizer**

Result: A **negative** image on an orange-masked base.

### What Happens When E-6 Film Hits C-41 Chemistry

When slide film is cross-processed in C-41:

- **No first developer**: E-6 film's first developer is a black-and-white developer that only reduces silver (no dye formation). When replaced by C-41's color developer, the dye-forming chemistry hits the emulsion layers in a completely unintended way.
- **Missing reversal step**: In normal E-6, the reversal bath fogs the remaining silver halide so the color developer can form dye from the *unexposed* portions. In C-41, there is no reversal step, so dye forms only where the film was *exposed*.
- **Wrong dye coupler activation**: E-6 films use different dye couplers than C-41 films. The C-41 color developing agent (CD-4) reacts with E-6 dye couplers in unpredictable ways — different rates, different color yields.
- **Timing mismatch**: E-6 color developer runs at 38°C for 6 minutes; C-41 color developer runs at 38°C for 3:15. The extended time in C-41 developer over-develops the dye layers.
- **No orange mask**: Slide film has a clear base (no orange mask like C-41 negative film), so the resulting negative lacks the orange mask correction that scanners and printing systems expect.

### Key Result
**E-6 film processed in C-41 yields a negative image on a clear base** with:
- **Increased contrast** (typically 1-2 stops more contrast)
- **Strong, predictable-but-variable color casts** (dependent on film stock)
- **Higher saturation** in the dominant color cast
- **Shifts between highlights and shadows** (often split-toned: shadows go one color, highlights another)

## Why Each Film Stock Cross-Processes Differently

E-6 films from different manufacturers and product lines use:
- Different **dye couplers** in each color layer
- Different **emulsion layer ordering** (which color layers are on top)
- Different **spectral sensitization** (how each layer responds to different wavelengths)
- Different **interlayer effects** (DIR couplers, interimage effects that control color accuracy)

When these variables hit C-41 chemistry, each film stock produces its own signature color shift because the C-41 color developer's interaction with each unique dye coupler set produces different color biases.

### Fuji Velvia Family
Velvia uses Fuji's proprietary dye couplers optimized for maximum saturation and color purity. Under E-6, Velvia 50 famously produces ultra-vivid greens, rich blues, and warm skin tones. Under C-41:
- The cyan-forming layer produces an intense **green** cast
- The magenta layer shifts towards magenta-purple in highlights
- Velvia's already-high contrast goes into overdrive
- Velvia 50: green + some blue cast
- Velvia 100: very red + some magenta or yellow (different dye coupler formulation from Velvia 50)

### Fuji Provia Family
Provia uses more neutral, balanced dye couplers designed for accuracy rather than saturation. Cross-processed, this produces:
- Milder color shifts than Velvia
- Provia 100F: cooler overall, cyan-blue tendencies
- Provia 400: green + yellow cast

### Fuji Sensia Family
Sensia was Fuji's consumer-grade slide film (discontinued). Simpler dye couplers:
- Sensia 100: strong red cast
- Sensia 400: blue + green cast

### Kodak Ektachrome
Ektachrome uses Kodak's proprietary T-grain emulsions and different dye couplers:
- Current E100: intense green cast, sometimes with metallic quality
- Older Ektachrome/EliteChrome: very green
- E200: warmer shifts, sometimes golden

### Fuji 64T (Tungsten)
Tungsten-balanced slide film with completely different spectral sensitivity:
- Extremely wild results cross-processed
- Heavy blue-green to turquoise shifts
- Designed for 3200K light, produces dramatic cool effects in daylight

## Exposure Guidelines

- **Underexpose slide film by ~1 stop** when cross-processing (shoot Velvia 50 at EI 100). Slide film has narrow latitude (~5 stops) vs negative film (~10+ stops). The C-41 process boosts contrast further, so underexposure helps prevent blown highlights.
- Overexposure in xpro tends to produce muddy, desaturated results.
- Bracketing is highly recommended — the unpredictability is part of the appeal.

## Sources
- Wikipedia: Cross Processing
- The Darkroom: Cross Processing Film — A Complete Guide
- Epic Edits: Cross Processing Tips and Suggestions
- Community knowledge from r/analog
