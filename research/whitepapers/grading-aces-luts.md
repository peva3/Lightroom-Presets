# ACES Color Pipeline and LUT Design for Photographers

**Sources:**
- ACESCentral Knowledge Base — LMTs Part 1 (https://acescentral.com/knowledge-base-2/lmts-part-1-what-are-they-and-what-can-they-do-for-me/) — Created Feb 2017, Updated Apr 2020
- ACESCentral Knowledge Base — LMTs Part 2 (https://acescentral.com/knowledge-base-2/lmts-part-2-how-do-they-work-and-how-are-they-made/) — Created Aug 2017, Updated Apr 2020
- ACESCentral Knowledge Base — ACES Primer (https://acescentral.com/knowledge-base-2/aces-primer-and-quick-start-guides/) — Apr 2020
- ACES Documentation (https://docs.acescentral.com/)

**Author:** Scott Dyer (ACESCentral), supplemented by ACES Documentation contributors

---

## What is ACES?

The Academy Color Encoding System (ACES) is an industry standard for managing color and digital files throughout the lifecycle of almost any media production, from motion pictures to television, video games, or immersive storytelling projects. ACES ensures a consistent color experience to preserve the creator's vision through all phases of production — from image capture through editing, VFX, mastering, public presentation, archiving, and future remastering.

ACES is free and open-source with dozens of companies having built ACES components into their tools.

### Why Use ACES?

- Simplify camera matching in Digital Intermediate
- Preserve original camera fidelity
- Remove ambiguity in communication of image files in multi-vendor workflows
- Add reliability to the color viewing pipeline
- Streamline the creation of multiple outputs
- Create a "known quantity" master for the archive

---

## The ACES Pipeline Architecture

The core workflow:
```
Camera Native → Input Transform → ACES2065-1 → [LMT] → Output Transform → Display
```

### Key Components

1. **Input Transforms (IDTs)**: Convert camera-native RGB (e.g., ARRI LogC, Sony S-Log3, RED Log3G10) into the ACES2065-1 linear color space
2. **ACES2065-1**: The archival, scene-referred working space with AP0 primaries — encompasses the entire visible spectrum
3. **Look Modification Transforms (LMTs)**: Optional ACES-to-ACES transforms for creative looks
4. **Output Transforms (ODTs)**: Convert ACES2065-1 to display-referred color spaces (Rec.709, P3, Rec.2020)

### ACES Color Spaces

- **ACES2065-1**: Linear, scene-referred, AP0 primaries — the archival format
- **ACEScg**: Linear, AP1 primaries — optimized for VFX/CGI workflows
- **ACEScct**: Log encoding with AP1 primaries — designed for color grading (similar feel to LogC/CLog)
- **ACEScc**: Alternative log encoding for grading
- **ACESproxy**: Lightweight encoding for on-set monitoring

---

## Look Modification Transforms (LMTs)

LMTs provide a mechanism to apply an infinite variety of "looks" to images in ACES-based workflows. LMTs are always ACES-to-ACES transforms: ACES2065-1 data is manipulated by the LMT to output new ACES2065-1 data (designated as ACES') that is then viewed through an ACES Output Transform.

### What LMTs Can Do

1. **Set a starting look** different from the default ACES rendering
2. **Apply project-wide adjustments** to reduce contrast/saturation across all shots
3. **Encapsulate preset creative looks** (e.g., film print emulation)
4. **Match camera-specific renderings** within an ACES workflow
5. **Create a library of looks** for reuse across projects

### The Rendering Concept

Camera-native image files are typically encoded in manufacturer-specific RGB spaces and log encodings designed to preserve maximum scene information:
- ARRI: ALEXA WideGamut / Log C
- Canon: Cinema Gamut / Canon Log 2
- Panasonic: V-Gamut / V-Log
- RED: REDWideGamutRGB / Log3G10
- Sony: S-Gamut3 / S-Log3

These unrendered images appear flat and desaturated — they must be processed through a rendering transform. In traditional film workflow, Cineon Log scans were viewed through Print Film Emulations (PFEs). In ACES, the equivalent is the Output Transform.

### Interchangeability of LMTs

The critical advantage of ACES: once in ACES, well-designed LMTs are interchangeable. An LMT designed to match a camera-specific rendering can be used for other cameras. Print film emulation LMTs can be used with digital cameras.

This works because disparate camera-specific encodings are translated into a common encoding space (ACES2065-1), enabling looks to be reusable within all contexts, regardless of image source.

---

## LMT Types and Construction

### Empirical LMTs

Derived from sampling another color reproduction process. Typically implemented as 3D LUTs that encapsulate a subsampling of the target process.

**Example: Matching a Print Film Emulation**

A grid of carefully selected ACES values is converted to ADX10 (density encoding), sent through the PFE 3D-LUT, resulting in X'Y'Z' code values. Those values are processed through the Inverse Output Transform for the target display, yielding ACES' values that encapsulate the PFE look.

**Example: Matching a Camera LUT**

ACES values are converted to a camera's native encoding (via inverse Input Transform), sent through the camera manufacturer's LUT, then processed through the Inverse Output Transform back to ACES'. The mapping is stored as a 3D-LUT.

### Analytic LMTs

Defined mathematically as a set of ordered operations. Examples include:
- ASC CDL (slope, offset, power per channel + global saturation)
- Channel mixing / matrix operations
- Custom tone curve functions
- Gamut compression

### Limitations of Empirical LMTs

Because empirical LMTs are derived from output-referred data, their dynamic range and color gamut are limited to the target transform. For example, a Rec.709 output-referred LUT will clip to Rec.709 gamut and standard dynamic range, even when viewed through a P3 or HDR Output Transform.

**Recommendation**: Empirical LMTs should only be used when necessary to exactly match an existing look, and should NOT be "baked in" to ACES data.

Analytic LMTs can preserve the full dynamic range of the original ACES-encoded imagery.

---

## LUT Design: 1D vs 3D LUTs

### 1D LUTs
- Map each input channel independently
- 3 separate curves for R, G, B
- Can adjust: exposure, contrast, gamma, white balance (channel gain)
- Cannot: shift hue, change saturation independently of brightness, do complex color transforms
- Small, fast, predictable

### 3D LUTs
- Map any RGB input triplet to any RGB output triplet
- Can perform: hue rotation, selective saturation, complex non-linear cross-channel transforms
- Size grows as cube of grid dimension: 17³ = ~5K entries, 33³ = ~36K entries, 65³ = ~275K entries
- Require trilinear or tetrahedral interpolation
- The standard format for film emulation and creative looks

### Common LUT Format (CLF)

ACES defines the Common LUT Format (CLF) as a standardized way to describe color transforms as XML files. CLF supports:
- 1D and 3D LUTs
- ASC CDL operations
- Matrix operations
- Range and log conversions
- Multiple operations in sequence

---

## Relevance to Still Photography and Lightroom Presets

### Parallel Concepts

| ACES Concept | Lightroom Equivalent |
|---|---|
| Input Transform | Camera Profile (Adobe Color, Camera Matching) |
| ACES2065-1 / ACEScct | Internal working color space (Melissa RGB) |
| LMT | Develop preset / user adjustments |
| Output Transform | Export color space (sRGB, Adobe RGB, ProPhoto) |

### Lessons for Preset Design

1. **Scene-referred thinking**: Preserve original data fidelity; make edits non-destructive and modular
2. **Look interchangeability**: A well-designed preset should work across different camera models (like LMTs work across cameras in ACES)
3. **Separation of concerns**: Foundation (WB, exposure, tone curve) → Character (HSL, color grading) → Output rendering (camera profile, process version)
4. **Empirical vs. analytic approaches**: Film emulation presets are like empirical LMTs — sampled from real film behavior. Creative presets are like analytic LMTs — mathematically defined.
5. **Avoid baking in limitations**: Don't clip dynamic range with extreme tone curve or HSL adjustments early in the pipeline
6. **The profile is the foundation**: Just as ACES requires proper Input and Output Transforms, Lightroom presets need correct ProcessVersion, Treatment, and Look (camera profile) settings
