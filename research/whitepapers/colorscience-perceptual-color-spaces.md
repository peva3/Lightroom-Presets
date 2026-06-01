# Perceptual Color Spaces for Image Processing: Oklab and Beyond

**Source:** https://bottosson.github.io/posts/oklab/
**Author:** Björn Ottosson
**Date:** Published December 23, 2020; updated with industry adoption note 2025

---

## Introduction

A perceptual color space is desirable when doing many kinds of image processing. It is useful for:
- Turning an image grayscale while keeping perceived lightness the same
- Increasing saturation while maintaining perceived hue and lightness
- Creating smooth and uniform looking transitions between colors

In 2020, Björn Ottosson introduced the **Oklab color space**, designed to be simple to use while doing a good job at predicting perceived lightness, chroma and hue. By 2025 it had become an industry standard used in Photoshop, web browsers (CSS Color Level 4/5), game engines (Unity, Godot), and countless open source libraries.

## The Oklab Color Space

Oklab uses a D65 whitepoint (matching sRGB and other common color spaces). The three coordinates are:
- **L** — perceived lightness
- **a** — how green/red the color is
- **b** — how blue/yellow the color is

### Polar Form (LCh)

```
C = sqrt(a² + b²)
h° = atan2(b, a)
```

And conversely:
```
a = C * cos(h°)
b = C * sin(h°)
```

### Conversion from XYZ to Oklab

**Step 1**: Convert XYZ to approximate cone responses:
```
[l, m, s]^T = M1 * [X, Y, Z]^T
```
Where M1 = [[+0.8189330101, +0.3618667424, -0.1288597137],
             [+0.0329845436, +0.9293118715, +0.0361456387],
             [+0.0482003018, +0.2643662691, +0.6338517070]]

**Step 2**: Apply nonlinearity (cube root):
```
[l', m', s']^T = [l^(1/3), m^(1/3), s^(1/3)]^T
```

**Step 3**: Transform to Lab:
```
[L, a, b]^T = M2 * [l', m', s']^T
```
Where M2 = [[+0.2104542553, +0.7936177850, -0.0040720468],
             [+1.9779984951, -2.4285922050, +0.4505937099],
             [+0.0259040371, +0.7827717662, -0.8086757660]]

### Inverse (Oklab to XYZ)

Step 1: [l', m', s']^T = M2^(-1) * [L, a, b]^T
Step 2: [l, m, s]^T = [l'^3, m'^3, s'^3]^T
Step 3: [X, Y, Z]^T = M1^(-1) * [l, m, s]^T

### Reference Values for Testing

| X | Y | Z | L | a | b |
|---|---|---|---|---|---|
| 0.950 | 1.000 | 1.089 | 1.000 | 0.000 | 0.000 |
| 1.000 | 0.000 | 0.000 | 0.450 | 1.236 | -0.019 |
| 0.000 | 1.000 | 0.000 | 0.922 | -0.671 | 0.263 |
| 0.000 | 0.000 | 1.000 | 0.153 | -1.415 | -0.449 |

## Requirements for a Good Perceptual Color Space

According to Ottosson:

1. **Should be an opponent color space** — similar to CIELAB
2. **Should predict lightness, chroma and hue well** — L, C, and h should be perceived as orthogonal so one can be altered without affecting the other two
3. **Blending should result in even transitions** — no hue shifts toward unexpected colors
4. **D65 whitepoint** — matches sRGB, rec2020, and Display P3
5. **Good numerical behavior** — easy to compute, numerically stable, differentiable
6. **Normal well-lit viewing conditions** — no dependence on absolute luminance or background adaptation info
7. **Scale invariance** — if exposure changes, perceptual coordinates should just scale

## Comparison with Existing Models

### CIELAB and CIELUV
- Largest issue: inability to predict hue, particularly in blue regions
- Other smaller issues exist

### CIECAM02-UCS / CAM16-UCS
- Good perceptual uniformity overall
- Drawbacks: bad numerical behavior, not scale invariant, blending doesn't behave well due to chroma compression

### OSA-UCS
- Good overall performance
- No analytical inverse — impractical

### IPT
- Great hue uniformity modeling
- Doesn't predict lightness and chroma well
- But meets all other requirements — simple, scale-invariant

### JzAzBz
- Fairly good overall
- Designed for uniform lightness scaling for HDR — introduces scale/exposure dependence

### HSV (sRGB)
- Widely used but meets almost none of the requirements
- Large perceptual non-uniformities

## Quantitative Comparison

Error metrics (RMSE and 95th percentile) across color spaces, tested on lightness, chroma, and hue prediction datasets:

| Color Space | L RMS | C RMS | H RMS | L 95% | C 95% | H 95% |
|---|---|---|---|---|---|---|
| Oklab | **0.20** | **0.81** | 0.49 | **0.44** | **1.78** | 1.06 |
| CIELAB | 1.70 | 1.84 | 0.69 | 3.16 | 3.96 | 1.56 |
| CIELUV | 1.72 | 2.32 | 0.68 | 3.23 | 5.03 | 1.51 |
| OSA-UCS | 2.05 | 1.28 | 0.49 | 4.04 | 2.73 | 1.08 |
| IPT | 4.92 | 2.18 | 0.48 | 9.89 | 4.64 | 1.02 |
| JzAzBz | 2.38 | 1.79 | **0.43** | 4.55 | 3.77 | **0.92** |
| CAM16-UCS | 0.00* | 0.00* | 0.59 | 0.00* | 0.00* | 1.31 |

*CAM16-UCS is the origin of the test data, hence zero error. Lower is better.

## Munsell Data Performance

When plotting Munsell color chart data (V=5), Oklab and CAM16-UCS predict the data well (rings appear as nearly perfect circles), while other spaces squash the circles in various ways — indicating Oklab does a better job at predicting chroma than most color spaces.

## Luo-Rigg Dataset and Full Gamut

Key observations:
- CIELAB and OSA-UCS show odd gamut shapes for highly saturated colors
- Except for CAM16-UCS, ellipses are stretched as chroma increases
- CAM16 explicitly compresses chroma to better match experimental data, which makes perceptual difference data look good but makes color blending worse
- Oklab and IPT show smooth, well-behaved gamut shapes

## Blending Performance

Oklab produces smooth, even transitions without hue shifts. CIELAB, CIELUV, and HSV all show hue shifts toward purple when blending white with blue. CAM16 has a different issue: colors desaturate quickly, resulting in less even transitions.

## How Oklab Was Derived

Three datasets were used for optimization:

1. **Lightness dataset** — CAM16-generated pairs of colors with same lightness but random hue and chroma (within Pointer's Gamut)
2. **Chroma dataset** — CAM16-generated pairs of colors with same chroma but random hue and lightness
3. **Hue dataset** — Uniform perceived hue data used to derive IPT (Ebner & Fairchild, 1998)

**Methodology**: For each dataset, coordinates that should be the same within a pair are swapped. The perceived distance between original and altered colors is computed using CIEDE2000. The error for each pair is the minimum of the two color differences. Parameters M1, M2, and γ were optimized to minimize RMSE across all datasets.

**Final tweaks**: The optimized γ value was very close to 1/3 (0.323). When looking at the sRGB gamut, blue colors folded in on themselves slightly. By forcing γ = 1/3 and adding a constraint that blue colors not fold inward, the final Oklab model was derived — with no noticeable effect on error.

## Industry Adoption (as of 2025)

- **Adobe Photoshop** — Default interpolation method for gradients
- **Web browsers** — Part of CSS Color Level 4 and 5, supported by Chrome, Firefox, Safari, Edge
- **Game engines** — Unity's gradients, Godot's color picker
- **Open source** — Numerous python libraries (colour-science is recommended)

## Related Color Spaces

### CIELAB (1976)
The original perceptual color space. Opponent model with L (lightness), a (red-green), b (yellow-blue). Simple but limited: poor hue constancy, particularly blue→purple shifts as L changes.

### IPT (1998)
Excellent hue uniformity. Structure identical to Oklab (M1, gamma, M2 pipeline) but M1 is an adapted Hunt-Pointer-Estevez matrix. Basis for ICtCp.

### ICtCp (2016)
Improves IPT for HDR and wide gamut. Used in Rec. 2100. Basis for ΔE_ITP (Rec. 2124).

### CAM16-UCS (2017)
Successor to CIECAM02-UCS. Most accurate perceptual uniformity overall, but complex and not scale-invariant.

### SRLAB2 (2009)
Modification of CIELAB using CIECAM02 chromatic adaptation matrix to fix the blue hue issue.

## References

- Ottosson, Björn (2020). "A perceptual color space for image processing". https://bottosson.github.io/posts/oklab/
- Ebner, F.; Fairchild, M.D. (1998). "Development and Testing of a Color Space with Improved Hue Uniformity". IS&T 6th Color Imaging Conference.
- Li, Changjun; et al. (2017). "Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS". Color Research & Application.
- Safdar, Muhammad; et al. (2017). "Perceptually uniform color space for image signals including high dynamic range and wide gamut". Optics Express.
- Levien, Raph (2021). "An interactive review of Oklab". https://raphlinus.github.io/color/2021/01/18/oklab-critique.html
