# HDR Display Technology and Wide Gamut Workflows

**Source URLs:**
- https://en.wikipedia.org/wiki/High-dynamic-range_television
- https://en.wikipedia.org/wiki/Gamut
- https://www.color.org/whitepapers.xalter (ICC White Papers)
**Author(s):** Wikipedia contributors, International Color Consortium (ICC)
**Date:** 2024-2025 (Wikipedia articles continuously updated)
**Additional Sources:** ICC WP47 (The value of iccMAX), ICC WP55 (Profiling using D65/10° observer)

---

## HDR Display Technology

High-dynamic-range television (HDR-TV) is a technology that uses high dynamic range (HDR) to improve the quality of display signals. It is contrasted with the retroactively-named standard dynamic range (SDR). HDR changes the way the luminance and colors of videos and images are represented in the signal and allows brighter and more detailed highlight representation, darker and more detailed shadows, and more intense colors.

HDR allows compatible displays to receive a higher-quality image source. It does not improve a display's intrinsic properties (brightness, contrast, and color capabilities). Not all HDR displays have the same capabilities, and HDR content will look different depending on the display used; the standards specify the required conversion depending on display capabilities.

HDR-TV is a part of HDR imaging, an end-to-end process of increasing the dynamic range of images and videos from their capture and creation to their storage, distribution and display. Often, HDR is used with wide color gamut (WCG) technology. WCG increases the gamut and number of distinct colors available. HDR increases the range of luminance available for each color. HDR and WCG are separable but complementary technologies.

### SDR vs HDR Limits
SDR formats are able to represent a maximum luminance level of around 100 nits. For HDR, this number increases to around 1,000–10,000 nits. HDR can represent darker black levels and more saturated colors. The most common SDR formats are limited to the Rec. 709/sRGB gamut, while common HDR formats use Rec. 2100, which is a wide color gamut (WCG).

In practice, HDR is not always used at its limits. HDR contents are often limited to a peak brightness of 1,000 or 4,000 nits and P3-D65 colors, even if they are stored in formats capable of more. Content creators can choose to what extent they make use of HDR capabilities. They can constrain themselves to the limits of SDR even if the content is delivered in an HDR format.

### Benefits of HDR
- **Highlights**: The brightest parts of an image can be brighter, more colorful, and more detailed. The larger capacity for brightness can be used to increase the brightness of small areas without increasing the overall image's brightness, resulting in bright reflections from shiny objects, bright stars in a dark night scene, and bright and colorful light-emissive objects (e.g. fire, and sunset).
- **Shadows**: The darkest parts of an image can be darker and more detailed.
- **Colors**: The colorful parts of the image can be even more colorful if a WCG is used.
- **Perceptual benefits**: More realistic luminance variation between scenes (such as sunlit, indoor, and night scenes), better surface material identification, and better in-depth perception, even with 2D imagery.

---

## HDR Formats

### HDR10
The most widespread of the HDR formats. Not backward compatible with SDR displays. Technically limited to a maximum peak brightness of 10,000 nits; however, HDR10 content is commonly mastered with a peak brightness between 1000 and 4000 nits. HDR10 lacks dynamic metadata — the metadata is static and constant with respect to each individual video. The interaction between display capabilities, video metadata, and the ultimate output is mediated by the display, with the result that the original producer's intent may not be preserved.

### Dolby Vision
An end-to-end ecosystem for HDR video, covering content creation, distribution, and playback. Uses dynamic metadata and is capable of representing luminance levels of up to 10,000 nits. Dolby Vision certification requires displays for content creators to have a peak luminance of at least 1,000 nits. Dolby Vision and HDR10+ include dynamic metadata while HDR10 and HLG do not. The dynamic metadata are used to improve image quality on limited displays that are not capable of reproducing an HDR video to its fullest intended extent.

### HDR10+
Same as HDR10 but with the addition of a system of dynamic metadata developed by Samsung. It is free to use for content creators and has a maximum $10,000 annual license for some manufacturers. Positioned as an alternative to Dolby Vision without the same expenses.

### HLG (Hybrid Log-Gamma)
An HDR format developed by the NHK and BBC that can be used for video and still images. Uses the HLG transfer function, Rec. 2020 color primaries, and a bit depth of 10 bits. The format is backwards compatible with SDR UHDTV, but not with older SDR displays that do not implement the Rec. 2020 color standards. It does not use metadata and is royalty-free.

### PQ10 (PQ Format)
Same as the HDR10 format, except it lacks metadata. Uses the perceptual quantizer (PQ) transfer function, Rec. 2020 color primaries and a bit depth of 10 bits.

### HDR Formats Comparison

| Feature | HDR10 | HDR10+ | Dolby Vision | HLG |
|---------|-------|--------|--------------|-----|
| **Developer** | CTA | Samsung | Dolby | NHK/BBC |
| **Year** | 2015 | 2017 | 2014 | 2015 |
| **Cost** | Free | Free (content), license fee (manufacturer) | Proprietary | Free |
| **Transfer Function** | PQ | PQ | PQ (most), SDR, HLG | HLG |
| **Bit Depth** | 10 bit | 10 bit+ | 10 bit (12 bit FEL) | 10 bit |
| **Peak Luminance (tech)** | 10,000 nits | 10,000 nits | 10,000 nits | Variable |
| **Peak Luminance (common)** | 1,000-4,000 nits | 1,000-4,000 nits | 4,000 nits | 1,000 nits |
| **Color Primaries (tech)** | Rec. 2020 | Rec. 2020 | Rec. 2020 | Rec. 2020 |
| **Color Primaries (content)** | P3-D65 | P3-D65 | At least P3-D65 | P3-D65 |
| **Metadata** | Static | Static + Dynamic | Static + Dynamic | None |
| **Backward Compatible** | None | HDR10 | Varies by profile | SDR UHDTV |

---

## Display Certifications

### VESA DisplayHDR
The DisplayHDR standard from VESA is an attempt to make the differences in HDR specifications easier for consumers to understand, mainly used in computer monitors and laptops.

| Tier | Min Peak Luminance | Color Gamut | Min Color Depth | Dimming | Max Black Level | Latency |
|------|-------------------|-------------|-----------------|---------|-----------------|---------|
| DisplayHDR 400 | 400 cd/m² | sRGB | 8-bit | Screen-level | 0.4 cd/m² | 8 frames |
| DisplayHDR 500 | 500 cd/m² | WCG* | 10-bit | Zone-level | 0.1 cd/m² | 8 frames |
| DisplayHDR 600 | 600 cd/m² | WCG* | 10-bit | Zone-level | 0.1 cd/m² | 8 frames |
| DisplayHDR 1000 | 1000 cd/m² | WCG* | 10-bit | Zone-level | 0.05 cd/m² | 8 frames |
| DisplayHDR 1400 | 1400 cd/m² | WCG* | 10-bit | Zone-level | 0.02 cd/m² | 8 frames |
| DisplayHDR 400 True Black | 400 cd/m² | WCG | 10-bit | Pixel-level | 0.0005 cd/m² | 2 frames |
| DisplayHDR 500 True Black | 500 cd/m² | WCG | 10-bit | Pixel-level | 0.0005 cd/m² | 2 frames |
| DisplayHDR 600 True Black | 600 cd/m² | WCG | 10-bit | Pixel-level | 0.0005 cd/m² | 2 frames |

The "True Black" tiers target OLED displays with per-pixel dimming. DisplayHDR 1000 and 1400 are primarily used in professional work like video editing. DisplayHDR 500 or 600 provide a noticeable improvement over SDR and are more often used for general computing and gaming.

### UHD Alliance Certifications
- **Ultra HD Premium**: For premium HDR televisions
- **Mobile HDR Premium**: For mobile devices

---

## Technical Details of HDR

### Transfer Functions
SDR uses a gamma curve transfer function that is based on CRT characteristics and is used to represent luminance levels up to around 100 nits. HDR uses newly developed PQ or HLG transfer functions instead.

**PQ (Perceptual Quantizer)** — SMPTE ST 2084: A transfer function developed for HDR that is able to represent luminance level up to 10,000 cd/m². It is the basis of HDR10, HDR10+, and Dolby Vision. PQ is not backward compatible with SDR. PQ encoded in 12 bits does not produce visible banding.

**HLG (Hybrid Log-Gamma)**: A transfer function developed by the NHK and BBC. It is backward compatible with SDR's gamma curve, and is the basis of an HDR format known as HLG. HLG is royalty-free.

### Color Primaries for HDR
SDR for HD video uses system chromaticity specified in Rec. 709 (same as sRGB). HDR is commonly associated with a WCG — a system chromaticity wider than Rec. 709. Rec. 2100 (HDR-TV) uses the same system chromaticity that is used in Rec. 2020 (UHDTV). HDR contents are commonly graded on a P3-D65 display.

### System Chromaticity Comparison

| Color Space | Red (xR, yR) | Green (xG, yG) | Blue (xB, yB) | White Point (xW, yW) |
|------------|--------------|----------------|---------------|----------------------|
| Rec. 709 / sRGB | 0.64, 0.33 | 0.30, 0.60 | 0.15, 0.06 | D65 (0.3127, 0.3290) |
| DCI-P3 | 0.680, 0.320 | 0.265, 0.690 | 0.150, 0.060 | D65 (0.3127, 0.3290) |
| Rec. 2020 / Rec. 2100 | 0.708, 0.292 | 0.170, 0.797 | 0.131, 0.046 | D65 (0.3127, 0.3290) |

### Bit Depth
Because of the increased dynamic range, HDR contents need to use more bit depth than SDR to avoid banding. While SDR uses a bit depth of 8 or 10 bits, HDR uses 10 or 12 bits, which when combined with the use of more efficient transfer function like PQ or HLG, is enough to avoid banding.

### Matrix Coefficients
Rec. 2100 specifies the use of RGB, YCbCr or ICTCP signal formats for HDR-TV. ICTCP is a color representation designed by Dolby for HDR and wide color gamut (WCG).

---

## Wide Gamut Workflows

### Understanding Gamut
In color reproduction and colorimetry, a gamut is a convex set containing the colors that can be accurately represented by an output device (e.g. printer or display) or measured by an input device (e.g. camera or visual system). Devices with a larger gamut can represent more colors.

### Wide-Color Gamut (WCG) Definition
The Ultra HD Forum defines a wide-color gamut as a color gamut wider than Rec. 709 and sRGB. Color spaces with WCGs include:

- **Rec. 2020** — ITU-R Recommendation for UHDTV
- **Rec. 2100** — ITU-R Recommendation for HDR-TV (same chromaticity of color primaries and white point as Rec. 2020)
- **DCI-P3 and DisplayP3** — Theater standard and Apple display standard
- **Adobe RGB color space** — Wider than sRGB, common in photography
- **DxO Wide Gamut** — Coverage of human visible gamut

### Gamut Hierarchy (from widest to narrowest)
1. **Laser video projector** — Uses three lasers for the broadest gamut available in practical display equipment today, derived from truly monochromatic primaries
2. **Photographic film** — Can reproduce a larger color gamut than typical television, computer, or home video systems
3. **DLP projectors** — Digital Light Processing technology from Texas Instruments
4. **Wide-gamut LCD (LED backlight)** — LCD screens with certain LED or wide-gamut CCFL backlights yield a more comprehensive gamut than CRTs
5. **CRT displays** — Roughly triangular color gamut covering a significant portion of the visible color space
6. **Standard LCD (CCFL)** — Limited to the emitted spectrum of the backlight
7. **Television broadcast** — Limited by Rec. 601/Rec. 709 standards
8. **Paint mixing** — Reasonably large gamut but overall smaller than CRTs for some colors
9. **CMYK printing** — Much narrower gamut than RGB displays
10. **Monochrome displays** — One-dimensional curve in color space

### Extended-Gamut Printing
The print gamut achieved by using cyan, magenta, yellow, and black inks is sometimes a limitation (e.g. when printing corporate logos). Extended gamut printing uses additional ink colors to achieve a larger gamut — green, orange, and violet inks to increase the achievable saturation of hues near those. These methods are variously called heptatone color printing, extended gamut printing, and 7-color printing.

### Pointer's Gamut
In 1980, Michael R. Pointer published a gamut for real surfaces with diffuse reflection using 4089 samples. Originally called a "Munsell Color Cascade," the limits are more commonly called Pointer's Gamut. This represents the practical limit of surface colors encountered in the real world — significantly smaller than the theoretical optimal color solid but more useful for practical color management.

---

## Ambient Light and Viewing Conditions

### Impact on Color Perception
The viewing environment significantly affects perceived color accuracy. Key factors:

1. **Adaptation white point**: The human visual system adapts to the ambient light's white point. A monitor calibrated to D65 will appear correct under D65-ish lighting, but may look too warm under cool fluorescent lights or too cool under warm incandescent light.

2. **Surround luminance**: The brightness of the area surrounding the display affects contrast perception. A dark surround increases perceived contrast; a bright surround reduces it.

3. **Screen reflections**: Glare from ambient light sources reduces effective contrast and color saturation. Matte screens help but can reduce sharpness.

4. **Metamerism**: Colors that match under one light source may not match under another. This is critical for print viewing — a print may look correct under D50 viewing booth but different under home lighting.

### ISO 3664: Viewing Conditions
This standard specifies viewing conditions for graphic technology and photography:
- **Illuminant**: D50 (5000K) as the standard reference
- **Illuminance**: 2000 lux ± 250 lux for critical comparison
- **Surround**: Neutral gray, matte finish, reflectance < 20%
- **Color rendering index (CRI)**: > 90 for viewing booth lights

### Recommended Setup for Color-Critical Work
- Calibrate monitor to D65/6500K, gamma 2.2, 120 cd/m² luminance
- Use neutral gray walls (18% reflectance) in the work area
- Eliminate direct light on the screen
- Use D50/D65 viewing booth for print comparison
- Avoid mixed lighting (e.g., daylight + tungsten)
- Allow 10-15 minutes for visual adaptation when changing lighting conditions
- Position monitor perpendicular to windows to avoid reflections

### ICC HDR Working Group
The ICC has established a working group on HDR to address color management challenges for HDR content. Key areas include:
- HDR metadata tags (registered in ICC metadata registry)
- Adaptive Gain Curve amendment to handle HDR transfer functions
- iccMAX for advanced HDR workflows beyond what ICC v4 provides

---

## ICC White Papers on Advanced Color Management

### WP47: The Value of iccMAX
iccMAX is a color management interchange format that addresses use cases beyond ICC v4. ICC v4 is widely used today, is straightforward to use and is uniformly implemented. However, in applications such as managing digital photographs or color managing packaging in store lighting conditions, v4 is missing some key features which are available in iccMAX. This paper is addressed to end users of color management systems and is intended to help decide when iccMAX rather than ICC v4 is the appropriate choice.

### WP55: Profiling Using D65/10° Observer
In ICC color management the Profile Connection Space (PCS) is CIE colorimetry based on D50 and the CIE 1931 2-degree observer. However, many industries employ colorimetry based on the D65 illuminant and the CIE 1964 10-degree observer. This document recommends an approach for D65/10 color reproduction while retaining interoperability with other v4 profiles, and outlines additional possibilities available with ICC version 5 (iccMAX) color management.
