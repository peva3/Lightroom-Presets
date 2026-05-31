# Full Aesthetic Breakdown: Lomography Cross-Processed Look

## Core Aesthetic Signature

The Lomography cross-processed aesthetic is defined by **controlled chaos** — deliberately unpredictable color shifts, heavy vignetting, high contrast, and saturated colors produced by running E-6 slide film through C-41 chemistry. When emulated digitally for Lightroom presets, the goal is to replicate these chemical accidents with consistency.

## Color Shift Patterns

### The Fundamental Shift: Purple Shadows → Yellow-Green Highlights

This is the most recognizable cross-processed color signature:

| Tonal Zone | Color Shift | Why It Happens |
|------------|-------------|----------------|
| Deep shadows | **Purple / Magenta / Blue** | Magenta + Cyan dye layers dominate in dark areas; yellow layer is weakest when coupled with wrong developer |
| Mid-shadows | **Blue-purple to cool cyan** | Transitional zone as dye layers interact unevenly |
| Midtones | **Shifted warm-cool balance** | Depends heavily on film stock and exposure |
| Mid-highlights | **Yellow-green / Chartreuse** | Yellow layer begins producing; cyan shifts toward green with CD-4 |
| Bright highlights | **Yellow-green / Lime / Acid green** | Full yellow layer output + green-shifted cyan → yellow-green cast |
| Skin tones | **Orange-red to yellow, often with green cast** | Particularly problematic; looks unnatural, "toxic" |
| Blues/skies | **Cyan to teal, sometimes vivid aqua** | Cyan layer dominates without proper magenta balance |
| Greens/foliage | **Hyper-saturated lime to olive** | Green-sensitive layer couples aggressively with CD-4 |
| Reds/warm colors | **Orange-red to magenta-pink** | Red-sensitive layer shifts warm |

### The "Cross-Processed Curve"

The characteristic cross-processed image has:
- **Crushed blacks** with a purple/blue tint in the deepest shadows
- **Lifted midtones** with a color cast that varies by film stock
- **Blown, tinted highlights** — highlights rarely stay neutral white; they skew yellow-green
- **High contrast** between shadows and highlights — the curve is effectively an S-curve on steroids

## Variance Per Film Stock

Different E-6 films cross-process radically differently. This is critical knowledge for building film-accurate presets.

### Fujichrome Velvia (50, 100, 100F)

**The king of cross-processed saturation.**

- **Shadows**: Deep, inky purple-blue. Almost black with a violet sheen.
- **Midtones**: Intense saturation. Reds go fire-engine red to magenta. Greens go radioactive.
- **Highlights**: Yellow-green to acid green. Very pronounced.
- **Contrast**: Extremely high. Velvia already has high native contrast; cross-processing amplifies it to near-unusable levels.
- **Overall palette**: Warm dominant with purple shadows and electric green highlights. The most "violent" cross-processed look.
- **Best for**: Landscapes, urban decay, anything where you want maximum visual impact.
- **Exposure sweet spot**: Rate at ISO 40 (Velvia 50), slight overexposure helps tame contrast.

### Fujichrome Provia (100F, 400X)

**The versatile, balanced cross-process stock.**

- **Shadows**: Cool blue with hints of purple, less intense than Velvia.
- **Midtones**: More neutral than Velvia. Greens are saturated but not radioactive. Blues skew slightly teal.
- **Highlights**: Yellow-green, but more golden than acid green. More restrained.
- **Contrast**: High but manageable. Provia 100F has a smoother tonal curve natively.
- **Overall palette**: Cool-leaning. Blues remain relatively true. The overall look is "cool cinematic" rather than "psychedelic."
- **Best for**: Portraits (relatively), street photography, fashion.
- **Exposure sweet spot**: Rate at box speed or +1/3 stop. Pushes well to 200 or 400.

### Fujichrome Sensia (100, 200, 400 — discontinued)

**The consumer cross-process sleeper hit.**

- **Shadows**: Purple-magenta; softer than Velvia, more magenta than Provia.
- **Midtones**: Warm-biased. Skin tones go orange-red. Greens go warm olive.
- **Highlights**: Golden-yellow with a hint of green. Warmer overall highlight caste than Velvia or Provia.
- **Contrast**: Medium-high. Less aggressive highlight clipping.
- **Overall palette**: Warm retro vibe. Think 1970s snapshot with purple shadows. The most "nostalgic" cross-process look.
- **Best for**: Casual/street/travel, warm golden hour light.
- **Exposure sweet spot**: Box speed or +1/2 stop.

### Kodak Ektachrome (E100G, E100GX, E100VS, E200 — and the new E100)

**The American cross-process palette.**

- **Shadows**: Blue-cyan rather than purple. Cooler, less magenta than Fuji stocks.
- **Midtones**: More color-accurate than Fuji films. The Ektachrome palette is generally cooler and more "honest."
- **Highlights**: Yellow-green but more subtle. Can go slightly cyan in the brightest highlights.
- **Contrast**: High but smooth. Ektachrome has a reputation for clean, "transparent" cross-processed results.
- **Overall palette**: Cool blue-cyan shadows, relatively accurate midtones, subtle yellow-green highlights. The most "elegant" cross-process look.
- **Best for**: Fashion, editorial, architecture.
- **Exposure sweet spot**: Box speed. The new E100 cross-processes very cleanly.

### Agfa CT Precisa (100, 200 — discontinued but available as Lomography X-Pro)

**Lomography's own cross-process film.**

- Actually repackaged/rebranded film (originally Agfa, later sourced from other manufacturers including Fuji).
- **Shadows**: Blue-purple, classic cross-processed look.
- **Highlights**: Yellow-green, very pronounced.
- **Contrast**: High, with dramatic color separation between tones.
- **Overall palette**: Designed specifically to look good cross-processed. Strong green-yellow highlights with cool purple shadows.

### Lomography X-Pro Chrome (100, 200)

**Purpose-built for cross-processing, sold by Lomography.**

- Available in 35mm, 120, and 110 formats.
- **Shadows**: Deep purple with blue undertones.
- **Highlights**: Intense yellow-green to acid green.
- **Contrast**: Very high — engineered for maximum cross-processed drama.
- **Color saturation**: Extreme. Lomography specifically formulated/marketed this film for the cross-process look.
- **Exposure**: Shoot at box speed. Very forgiving.

### Comparison Matrix

| Film | Shadow Cast | Highlight Cast | Contrast | Saturation | Warm/Cool |
|------|------------|----------------|----------|------------|-----------|
| Velvia 50/100 | Purple-blue (intense) | Acid green (intense) | Extreme++ | Extreme | Warm dominant |
| Provia 100F | Cool blue-purple (subtle) | Golden-green | High | High | Cool dominant |
| Sensia 100 | Purple-magenta (warm) | Golden-yellow-green | Medium-high | Medium-high | Warm dominant |
| Ektachrome E100 | Blue-cyan (cool) | Subtle yellow-green | High | High | Cool dominant |
| Agfa CT Precisa | Blue-purple | Yellow-green | High | High | Neutral-cool |
| Lomo X-Pro | Purple-blue | Acid green-yellow | Very high | Extreme | Variable |

## Vignette Characteristics

The Holga/Diana toy camera aesthetic adds physical vignetting that combines with cross-processed chemistry:

### Optical Vignetting (from plastic meniscus lens)
- **Shape**: Circular, soft falloff from center
- **Intensity**: 2-4 stops darker at extreme corners
- **Character**: The Holga f/8 (actual ~f/13) meniscus lens has an image circle that barely covers the film frame — this is the source of the famous Holga vignette
- **Color shift within vignette**: The darkened edges often take on a stronger purple/blue cast from the cross-processing, creating a "frame within a frame" effect

### Combined Aesthetic
- Heavy, soft-edged vignette
- Vignette area skews cooler (more purple/blue) than center
- Center of frame is brighter with more yellow-green highlight presence
- Creates dramatic depth and focuses attention

## Additional Lens Characteristics (Holga/Diana)

- **Soft focus**: The single-element meniscus lens is inherently soft, especially at edges
- **Chromatic aberration**: Color fringing at high-contrast edges, adding to the "lo-fi" feel
- **Light leaks**: Random red/orange/white streaks from the plastic body not being light-tight
- **Film flatness issues**: The 120 film can bow, creating uneven focus across the frame
- **Zone focusing**: Four vague settings (1m, 2m, 6m, infinity) — most shots are slightly out of focus

## Lightroom Emulation Targets

For accurate Lightroom preset creation, the digital emulation should target:

1. **Tone Curve**: Strong S-curve with crushed blacks and pushed highlights
2. **Split Toning**: Purple/blue in shadows (~240-270° hue), yellow-green in highlights (~50-70° hue)
3. **HSL Adjustments**: Shift reds toward magenta, blues toward cyan/teal, greens toward lime/yellow, yellows toward green
4. **Vignette**: Heavy (Amount: -40 to -60), midpoint shifted inward for Holga effect
5. **Clarity/Texture**: Negative clarity (-10 to -20) for soft focus feel, or positive contrast for the punchy xpro look
6. **Calibration**: Shift blue primary toward cyan/teal, red primary toward magenta, green primary toward yellow

## Sources
- Wikipedia: Cross processing, Holga, Diana camera, Lomography
- r/analog community knowledge
- Lomography.com film specifications
- Photographic community testing and documentation
