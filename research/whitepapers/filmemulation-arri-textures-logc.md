# ARRI Textures and Log C: Digital Emulation of Film Stock Character

**Source URL:** https://www.arri.com/en/learn-help/learn-help-camera-system/image-science
**Author:** ARRI Group
**Date:** 2024–2025 (continuously updated)

**Document Source:** ARRI Learn & Help — Image Science section

---

## ARRI Textures: "Like Selecting a Film Stock's Character"

ARRI digital cameras have a set of values that determine how cameras process images at their core. These values, comprising various carefully balanced parameters, shape:

1. The **amount and character of grain** in the image
2. The **amount of contrast at different levels of detail**, which influences perceived sharpness (technically the **MTF curve** — Modulation Transfer Function)

In ALEXA 35 and ALEXA 35 Xtreme, these parameters are combined into **ARRI Textures**. Each Texture defines a specific combination of values that tunes the image character. Changing the Texture is analogous to selecting a different film stock.

### How Textures Work in the Image Pipeline

Textures operate at a fundamental level within the ALEXA image processing chain. After light hits the ALEV 4 sensor, the raw data passes through a series of processing stages, with Textures determining the grain structure and detail contrast characteristics. This shapes the fundamental "look" before any subsequent color grading is applied.

### Grain and MTF Relationship

The ARRI Texture parameters balance two key attributes:
- **Grain amount** — Controls the noise characteristic, from ultra-clean to noticeably textured
- **MTF at different detail levels** — Controls contrast at fine, medium, and coarse detail frequencies

This is directly analogous to how different film stocks exhibit different combinations of grain structure and sharpness perception. A high-resolution fine-grain stock maintains detail contrast at high spatial frequencies with minimal grain, while a high-speed stock has prominent grain and softer fine detail.

---

## Log C Encoding

### What Is Log C?

ARRI cameras record images in **Log C wide gamut color space**. The "C" stands for Cineon — the original Cineon log encoding is based on the density of color film negative.

Images encoded with Log C can be identified by their flat and desaturated nature. Whites and blacks are not extended to their maximum values because the Log C curve follows a logarithmic encoding with a grayscale characteristic similar to a scan from negative film.

This design is based on the same principle as the Cineon system, which was originally created by Kodak in the 1990s to standardize the digitization of film negatives for visual effects and digital intermediate work. Cineon's 10-bit log encoding captured the full density range of color negative film (from D-min to D-max), allowing scanned film frames to be manipulated digitally and then recorded back to film with minimal quality loss.

### Why Log Encoding?

Linear encoding would require an excessive number of bits to represent the dynamic range of modern sensors due to the non-linear perceptual response of human vision. Logarithmic encoding distributes code values more perceptually uniformly:
- More code values in shadows (where the eye is more sensitive to differences)
- Fewer code values in highlights (where perceptual differences are smaller)

### ARRI Wide Gamut

Log C images are recorded in **ARRI Wide Gamut**, a color space with primaries that encompass all colors the sensor can capture — including colors beyond Rec. 709 and even beyond DCI-P3. This "scene-referred" approach preserves all captured color information for maximum flexibility in post-production.

### REVEAL Color Science

REVEAL is the latest generation of ARRI color science, introduced with ALEXA 35. It is backwards-compatible with ARRIRAW from all previous ALEXA and AMIRA cameras. REVEAL improves:
- Color separation and subtle hue discrimination
- Skin tone rendering
- Highlight handling and rolloff
- Overall image texture and dimensionality

---

## Log C and Film Emulation: The Connection

The key insight connecting Log C to film emulation is:

1. **Cineon log was designed to encode negative film density**
2. **Log C follows the same principle for digital sensors**
3. **Print Film Emulation (PFE) LUTs designed for Cineon log can, with appropriate adaptation, work for Log C**

This is the same principle discussed in the ACES documentation — traditional film scans were viewed through PFEs (print film emulations), and the scene-referred to display-referred rendering concept is universal: digital log images need a rendering transform just as Cineon scans needed a PFE.

---

## ARRI Look Library and ARRI Film Lab

### ARRI Look Library

The ARRI Look Library provides a collection of pre-built creative looks that can be applied in-camera or in post. These looks are designed by professional colorists and encompass a wide range of styles, including looks inspired by classic film aesthetics.

### ARRI Film Lab

The ARRI Film Lab tool allows cinematographers and colorists to create custom film-emulation looks, adjusting parameters that affect grain character, color response, and contrast in ways that emulate traditional photochemical processes.

---

## Practical Implications for Film Emulation Development

1. **Grain isn't just noise** — it's a structural element tied to detail contrast at multiple spatial frequencies
2. **The MTF curve matters as much as grain** — perceived sharpness and "film look" come from the interplay of resolution, grain, and contrast at different detail scales
3. **Log encoding is the bridge** — Cineon/Log C style log curves are essential for interfacing with PFE-style transforms
4. **Film stock selection was about choosing a Texture** — the paradigm ARRI established makes this explicit
