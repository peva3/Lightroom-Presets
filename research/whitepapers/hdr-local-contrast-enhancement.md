# Local Contrast Enhancement: Unsharp Masking, Clarity, Texture, and Dehaze

**Source URL:** https://en.wikipedia.org/wiki/Unsharp_masking
**Additional:** Cambridge in Colour, ACES Documentation
**Date:** Wikipedia revision March 16, 2026

---

## Historical Background

### Film Darkroom Origins
Unsharp masking originated in photographic darkrooms. The process:
1. Contact-copy a large-format negative onto low-contrast film to create a positive
2. Make the positive blurred by copying with the original's back (not emulsion-to-emulsion)
3. Place the blurred positive in contact with the back of the original negative
4. When light passes through both, the positive partially cancels low-frequency information
5. The mask reduces the dynamic range of the original negative
6. The resulting print emphasizes high-spatial-frequency details (increased acutance)

The Zone System by Ansel Adams extended tonal range from ~7 stops to ~10 stops by controlling both exposure (shadows) and development time (highlights). Dodging and burning were used to overcome print process limitations.

## Digital Unsharp Masking (USM)

### The Core Algorithm

The standard unsharp masking formula:

```
sharpened = original + (original − blurred) × amount
```

Where:
- **Amount** (percentage): Controls the magnitude of edge overshoot (contrast added at edges)
- **Radius** (pixels): Size of edges to enhance; larger radius affects broader transitions
- **Threshold** (levels): Minimal brightness change before sharpening activates (prevents noise amplification in smooth areas)

### USM Parameters in Detail

| Parameter | Small Values | Large Values | Typical Range |
|-----------|-------------|-------------|---------------|
| **Amount** | Subtle enhancement | Aggressive sharpening, halos | 50-150% |
| **Radius** | Fine detail (texture) | Broad contrast (clarity) | 0.5-100 px |
| **Threshold** | Sharpen everything (noisy) | Only strong edges (safe for skin) | 0-10 levels |

### The Kernel Representation
A simple 3x3 sharpening kernel:

```
[ 0  -1   0 ]
[-1   5  -1 ]
[ 0  -1   0 ]
```

Derived from: identity kernel + (identity - blur kernel) × amount
With a uniform 3x3 blur kernel and amount=5.

## Local Contrast Enhancement (LCE)

### The Key Insight
Unsharp masking can be used in TWO fundamentally different ways depending on the radius:

| | **Sharpening** | **Local Contrast Enhancement** |
|---|---|---|
| **Radius** | 0.5-3 pixels | 30-100+ pixels |
| **Amount** | 50-500% | 5-30% |
| **Threshold** | 0-3 | 0 |
| **Effect** | Edge acuity | Mid-tone contrast, "pop" |
| **Artifacts** | Halos at strong edges | Subtle tonal shift |
| **Equivalent** | Traditional USM | Clarity slider |

### LCE Formula and Mechanism
```
enhanced = original + (original − gaussian_blur(original, large_radius)) × small_amount
```

What this does:
1. The large-radius blur captures local luminance averages
2. Subtracting it from the original isolates the deviation from local mean
3. Adding a fraction back boosts the deviation → increased local contrast
4. Because the radius is large, fine details are in both the blurred and original versions (no sharpening)
5. Broad tonal transitions are amplified → increased "clarity" or "pop"

### Relationship to Tone Mapping
Local contrast enhancement is effectively a simple global tone mapping operator. More powerful local tone mapping algorithms (bilateral filter decomposition, gradient domain methods) can be seen as sophisticated extensions of the same principle.

## Lightroom Equivalents

### Clarity
**Mechanism:** Local contrast enhancement via large-radius unsharp masking
**Typical effective parameters:** Radius 50-100px, amount 5-30%
**What it affects:** Mid-tone contrasts, broad tonal transitions
**Use cases:** Adding "punch" to landscapes, architecture, portraits (negative Clarity for skin softening)
**Caveats:** Can create dark halos around bright objects at extreme values

### Texture
**Mechanism:** Sharpening at medium radius (between Clarity and Sharpening)
**Typical effective parameters:** Radius 5-15px, moderate amount
**What it affects:** Fine-to-medium texture detail
**Use cases:** Enhancing fabric, foliage, skin pores without global contrast changes
**Advantage over Clarity:** More targeted, avoids the broad tonal shifts of Clarity

### Dehaze
**Mechanism:** More complex than simple USM; involves:
- Local contrast enhancement at multiple scales
- Color saturation adjustment (haze desaturates, Dehaze resaturates)
- Black point adjustment based on local transmission estimation
**What it affects:** Atmospheric haze reduction, global contrast, saturation
**Use cases:** Landscape photos with atmospheric haze, underwater photos
**Caveats:** Can introduce unnatural colors, halos, crushed blacks at extreme values

### Sharpening (Detail Panel)
**Mechanism:** Traditional USM at small radius
**Typical effective parameters:** Radius 0.5-3px, amount 25-150%
**What it affects:** Edge acuity, fine detail crispness
**Use cases:** Output sharpening for print/web, capture sharpening
**Key parameters:**
- Amount: Overall sharpening strength
- Radius: Edge width to enhance
- Detail: 0=halo suppression (edges only), 100=full USM
- Masking: 0=sharpen everything, 100=edges only

## ACES Reference Gamut Compression

The ACES system includes a Reference Gamut Compression transform (introduced in ACES 1.3) that addresses a related problem: handling colors that fall outside the display gamut after tone mapping. This operates in a perceptually uniform space and compresses chroma while preserving hue, similar in spirit to how local contrast enhancement preserves edges while compressing global range.

### Key Design Principles
1. Operates in perceptually uniform space (JMh)
2. Compresses only the M (colorfulness) component
3. Preserves hue (h) exactly
4. Progressive compression: minimal effect on in-gamut colors, strong compression on far-out-of-gamut colors
5. Avoids the "neon" look of clipped-out-of-gamut colors

## Human Visual System Basis

### Simultaneous Contrast
The perceived brightness of a region depends on its surroundings. A gray patch looks darker on a white background and lighter on a black background. Local contrast enhancement exploits this perceptual phenomenon.

### Mach Bands
The human visual system exaggerates contrast at edges through lateral inhibition in the retina. USM creates artificial Mach bands (overshoot/undershoot at edges) that the visual system interprets as enhanced sharpness.

### Contrast Sensitivity Function (CSF)
The human eye is most sensitive to spatial frequencies around 2-5 cycles/degree, with reduced sensitivity at both very high and very low frequencies. This is why:
- Sharpening (high frequency): Needs strong boost to be visible
- Clarity (medium frequency): Most visible/effective range
- Global contrast (very low frequency): Subtle perception

## Advanced Techniques

### Frequency Separation
A technique used in portrait retouching:
1. Decompose image into high-frequency (texture) and low-frequency (color/tone) layers
2. Edit each layer independently
3. Recombine for natural-looking results

This is a general case of the base+detail decomposition used in Durand's bilateral tone mapping.

### Multi-Scale Enhancement
Applying local contrast enhancement at multiple scales simultaneously:
- Small radius → fine texture
- Medium radius → clarity
- Large radius → local tonal balance

Adobe's Dehaze likely uses multi-scale processing.

### Bilateral Filter for Edge-Aware Enhancement
Unlike Gaussian blur (which blurs across edges creating halos), the bilateral filter:
- Blurs similar colors/luminances together
- Preserves edges
- Is the foundation of edge-aware local contrast enhancement

Formula for bilateral filtering at pixel p:
```
BF[I]_p = (1/W_p) * sum(G_s(||p-q||) * G_r(|I_p - I_q|) * I_q)
```
Where G_s is spatial Gaussian, G_r is range (intensity) Gaussian.

### Guided Filter
A faster alternative to the bilateral filter with better edge preservation. Used in Adobe's implementations.

## Practical Guidelines for Preset Design

### When to Use Clarity vs Texture vs Sharpening

| Goal | Use | Typical Value |
|------|-----|---------------|
| Add overall "punch" | Clarity | +10 to +25 |
| Soften skin, dreamy look | Clarity (negative) | -15 to -30 |
| Enhance fabric/foliage detail | Texture | +10 to +30 |
| Reduce noise appearance | Texture (negative) | -10 to -20 |
| Output for print | Sharpening | 25-50%, Radius 0.8-1.5 |
| Output for web | Sharpening | 40-80%, Radius 0.5-1.0 |
| Landscape haze removal | Dehaze | +10 to +30 |
| Add atmospheric softness | Dehaze (negative) | -10 to -20 |

### Grain vs Sharpening Interaction
For presets that include grain:
- Sharpening MUST be low (≤10) to prevent digital sharpening from turning organic grain into jagged digital noise
- Clarity and Texture should be at 0 to let grain structure carry the character
- Luminance noise reduction should be at 0 to avoid smearing grain

### Preset Safety Limits
- **Clarity**: ±30 (beyond this can create unnatural halos)
- **Texture**: ±40
- **Dehaze**: ±30 (beyond this crushes blacks or creates unnatural saturation)
- **Sharpening for grain presets**: 0-10 max
- **Sharpening for clean presets**: 25-80 with appropriate masking

## Key References

1. Cambridge in Colour. "Local Contrast Enhancement." http://www.cambridgeincolour.com/techniques/local-contrast-enhancement.htm
2. Cambridge in Colour. "Guide to Image Sharpening." http://www.cambridgeincolour.com/techniques/image-sharpening.htm
3. Margulis, D. (2005). "Life on the Edge." Makeready Column.
4. Margulis, D. (1998). "Sharpening With a Stiletto." Makeready Column.
5. Durand, F. and Dorsey, J. (2002). "Fast Bilateral Filtering for the Display of High-Dynamic-Range Images." SIGGRAPH 2002.
6. Paris, S. and Durand, F. (2006). "A Fast Approximation of the Bilateral Filter using a Signal Processing Approach."
7. He, K. et al. (2013). "Guided Image Filtering." IEEE TPAMI.
8. ACES Documentation - Reference Gamut Compression. https://docs.acescentral.com
