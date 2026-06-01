# Display Color Accuracy Standards and Color Management Fundamentals

**Source URLs:**
- https://www.cambridgeincolour.com/tutorials/color-management1.htm (Color Management Overview)
- https://www.cambridgeincolour.com/tutorials/color-spaces.htm (Color Spaces)
- https://www.cambridgeincolour.com/tutorials/gamma-correction.htm (Gamma Correction)
- https://www.color.org/whitepapers.xalter (ICC White Papers catalog)
**Author(s):** Sean McHugh (Cambridge in Colour), International Color Consortium (ICC)
**Date:** 2004-2022 (continuously updated)

---

## Color Management Overview

"Color management" is a process where the color characteristics for every device in the imaging chain is known precisely and utilized in color reproduction. It often occurs behind the scenes and doesn't require any intervention, but when color problems arise, understanding this process can be critical.

In digital photography, this imaging chain usually starts with the camera and concludes with the final print, and may include a display device in between.

Many other imaging chains exist, but in general, any device which attempts to reproduce color can benefit from color management. For example, with photography it is often critical that your prints or online gallery appear how they were intended. Color management cannot guarantee identical color reproduction, as this is rarely possible, but it can at least give you more control over any changes which may occur.

## The Need for Profiles & Reference Colors

Color reproduction has a fundamental problem: a given "color number" doesn't necessarily produce the same color in all devices. To solve this, color management uses three key principles:

1. **Characterize** each device's color response by creating a personalized table/profiling it
2. **Standardize** this response based on a reference color space (Profile Connection Space/PCS)
3. **Translate** values from one device into equivalent values for another using color-aware software

### Color Profiles
A device's color response is characterized where various numbers are sent to this device, and its output is measured in each instance. Real-world color profiles include all three colors, more values, and are usually more sophisticated than simple tables — but the same core principles apply. However, just as with the spiciness example, a profile on its own is insufficient. These profiles have to be recorded in relation to standardized reference colors, and you need color-aware software that can use these profiles to translate color between devices.

## Color Management: Three Steps

1. **Characterize**. Every color-managed device requires a personalized table, or "color profile," which characterizes the color response of that particular device.
2. **Standardize**. Each color profile describes these colors relative to a standardized set of reference colors (the "Profile Connection Space").
3. **Translate**. Color-managed software then uses these standardized profiles to translate color from one device to another. This is usually performed by a Color Management Module (CMM).

The above color management system was standardized by the International Color Consortium (ICC), and is now used in most computers. It involves several key concepts: color profiles, color spaces, and translation between color spaces.

### Color Space
This is just a way of referring to the collection of colors/shades that are described by a particular color profile. Put another way, it describes the set of all realizable color combinations. Color spaces are therefore useful tools for understanding the color compatibility between two different devices.

### Profile Connection Space (PCS)
This is a color space that serves as a standardized reference (a "reference space"), since it is independent of any particular device's characteristics. The PCS is usually the set of all visible colors defined by the Commission International de l'éclairage (CIE) and used by the ICC.

Note: The thin trapezoidal region drawn within the PCS is what is called a "working space." The working space is used in image editing programs (such as Adobe Photoshop), and defines the subset of colors available to work with when performing any image editing.

### Color Translation
The Color Management Module (CMM) is the workhorse of color management, and is what performs all the calculations needed to translate from one color space into another. Contrary to previous examples, this is rarely a clean and simple process. For example, what if the printer weren't capable of producing as intense a color as the display device? This is called a "gamut mismatch," and would mean that accurate reproduction is impossible. In such cases the CMM therefore just has to aim for the best approximation that it can.

---

## Color Spaces

A "color space" is a useful conceptual tool for understanding the color capabilities of a particular device or digital file. When trying to reproduce color on another device, color spaces can show whether you will be able to retain shadow/highlight detail, color saturation, and by how much either will be compromised.

### Visualizing Color Spaces
A color space relates numbers to actual colors, and is a three-dimensional object which contains all realizable color combinations. Similar to how one would organize a paint palette, each direction in "color space" often represents some aspect of color, such as lightness, saturation or hue (depending on the type of space).

The outer surface of a color space represents the most extreme colors which are reproducible within this particular color space (the "color gamut"). Everything inside the color space is therefore a more subtle combination of the colors shown on the surface.

### Comparing Color Spaces
In order to visualize more than one color space at a time, color spaces are often represented using two-dimensional slices from their full 3D shape. These are more useful for everyday purposes, because they allow you to quickly see the entire boundary of a given cross-section. Unless specified otherwise, two-dimensional diagrams usually show the cross-section containing all colors which are at 50% luminance (a horizontal slice at the vertical midpoint).

For example, "Wide Gamut RGB" color space contains more extreme reds, purples, and greens, whereas "sRGB" color space contains slightly more blues. This analysis only applies for colors at 50% luminance, which is what occupies the midtones of an image histogram. If we were interested in the color gamut for the shadows or highlights, we could instead look at 2D cross-sections at roughly 25% and 75% luminance, respectively.

### Types: Device Dependent & Working Spaces
- **Device-dependent spaces** express color relative to some other reference space. These can tell you valuable information about the subset of colors which can be displayed using a particular monitor or printer, or can be captured using a particular digital camera or scanner.
- **Device-independent spaces** express color in absolute terms. These often serve as universal reference colors, so they're useful as a backdrop for comparing other devices. Otherwise these are usually an unseen color space.
- **Working spaces** are used by image editing programs and file formats to constrain the range of colors to a standard palette. Two of the most commonly used working spaces in digital photography are Adobe RGB 1998 and sRGB IEC61966-2.1.

Devices or working spaces that can realize more extreme colors are said to have a "wide gamut," whereas the opposite is true for "narrow gamut" color spaces.

### Reference Spaces
Nearly all color management software today uses a device-independent space defined by the Commission International de l' éclairage (CIE) in 1931. This space aims to describe all colors visible to the human eye based upon the average response from a set of people with no vision problems (termed a "standard colorimetric observer").

The CIE space of visible color is expressed in several common forms:
- **CIE xyz (1931)**: Based on a direct graph of the signals from each of the three types of color sensors in the human eye (tristimulus functions). However, this representation allocates too much area to the greens — confining most of the apparent color variation to a small area.
- **CIE L u'v' (1976)**: Created to correct for the CIE xyz distortion by distributing colors roughly proportional to their perceived color difference. A region that is twice as large in u'v' will therefore also appear to have twice the color diversity.
- **CIE L\*a\*b\***: Remaps the visible colors so that they extend equally on two axes — conveniently filling a square. Each axis in the L\*a\*b\* color space also represents an easily recognizable property of color, such as the red-green and blue-yellow shifts. These traits make L\*a\*b\* a useful color space for editing digital images.

---

## Gamma Correction

Gamma is an important but seldom understood characteristic of virtually all digital imaging systems. It defines the relationship between a pixel's numerical value and its actual luminance. Without gamma, shades captured by digital cameras wouldn't appear as they did to our eyes (on a standard monitor).

### Why Gamma Is Useful

**1. Our eyes do not perceive light the way cameras do.** With a digital camera, when twice the number of photons hit the sensor, it receives twice the signal (a "linear" relationship). That's not how our eyes work. Instead, we perceive twice the light as being only a fraction brighter — and increasingly so for higher light intensities (a "nonlinear" relationship). Compared to a camera, we are much more sensitive to changes in dark tones than we are to similar changes in bright tones.

**2. Gamma encoded images store tones more efficiently.** Since gamma encoding redistributes tonal levels closer to how our eyes perceive them, fewer bits are needed to describe a given tonal range. Otherwise, an excess of bits would be devoted to describe the brighter tones (where the camera is relatively more sensitive), and a shortage of bits would be left to describe the darker tones (where the camera is relatively less sensitive).

### Gamma Workflow: Encoding & Correction

A gamma encoded image has to have "gamma correction" applied when it is viewed — which effectively converts it back into light from the original scene. The purpose of gamma encoding is for recording the image — not for displaying the image. Fortunately this second step (the "display gamma") is automatically performed by your monitor and video card.

**1. Image Gamma.** This is applied either by your camera or RAW development software whenever a captured image is converted into a standard JPEG or TIFF file. It redistributes native camera tonal levels into ones which are more perceptually uniform, thereby making the most efficient use of a given bit depth.

**2. Display Gamma.** This refers to the net influence of your video card and display device, so it may in fact be comprised of several gammas. The main purpose of the display gamma is to compensate for a file's gamma — thereby ensuring that the image isn't unrealistically brightened when displayed on your screen. A higher display gamma results in a darker image with greater contrast.

**3. System Gamma.** This represents the net effect of all gamma values that have been applied to an image, and is also referred to as the "viewing gamma." For faithful reproduction of a scene, this should ideally be close to a straight line (gamma = 1.0). A straight line ensures that the input (the original scene) is the same as the output (the light displayed on your screen or in a print). However, the system gamma is sometimes set slightly greater than 1.0 in order to improve contrast.

### Image File Gamma
The precise image gamma is usually specified by a color profile that is embedded within the file. Most image files use an encoding gamma of 1/2.2 (such as those using sRGB and Adobe RGB 1998 color), but the big exception is with RAW files, which use a linear gamma. However, RAW image viewers typically show these presuming a standard encoding gamma of 1/2.2, since they would otherwise appear too dark.

If no color profile is embedded, then a standard gamma of 1/2.2 is usually assumed. Files without an embedded color profile typically include many PNG and GIF files, in addition to some JPEG images that were created using a "save for the web" setting.

### Display Gamma
This is the gamma that you are controlling when you perform monitor calibration and adjust your contrast setting. Fortunately, the industry has converged on a standard display gamma of 2.2, so one doesn't need to worry about the pros/cons of different values. Older macintosh computers used a display gamma of 1.8, which made non-mac images appear brighter relative to a typical PC, but this is no longer the case.

The overall display gamma is actually comprised of (i) the native monitor/LCD gamma and (ii) any gamma corrections applied within the display itself or by the video card. However, the effect of each is highly dependent on the type of display device.

- **CRT Monitors.** Due to an odd bit of engineering luck, the native gamma of a CRT is 2.5 — almost the inverse of our eyes. Values from a gamma-encoded file could therefore be sent straight to the screen and they would automatically be corrected.
- **LCD Monitors.** LCD monitors weren't so fortunate; ensuring an overall display gamma of 2.2 often requires substantial corrections, and they are also much less consistent than CRT's. LCDs therefore require something called a look-up table (LUT) in order to ensure that input values are depicted using the intended display gamma.

---

## ICC White Papers Reference

The International Color Consortium (ICC) maintains a comprehensive set of white papers on color management. Key papers relevant to display accuracy:

### Fundamentals
- **WP3: Recommendations for colour measurement** (Revised June 2021) — Summarizes issues users should consider when making color measurements for constructing ICC profiles.
- **WP7: ICC profiles in a colour reproduction system** (Revised June 2021) — How ICC profiles may be used in achieving successful reproductions.
- **WP20: Digital photography color management basics** — Steps an image undergoes from raw camera capture to rendered output and data encoding. Explains scene-referred and output-referred colorimetry.
- **WP23: RGB Color Managed Workflow Example** — "Late binding" workflow principle: keep as close as possible to the source encoding until as late as possible.

### Intermediate
- **WP4: Color management overview** (Updated Oct 2020) — Conceptual overview of colour management and its evolution, and a summary of color rendering options.
- **WP6: Differences between v2 and v4 display profiles** (Updated Oct 2020) — v4 requires display profiles to assume the viewer is fully adapted to the display white point.
- **WP9: Common color management workflows & rendering intent usage** — Documents common workflows and provides advice about rendering intent usage.
- **WP40: Black-point compensation: theory and application** — Explanation of the BPC concept and its use in ICC systems (now superseded by ISO 18619).

### Advanced
- **WP1: Perceptual rendering fundamentals** (Revised Feb 2012) — ICC v4 differentiates clearly between perceptual rendering and colorimetric rendering.
- **WP2: Perceptual rendering intent use case issues** — Ways of using v4 specification features to achieve different colour reproduction objectives.
- **WP55: Profiling using colorimetry for D65 and 10° observer** — Approach for D65/10 color reproduction while retaining interoperability with v4 profiles.

---

## Delta E and Color Accuracy

Delta E (ΔE) is the standard metric for measuring color difference between two color samples. In the context of displays:

### Delta E Benchmarks
- **ΔE < 1.0**: Imperceptible to the human eye (reference-grade)
- **ΔE < 2.0**: Excellent — suitable for professional color-critical work
- **ΔE < 3.0**: Good — acceptable for most photography work
- **ΔE < 5.0**: Noticeable to trained eyes — marginal for color work
- **ΔE > 5.0**: Clearly visible difference — not suitable for color-critical work

### Display Uniformity
Display uniformity measures how consistently a monitor displays the same color and brightness across the entire screen. Key metrics:
- **Luminance uniformity**: Maximum deviation in brightness from center to edges (should be < 5-10%)
- **Color uniformity**: Maximum ΔE variation across the screen (should be < 3.0)
- **Digital Uniformity Equalizer (DUE)**: EIZO's proprietary correction technology that compensates for uniformity errors at the hardware level

### Calibration Validation
After calibration, validation involves measuring the display against known reference values to verify:
1. Average ΔE across the grayscale ramp
2. Maximum ΔE (worst-case color)
3. White point accuracy
4. Gamma tracking accuracy
5. Gamut coverage percentage vs. target color space
