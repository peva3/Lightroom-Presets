# Color Appearance Models: CIECAM02 and Beyond

**Source:** https://en.wikipedia.org/wiki/CIECAM02 and https://en.wikipedia.org/wiki/Color_appearance_model
**Authors:** Wikipedia contributors (primary: CIE Technical Committee 8-01, Nathan Moroney, Mark D. Fairchild, Robert W.G. Hunt, Changjun Li, M. Ronnier Luo)
**Date:** CIECAM02 published 2002; Wikipedia article last updated 2025

---

## Overview

In colorimetry, **CIECAM02** is the color appearance model (CAM) published in 2002 by the International Commission on Illumination (CIE) Technical Committee 8-01 (*Color Appearance Modelling for Color Management Systems*) and the successor of CIECAM97s. It has since been superseded by CIECAM16.

The two major parts of the model are its chromatic adaptation transform, CIECAT02, and its equations for calculating mathematical correlates for the six technically defined dimensions of color appearance: brightness (luminance), lightness, colorfulness, chroma, saturation, and hue.

## Color Appearance Dimensions

- **Brightness** - the subjective appearance of how bright an object appears given its surroundings and how it is illuminated
- **Lightness** - the subjective appearance of how light a color appears to be
- **Colorfulness** - the degree of difference between a color and gray
- **Chroma** - the colorfulness relative to the brightness of another color that appears white under similar viewing conditions (allows for increasing colorfulness as illumination increases)
- **Saturation** - the colorfulness of a color relative to its own brightness
- **Hue** - the degree to which a stimulus can be described as similar to or different from red, green, blue, and yellow (unique hues)

Colors that make up an object's appearance are best described in terms of lightness and chroma when talking about the colors that make up the object's surface, and in terms of brightness, saturation and colorfulness when talking about the light that is emitted by or reflected off the object.

## CIECAM02 Inputs

CIECAM02 takes for its input:
- The tristimulus values of the stimulus (CIE XYZ)
- The tristimulus values of an adapting white point
- Adapting background luminance
- Surround luminance information
- Whether or not observers are discounting the illuminant (color constancy)

The model can be used to predict appearance attributes or, with forward and reverse implementations for distinct viewing conditions, to compute corresponding colors.

## Viewing Conditions

The model defines three surround conditions with associated parameters:

| Surround Condition | Surround Ratio | F | c | Nc | Application |
|---|---|---|---|---|---|
| Average | SR > 0.15 | 1.0 | 0.69 | 1.0 | Viewing surface colors |
| Dim | 0 < SR < 0.15 | 0.9 | 0.59 | 0.9 | Viewing television |
| Dark | SR = 0 | 0.8 | 0.525 | 0.8 | Projector in dark room |

Where:
- SR = L_sw / L_dw: ratio of absolute luminance of reference white in surround field to display area
- F: factor determining degree of adaptation
- c: impact of surrounding
- Nc: chromatic induction factor

The absolute luminance of the adapting field can be calculated as: L_A = L_W / 5 (using "medium gray" assumption)

## Chromatic Adaptation (CAT02)

CIECAM02's chromatic adaptation transform (CAT02) follows these steps:

1. **Convert to spectrally sharpened LMS space** — The CAT02 matrix transforms XYZ tristimulus values to a "sharpened" LMS cone response space:
```
[L, M, S]^T = M_CAT02 * [X, Y, Z]^T
```
Where M_CAT02 = [[0.7328, 0.4296, -0.1624], [-0.7036, 1.6975, 0.0061], [0.0030, 0.0136, 0.9834]]

2. **Perform chromatic adaptation** — The degree of adaptation is controlled by the D parameter:
```
D = F * (1 - (1/3.6) * e^(-(L_A + 42)/92))
```
Where D ranges from 0.65 to 1.0. D=0 means no adaptation (self-luminous stimulus), D=1 means complete adaptation (full color constancy).

3. **Post-adaptation** — Convert to Hunt-Pointer-Estevez cone space and apply nonlinear response compression using the generalized Michaelis-Menten equation. The luminance level adaptation factor F_L is proportional to the cube root of L_A in photopic conditions.

## Appearance Correlates

CIECAM02 computes:

- **Red-green correlate (a)**: a = L'_a - (12/11)M'_a + (1/11)S'_a
- **Yellow-blue correlate (b)**: b = (1/9)(L'_a + M'_a - 2S'_a)
- **Hue angle (h)**: h = atan2(b, a)
- **Lightness (J)**: J = 100 * (A/A_w)^(cz), where z = 1.48 + sqrt(n)
- **Brightness (Q)**: Q = (4/c) * sqrt(J/100) * (A_w + 4) * F_L^(1/4)
- **Chroma (C)**: C = t^0.9 * sqrt(J/100) * (1.64 - 0.29^n)^0.73
- **Colorfulness (M)**: M = C * F_L^(1/4)
- **Saturation (s)**: s = 100 * sqrt(M/Q)

## Color Spaces

The appearance correlates J, a, b form a uniform color space for calculating color differences under fixed viewing conditions. The **CAM02 Uniform Color Space** (CAM02-UCS) extends this with tweaks to better match experimental data (Luo, Cui & Li, 2006).

## CIECAM02 as a Model of Visual Processing

CIECAM02 has been shown to be a more plausible model of neural activity in the primary visual cortex compared to CIELAB. Both its achromatic response A and red-green correlate a can be matched to EMEG activity (brainwave entrainment), each with their own characteristic delay.

## The Windows Color System

The Windows Color System (WCS) introduced in Windows Vista uses Canon's Kyuanos technology for mapping image gamuts between output devices, which in turn uses CIECAM02 for color matching.

## Other Color Appearance Models

### CIELAB (1976)
The first color appearance model, created as a perceptually uniform color space (UCS) for color difference. Still the most widely used due to being a building block of color management with ICC profiles. Limitations: poor "wrong" von Kries transform directly in XYZ space, poor hue prediction for blues, non-constant hue lines.

### CIECAM97s (1997)
The CIE's first comprehensive CAM. Comprehensive but complex. Widespread acceptance as a standard until CIECAM02.

### IPT
Addresses the issue of non-constant lines of hue. Converts D65-adapted XYZ to LMS using an adapted Hunt-Pointer-Estevez matrix. Excellent hue uniformity, making it well-suited for gamut mapping implementations.

### ICtCp
ITU-R BT.2100 color space that improves IPT for HDR and larger color gamuts. Basis for Rec. 2124 wide gamut color difference metric ΔE_ITP.

### CAM16 (2016/2022)
Successor of CIECAM02 with various fixes and improvements. Includes CAM16-UCS color space. Used in Material Design color system in a cylindrical version called "HCT" (hue, chroma, tone). CIECAM16 standard was released in 2022.

### OKLab (2020)
A 2020 UCS designed for normal dynamic range color. Same structure as CIELAB but fitted with improved data (CAM16 output for lightness and chroma; IPT data for hue). Part of CSS Color Level 4, supported by all major browsers. Meant to be easy to implement and use.

### iCAM06
An image color appearance model that treats each pixel in the context of the complete image. Incorporates spatial color appearance parameters like contrast. Well-suited for HDR images.

### Hunt Model
Focuses on color image reproduction. Development started in the 1980s at Kodak Research Laboratories. Very complex (includes rod cell responses). Had significant impact on CIECAM02 but difficult to use directly.

### RLAB
Improves on CIELAB limitations with focus on image reproduction. Uses proper von Kries step and allows tuning degree of adaptation with customizable D value.

### Nayatani et al. Model
Focuses on illumination engineering and color rendering properties of light sources.

### OSA-UCS (1947)
A uniform color scale with good properties but no closed-form expression for CIEXYZ conversion, making it hard to use in practice.

### JzAzBz (2017)
A UCS designed for HDR color. Has J (lightness) and two chromaticities.

## Key Phenomena Modeled by CAMs

1. **Chromatic Adaptation** — The ability to abstract from white point/color temperature of the illuminating light source (color constancy)
2. **Bezold-Brücke Hue Shift** — Hue changes with luminance at constant chromaticity
3. **Abney Effect** — Hue of monochromatic light changes with addition of white light
4. **Stevens Effect** — Contrast increases with luminance
5. **Bartleson-Breneman Effect** — Image contrast increases with luminance of surround lighting
6. **Hunt Effect** — Colorfulness increases with luminance
7. **Helmholtz-Kohlrausch Effect** — Brightness increases with saturation

## References

- Fairchild, Mark D. (2013). *Color Appearance Models* (3rd ed.). Wiley-IS&T.
- Moroney, Nathan; Fairchild, Mark D.; Hunt, Robert W.G.; Li, Changjun; Luo, M. Ronnier; Newman, Todd (2002). "The CIECAM02 Color Appearance Model". IS&T/SID Tenth Color Imaging Conference.
- CIE TC 8-01 (2004). *A Color appearance model for color management systems*. Publication 159. CIE Central Bureau.
- Schanda, János (2007). "The Future of Colorimetry in the CIE: Color Appearance". *Colorimetry: Understanding the CIE System*. Wiley Interscience.
