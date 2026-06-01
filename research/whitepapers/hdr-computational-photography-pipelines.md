# Computational Photography Pipelines: ProRAW, HDR+, and ACES

**Source URLs:**
- https://en.wikipedia.org/wiki/Computational_photography
- https://en.wikipedia.org/wiki/High-dynamic-range_imaging
- https://docs.acescentral.com (ACES Documentation)
- https://gregbenzphotography.com/hdr/ (Greg Benz - HDR Practical Guide)
**Date:** Wikipedia revisions Dec 2025, ACES docs Sept 2025

---

## Overview

Computational photography refers to digital image capture and processing techniques that use digital computation instead of optical processes. It can improve camera capabilities, introduce features impossible with film-based photography, or reduce the cost/size of camera elements.

## Taxonomy of Computational Photography

According to Shree K. Nayar's taxonomy, computational photography encompasses:

### 1. Computational Illumination
Controlling photographic illumination in a structured fashion, then processing the captured images. Applications include image-based relighting, image enhancement, image deblurring, geometry/material recovery.

**Key technique: High Dynamic Range (HDR) Imaging**
Uses differently exposed pictures of the same scene to extend dynamic range. The process:
1. Capture multiple exposures (typically -2EV, 0EV, +2EV)
2. Estimate the camera response function
3. Merge exposures into a radiance map (HDR image)
4. Apply tone mapping for display

### 2. Computational Optics
Capture of optically coded images, followed by computational decoding:
- **Coded aperture imaging**: Applied in astronomy and X-ray imaging
- **Coded exposure imaging**: Shutter on/off state is coded to modify motion blur kernel, making deblurring well-conditioned
- **Lens-based coded aperture**: Mask-modified aperture for well-conditioned defocus deblurring

### 3. Computational Imaging
Combines data acquisition and processing to create images through indirect means, yielding enhanced resolution, additional information (optical phase, 3D reconstruction). Common techniques:
- Lensless imaging
- Computational speckle imaging
- Ptychography and Fourier ptychography

### 4. Computational Processing
Processing of non-optically-coded images to produce new images.

### 5. Computational Sensors
Detectors that combine sensing and processing, typically in hardware (e.g., oversampled binary image sensor).

## Apple ProRAW

Apple ProRAW combines the flexibility of RAW with Apple's computational photography pipeline.

### Key Features
- **12-bit DNG format** with embedded semantic information
- **Multi-frame processing**: Merge multiple exposures for noise reduction and dynamic range
- **Deep Fusion**: Pixel-by-pixel neural processing for optimal texture, detail, and noise
- **Smart HDR**: Intelligent highlight recovery and shadow lifting
- **Linear scene-referred data**: The DNG contains linearized, demosaiced data ready for editing
- **Embedded gain map**: Supports HDR display on compatible devices

### Pipeline
```
Sensor Capture → Multiple Exposures → Deep Fusion/Smart HDR →
Demosaicing → White Balance → Lens Correction → 
Linear Scene-Referred DNG → Editing Applications
```

### ProRAW vs Traditional RAW
- Traditional RAW: Raw sensor data, no processing applied
- ProRAW: Computational photography applied, but delivered as linear DNG
- ProRAW retains highlight recovery headroom (~2-3 stops above clipping)
- Noise reduction is partially applied (neural, not destructive)
- Tone mapping from the computational pipeline is NOT baked in

## Google HDR+ Pipeline

Google's HDR+ is a burst photography system for high dynamic range and low-light imaging on mobile cameras, described in the seminal SIGGRAPH 2016 paper "Burst photography for high dynamic range and low-light imaging on mobile cameras" by Hasinoff et al.

### Pipeline Overview
```
Burst Capture → Frame Alignment → Merge → 
Tone Mapping → Sharpening → Output
```

### Key Stages

1. **Burst Capture**: Continuous shooting of 8-15 underexposed frames
   - Underexposure protects highlights
   - Short exposures reduce motion blur

2. **Frame Alignment**: Dense pairwise alignment using tile-based 2D translation
   - Tiles with low alignment confidence are rejected
   - Robust to local motion (moving objects)

3. **Merge**: Temporal denoising and dynamic range extension
   - Use Wiener filter in the frequency domain
   - Weighted by alignment confidence and noise estimate
   - Merging underexposed frames effectively extends dynamic range

4. **Tone Mapping**: Local tone mapping for display
   - Reinhard-style global operator as base
   - Local dodging and burning for contrast
   - S-shaped curve for highlight and shadow rolloff

5. **Spatially Varying Sharpening**: Detail enhancement that varies by local SNR
   - Stronger sharpening in high-SNR regions
   - Weaker or no sharpening in low-SNR (dark) regions

### Night Sight Mode
Extension of HDR+ for extreme low light:
- Longer exposures per frame
- More frames (up to 15)
- Motion metering to adjust exposure per frame based on detected motion
- Learning-based white balance via neural network

## Apple Deep Fusion

Introduced in iPhone 11 (2019), Deep Fusion is a neural image processing pipeline:

### Pipeline
```
4 Short Frames + 1 Long Exposure → AI Analysis → 
Pixel-by-Pixel Selection/Blend → Final Array of Pixels
```

### Stages
1. Camera captures 4 short-exposure frames and 1 long-exposure frame before the shutter press
2. When shutter is pressed, a single "reference" frame is captured
3. Neural network analyzes all frames pixel-by-pixel
4. For each pixel, the network selects the optimal source or blends multiple sources
5. Result optimizes for texture detail in mid-tones, noise reduction in shadows, and sharpness overall

## ACES (Academy Color Encoding System)

### Overview
ACES is an industry standard for managing color throughout the lifecycle of media production, from motion pictures to television, video games, and immersive storytelling. It is free and open-source.

### Core Architecture

```
Camera 1 → Input Transform ─┐
Camera 2 → Input Transform ─┤
CGI ────→ ACEScg to ACES ──┼──→ ACES (Scene-Linear) ──→ Rendering Transform ──→ Display Encoding ──→ Output
                                                         ──→ Rendering Transform ──→ Display Encoding ──→ Output
                                                         ──→ Rendering Transform ──→ Display Encoding ──→ Output
```

### Key Components

#### Transforms
- **Input Transforms (IDTs)**: Convert camera-native data into ACES2065-1
- **Color Space Conversion Transforms (CSCs)**: Convert between color encodings
- **Output Transforms (ODTs)**: Prepare scene-linear ACES data for display
  - Rendering Transform: Scene-referred → display-referred color space
  - Display Encoding Transform: Colorimetry → display signal
- **Look Transforms (LMTs)**: Technical or creative adjustments in scene-referred space
- **Reference Gamut Compression**: Technical LMT for out-of-gamut values (ACES 1.3+)

#### Encodings
- **ACES2065-1**: Linear encoding in wide-gamut RGB (AP0); core interchange encoding
- **ACEScg**: Linear encoding with AP1 primaries; optimized for CGI/compositing
- **ACEScct**: Logarithmic encoding with AP1 primaries; for scene-referred grading
- **ACEScc**: Logarithmic encoding variant
- **ACESproxy**: Lightweight integer encoding for on-set monitoring
- **APD (Academy Printing Density)**: Based on spectral characteristics of film print stocks
- **ADX**: Integer encoding of APD for film scanning workflows

### ACES 2 Rendering Transform

The ACES 2 Output Transform pipeline processes scene-linear data through sequential stages:

```
ACES RGB Input
  → ACES to JMh (perceptually uniform color space)
  → Tonescale (J channel only, S-shaped Michaelis-Menten curve)
  → Chroma Compression (M channel only, manages saturation at extremes)
  → Gamut Compression (J & M, handles out-of-gamut colors)
  → White Limiting (prevents highlight color shifts)
  → Display Encoding (converts to display signal)
  → Display RGB Output
```

### Benefits of ACES
- Simplifies camera matching in DI
- Preserves original camera fidelity
- Removes ambiguity in multi-vendor workflows
- Adds reliability to color viewing pipeline
- Streamlines creation of multiple outputs (SDR, HDR, cinema)
- Creates a "known quantity" master for archive

## Modern Mobile Computational Photography

### Multi-Frame Super Resolution
Combines multiple frames with sub-pixel shifts to reconstruct a higher-resolution image. Used in Google's Super Res Zoom and similar implementations.

### Portrait Mode / Synthetic Bokeh
- Dual-pixel or multi-camera depth estimation
- Semantic segmentation for subject/background separation
- Physically-based defocus rendering

### Night Mode
- Long multi-frame capture with alignment
- Motion-adaptive exposure
- Learning-based noise reduction and color correction

### Semantic Segmentation and Local Processing
Modern pipelines segment the image into semantic regions (sky, skin, foliage, etc.) and apply different processing parameters per region:
- Sky enhancement
- Skin tone optimization
- Texture preservation in foliage

## Displays and HDR Photography (Practical Guide)

### Capture
Any camera works for HDR photography. RAW files capture ~14 stops of dynamic range, which is sufficient for HDR displays. Exposing to the right (ETTR) maximizes quality. Even 8-bit JPEG midjourney/AI-generated images can be converted to HDR.

### Editing HDR in Lightroom
- Enable HDR mode in the histogram panel
- Use the HDR-specific sliders for highlight brightness
- SDR settings continue to work for the SDR portion
- Gain map metadata is automatically embedded on export

### HDR Formats for Still Images
- **ISO 21496-1 Gain Map**: Universal standard (Apple + Adobe unified)
- **AVIF + Gain Map**: 50% size reduction vs JPEG, higher quality, transparency support
- **JPEG XL + Gain Map**: Higher resolution, 32-bit capability
- **HEIC/HEIF**: Apple's native HDR format

### Browser Support for HDR Images (as of 2025)
- **Full support**: Safari 26+, Chrome, Edge, Brave, Opera, Vivaldi, Arc
- **Partial**: Comet (Perplexity)
- **Not supported**: Firefox (falls back to SDR via gain map)

## Key References

1. Hasinoff, S.W. et al. (2016). "Burst photography for high dynamic range and low-light imaging on mobile cameras." SIGGRAPH 2016.
2. Mann, S. (1993). "Compositing Multiple Pictures of the Same Scene." IS&T 46th Annual Conference.
3. Reinhard, E. et al. (2005). "High Dynamic Range Imaging: Acquisition, Display, and Image-Based Lighting." Morgan Kaufmann.
4. ACES Documentation - https://docs.acescentral.com
5. Apple ProRAW - developer.apple.com/documentation/avfoundation/photo_capture
6. ISO 21496-1 - Gain Map specification
7. Nayar, S.K. (2007). "Computational Cameras." Conference on Machine Vision Applications.
