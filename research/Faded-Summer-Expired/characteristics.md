# Characteristics — Full Aesthetic Breakdown of the "Faded Summer / Expired Film" Look

## Overview

The "Faded Summer / Expired Film" aesthetic is a creative look inspired by cheap consumer color negative film that has been improperly stored—specifically, film that has sat in a hot attic, garage, or glovebox for 10–15 years—then deliberately overexposed by approximately +2 stops when shot.

It is **not** a specific film stock. It is a degradation pattern. Understanding the chemistry of what actually happens to heat-damaged film is essential for replicating the look digitally.

---

## Part 1: Heat Damage Effects on Film (The Chemistry)

### What Happens When Color Film Bakes

Consumer color negative film (C-41 process) consists of multiple emulsion layers, each sensitive to a different wavelength of light (red, green, blue). Each layer contains:

- **Silver halide crystals** — the light-sensitive component
- **Dye couplers** — organic compounds that form the visible dye image during development
- **Sensitizing dyes** — expand the silver halide's spectral sensitivity
- **Gelatin binder** — holds everything together

When film is exposed to sustained high temperatures (attic conditions: 30-50°C / 85-122°F for months/years), several chemical processes occur:

### 1. Dye Coupler Degradation (Primary Color Shift Driver)

Dye couplers are unstable organic molecules. Under heat:

- **Yellow dye coupler**: Relatively stable. The yellow layer (blue-sensitive) degrades least.
- **Magenta dye coupler**: Moderately unstable. Begins breaking down, reducing magenta/red reproduction. This is why reds become muted and shift toward orange.
- **Cyan dye coupler**: **Most unstable**. Degrades significantly under heat. The loss of cyan dye means:
  - Blues lose their coolness and become muted, teal, or muddy
  - Greens lose their cyan component, leaving only yellow → **greens shift to yellow-brown**
  - Overall image takes on a **red/yellow color cast** (the remaining warmer dye layers dominate)

**The color degradation is uneven across layers, which is critically important for emulation:**
- Blue layer (top): degrades first/most (accessible to atmospheric oxygen + heat)
- Green layer (middle): moderate degradation
- Red layer (bottom): least degradation, but still affected

This uneven layer degradation creates a specific, recognizable color palette that is difficult to reproduce with simple global white balance shifts.

### 2. Base Fog Formation

The most visually distinctive characteristic of heat-damaged film is **base fog** — a uniform, low-level density across the entire negative, including unexposed areas.

**Causes:**
- Heat energy causes spontaneous reduction of silver halide crystals (thermal fog)
- Outgassing from film base (acetate or polyester) reacts with emulsion
- Cosmic and background radiation accumulate silver speck formation over years (even cold-stored)

**Visual effect:**
- Blacks are never truly black — minimum density is raised
- Shadows take on a milky, hazy quality
- The fog color itself varies by film stock:
  - Kodak films: warm reddish-brown fog
  - Fuji films: greenish or magenta fog
  - Agfa/European films: yellowish-brown fog
  - Generic/drugstore brands: muddy brown-gray

### 3. Contrast Loss

Heat degradation affects contrast in multiple ways:

- **Base fog raises the noise floor**: signal-to-noise ratio drops
- **Dye coupler degradation reduces maximum density (D-max)**: highlights can't reach full saturation
- **Silver halide sensitivity drift**: different emulsion layers lose sensitivity at different rates, creating uneven contrast between color channels
- **Latent image regression**: even after exposure, the latent image fades faster at high temperature during the delay between shooting and development

The net effect: images look flat, soft, and "washed out" — with neither deep blacks nor bright whites.

### 4. Grain Structure Changes

Film grain is not uniform spheres — it's crystalline silver halide with complex structure. Under heat:

- **Grain clumping**: small grains aggregate into larger, irregular clusters
- **Selective fogging**: some grains fog while others don't, creating uneven granularity
- **Grain size distribution shifts**: fine grains (shadow detail) fog first and become indistinguishable; coarse grains (highlights) survive longer

The result: expired film grain looks different from fresh film grain. It's rougher, more irregular, less "tight," and more visible in the midtones and shadows than in highlights.

### 5. Color Sensitivity Drift (Spectral Sensitivity Changes)

The sensitizing dyes that give each layer its color response are themselves unstable:

- **Red sensitivity**: generally drifts downward (loses red sensitivity), making reds weaker
- **Green sensitivity**: may increase slightly, creating over-sensitivity in the green channel
- **Blue sensitivity**: typically most stable, but blue-sensitive layer sits on top and captures more scattered light due to emulsion damage

This drift means expired film "sees" color differently than fresh film — it's not just a post-processing color shift, it's a different spectral capture altogether. This is arguably the hardest aspect to emulate digitally.

### 6. Emulsion Physical Damage

Beyond chemistry, physical changes occur:

- Gelatin can partially melt and re-set, creating micro-wrinkles in the emulsion
- Film base (especially acetate "safety film") can warp, creating focus plane anomalies
- The anti-halation layer (rem-jet on some films) can degrade and allow light piping from frame edges
- Edge lettering and frame numbers can fade or become distorted

---

## Part 2: What Makes the "Expired" Look Distinct

### The Core Visual Signature

| Element | Fresh Film | Expired/Baked Film |
|---------|-----------|-------------------|
| Blacks | Deep, rich, neutral or slightly cool | Raised, muddy, warm brown (never true black) |
| Whites | Clean, bright, neutral | Creamy, warm, slightly dull |
| Shadows | Clean separation from midtones | Muddy, merged with midtones; base fog veil |
| Midtones | Accurate color, good saturation | Reduced saturation, warm shift |
| Highlights | Crisp roll-off | Soft, bloomed, lowered contrast |
| Overall contrast | Normal (gamma ~2.2 equivalent) | Significantly reduced (gamma ~1.5-1.8 equivalent) |
| Color temperature | As designed by manufacturer | Consistently warm, with specific channel shifts |
| Green foliage | Rich greens | Yellow-brown, olive, desaturated khaki |
| Blue skies | Strong cyan or blue | Pale, muted, slightly teal/purple |
| Skin tones | Natural pink/peach | Orange-tan, "suntan" look |
| Grain | Fine, regular, pleasant | Coarse, irregular, prominent in shadows |

### The "Faded Summer" Sub-aesthetic

"Faded Summer" is a specific mood within the expired film family that emphasizes:

1. **Nostalgia signal**: The look mimics photographs found in a shoebox from childhood summers — warm, faded, dreamlike
2. **Golden hour overdrive**: The baked-in warmth interacts with actual golden-hour light to create an almost monochromatic amber palette
3. **Vernacular quality**: Deliberately "bad" or "cheap" looking — anti-professional, intimate, diaristic
4. **Temporal distance**: The degradation signals time passed, creating emotional distance and longing
5. **Imperfection as feature**: Light leaks, uneven color, grain, and softness convey authenticity and materiality

The "Faded Summer" variant tends to be:
- Warmer than general expired film (emphasizes golden tones over brown)
- More desaturated in greens and blues specifically (the "summer" foliage and sky)
- Higher base fog (more milky/lifted)
- Slightly overexposed beyond just the base +2 stops (+2.5 to +3 equivalent)

---

## Part 3: Color Channel Degradation Patterns

### The Green Channel Collapse

The single most defining characteristic of heat-damaged color negative film:

**Fresh film green rendering:**
- Cyan dye + yellow dye = green
- Rich, varied greens across the spectrum

**Heat-damaged green rendering:**
- Cyan dye degrades → less cyan available
- Yellow dye survives → green becomes yellow-dominant
- Foliage shifts from green → olive → khaki → yellow-brown
- The shift is progressive: deep greens shift first (more cyan needed), yellow-greens shift last

**Lightroom emulation:**
- Green Hue: +30 to +50 (push toward yellow)
- Green Saturation: -30 to -50 (reduce intensity)
- Green Luminance: -5 to -10 (darken slightly, matching the reduced reflectance)
- Yellow Hue: +10 to +20 (push toward green-yellow for the "olive" stage)

### The Blue Channel Degradation

Heat disproportionately affects the blue-sensitive layer (top layer, most exposed to heat and oxygen).

**Fresh film blue rendering:**
- Cyan dye dominant, slight magenta for neutrality
- Sky blues are punchy and saturated

**Heat-damaged blue rendering:**
- Cyan dye degrades → blues become desaturated
- Remaining cyan shifts toward teal (greenish-blue)
- Deep blues go muddy (insufficient dye density)
- Light blues wash out entirely

**Lightroom emulation:**
- Blue Saturation: -20 to -35
- Blue Luminance: +5 to +15 (lighter, washier)
- Blue Hue: +5 to +15 (toward cyan/teal)
- Aqua Saturation: -20 to -30
- Color Grading: avoid blue in shadows (it fights the warm base fog)

### The Red/Orange Channel (Mostly Survives)

The red-sensitive layer is at the bottom of the emulsion stack — most protected from heat and oxygen.

**Fresh film red rendering:**
- Magenta dye + yellow dye = red
- Rich, saturated reds

**Heat-damaged red rendering:**
- Magenta coupler degrades somewhat
- Reds shift toward orange (more yellow, less magenta)
- Red saturation decreases moderately
- Deep reds become brownish

**Lightroom emulation:**
- Red Hue: -5 to +5 (very slight shift toward orange)
- Red Saturation: -5 to -15
- Orange Hue: 0 to -5
- Orange Saturation: -10 to -20

### The Skin Tone Shift

Skintones are a blend of red, orange, and yellow channels — and they shift distinctively:

- Fresh film: natural pink/peach/beige depending on subject
- Expired film: over-tanned, orange-bronze, "California summer 1978"
- This is partly the magenta dye loss (less pink/red in skin) and partly the overall warm cast

**Lightroom emulation:**
- Orange Luminance: +10 to +20 (brighter skin = overexposed look)
- Orange Saturation: -10 to -15 (but not too desaturated)
- Orange Hue: -5 (slightly redder to compensate for yellow shift)

### Shadow Color (The "Muddy" Signature)

Fresh film shadows are neutral to slightly cool (to counteract the warm overall balance of most color neg stocks).

Expired film shadows are:
- Warm (heat fog deposits warm-colored density)
- Brown/sepia/mud-colored
- Never neutral gray — this is a key authenticity marker
- The shadow warmth is independent of highlight color temperature

**Lightroom emulation:**
- Color Grading → Shadows: Hue 45-55, Saturation 15-25
- Tone Curve: apply a red-channel curve that lifts more than green/blue in shadows
- Calibration: Blue Primary Hue shift can affect shadow response

---

## Part 4: Anatomy of a Typical Expired Film Scan

When you look at an actual scan of heat-damaged, overexposed expired film, you see a specific visual hierarchy:

### 1. The Fog Layer (Bottom)
A uniform, low-level warm/brown density across the entire frame. In Lightroom terms, this is the lifted black point + warm split-tone shadows. Everything sits on top of this.

### 2. The Color Shift Layer
The uneven dye coupler degradation creates color that is:
- Warm overall (yellow-orange dominant)
- Green foliage shifted yellow-brown
- Blue sky desaturated and teal-tinted
- Red/orange mostly intact but slightly desaturated

### 3. The Exposure Layer
+2 stops of overexposure does several things:
- Pushes midtones into the highlight region, further reducing contrast
- Opens up shadows, making the base fog more visible
- Creates a slightly blown/glowing highlight quality ("bloom")
- Reduces saturation in highlights (color neg film desaturates at extreme exposure)

### 4. The Grain Layer (Top)
Irregular, pronounced grain that is:
- More visible in midtones and shadows
- Larger and clumpier than fresh film grain
- Lightroom grain emulation: Size 35-50, Roughness 60-80, Amount 40-60

### 5. The Uneven Damage (Irregularities)
Real expired film rarely degrades perfectly evenly:
- Edge fog (more fog at frame edges, especially the side exposed to the film canister felt)
- Light leaks (the felt light seal degrades too)
- Occasional color blotches (localized dye coupler failure)
- Frame-to-frame variation (some frames worse than others)

For maximum authenticity, vary your adjustments slightly across a set of images rather than applying identical settings to all.

---

## Part 5: Reference Palette Values

Approximate hex/HSL values for key tones in the Faded Summer / Expired aesthetic:

| Element | Approximate Hex | HSL | Description |
|---------|----------------|-----|-------------|
| "Black" / Shadow | #2B2318 to #3D3224 | 35-40°, 20-30%, 12-16% | Muddy warm brown, not black |
| Mid-gray | #8B7D6A | 38°, 15%, 48% | Warm gray/taupe |
| White / Highlight | #E8DDCF to #F2E8D8 | 38-42°, 30-45%, 88-92% | Cream/warm paper |
| Green foliage | #8A7B3A to #9E8F4D | 48-55°, 35-40%, 38-44% | Yellow-olive-khaki |
| Blue sky | #8BA5B8 to #9DB4C4 | 200-210°, 20-28%, 64-72% | Muted, desaturated blue-gray |
| Skin (Caucasian) | #C49A7A to #D4A888 | 25-28°, 35-42%, 65-75% | Orange-tan |
| Red | #B84D3D to #C45A48 | 8-12°, 45-55%, 42-48% | Muted brick red |

---

## Part 6: How Overexposure Interacts With Age

The +2 stop overexposure is not arbitrary — it's a practical necessity and aesthetic choice:

### Why Overexpose Expired Film?
1. **Compensate for speed loss**: Film loses sensitivity as it ages (roughly 1 stop per decade for consumer film, more for high-ISO). The +2 stops for 15-year film compensates for lost speed.
2. **Push through base fog**: Overexposure ensures the image information is recorded above the fog level, improving signal-to-noise.
3. **Embrace the aesthetic**: Overexposure on color negative film produces pleasing highlight roll-off and a dreamy quality that complements the degradation.

### The Overexposure × Age Matrix

| Film Age | Base Speed | Shoot At (Effective ISO) | Visual Result |
|----------|-----------|--------------------------|---------------|
| Fresh | ISO 200 | ISO 200 | Normal |
| 5 years, room temp | ~ISO 160 | ISO 100 | Slight warmth, minimal fog |
| 10 years, attic | ~ISO 100 | ISO 50 | Moderate warmth, visible fog |
| 15 years, attic | ~ISO 50 | ISO 25-50 | Strong warmth, heavy fog, color shifts |
| 20+ years, attic | ~ISO 12-25 | ISO 10-25 | Extreme degradation, near-monochrome warmth |

For the "Faded Summer" aesthetic we target the **10-15 year attic** range: heavy enough to be clearly visible and stylized, not so heavy the image loses all color information.

---

## Part 7: Common Mistakes When Emulating This Look

### 1. Only Using White Balance for Warmth
Adding global color temperature doesn't reproduce the **uneven channel degradation** that makes real expired film look the way it does. You need HSL shifts per color channel.

**Fix**: Use HSL panel + Calibration panel in addition to White Balance.

### 2. Not Lifting Blacks Enough
If black pixels stay at 0,0,0 (RGB), it will never look like expired film. Real expired color negative film has no true black.

**Fix**: Tone Curve black point must be lifted. Aim for minimum pixel values around RGB 25-35.

### 3. Using Too Much Dehaze Negative
The Dehaze slider at negative values creates a uniform haze that looks digital and artificial. Base fog is different—it's a density in the shadows specifically, not a global atmospheric effect.

**Fix**: Lift shadows/blacks instead. Avoid negative Dehaze values below -5.

### 4. Keeping Greens Green
This is the most common miss. People add warmth and lift blacks but leave greens looking healthy and vibrant. Real heat-damaged film cannot render green properly.

**Fix**: Green Hue +30 minimum, Green Saturation -30 minimum.

### 5. Perfect Symmetry
Real degradation is chaotic. Same settings on every image in a set screams "preset," not "found film."

**Fix**: Add ±5% random variation to key parameters across images. Add occasional "defects" (one frame with a light leak, one with blotchy color, etc.)

### 6. Too Clean Grain
Lightroom's default grain (Size 25, Roughness 50, Amount 25) looks like digital noise, not film grain.

**Fix**: Use Size 35-50, Roughness 60-80, Amount 40-60. Consider real grain overlays in Photoshop for best results.

---

## Summary: The Five Pillars of the Aesthetic

1. **Lifted warm blacks** — base fog, the foundation
2. **Green → yellow-brown shift** — cyan dye coupler collapse, the signature
3. **Global warmth + selective desaturation** — temperature and color exhaustion
4. **Reduced contrast with bloom** — overexposure over degraded medium
5. **Coarse irregular grain** — the texture of time
