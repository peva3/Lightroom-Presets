# HDR Perceptual Quantization and Transfer Functions

**Source URL:** https://en.wikipedia.org/wiki/Perceptual_quantizer
**Additional sources:** Wikipedia: Transfer functions in imaging, Rec. 2100, HLG
**Date:** PQ Wikipedia revision December 1, 2025 | Transfer functions: March 12, 2026

---

## Overview

Transfer functions in imaging describe the relationship between electrical signals, scene light, and displayed light. The choice of transfer function is critical for HDR imaging: it determines how many bits are needed to avoid visible banding, how much dynamic range can be encoded, and how perceptually uniform the encoding is.

## Fundamental Definitions

### OETF (Opto-Electronic Transfer Function)
The transfer function having scene light as input and converting into the picture/video signal as output. This is typically done within a camera.

### EOTF (Electro-Optical Transfer Function)
The transfer function having the picture/video signal as input and converting it into the linear light output of the display. This is done within a display device.

### OOTF (Opto-Optical Transfer Function)
The transfer function having scene light as input and displayed light as output. The OOTF is the composition of the OETF and the EOTF and is usually non-linear.

## SDR Transfer Functions

### Gamma Curves (Rec. 601, 709, 2020)
Standard dynamic range television uses a gamma-based OETF and the BT.1886 EOTF (which is effectively a 2.4 gamma). The key SDR standards:

- **Rec. 601**: SD-TV reference OETF
- **Rec. 709**: HD-TV reference OETF
- **Rec. 2020**: UHD-TV reference OETF (same OETF as 709, wider gamut primaries)
- **BT.1886**: Reference EOTF for SDR flat panel displays

### sRGB (IEC 61966-2-1:1999)
Used for monitors, printers, and the Web. Uses a gamma curve with a linear portion near black. Approximate gamma of 2.2.

### Linear
RAW formats store linear scene-referred data. Some OETF/EOTF have an initial linear portion followed by a non-linear part (e.g. sRGB and Rec.709).

### Logarithmic
Used by cinema cameras to increase captured dynamic range:
- **S-Log**: Sony
- **Canon Log**: Canon
- **Arri Log C**: Arri

These encode wide dynamic range into a standard bit depth by compressing highlights logarithmically.

## HDR Transfer Functions

### Perceptual Quantizer (PQ) - SMPTE ST 2084

The perceptual quantizer, published by SMPTE as SMPTE ST 2084, is a transfer function that allows for HDR display by replacing the gamma curve used in SDR. Its 0-1 value range represents luminance levels from 0 to 10,000 cd/m2 (nits). It was developed by Dolby and standardized in 2014 by SMPTE and in 2016 by ITU in Rec. 2100.

PQ is the basis of HDR video formats:
- **Dolby Vision**
- **HDR10**
- **HDR10+**

PQ is NOT backward compatible with BT.1886 EOTF (SDR gamma curve), while HLG is compatible.

#### Key Property: Perceptual Uniformity
PQ is a non-linear transfer function based on human visual perception of banding. It can produce no visible banding in 12 bits. A power function (gamma) extended to 10,000 cd/m2 would require 15 bits to achieve the same. This ~3-bit savings makes PQ dramatically more efficient for HDR encoding.

#### PQ EOTF Formula

The PQ EOTF (electro-optical transfer function) is:

```
FD = EOTF[E'] = 10000 * (max[(E'^(1/m2) - c1), 0] / (c2 - c3 * E'^(1/m2)))^(1/m1)
```

The PQ inverse EOTF is:

```
E' = EOTF^-1[FD] = ((c1 + c2 * Y^m1) / (1 + c3 * Y^m1))^m2
```

Where:
- E' is the non-linear signal value, in the range [0, 1]
- FD is the displayed luminance in cd/m2
- Y = FD / 10000 is the normalized linear displayed value
- m1 = 2610/16384 = 0.1593017578125
- m2 = 2523/32 = 78.84375
- c1 = 3424/4096 = 0.8359375 = c3 - c2 + 1
- c2 = 2413/128 = 18.8515625
- c3 = 2392/128 = 18.6875

#### Design Philosophy
The PQ curve is modeled after the Barten CSF (Contrast Sensitivity Function) ramp. It allocates code values according to the human visual system's sensitivity:
- More code values in dark regions (where the eye is most sensitive to banding)
- Fewer code values in bright regions (where visual sensitivity to banding drops)
- Covers the full 0-10,000 nit range with only 10-12 bits

### Hybrid Log-Gamma (HLG)

HLG is a transfer function developed by NHK and BBC for HDR that offers backward compatibility on SDR displays. It is a hybrid transfer function:
- **Lower half** of signal values: Uses a gamma curve (compatible with SDR)
- **Upper half** of signal values: Uses a logarithmic curve (extends to HDR)

This means HLG content can be viewed on SDR displays without a separate SDR grade, though the SDR appearance will differ from a dedicated SDR grade. HLG is standardized in Rec. 2100 as well.

### Rec. 2100

ITU-R Recommendation BT.2100 defines image parameter values for HDR television. It specifies:
- **Two transfer functions**: PQ and HLG
- **Color primaries**: Rec. 2020 (wide color gamut)
- **Bit depth**: 10-bit or 12-bit
- **Resolution**: 3840x2160 (4K) or 7680x4320 (8K)

## Scene-Referred vs Display-Referred Imaging

### Scene-Referred
Scene-referred imaging works with data that represents the original scene light values. The data is linear with respect to scene luminance. Operations are performed in a space proportional to physical light.

**Examples:**
- RAW files from cameras
- ACES2065-1 encoding
- OpenEXR files

**Advantages:**
- Physically accurate
- Consistent results across different display technologies
- Enables proper HDR to SDR conversion
- Future-proof for new display technologies

### Display-Referred
Display-referred imaging works with data that has already been encoded for a specific display. Operations are performed in a space that already includes the display's transfer function.

**Examples:**
- sRGB JPEGs
- Rec. 709 video

**Limitations:**
- Tied to a specific display standard
- Dynamic range is fixed (typically ~8 stops)
- Cannot properly represent scene values beyond the display's range
- Converting between display standards can introduce artifacts

### The ACES Approach
ACES is a pure scene-referred system:
1. Camera-native data is converted to ACES2065-1 (linear, wide-gamut, scene-referred) via Input Transforms
2. All creative work happens in scene-referred space
3. Output Transforms (Rendering Transform + Display Encoding) convert to specific display formats at the very end

This separation of creative intent from display technology is the key architectural insight of modern color pipelines.

## Practical Implications for Photo Editing

### Why 10-bit Matters for HDR
- 8 bits with gamma: ~256 levels (visible banding in smooth gradients)
- 10 bits with PQ: ~1024 levels (no visible banding up to 10,000 nits)
- 12 bits with PQ: ~4096 levels (necessary for 10,000+ nit mastering)

### RAW Development Pipeline
```
Sensor Data → Linearization → Demosaicing → White Balance → 
Scene-Referred Processing (exposure, highlight recovery) → 
Color Space Transform → Tone Mapping → Display-Referred Output
```

### ISO 21496-1 Gain Maps
A modern approach for HDR still images: store an SDR base image plus a "gain map" that describes how to recover the HDR information. This is:
- Backward compatible (SDR displays see the base image)
- Forward compatible (HDR displays use the gain map for full dynamic range)
- Supported by Apple (Adaptive HDR), Google (Ultra HDR), Samsung (Super HDR)

## HDR Display Standards

### Ultra HD Alliance Premium Certification
- Peak brightness > 1000 cd/m2 AND black level < 0.05 cd/m2 (contrast > 20,000:1)
- OR peak brightness > 540 cd/m2 AND black level < 0.0005 cd/m2 (contrast > 1,080,000:1)
- Color gamut: > 90% DCI-P3
- Bit depth: 10-bit

### HDR Static Metadata (SMPTE ST.2086)
- **MaxFALL** (Maximum Frame Average Light Level)
- **MaxCLL** (Maximum Content Light Level)
- Color primaries and white point of the mastering display

### HDR Dynamic Metadata (SMPTE ST 2094)
Allows scene-by-scene or frame-by-frame optimization:
- Dolby Vision metadata
- HDR10+ metadata

## Key References

1. SMPTE ST 2084:2014 - High Dynamic Range Electro-Optical Transfer Function of Mastering Reference Displays
2. ITU-R BT.2100 - Image parameter values for HDR television
3. Dolby Vision Whitepaper
4. ITU-R BT.1886 - Reference EOTF for flat panel displays
5. ITU-R BT.709 - HDTV parameter values
6. IEC 61966-2-1:1999 - sRGB
7. ISO 21496-1 - Gain Map specification
