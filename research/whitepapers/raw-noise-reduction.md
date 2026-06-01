# Noise Reduction Algorithms in RAW Processing

**Source URLs:**
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/denoise-profiled/ (darktable 3.8 Manual)
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/raw-denoise/ (darktable 3.8 — Raw Denoise)
- https://www.libraw.org/articles/bayer-moire.html (LibRaw — noise interaction with demosaicing)

**Author(s):** darktable project contributors, LibRaw LLC
**Date:** 2021 (darktable 3.8 release), 2012+ (LibRaw)

---

## Overview

Noise in digital camera sensors comes from several sources:
- **Photon shot noise** (random arrival of photons — dominant in brighter areas)
- **Read noise** (electronic noise from sensor readout circuitry — dominant in shadows)
- **Dark current / thermal noise** (temperature-dependent, important for long exposures)
- **Pattern noise** (fixed-pattern noise — can be subtracted with dark frames)
- **Quantization noise** (analog-to-digital conversion)

The two main visible categories are:
- **Luma noise**: Grain-like brightness variations
- **Chroma noise**: Random color speckles (often more objectionable)

---

## Profiled Denoising (darktable)

### Why Profiling Matters

Traditional denoising algorithms assume noise variance is **independent of signal luminosity**. In reality, noise characteristics change significantly across the tonal range. By profiling a camera sensor at different ISO settings, the variance at different luminosities can be assessed, allowing the denoising algorithm to adjust more evenly.

Darktable has sensor noise profiles for **over 300 camera models** from all major manufacturers.

### Key Insight: Pipeline Placement

The denoise (profiled) module is placed **before** the input color profile in the pixelpipe. This is critical because:
- White balance amplifies RGB channels differently → different noise levels per channel
- The module must work on data where the noise profile parameters are accurate

The "whitebalance-adaptive transform" checkbox makes the denoising algorithm adapt to white balance adjustments, since WB amplification changes per-channel noise levels.

---

## Denoising Algorithms

### Non-Local Means (NL-Means)

**Spatial domain algorithm.** Averages each pixel with surrounding pixels, weighted by the **similarity of their neighborhoods**. A "patch" with defined size measures that similarity.

Key parameters:
- **Patch size**: Size of neighborhoods being compared. Larger = more noise reduction but may smooth fine edges. Minimal processing time impact.
- **Search radius**: How far to search for similar patches. Larger = better for coarse noise, but processing time increases with the **square** of this parameter.
- **Scattering (coarse-grain noise)**: Like search radius but without increasing the number of patches considered. Processing time stays constant. Particularly effective at reducing chroma noise.

**Resource intensity**: High — this is computationally expensive.

### Wavelets (Default)

**Frequency domain algorithm.** Decomposes the image into frequency bands (wavelet decomposition), allowing noise to be targeted at specific detail scales.

Two color modes:
- **Y0U0V0 mode** (preferred): Separates denoising into luminance (Y0) and color (U0V0) components. Use the Y0 curve for luma noise, U0V0 curve for chroma noise.
- **RGB mode** (legacy): Direct control over R, G, B channels independently or together.

The **wavelet curves** allow adjusting denoising strength by noise coarseness:
- Left end of curve → very coarse grain noise
- Right end of curve → very fine grain noise
- Raising curve → more smoothing
- Lowering curve → less smoothing

Practical example: preserve fine-grain noise (for texture) by pulling the right-most part of the curve down. For chroma noise on a U0V0 curve, safely raise the right side (colors don't change much at fine scales).

**Resource intensity**: Lower than NL-means.

---

## Luma vs. Chroma Noise

Both algorithms can tackle luma and chroma noise independently. **Previous guidance** suggested using two separate module instances (one with chroma blend mode, one with lightness). This is **no longer recommended** because:
- Denoise (profiled) is placed before input color profile in the pipeline
- Color blending modes should only be used after the input color profile has been applied
- Current algorithms provide their own internal luma/chroma separation

**RGB channel denoising caveat**: Independently denoising R, G, B channels can leave residual chroma noise requiring excessive smoothing. This was a key motivation for implementing the Y0U0V0 color mode.

---

## Controls Reference

### Common Controls (both algorithms)

| Control | Function |
|---------|----------|
| **Profile** | Auto-detected from camera model + ISO via Exif. Interpolated for intermediate ISOs. |
| **Mode** | Algorithm selection + auto/manual interface toggle |
| **Whitebalance-adaptive transform** | Adapts denoising to WB channel amplification differences |
| **Adjust autoset parameters** (auto only) | Single slider for exposure compensation noise (multiplies effective ISO) |
| **Strength** | Fine-tune denoising strength (balance noise vs. detail) |
| **Preserve shadows** (advanced only) | Lower = more aggressive shadow denoising |
| **Bias correction** (advanced only) | Correct color cast in shadows: increase if too green, decrease if too purple |

### NL-Means Specific

| Control | Function |
|---------|----------|
| **Central pixel weight (details)** | Low = equal luma+chroma treatment. High = less luma denoising, primarily chroma |
| **Patch size** | Neighborhood comparison size (minimal speed impact) |
| **Search radius** | Search distance for similar patches (speed impact: O(n²)) |
| **Scattering** | Similar to search radius but without computational cost increase |

### Wavelets Specific

The wavelet curves interface provides per-frequency-band control. The Y0 curve controls luminance noise, the U0V0 curve controls color noise.

---

## Demosaicing + Noise Reduction Interaction

The choice of demosaicing algorithm significantly affects noise appearance:

- **LMMSE and IGV** are recommended for high ISO images in conjunction with noise reduction — they prevent false maze patterns and keep images from looking washed-out
- **AMaZE and RCD** can generate overshooting artifacts on noisy images — use LMMSE/IGV instead
- **False color suppression** steps (median filter passes during demosaicing) can help, but reduce color resolution

---

## Raw Denoise (darktable)

Darktable also has a **raw denoise** module operating directly on raw sensor data before demosaicing. This is distinct from the profiled denoise module which works after demosaicing. The raw denoise module removes noise at the sensor data level before CFA interpolation can spread it into patterns.

---

## Noise Profiles: Contributing

If you generate a noise profile for an unsupported camera, submit it to the darktable project. See the [camera support page](https://github.com/darktable-org/darktable/wiki/Camera-support) for details.

---

## References

- darktable denoise (profiled): https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/denoise-profiled/
- darktable raw denoise: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/raw-denoise/
- LibRaw Bayer moire & noise: https://www.libraw.org/articles/bayer-moire.html
