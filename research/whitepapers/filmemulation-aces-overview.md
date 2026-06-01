# ACES (Academy Color Encoding System): Foundation for Film Emulation

**Source URL:** https://docs.acescentral.com/
**Author:** Academy of Motion Picture Arts and Sciences / Academy Software Foundation
**Date:** 2024–2025 (continuously updated)

**Document Source:** ACES Documentation — Getting Started

---

## What Is ACES?

The Academy Color Encoding System (ACES) is an **industry standard for managing color** and digital files throughout the lifecycle of any media production, from motion pictures to television, video games, and immersive storytelling.

ACES ensures a consistent color experience to preserve the creator's vision through all phases of production — image capture, editing, VFX, mastering, public presentation, archiving, and future remastering.

ACES is **free and open-source**, and dozens of companies have built ACES components into their tools.

## Why Use ACES?

ACES helps to:
- Simplify camera matching in DI (Digital Intermediate)
- Preserve original camera fidelity
- Remove ambiguity in communication of image files in multi-vendor workflows
- Add reliability to the color viewing pipeline
- Streamline the creation of multiple outputs
- Create a "known quantity" master for the archive

---

## ACES Components

### Encodings

ACES defines several standard color encodings:

- **ACES2065-1** — The archival format using the AP0 primaries, a wide-gamut scene-referred working space. 16-bit floating point linear encoding. This is the "master" encoding from which all other representations derive.

- **ACEScg** — A working space for visual effects and CGI, using AP1 primaries (smaller than AP0, optimized for common working gamuts).

- **ACEScct** — A log-encoded version of ACES optimized for color grading, providing a "quasi-logarithmic" encoding that distributes code values perceptually.

- **ACEScc** — A pure logarithmic encoding of ACES, also designed for color grading operations.

- **ACESproxy** — A lightweight integer encoding of ACES for use on-set and in monitoring applications.

- **APD (Academy Printing Density)** — A densitometric encoding representing film printing density.

- **ADX (Academy Density Exchange)** — A standardized encoding for exchanging film density data from scanners.

### Color Space Architecture

```
AP0 (ACES2065-1 primaries) — The largest set, encompassing all real-world colors
  └── AP1 (ACEScg, ACEScct primaries) — Optimized for production workflows
```

The AP0 primaries were chosen to encompass the entire spectral locus, ensuring no gamut clipping occurs when converting between real-world camera spaces.

### ACES White Point

The ACES system uses a **D60 white point** (correlated color temperature approximately 6000K), chosen as a compromise between D65 (daylight standard, ~6500K) and D55 (midday sunlight, ~5500K). This choice balances daylight and tungsten capture scenarios.

---

## Transforms

### Input Transforms (IDTs)

Input Transforms convert camera-native image data into ACES2065-1. Each camera manufacturer has a specific IDT:
- ARRI → ALEXA WideGamut/Log C → IDT → ACES2065-1
- RED → REDWideGamutRGB/Log3G10 → IDT → ACES2065-1
- Sony → S-Gamut3/S-Log3 → IDT → ACES2065-1
- Canon → Cinema Gamut/Canon Log 2 → IDT → ACES2065-1
- Panasonic → V-Gamut/V-Log → IDT → ACES2065-1

IDTs are defined by an Academy procedure (P-2013-001) that specifies how to measure camera response and derive the mathematical transform.

### Output Transforms (ODTs)

Output Transforms convert ACES data to specific display devices. The structure includes:
1. **Tone Mapping** — Controls the transition from scene-referred linear to display-referred
2. **Chroma Compression** — Handles out-of-gamut colors
3. **Gamut Compression** — Maps wide-gamut ACES data to display gamut
4. **White Limiting** — Controls maximum brightness
5. **Display Encoding** — Final gamma or PQ encoding for the target display

### Look Transforms (LMTs)

Look Modification Transforms modify ACES data to achieve creative looks. They are ACES-to-ACES transforms, meaning they operate entirely within the scene-referred domain. This makes them portable across all input and output configurations.

---

## Reference Gamut Compression (RGC)

ACES 2.0 introduced Reference Gamut Compression, a standardized algorithm for handling extreme gamut values (e.g., LED lighting, lasers). RGC compresses out-of-gamut values in a perceptually uniform manner, preventing clipping artifacts while preserving the visual appearance of in-gamut content.

---

## Common LUT Format (CLF)

The Common LUT Format is the standardized file format for Look Transforms. CLF supports:
- **1D LUTs** — Including half-domain floating point LUTs for ACES
- **3D LUTs** — For complex, empirically derived transforms
- **Matrices** — For primary color space conversions
- **ASC CDL** — For primary grading operations (slope, offset, power, saturation)
- **Range definitions** — Input and output ranges for every node
- **Inverse shaper LUTs** — For proper LUT interpolation in log-like spaces

---

## ACES Metadata File (AMF)

The AMF is a standardized container for metadata describing the ACES pipeline for a production. It can reference:
- Camera types and Input Transforms used
- Look Transforms applied
- Output Transforms for various deliverables
- Grading metadata

This ensures portability and archiving: anyone receiving ACES files can reconstruct the entire color pipeline.

---

## Relevance to Film Emulation

ACES provides the ideal framework for film emulation because:

1. **Scene-referred architecture** — Film emulation naturally operates on scene-referred data (what the camera captured), applying transforms that simulate how film would have rendered that scene.

2. **Normalized input** — Regardless of capture device, all sources are normalized to ACES, so a single film emulation Look Transform works for any source.

3. **Print Film Emulation compatibility** — ACES preserves the Cineon-to-PFE pipeline concept, allowing traditional PFE 3D-LUTs to be wrapped as Look Transforms.

4. **Preserved dynamic range** — Well-designed Look Transforms preserve dynamic range, ensuring emulation doesn't clip highlights or crush shadows that could be recovered.

5. **Standardized transport** — CLF and AMF ensure film emulation presets are portable and archivable.

---

## ACES Standards

ACES is standardized through SMPTE (Society of Motion Picture and Television Engineers) and maintained by the Academy Software Foundation (ASWF) at https://github.com/aces-aswf/.
