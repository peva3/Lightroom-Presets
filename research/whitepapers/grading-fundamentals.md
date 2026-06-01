# Color Grading Fundamentals: Primary vs Secondary Corrections

**Source:** Wikipedia - Color Grading (https://en.wikipedia.org/wiki/Color_grading)
**Date:** Last edited April 14, 2026
**Authors:** Wikipedia contributors

---

## Overview

Color grading is a post-production process common to filmmaking and video editing of altering the appearance of an image for presentation in different environments on different devices. Various attributes of an image such as contrast, color, saturation, detail, black level, and white balance may be enhanced whether for motion pictures, videos, or still images.

Color grading and color correction are often used synonymously as terms for this process and can include the generation of artistic color effects through creative blending and compositing of different layer masks of the source image.

The earlier photochemical film process, referred to as color timing, was performed at a film lab during printing by varying the intensity and color of light used to expose the rephotographed image. In the 2000s, with the increase of digital technology, color grading in Hollywood films became more common.

## Color Correction vs. Color Enhancement

Some of the main artistic functions of color correction (digital color grading) include:

1. Reproducing accurately what was shot
2. Compensating for variations in the material (i.e., film errors, white balance, varying lighting conditions)
3. Compensating for the intended viewing environment (dark, dim, bright surrounds)
4. Optimizing base appearance for inclusion of special visual effects
5. Establishing a desired artistic 'look'
6. Enhancing and/or altering the mood of a scene — the visual equivalent to the musical accompaniment of a film

Note that some of these functions must be prioritized over others; for example, color grading may be done to ensure that the recorded colors match those of the original scene, whereas other times, the goal may instead be to establish a very artificial stylized look.

Traditionally, color grading was done towards practical goals. For example, in the film Marianne, grading was used so that night scenes could be filmed more cheaply in daylight. Secondary color grading was originally used to establish color continuity; however, the trend today is increasingly moving towards creative goals such as improving the aesthetics of an image, establishing stylized looks, and setting the mood of a scene through color. Due to this trend, some colorists suggest the phrase "color enhancement" over "color correction".

## Primary and Secondary Color Grading

This is the fundamental distinction in color grading:

**Primary color grading** affects the whole image by providing control over the color density curves of red, green, blue color channels, across the entire frame. Primary corrections include:
- White balance / color temperature adjustments
- Exposure and contrast
- Global saturation
- Lift/Gamma/Gain (shadow, midtone, highlight) adjustments
- Overall hue rotation

**Secondary grading** can isolate a range of hue, saturation and brightness values to bring about alterations in hue, saturation and luminance only in that range, allowing the grading of secondary colors, while having a minimal or usually no effect on the remainder of the color spectrum.

Using digital grading, objects and color ranges within a scene can be isolated with precision and adjusted. Color tints can be manipulated and visual treatments pushed to extremes not physically possible with laboratory processing. With these advancements, the color grading process has become increasingly similar to well-established digital painting techniques.

### Secondary Corrections in Practice

- **HSL Qualifiers**: Isolate specific hue ranges (e.g., make only the greens more vibrant)
- **Luma Keying**: Isolate based on brightness (e.g., darken only the highlights)
- **Saturation Qualifiers**: Target specific saturation ranges
- **Skin Tone Isolation**: Protect or enhance skin tones separately
- **Vectorscope-based selection**: Pinpoint specific hues on the vectorscope

### In Lightroom / Still Photography

The same principles apply but with different terminology:
- **Primary**: Basic panel (WB, Exposure, Contrast, global Saturation)
- **Secondary**: HSL/Color panel, Color Grading wheels, Calibration panel
- **Local**: Masks, brushes, gradients, range masks

## Masks, Mattes, Power Windows

The evolution of digital color grading tools has advanced to the point where the colorist can use geometric shapes (such as mattes or masks) to isolate color adjustments to specific areas of an image. These tools can highlight a wall in the background and color only that wall, leaving the rest of the frame alone, or color everything but that wall.

Subsequent color grading tools (typically software-based) have the ability to use spline-based shapes for even greater control over isolating color adjustments. Color keying is also used for isolating areas to adjust.

Inside and outside of area-based isolations, digital filtration can be applied to soften, sharpen or mimic the effects of traditional glass photographic filters.

## Orange and Teal

In the 2000s, with the increase of digital technology, color grading in Hollywood films became more common. From 2010, many films, such as Hot Tub Time Machine and Iron Man 2, began using the complementary colors orange and teal. This look has become a defining characteristic of contemporary blockbuster cinema.

The orange-and-teal look works because:
- Skin tones naturally fall in the orange range
- Teal is the complementary color to orange on the color wheel
- Pushing shadows toward teal and highlights toward warm creates maximum color contrast
- It creates depth: warm subjects "pop" against cool backgrounds

## Color Timing (Historical Context)

Color timing is specified in printer points which represent presets in a lab contact printer where 7 to 12 printer points represent one stop of light. The number of points per stop varied based upon negative or print stock and different presets at film labs.

In a film production, the creative team would meet with the "lab timer" who would watch a running film and make notes dependent upon the team's directions. After the session, the timer would return to the lab and put the film negative on a device (the Hazeltine) which had preview filters with a controlled backlight, picking exact settings of each printer point for each scene.

## Digital Intermediate (DI)

The evolution of the telecine device into film scanning allowed the digital information scanned from a film negative to be of sufficient resolution to transfer back to film. In the early 1990s, Kodak developed the Cineon Film System to capture, manipulate, and record back to film and they called this the "Digital Intermediate."

In Hollywood, O Brother, Where Art Thou? was the first film to be wholly digitally graded. The negative was scanned with a Spirit DataCine at 2K resolution, then colors were digitally fine-tuned using a Pandora MegaDef color corrector on a Virtual DataCine.

Modern motion picture processing typically uses both digital cameras and digital projectors. Calibrated devices are most commonly used to maintain a consistent appearance within the workflow.

## Hardware-based versus Software-based Systems

Hardware-based systems (da Vinci 2K, Pandora International MegaDEF, etc.) have historically offered better performance but a smaller feature set than software-based systems. Their real time performance was optimized to particular resolution and bit depths, as opposed to software platforms using standard computer industry hardware that often trade speed for resolution independence.

The line between hardware and software no longer exists as many software-based color correctors (Pablo, Mistika, SCRATCH, Autodesk Lustre, Nucoda Film Master, Baselight, DaVinci Resolve) use multi processor workstations and a GPU as a means of hardware acceleration.

## Application to Preset Design

For Lightroom preset creation:

1. **Primary adjustments come first**: WB, Exposure, Contrast form the foundation
2. **Tone curve is primary**: It affects the entire image's contrast structure
3. **HSL is secondary**: Target specific color ranges without affecting the whole image
4. **Color Grading wheels** (lift/gamma/gain with hue offsets) bridge primary and secondary
5. **Keep the hierarchy clean**: Don't fight tone curve choices with HSL, and don't fight HSL with calibration
6. **The "simple" originals worked**: Having 8-15 attributes targeting the right things beats 60+ attributes fighting each other
