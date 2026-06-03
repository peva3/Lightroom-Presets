# Super 8 / Home Movie Aesthetic Lightroom Preset — Full Characteristics Breakdown

## Overview

The Super 8 Home Movie Lightroom preset recreates this look digitally using Lightroom's color grading tools for authentic film emulation. The Super 8 home movie aesthetic is the dominant vintage-film look in contemporary wedding and lifestyle photography. It emulates the look of amateur 8mm motion picture film shot on Kodak consumer cameras between 1965 and the early 1980s. The aesthetic is warm, nostalgic, imperfect, and emotionally evocative — the antithesis of crisp, clinical digital capture.

Unlike clean 35mm still-film emulation, the Super 8 look deliberately embraces *degradation artifacts* that signal "memory" and "home" — the visual equivalent of a worn family photo album.

---

## 1. Gate Weave (Frame Instability)

**What it is:** In a real Super 8 projector, the film moves through a mechanical gate that holds each frame briefly in front of the lamp. Wear, loose tolerances, and film shrinkage cause the frame to shift slightly side-to-side or up-and-down between exposures. This produces a subtle, continuous "weaving" or "swimming" motion.

**Why it matters aesthetically:** Gate weave is one of the strongest subliminal cues that footage is analog film, not digital. It imparts a living, breathing quality — the image is never perfectly still. Even in a still photograph emulation, subtle rotational jitter or edge instability can evoke this.

**How to emulate in stills (pre-grade approach):**
- Very subtle vignette that is slightly off-center (0.5–1.5% offset)
- Slight rotation of whole image (0.2°–0.8°) on individual frames in a series
- Crop variation between 1–3% across frames in a set
- In Lightroom: done in post via export batch with variable crop/rotation, or simulated with a clone/heal layer creating uneven edge softness

---

## 2. Light Leaks

**What they are:** Accidental exposure of film to light outside the camera body — through worn seals, cartridge gaps, or during loading. Appears as irregular patches of color (typically red, orange, yellow, or white) bleeding in from the edges or sprocket area.

**Characteristic patterns:**
- Orange/amber leaks: light passing through the orange film base from the back
- Red leaks: light striking the emulsion from the front (red-sensitive layer bleeds)
- White/cyan leaks: severe overexposure, often near the cartridge gate
- Streaky, flame-like shapes: light leaks through the film door felt seal during mid-roll

**Common Super 8 leak locations:**
- Top and bottom edges (film gate area)
- Right edge (cartridge window side)
- Left edge (sprocket hole side — often patterned)

**How to emulate in Lightroom/Photoshop:**
- Radial gradient overlays at edges with warm orange/red tones
- Linear gradients with blend mode set to Screen or Lighten
- Custom brush painting on a separate layer, masked to edges
- Use of LUT overlays or PNG texture packs with real scanned light leaks

---

## 3. Warm Color Cast / Desaturated Color Palette

**What it is:** Super 8 film stocks, especially Kodak Ektachrome 64T and 160T (tungsten-balanced), produced a characteristic warm shift. The 64T had muted saturation with a slight amber/sepia lean. 160T was even warmer, often with a brownish-gold cast. When tungsten films were shot outdoors without a correction filter, they produced a pronounced orange/amber cast that became iconic of the format.

**Key color characteristics:**
- White balance shifted warm: 4500K–5500K (toward amber, not clinical yellow)
- Overall desaturation: -10 to -30 global saturation
- Skin tones lean toward peach/amber (not magenta or orange)
- Greens are muted, slightly yellow-brown
- Blues are desaturated, tending toward teal/cyan
- Shadows have a subtle brown/magenta tint
- Highlights roll off toward warm cream or pale yellow

**How to emulate in Lightroom:**
- WB: Temp +800 to +2000, Tint -5 to +10 (toward magenta slightly)
- Saturation: -15 global
- HSL: Lower blue saturation -20, shift blue hue toward cyan +10
- HSL: Lower green saturation -25, darken greens luminance -15
- HSL: Orange hue toward yellow (+5 to +10), lower orange saturation -5
- Tone Curve: Lift blacks slightly, soften highlights
- Calibration: Red Primary Hue +20 toward orange, Blue Primary Hue -15 toward cyan, reduce Blue Primary Saturation -20

---

## 4. Soft Focus / Low Apparent Sharpness

**What it is:** Super 8 cameras used small, simple prime lenses (often fixed-focus or zone-focus) with limited resolving power. Combined with the tiny 5.46×4.01mm frame, the effective resolution was very low — roughly equivalent to 0.3–0.5 megapixels of usable detail in the best conditions. Consumer-grade lenses added spherical aberration.

**Visual characteristics:**
- No micro-contrast or edge sharpness
- Details blur together slightly
- Fine textures (hair, fabric, foliage) lose definition
- No "clinical" sharpness anywhere in the frame
- Subtle glow around bright objects

**How to emulate in Lightroom:**
- Sharpening: set to 0, or reduce to negative with masking
- Texture: -15 to -30
- Clarity: -10 to -25 (negative clarity is critical)
- Dehaze: -5 to -15 (adds atmospheric softness)
- In-camera: use a diffusion/mist filter (Tiffen Black Pro-Mist 1/8 or 1/4, CineBloom 10%, Glimmerglass 1)

---

## 5. Halation

**What it is:** Halation occurs when bright light passes through the film emulsion, bounces off the film base, and re-exposes the emulsion from behind, creating a red/orange glow halo around bright light sources and high-contrast edges. On Super 8 reversal film (no anti-halation backing), this is especially pronounced because the film base acts as a light pipe.

**Visual signature:**
- Red/orange fringing around specular highlights
- Glow extending 2–5% of image width beyond bright edges
- Most visible in high-contrast transitions (window light, backlit hair, candle flames)
- Affects bright light sources on dark backgrounds

**How to emulate in Lightroom/Photoshop:**
- Negative Dehaze (-10 to -20) creates atmospheric glow
- Lower Contrast helps soften hard transitions
- In Photoshop: duplicate layer, Gaussian Blur 15–30px, set blend mode to Screen at 15–30% opacity, mask to highlights only
- Red/pink color cast can be added to the glow layer with a Photo Filter adjustment clipped to it
- Diffusion filters in-camera (Pro-Mist, CineBloom) produce a related optical effect

---

## 6. Bloom (Highlight Glow)

**What it is:** A soft, diffuse glow that spreads from bright areas into adjacent darker areas. Related to halation but more about lens veiling flare + film scatter than base reflection. Super 8 lenses had minimal coatings, making them prone to veiling flare that wraps light softly around subjects.

**Visual signature:**
- Highlights "bleed" softly into midtones
- Window light, sky, and rim light spread gently
- Reduced contrast at highlight boundaries
- Overall dreamy, ethereal quality
- Shadows remain relatively intact (bloom is highlight-centric)

**How to emulate in Lightroom:**
- Highlights: -30 to -60 (pulls down highlight peaks but keeps glow)
- Whites: -10 to -25
- Clarity: -15 to -30 (reduces midtone contrast)
- Dehaze: -5 to -20
- Tone Curve: pull down the top-right point slightly, create a smooth roll-off
- In-camera: Tiffen Pro-Mist 1/4, CineBloom 20%, or Glimmerglass 1 filter

---

## 7. Edge Softness / Vignette

**What it is:** Super 8 lenses were plastic or low-grade glass with poor edge performance. Corners exhibit significant falloff in sharpness, light transmission, and color fidelity. Combined with the natural vignette of small-format projection, edges are darker, softer, and color-shifted.

**Visual characteristics:**
- Strong natural vignette (2–3 stops darker at corners)
- Sharpness falls off significantly toward edges
- Chromatic aberration fringing at extreme edges (magenta/cyan)
- Edge distortion (barrel distortion from wide-angle adapters)
- The center "sweet spot" carries most emotional weight

**How to emulate in Lightroom:**
- Post-Crop Vignetting: -15 to -30, Midpoint 35–50, Feather 50–75
- Use radial filters at edges with negative Sharpness (-30 to -50) and negative Clarity
- Edge color shift: subtle warm amber radial gradient at corners (match to overall warm cast)
- Add slight chromatic aberration simulation: split-tone edge coloring in Photoshop with red/cyan

---

## 8. Grain Structure

**What it is:** Super 8 grain is noticeably coarse because of the extreme enlargement ratio (5.46×4.01mm frame projected to screen size). Ektachrome 64T grain was fine for the format but chunky by modern standards. 160T was significantly grainier. The grain structure is also irregular — not the uniform digital noise of a sensor, but organic, clustered, with variation in size and density.

**Key grain characteristics for Super 8:**
- Mid-to-heavy grain presence
- Visible even in well-exposed frames
- Grain is larger and more textured in shadow areas
- Color noise in shadows: red/green chroma speckles
- Grain "dances" (in video) — for stills, organic clumping patterns

**How to emulate in Lightroom:**
- Grain Amount: 30–55
- Grain Size: 25–40 (larger than 35mm film emulation)
- Grain Roughness: 55–75 (rough, not smooth)
- In Photoshop: add a 50% gray layer, apply Film Grain or Add Noise (Gaussian, Monochromatic), set to Overlay at 20–35%

---

## 9. Aspect Ratio & Framing

**What it is:** Super 8's native aspect ratio is approximately 1.36:1 (virtually 4:3). This squarish frame is a powerful nostalgic signifier, immediately differentiating it from modern 3:2 or 16:9 capture.

**How to emulate:**
- Crop to 4:3 (8×6, 1200×900, or similar)
- Consider a slight letterbox effect for projection simulation
- Rounded corners (slight, 2–4px radius) suggest a projected frame

---

## 10. Color Timing / Print Fade

**What it is:** Over decades, Ektachrome reversal film fades. Highlights shift toward yellow/magenta, shadows lose density, and overall contrast decreases. This "aged film" look is often what people actually mean when they say "film look" — not fresh film, but film that's been in a shoebox for 40 years.

**How to emulate:**
- Slightly lifted (faded) blacks in Tone Curve
- Yellow bias in highlights via Color Grading panel
- Magenta tint in highlights and midtones (subtle, +3 to +8)
- Contrast: -10 to -20
- White point: slightly yellow-cream rather than pure white

---

## Summary: The Super 8 "Recipe" in Priority Order

1. **Warm color cast** (4500K–5500K, amber/gold lean) + desaturation
2. **Soft/glowing highlights** (bloom + halation) — negative Clarity, negative Dehaze
3. **Prominent grain** (coarse, rough, organic)
4. **Lifted/matte blacks** (faded shadows in tone curve)
5. **Cyan-teal shifted blues**, yellow-magenta highlights (Calibration + Split Toning)
6. **4:3 crop** with vignette
7. **Added light leaks** (orange/red edge gradients)
8. **Gate weave simulation** (subtle frame-to-frame instability for series)
9. **Soft/muted greens** (desaturated, darkened)
10. **Peach/amber skin tones** (orange hue shift, low saturation)

**Primary software tools for stills:**
- Lightroom: Basic panel, Tone Curve, HSL, Color Grading, Calibration, Effects (Grain), Lens Corrections (disable), Transform (slight rotation offset)
- Photoshop: Light leak overlays, halation glow layers, edge softening, chromatic aberration simulation
- In-camera: diffusion filters, warm white balance preset, underexpose 1/3 to 2/3 stop, shoot through vintage glass or adapters

## See Also

- [Creative Presets](../../docs/creative.md)
- [Color Negative Presets](../../docs/color-negative.md)
- [Video Presets](../../docs/video.md)
- [All Lightroom Preset Categories](../../docs/index.md)

