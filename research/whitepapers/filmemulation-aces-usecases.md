# ACES Look Transforms: Use Cases for Film Emulation and Creative Grading

**Source URL:** https://docs.acescentral.com/system-components/look-transforms/use-cases/
**Author:** Academy Color Encoding System (ACES) Documentation
**Date:** September 2025

**Document Source:** ACES Documentation — Technical Details, Look Transforms

---

## Introduction

Two styles of image modification are common in post-production:
- **Interactive modification** — either across the entire frame or in isolated regions ("grading")
- **Preset systematic modification** — across the entire frame ("look modification")

The ACES term for preset systematic, full-frame image modification is **Look Modification**, performed using a **Look Transform** (historically abbreviated LMT, from "Look Modification Transform").

---

## Use Case 1: Emulation of Photochemical Processing

Some whole-frame color transformations are too complex for even a skilled colorist to accomplish using grading system controls. The complexity often arises when simulating the nonlinear color and exposure relationships used in film laboratory photochemical processing.

### Examples of Photochemical Emulations

- **Bleach Bypass / Skip Bleach:** Modification of color values to achieve a desaturated appearance mimicking projection of a print that had skipped the normal laboratory bleaching step. This produces a distinctive desaturated, high-contrast look.

- **Technicolor 3-Strip Emulation:** Modification of color values to achieve a saturated, higher-contrast appearance mimicking projection of a print from Technicolor's imbibition dye transfer process (c. 1938).

- **Kodak Vision 3 Print Film Emulation:** Modification of color values to achieve reproduction of the relationship between scene exposure values and projected film imagery resulting from the use of Kodak's latest film stocks.

### Workflow

In an ACES pipeline, one or more emulation Look Transforms are prepended to the RRT (which itself precedes a selected ODT). The colorist applies grading adjustments first, followed by the process emulation provided by the Look Transform(s). This allows the colorist's time to be spent on sequence-, shot-, and region-specific creative color requests from clients.

---

## Use Case 2: Systematic Color Correction and ASC CDL

Look Transforms take ACES input and yield ACES output, meaning they can be **chained together** sequentially. In a typical workflow:
1. An "ASC CDL" Look Transform is applied (with values chosen by the cinematographer on-set)
2. A "Kodak Vision 3 emulation" Look Transform follows

The ASC CDL values are only valid in the context of the selected emulation. If the emulation Look Transform is removed, the ASC CDL values may no longer be valid. CLF (Common LUT Format) supports wrapping ASC CDL operations with ACES↔ACEScc conversions before and after.

---

## Use Case 3: Trim Pass Grading

Content is delivered across a wide range of output devices, each with their own color space and characteristic brightness. Different Look Transforms can be prepared for:
- Theatrical exhibition (cinema projector)
- Home video (Rec. 709/Rec. 2020)
- Mobile streaming (various displays)

Different ODTs are paired with different Look Transforms appropriate to each viewing environment.

---

## Use Case 4: Flexible Pre-Sets for Creative Modifications

Separation of grading and Look Transform(s) allows significant creative changes to the entire frame without requiring the colorist to start from scratch. Examples:
- "Day for Night" Look Transform can be swapped for "Day for Dusk" without expensive colorist intervention
- Multiple creative directions can be previewed by swapping LMTs

---

## Use Case 5: Permanent Color Modification (Archival)

It is valid to archive the input to the RRT as an ACES container file, **baking in** the grade and any Look Transform application(s). A person retrieving the ACES file need not know about the grades and Look Transforms applied — by virtue of being an ACES file, the image "speaks for itself" when the RRT and a selected ODT are applied.

### Critical Requirement: Dynamic Range Preservation

Look Transform authors must preserve as much dynamic range as possible. This provides maximum latitude for:
- Colorists grading through the Look Transform
- Future remastering for radically different displays (e.g., higher dynamic range)

While full preservation of dynamic range and gamut is almost never possible, the author should always choose the option that retains more input dynamic range and color gamut. Severe distortions (e.g., very large or very small CDL "power" parameters applied as gamma operations) should be avoided.

---

## Use Case 6: Portability

Look Transforms are expressed and transported using the **Common LUT Format** (CLF / Academy/ASC Common LUT Format). Building blocks include:
- Basic arithmetical operations
- Simple matrix application
- 1D LUTs
- 3D LUTs

Straightforward color transforms can be expressed analytically using the first three. Complex empirically derived Look Transforms are conveyed as 3D LUTs. Using floating point ACES RGB relative exposure values directly as 1D LUT indices requires a more complex lookup mechanism supported by CLF's `halfDomain` attribute.

---

## Use Case 7: Look Transforms and Pre-Grading for VFX

Color corrections may be created prior to the colorist session in a scene-balancing "pre-grade," allowing all shots in a sequence to share identical Look Transforms downstream. This is particularly useful for long sequences with varying color temperature (e.g., a sequence of daylight shots).

When VFX are complete, frames supplied to the colorist have both the pre-grade and VFX "baked in." The Look Transform is not baked in — it must be applied after the grade — and is carried as metadata referenced by the ACES Metadata File (AMF).

---

## Summary: The Architecture of Film Emulation in ACES

```
Camera → IDT → ACES2065-1 → [GRADE] → [LMT(s)] → ACES' → RRT → ODT → Display
                                         ↑
                                   Look Transform(s)
                                   - Print Film Emulation
                                   - Bleach Bypass
                                   - ASC CDL adjustments  
                                   - Creative presets
```

This decoupled architecture is what makes ACES uniquely suited for film emulation:
1. **Input-agnostic** — Any camera source is normalized to ACES
2. **Look-portable** — Any LMT works with any source
3. **Archivable** — Scene-referred data preserved for future mastering
4. **Chainable** — Multiple LMTs can be combined
5. **Standardized format** — CLF ensures cross-tool compatibility
