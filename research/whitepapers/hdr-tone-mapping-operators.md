# HDR Tone Mapping Operators: A Comprehensive Survey

**Source URL:** https://en.wikipedia.org/wiki/Tone_mapping
**Additional sources:** ACES Documentation (https://docs.acescentral.com), SIGGRAPH papers
**Date:** Wikipedia revision April 28, 2026 | ACES documentation September 10, 2025

---

## Overview

Tone mapping is a technique used in image processing and computer graphics to map one set of colors to another to approximate the appearance of high-dynamic-range (HDR) images in a medium that has a more limited dynamic range. Print-outs, CRT or LCD monitors, and projectors all have a limited dynamic range that is inadequate to reproduce the full range of light intensities present in natural scenes. Tone mapping addresses the problem of strong contrast reduction from the scene radiance to the displayable range while preserving the image details and color appearance.

**Inverse tone mapping** is the inverse technique that allows expansion of the luminance range, mapping a low dynamic range image into a higher dynamic range image. It is notably used to upscale SDR videos to HDR videos.

## Background

The introduction of film-based photography created issues since capturing the wide dynamic range of lighting from the real world on a chemically limited negative was very difficult. Early film developers attempted to remedy this issue by designing film stocks and print development systems that gave a desired S-shaped tone curve with slightly enhanced contrast (about 15%) in the middle range and gradually compressed highlights and shadows.

The advent of the Zone System, which bases exposure on the desired shadow tones along with varying the length of time spent in the chemical developer (thus controlling highlight tones) extended the tonal range of black and white (and later, color) negative film from its native range of about seven stops to about ten. Photographers have also used dodging and burning to overcome the limitations of the print process.

One of the earliest digital algorithms employed by Land and McCann in 1971 was Retinex, inspired by theories of lightness perception. Computational models such as CIECAM02 or iCAM were used to predict color appearance.

## Classification of Tone Mapping Operators

Various tone mapping operators have been developed over the years. They all can be divided into two main types:

### Global (Spatially Uniform) Operators

These are non-linear functions based on the luminance and other global variables of the image. Once the optimal function has been estimated according to the particular image, every pixel in the image is mapped in the same way, independent of the value of surrounding pixels. Those techniques are simple and fast (since they can be implemented using look-up tables), but they can cause a loss of contrast.

**Simple global tone mapping filter** (Reinhard):

```
Vout = Vin / (Vin + 1)
```

Where Vin is the luminance of the original pixel and Vout is the luminance of the filtered pixel. This function maps luminance in the domain [0, ∞) to a displayable output range of [0, 1). While this filter provides decent contrast for parts of the image with low luminance (particularly when Vin < 1), parts with higher luminance get increasingly lower contrast.

**Gamma compression**:

```
Vout = A * Vin^γ
```

Where A > 0 and 0 < γ < 1. γ regulates the contrast of the image; a lower value gives lower contrast. While a lower constant γ gives a lower contrast and perhaps a duller image, it increases the exposure of underexposed parts while decreasing the exposure of overexposed parts.

### Local (Spatially Varying) Operators

The parameters of the non-linear function change in each pixel, according to features extracted from the surrounding parameters. These algorithms are more complicated than global ones; they can show artifacts (e.g. halo effect and ringing); and the output can look unrealistic, but they can provide the best performance, since human vision is mainly sensitive to local contrast.

## Major Tone Mapping Operators

### Reinhard et al. (2002) - Photographic Tone Reproduction

**Paper:** "Photographic Tone Reproduction for Digital Images" - SIGGRAPH 2002
**Authors:** Erik Reinhard, Michael Stark, Peter Shirley, James Ferwerda
**Source:** ACM Transactions on Graphics, 21(3):267-276

The Reinhard operator simulates the Zone System from film photography. It uses:

1. **Luminance scaling**: Computes the log-average luminance to set an initial exposure
2. **Dodging and burning**: A local operator that applies an automatic dodging-and-burning effect based on the photographic principle

The global version uses the simple formula Vout = Vin / (Vin + 1), while the local version uses center-surround functions to simulate dodging and burning.

### Durand and Dorsey (2002) - Fast Bilateral Filtering

**Paper:** "Fast Bilateral Filtering for the Display of High-Dynamic-Range Images" - SIGGRAPH 2002
**Authors:** Fredo Durand, Julie Dorsey
**Source:** ACM Transactions on Graphics, 21(3):257-266

This approach decomposes the HDR image into:
- **Base layer**: Large-scale luminance variations (using bilateral filtering)
- **Detail layer**: Fine details and texture

The base layer is compressed (reducing global contrast), while the detail layer is preserved (maintaining local contrast). The bilateral filter preserves edges while smoothing, preventing halos that occur with simple Gaussian-based decomposition.

Key insight: Human vision is more sensitive to local contrast than global contrast. By preserving the detail layer and attenuating only the base layer, the image retains visual clarity while fitting within the display's dynamic range.

### Fattal et al. (2002) - Gradient Domain Compression

**Paper:** "Gradient Domain High Dynamic Range Compression"
**Authors:** Raanan Fattal, Dani Lischinski, Michael Werman

This method operates in the gradient domain. The key steps:
1. Compute the gradient field of the luminance image
2. Attenuate large gradients (representing abrupt luminance changes) while preserving small gradients (detail)
3. Reconstruct the compressed image from the attenuated gradient field by solving a Poisson equation

This approach produces very sharp images that preserve small contrast details, but may flatten overall image contrast and produce halos around dark objects.

### Mantiuk et al. (2006) - Perceptual Framework for Contrast Processing

**Paper:** "A Perceptual Framework for Contrast Processing of High Dynamic Range Images"
**Authors:** Rafal Mantiuk, Karol Myszkowski, Hans-Peter Seidel

This framework is based on models of the human visual system (HVS). It operates in the contrast domain and considers:
- Contrast sensitivity functions (CSF)
- Visual masking effects
- Just-noticeable differences (JNDs)

The method optimizes contrast reproduction within the visibility constraints of the display device, ensuring that perceived contrast is as close as possible to the original scene.

### Mantiuk, Daly, and Kerofsky (2008) - Display Adaptive Tone Mapping

**Paper:** "Display Adaptive Tone Mapping" - SIGGRAPH 2008
**Authors:** Rafal Mantiuk, Scott Daly, Louis Kerofsky

This operator explicitly models both the HVS and the specific display device characteristics (peak luminance, black level, ambient illumination, reflectivity). The tone curve is computed as an optimization problem that minimizes contrast distortions weighted by their perceptual visibility, solved using a fast quadratic solver.

The method can be extended to video with temporal filters that ensure frame-to-frame tone curve changes are not salient.

### Krawczyk et al. (2005) - Lightness Perception in Tone Reproduction

**Paper:** "Lightness Perception in Tone Reproduction for High Dynamic Range Images"
**Authors:** Grzegorz Krawczyk, Karol Myszkowski, Hans-Peter Seidel

Inspired by the anchoring theory of lightness perception, this method:
1. Decomposes an HDR image into areas (frameworks) of consistent illumination
2. Computes local lightness values
3. Merges frameworks proportionally to their strength
4. Uses anchoring to determine which luminance is perceived as white

This approach does not affect local contrast and preserves natural colors due to linear handling of luminance.

### iCAM06

Based on both the color appearance model and hierarchical mapping. After bilateral filtering, the image is broken into a base layer and a detail layer. White point adaptation and chrominance adaptation are applied to the base layer, while detail enhancement is applied to the detail layer. Eventually the two layers are merged and converted to the IPT color space.

### Cao et al. (2022) - Perceptually Optimized and Self-Calibrated TMO

**Paper:** arXiv:2206.09146
**Authors:** Peibei Cao, Chenyang Le, Yuming Fang, Kede Ma

A modern neural network-based two-stage TMO:
1. **Stage one**: Uses a normalized Laplacian pyramid decomposition; two lightweight DNNs estimate the LDR pyramid from the HDR pyramid, optimized using the Normalized Laplacian Pyramid Distance (NLPD) perceptual metric
2. **Stage two**: Self-calibration by feeding rescaled HDR images to the network to generate a pseudo-multi-exposure image stack, then fusing with MEF-SSIM optimization

This is among the fastest local TMOs due to its lightweight DNN architecture.

## ACES Tone Mapping (ACES 2)

The Academy Color Encoding System (ACES) 2 introduced a new rendering transform with the following tone mapping design requirements:

### Requirements
- **S-shaped**: Tone scale shall have an "S-shaped" curve with a toe and shoulder
- **Monotonic**: Tone scale shall be continuously increasing over the domain
- **Non-asymptotic**: Tone scale shall not have any vertical or horizontal asymptotes
- **Continuity**: Tone scale shall be defined continuously over the domain
- **Domain**: Tone scale shall be defined for all float values
- **Contrast**: Tone scale shall have a log-log slope (gamma) through 18% mid-gray less than 1.55 (which was the mid-slope contrast in ACES 1)
- **Dynamic Range**: Shall provide consistent output for arbitrary dynamic ranges with presets for common display setups (48 nit cinema, 100 nit video, 108 nit Dolby Cinema, 1000 nit HDR)

### Implementation
The data is first converted to a JMh representation. The J channel is sent through the tone scale function, which is based on a Michaelis-Menten curve parameterized such that certain control values are derived from a single control parameter based on the peak luminance value. The full rendering transform pipeline is:

```
ACES RGB Input → ACES to JMh → Tonescale (J Only) → Chroma Compression (M Only)
→ Gamut Compression (J & M) → White Limiting → Display Encoding → Display RGB Output
```

### ACES Output Transform Peak Luminance Values

| ACES Peak Luminance (nits) | 0 | 0.18 | 1.0 | 2.0 |
|---|---|---|---|---|
| 100 | 0.000 | 10.000 | 45.757 | 63.988 |
| 500 | 0.000 | 13.193 | 89.098 | 158.949 |
| 1000 | 0.000 | 14.512 | 106.564 | 205.783 |
| 2000 | 0.000 | 15.747 | 121.664 | 248.779 |
| 4000 | 0.000 | 16.824 | 133.883 | 284.433 |

## Tone Mapping in Practice

### Digital Photography
HDR tone mapping, usually using local operators, has become increasingly popular as a post-processing technique where several exposures at different shutter speeds are combined to produce an HDR image and a tone mapping operator is then applied to the result.

### Common Artifacts
- **Halos**: Bright halos around dark objects or dark halos around bright objects
- **Cartoon-like appearance**: Extremely vivid colors and lack of large-scale color variations
- **Loss of photographic realism**: Local operators can pervert the nature of a documentary photographic image

### Unsharp Masking for Local Contrast Enhancement
One simple form of tone mapping takes a standard image and applies unsharp masking with a large radius (e.g., 30-100 pixel radius and 5-20% amount), which increases local contrast rather than sharpening. This is effectively what Adobe Lightroom's "Clarity" slider does.

## Open Source Tools

- **pfstmo**: Implementation of tone mapping operators (https://www.mpii.mpg.de/resources/tmo/)
- **pfstools**: Open-source set of command line programs for reading, writing and manipulating HDR images
- **Luminance HDR/QtPfsGui**: Free HDR-workflow software for Linux, Windows and Mac OS X
- **OpenCV**: Includes HDR imaging and tone mapping modules

## Key References

1. Reinhard, E. et al. (2002). "Photographic Tone Reproduction for Digital Images." ACM TOG, 21(3):267-276.
2. Durand, F. and Dorsey, J. (2002). "Fast Bilateral Filtering for the Display of High-Dynamic-Range Images." ACM TOG, 21(3):257-266.
3. Fattal, R. et al. (2002). "Gradient Domain High Dynamic Range Compression." ACM TOG.
4. Mantiuk, R. et al. (2006). "A Perceptual Framework for Contrast Processing of High Dynamic Range Images."
5. Mantiuk, R., Daly, S., Kerofsky, L. (2008). "Display Adaptive Tone Mapping." SIGGRAPH 2008.
6. Krawczyk, G. et al. (2005). "Lightness Perception in Tone Reproduction for High Dynamic Range Images."
7. Cao, P. et al. (2022). "A Perceptually Optimized and Self-Calibrated Tone Mapping Operator." arXiv:2206.09146.
