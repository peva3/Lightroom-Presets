# LMTs: Look Modification Transforms — The Complete Guide

**Source URL:** https://acescentral.com/knowledge-base-2/ (Parts 1-4)
**Author:** Scott Dyer (for the Academy of Motion Picture Arts and Sciences)
**Date:** February–September 2017 (Last Updated: July 2020)

**Document Source:** ACESCentral Knowledge Base, Academy Color Encoding System (ACES)

---

## Part 1: What Are LMTs and What Can They Do For Me?

Look Modification Transforms (LMTs) are a very powerful component of the Academy Color Encoding System and offer extraordinary flexibility in ACES-based workflows.

**LMTs provide a mechanism to apply an infinite variety of "looks" to images in ACES-based workflows.** LMTs are always ACES-to-ACES transforms. ACES2065-1 data directly translated from camera-native image data via an Input Transform is manipulated by the LMT to output new ACES2065-1 data (designated as ACES') that is then viewed through an ACES Output Transform.

### Types of LMT Applications

LMTs can be used to set a "starting look" different from the default rendering associated with an ACES Output Transform. By this definition, a "look" can be as simple as ASC CDL values preserved from set to define a starting grade.

LMTs can be used project-wide to reduce contrast and saturation across all shots, providing a preferred starting point for colorists accustomed to flatter and more muted starting images.

LMTs can encapsulate preset creative looks. Very complex creative looks, such as **film print emulation**, are more easily modeled in a systematically derived transform than by asking a colorist to manually match using only the controls in a color corrector. Over time, a collection of LMTs may be collected into a **"library of looks"**.

LMTs are image-wide; they cannot capture power windows, mattes, etc.

### Rendering: Film vs Digital

Traditional film scans (Cineon Log) were viewed through **print film emulations (PFEs)**. A Cineon-encoded DPX film scan appears flat and desaturated in its native log-encoded state, but viewed through a PFE gains contrast and saturation. This basic concept of a default scene-referred to display-referred rendering transform is not new.

Digital camera-native images (ARRI Log C, RED Log3G10, Sony S-Log3, etc.) must also be processed through camera-specific rendering transforms. In ACES, all camera types use Input Transforms to convert camera-native encodings into ACES2065-1, meaning any camera can be viewed through the ACES processing path.

### Matching Existing Looks

An LMT can be inserted in the ACES rendering chain to match a camera-specific rendering or any other desired starting point. Once in ACES, **well-designed LMTs are interchangeable** — a PFE LMT can be used with digital cameras, or a camera-specific LMT can be used for different cameras. Because all camera encodings are translated into ACES2065-1, looks are reusable within all contexts.

---

## Part 2: How Do LMTs Work and How Are They Made?

### LMT Types

LMTs can be characterized as either **"empirical"** or **"analytic"**.

**Empirical LMTs** are derived from sampling another color reproduction process and are typically implemented as 3D LUTs. **Analytic LMTs** are defined mathematically as a set of ordered mathematical operations to adjust ACES values.

### Empirical LMTs

#### Example 1: Match Print Film Emulation (PFE)

An empirical LMT implementing a PFE is a 3D-LUT that expects 10-bit log DPX as input and supplies X'Y'Z' code values as output. A grid of carefully selected ACES values is converted to ADX10, sent through the PFE 3D-LUT (producing X'Y'Z' code values), then processed through the Inverse Output Transform for DCDM (combined Inverse ODT and Inverse RRT). This yields ACES' values encapsulating the PFE mapping. This input-to-output relationship is saved as a 3D-LUT that becomes a PFE LMT.

#### Example 2: Match Vendor LUT X

Using inverse Input Transforms, ACES values are converted to the camera-specific encoding needed for "LUT X" input. The output goes through the Inverse Output Transform to produce ACES' values. The mapping is stored as a 3D-LUT to recreate the look within ACES.

### Limitations of Empirical LMTs

Because empirical LMTs are derived from output-referred data, the range of output values is limited to the dynamic range and color gamut of the original transform. **It is recommended empirical LMTs only be used when necessary to exactly match an existing look.** Empirical LMTs should not be "baked in" to ACES data.

Analytic LMTs can avoid this limitation because they do not use inverse Output Transforms.

---

## Part 3: Analytic LMTs

Analytic LMTs are defined mathematically and expressed as a set of ordered mathematical operations on color component values. There is no limit to the order or number of operations, nor to the number of individual LMTs that may be sequenced.

### Example 1: Lower Contrast & Saturation

A simple analytic LMT converts ACES2065-1 to ACEScct, applies ASC CDL adjustments (slope, offset, power, saturation), and converts back. An alternate approach applies a gamma adjustment directly in linear ACES space, which produces a different curve behavior — the gamma curve continues to extend to zero without the flare-up seen with CDL in ACEScct.

### Example 2: Neutral Tone Scale Match

To match exactly the neutral tone scale rendering of another transform (e.g., "LUT X"), a 1D-LUT is derived. A ramp of neutral ACES values is converted to the camera encoding, processed through LUT X, then through the Inverse Output Transform, producing ACES' values. This 1D-LUT is extrapolated in log space (linear extrapolation in log-log space) to support a much larger range of ACES values beyond the original ~10 stops.

### Example 3: Complex Print Film Emulation Look

A chain of operations approximating a print film emulation:
1. **Reduce "chroma"** — Convert to YCH, multiply C channel by scalar (0.7)
2. **ASC CDL adjustment** — Minor blue slope/offset shift for yellow balance
3. **Gamma adjust** — Contrast boost (gamma 1.5) in linear space
4. **Hue-qualified secondary corrections** — Using cubic basis shaper functions for smooth transitions:

- Rotate R toward Y (center 0°, width 30°, amount +5°)
- Rotate G toward Y (center 80°, width 60°, amount -15°)
- Rotate Y toward R (center 52°, width 50°, amount -14°)
- Boost chroma in Y (center 45°, width 40°, scale 1.4)
- Rotate C toward B (center 190°, width 40°, amount +30°)
- Boost chroma in B (center 45°, width 40°, scale 1.4)

### Yab and YCH Color Spaces

Yab is a lightness/opponent color space (a rotated RGB unit cube with the neutral axis vertical). YCH is the cylindrical representation where C is distance from the neutral axis and H is hue angle in degrees. These are used for targeting specific lightness, hues, or chroma.

### Cubic Basis Shaper Function

To avoid harsh transitions, a cubic basis shaper function tapers from full power (1.0) at the center hue down to zero at the desired region width:

```
fH = 1 - (3 * (dH/width)^2) + (2 * (dH/width)^3)
```

where dH is the magnitude of hue distance from the centered hue.

---

## Part 4: Complex LMTs — Bleach Bypass and Parallel Processing

### Example 4: Bleach Bypass / Skip Bleach

This LMT recreates a "bleach bypass" or "skip bleach" look using a node graph with parallel color correction blended together.

**Processing chain:**
Two copies are made from input ACES2065-1 data:
- **Node A:** Slightly desaturated (sat=0.9), exposure doubled (scale 2.0)
- **Node B:** Fully desaturated (sat=0.0), contrast boosted (gamma 1.2)

The two modified copies are blended using the **"overlay" blending mode** in ACEScct space.

### Implementation Notes

The Common LUT Format (CLF) is designated as the official carrier for LMTs. CLF can encapsulate 1D LUTs, 3D LUTs, matrices, and ASC CDL operations. Math formulas must be sampled to LUTs for CLF implementation.

ACES values are radiometrically linear with very wide floating-point range. Spacing nodes directly in linear space does not always provide good sampling. CLF provides forward/inverse 'shaper LUT' operations that, when wrapped around an appropriately constructed 3D-LUT, produce well-spaced LUTs with minimal interpolation errors.

### Key Takeaways

1. **LMTs are ACES-to-ACES transforms** that modify appearance while preserving scene-referred data
2. **Empirical LMTs** (3D LUTs) exactly match existing looks but limit dynamic range/gamut
3. **Analytic LMTs** (mathematical operations) preserve full dynamic range and can be arbitrarily complex
4. **LMTs are interchangeable** — a PFE LMT works with any camera source
5. Complex hue-qualified operations use Yab/YCH spaces with smooth cubic basis shapers
6. CLF is the portable format for LMT transport
7. LMTs enable **libraries of looks** that can be re-used across productions

---

**Supporting CTL transforms** (original Dropbox links):
- LMT.Academy.Empirical_1.ctl — PFE match
- LMT.Academy.Empirical_2.ctl — LUT X match
- LMT.Academy.Analytic_1a.ctl — Lower contrast/saturation (CDL in ACEScct)
- LMT.Academy.Analytic_1b.ctl — Even lower contrast/saturation
- LMT.Academy.Analytic_1c.ctl — Lower contrast/saturation in linear
- LMT.Academy.Analytic_2.ctl — 1D-LUT tonescale match
- LMT.Academy.Analytic_3.ctl — Complex PFE-like look with hue-qualified adjustments
- LMT.Academy.Analytic_4.ctl — Bleach bypass using overlay blend mode

Dependencies: aces-dev, ACESlib.LMT_Common.ctl
