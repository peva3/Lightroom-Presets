# Color Difference Formulas: From Delta E to CIEDE2000

**Source:** https://en.wikipedia.org/wiki/Color_difference
**Authors:** Wikipedia contributors (primary: CIE, Gaurav Sharma, Bruce Lindbloom)
**Date:** CIEDE2000 published 2001; Wikipedia article last updated 2025

---

## Overview

In color science, **color difference** or **color distance** is the separation between two colors. This metric allows quantified examination of what formerly could only be described with adjectives. Common definitions use Euclidean distance in a device-independent color space.

Delta (Δ) is the Greek letter used to denote difference, and E stands for *Empfindung* (German for "sensation"), a term traced back to Hermann von Helmholtz and Ewald Hering.

All ΔE* formulae are originally designed to have a difference of 1.0 stand for a Just Noticeable Difference (JND). However, experimental validation has shown this assumption varies — for CIE76, a JND corresponds to approximately ΔE*_ab ≈ 2.3.

## Euclidean Distance (Simple RGB)

The simplest approach: Euclidean distance in RGB space:
```
distance = sqrt((R2-R1)² + (G2-G1)² + (B2-B1)²)
```

For computational simplicity, the squared distance can be used:
```
distance² = (R2-R1)² + (G2-G1)² + (B2-B1)²
```

### Weighted RGB ("redmean")

A better low-cost approximation that compensates for the eye's varying sensitivity to different colors:
```
r̄ = (R1 + R2) / 2
ΔC = sqrt((2 + r̄/256) * ΔR² + 4 * ΔG² + (2 + (255-r̄)/256) * ΔB²)
```

Limitations: RGB-based methods do not account for differences in human color perception in a systematic way.

## Uniform Color Spaces for Color Difference

A **uniform color space** is one in which equivalent numerical differences represent equivalent visual differences, regardless of location within the color space. This is the goal of color difference formulae.

CIELAB and CIELUV are relatively perceptually-uniform color spaces used for Euclidean color difference measures. However, their non-uniformity was later discovered, leading to more complex formulae.

Spaces that improve on this issue include:
- **CAM02-UCS** — Based on CIECAM02
- **CAM16-UCS** — Based on CAM16
- **JzAzBz** — Designed for HDR

## CIELAB ΔE* Formulae

### CIE76 (ΔE*_ab)

The first formula relating measured color difference to CIELAB coordinates:
```
ΔE*_ab = sqrt((L*2 - L*1)² + (a*2 - a*1)² + (b*2 - b*1)²)
```

**Limitations**: The CIELAB space is not as perceptually uniform as intended, especially in saturated regions. This formula overrates saturated color differences. Now superseded by 1994 and 2000 formulas.

A JND corresponds to approximately ΔE*_ab ≈ 2.3.

### CMC l:c (1984)

Developed by the Colour Measurement Committee of the Society of Dyers and Colourists. Based on the CIE L*C*h color model (cylindrical CIELAB).

Accepts two parameters:
- **l** (lightness weight)
- **c** (chroma weight)

Common values: 2:1 for acceptability, 1:1 for imperceptibility threshold.
```
ΔE*_CMC = sqrt((ΔL*/(l·SL))² + (ΔC*/(c·SC))² + (ΔH*/SH)²)
```
Where SL, SC, and SH are weighting functions based on the reference color.

Designed for use with D65 and the CIE Supplementary Observer.

### CIE94 (ΔE*_94)

Extends CIE76 to address perceptual non-uniformities while retaining CIELAB space. Introduces application-specific parametric weighting factors:
```
ΔE*_94 = sqrt((ΔL*/(kL·SL))² + (ΔC*/(kC·SC))² + (ΔH*/(kH·SH))²)
```

Where:
- SL = 1
- SC = 1 + K1·C*1
- SH = 1 + K2·C*1

Parametric factors depend on application:

| Application | kL | K1 | K2 |
|---|---|---|---|
| Graphic arts | 1 | 0.045 | 0.015 |
| Textiles | 2 | 0.048 | 0.014 |

Note: CIE94 violates symmetry (like CMC l:c), making it a quasimetric — SC and SH depend on the reference color C*1 only.

### CIEDE2000 (ΔE*_00)

The current CIE standard, published in 2001. Adds five corrections to CIE94:

1. **Hue rotation term (R_T)** — Addresses the problematic blue region (hue angles near 275°)
2. **Neutral color compensation** — Primed values in L*C*h differences
3. **Lightness compensation (S_L)**
4. **Chroma compensation (S_C)**
5. **Hue compensation (S_H)**

```
ΔE*_00 = sqrt((ΔL'/(kL·SL))² + (ΔC'/(kC·SC))² + (ΔH'/(kH·SH))² + RT·(ΔC'/(kC·SC))·(ΔH'/(kH·SH)))
```

The hue rotation term is:
```
R_T = -2 * sqrt(C̄'⁷/(C̄'⁷ + 25⁷)) * sin[60° * exp(-((h̄' - 275°)/25°)²)]
```

This term specifically addresses the known issue that CIELAB space has poor perceptual uniformity in the blue region.

**Known Issues**: CIEDE2000 is not mathematically continuous (maximum discontinuity ~4% of ΔE when hues are ~180° apart). Not reliable below 1 cd/m² and not verified above 100 cd/m².

## ΔE_ITP (Rec. ITU-R BT.2124, 2019)

Introduced for WCG (Wide Color Gamut) and HDR applications where CIEDE2000 is inadequate. Derived from display-referenced ICtCp:
```
ΔE_ITP = 720 * sqrt((I1 - I2)² + (T1 - T2)² + (P1 - P2)²)
```
Where T = 0.5 * C_T (scaling for approximate uniformity).

Scaled so a value of 1 indicates the potential of a just noticeable color difference.

## HyAB (2020)

A hybrid approach for large color differences (beyond 10 units where Euclidean measures work poorly):
```
ΔE_HyAB = sqrt((a2-a1)² + (b2-b1)²) + |L2 - L1|
```
Uses taxicab distance for lightness and Euclidean for chroma. Shown to work better than Euclidean and CIEDE2000 for large color differences.

## Tolerance

**Tolerancing** answers: "What is a set of colors that are imperceptibly/acceptably close to a given reference?" If the distance measure is perceptually uniform, the answer is simply the set of points within the JND threshold.

In the CIE 1931 color space, tolerance contours are defined by MacAdam ellipses (holding L* fixed). The ellipses vary in size — this non-uniformity led to the creation of CIELUV and CIELAB. When lightness varies, tolerance sets become ellipsoidal.

## Industry-Specific Tolerances

- **Automotive**: ΔE*_CMC often less than 0.5 under D65/10
- **Printing**: Typical limit 2.0 under D50, though some processes allow up to 5.0
- **CMYK solids**: CIELAB metric used to define color tolerance

## Practical Guidance for Photography

- **ΔE < 1.0**: Not perceptible by human eyes
- **ΔE 1.0 - 2.0**: Perceptible through close observation
- **ΔE 2.0 - 10.0**: Perceptible at a glance
- **ΔE 11.0 - 49.0**: Colors are more similar than opposite
- **ΔE 50.0 - 100.0**: Colors are exact opposites

## Summary Comparison

| Formula | Year | Basis | Key Feature | Best Use |
|---|---|---|---|---|
| CIE76 | 1976 | CIELAB | Simple Euclidean | Legacy/basic applications |
| CMC l:c | 1984 | CIELCh | Adjustable l:c ratio | Textiles, paint |
| CIE94 | 1994 | CIELCh | Application weighting | Graphic arts, textiles |
| CIEDE2000 | 2001 | CIELCh | 5 corrections incl. blue fix | Modern color difference standard |
| ΔE_ITP | 2019 | ICtCp | HDR/WCG support | HDR television, wide gamut |
| HyAB | 2020 | CIELAB | Hybrid taxicab+Euclidean | Large color differences (>10) |

## References

- Gaurav Sharma (2003). *Digital Color Imaging Handbook*. CRC Press.
- Sharma, Wu, and Dalal (2005). "The CIEDE2000 color-difference formula: Implementation notes, supplementary test data, and mathematical observations". Color Research & Application.
- CIE (2001). "Improvement to Industrial Colour-Difference Evaluation". CIE Publication 142-2001.
- ITU-R (2019). "Objective metric for the assessment of the potential visibility of colour differences in television". Rec. ITU-R BT.2124-0.
- Abasi, Amani Tehran, Fairchild (2020). "Distance metrics for very large color differences". Color Research & Application.
