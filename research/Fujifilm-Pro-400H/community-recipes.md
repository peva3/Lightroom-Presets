# Fujifilm Pro 400H — Community Lightroom Recipes

> Community attempts to recreate the Pro 400H look digitally. Gathered from Reddit, YouTube, forums, and preset-share sites. Treated as starting points — the real look depends heavily on base image color, exposure, and white balance.

---

## 1. Lightroom Zen — Fuji Pro Free Preset (2016)

**Source:** `lightroomzen.com` (r/Lightroom thread, 2016)
**Thread:** r/Lightroom/comments/50ol5r — "Free Preset - Fuji Pro Film"

This was an early community attempt at a Fuji Pro 400H emulation. The preset took a generic "Fuji Pro" approach without distinguishing between 400H and other Fuji stocks. It was described as lowering contrast and introducing cool tones.

**General approach from this era:**
- Pull contrast down (−15 to −25)
- Lift shadows (+20 to +40)
- Cool the temp slightly (−200 to −400K from auto WB)
- Add subtle magenta tint (+5 to +15)
- Reduce saturation (−10 to −20)

---

## 2. Reddit r/Lightroom — Mastin Fuji 400H Preset Discussion (2016)

**Thread:** r/Lightroom/comments/5f15uu — "Mastin Fuji 400h preset--does this look too bright?"

A user applied the Mastin Labs Fuji 400H preset and asked the community for feedback. Key community feedback from that thread:

### The Preset Was Described As:
- Initially too bright/flat — OP had increased both **temperature** and **exposure** beyond the Mastin defaults
- "Maybe a tad, but mostly just flat. Bring down them shadows a bit." — u/deleted
- "Drop the exposure a little see if it looks any better. Presets are starting points, not end points." — u/ApatheticAbsurdist
- One user corrected by pulling exposure down ~1 stop and noted it looked "pretty good"

### Community Adjustments Applied:
- Reduce exposure slightly from preset default
- Pull down shadows for depth while keeping the airy feel
- Slight negative vignette for focus
- Add vibrance (not saturation) to bring back some color life

**Takeaway:** The Mastin preset erred on the side of the "overexposed 400H look" — bright, low-contrast, pastel. Users consistently found they needed to pull exposure back and deepen shadows from the default to taste.

---

## 3. Community Film Emulation Presets (PresetsHeaven, 2009)

**Thread:** r/Lightroom/comments/ggjra — "Quality sets of pro-film emulsion presets for lightroom"

These were early (2008–2009) community-generated film emulation presets based on "analysis of pro film stocks." The Fuji Pro 400H preset in "MikeyG's collection" was described as:

- Good starting point, not perfectly accurate
- Did "remove some of your digital flatness"
- The collection included both color and B&W film emulations

These are historically interesting but very dated relative to modern tools.

---

## 4. Cobalt Image / RNI — DCP Profile Discussion (2025)

**Thread:** r/Lightroom/comments/1s9111i — "Camera RAW/Lightroom profiles: On the hunt for good Fuji Pro and Ektachrome (DCP)"

A serious community discussion about moving beyond basic presets to **DCP camera profiles** for authentic film emulation:

### Community Consensus:
- **Cobalt Image** — technically superior, sensor-specific profiles, complex documentation. Considered the "pro" choice.
- **RNI (Really Nice Images) All Films 5 Pro** — easier to use, good for professional work, "mystery box" approach to methodology.
- Most free profiles only work well in high-key/0EV environments — they break when pushing files.
- Serious emulation requires DCP profiles (not just slider presets) for highlight color accuracy and no clipping.

### Key Requirements for a "Real" Pro 400H Emulation (from the thread):
- Authentic tones
- Highlight color accuracy (no clipping/false color)
- Works at varying exposures, not just 0EV
- Doesn't "break" the file

---

## 5. r/AnalogCommunity — DIY Digital Archival Approach (2021)

**Thread:** r/AnalogCommunity/comments/ohjgma — "Digitally archiving Fuji Pro 400H"

A community member proposed a rigorous methodology for creating accurate Pro 400H emulations:

### Proposed Method:
1. Take **identical Pro 400H and digital shots** through the same lens
2. Photograph color calibration charts and **HALD CLUT charts**
3. Digitally align images and measure color differentials
4. Account for different light temperatures and exposure levels
5. Create sensor-specific color maps and grain scans

### Key Insight from OP:
> *"My problem with the film simulations that are out there is that, because nobody ever publishes their methodology or source material, I have no idea whether they used an even vaguely film-accurate method, or whether they're eyeballing it. I think a lot of times it's just being eyeballed."*

This approach — shooting physical Pro 400H alongside digital, measuring the real color transform — is how professional film emulation LUTs are made (Mastin, RNI, Cobalt). The community acknowledged this is the gold standard but very labor-intensive.

---

## 6. DIY Lightroom Recipe — Community-Sourced Approximate

Based on aggregating community discussions across r/Lightroom, r/analog, and various forums. **This is approximate — use as a starting point only.**

### Basic Panel
| Setting | Value | Rationale |
|---|---|---|
| **WB Temp** | −200 to −400 from auto | Cool the image toward 400H's neutral-cool palette |
| **WB Tint** | +5 to +15 magenta | Pro 400H has slight magenta bias |
| **Exposure** | +0.30 to +0.70 | Simulates shooting at ISO 200 (the ideal) |
| **Contrast** | −15 to −25 | Lower contrast for pastel bloom |
| **Highlights** | −40 to −60 | Recover highlight detail (400H holds highlights beautifully) |
| **Shadows** | +20 to +40 | Lift shadows into pastel range |
| **Whites** | 0 to −10 | Keep whites clean but not clipped |
| **Blacks** | −10 to −20 | Slight black deepening for anchor |

### Tone Curve
| Point | Adjustment |
|---|---|
| **Darks (shadows)** | Lift slightly — create a soft toe |
| **Lights (highlights)** | Lower slightly — create a soft shoulder |
| **Point curve** | S-curve with lifted blacks and compressed highlights |

### HSL / Color Mixer
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| **Red** | +5 toward orange-pink | −10 to −15 | +5 |
| **Orange** | 0 | −15 | +10 (lifts skin tones) |
| **Yellow** | +5 toward green-yellow | −15 to −20 | +10 |
| **Green** | +20 toward cyan/teal | −20 to −30 | −5 |
| **Aqua** | +5 toward blue | −10 | +5 |
| **Blue** | −5 toward cyan | −15 to −20 | +15 (pastel sky) |
| **Purple** | +10 toward magenta | −10 | 0 |
| **Magenta** | +10 toward pink | −5 | +5 |

**The most important HSL moves:**
1. **Green hue → +20 toward cyan** — this creates the cool minty green that defines 400H's palette
2. **Blue luminance → +15** — lightens blues to pastel
3. **All saturation values down** — the 400H look is fundamentally desaturated/pastel

### Color Grading (Split Toning)
| Region | Hue | Saturation |
|---|---|---|
| **Shadows** | 180–200 (teal/cyan) | 5–10 |
| **Midtones** | 0 | 0 (keep neutral) |
| **Highlights** | 40–50 (warm, subtle) | 3–5 |

The **teal/cyan shadow split** is critical — it's the digital equivalent of Pro 400H's mint-green shadow signature. Keep it subtle.

### Calibration Panel
| Channel | Hue | Saturation |
|---|---|---|
| **Red Primary** | +10 toward orange | −5 |
| **Green Primary** | +10 toward cyan | −10 |
| **Blue Primary** | −5 toward cyan | −5 |

The green primary shift toward cyan is the key calibration move — it tilts the entire green channel toward the minty-cool 400H palette.

### Effects
| Setting | Value |
|---|---|
| **Grain** | Amount: 15–25, Size: 25 (35mm), Roughness: 50 |
| **Vignette** | −5 to −10 (subtle) |

### Detail
| Setting | Value |
|---|---|
| **Sharpening** | 40–60 (standard digital, do not over-sharpen) |
| **Noise Reduction** | As needed per sensor |

---

## 7. YouTube Creator Recipes

While specific video URLs change frequently, the consistent pattern from YouTube tutorials on "Pro 400H Lightroom" has been:

1. Start from a **flat/neutral camera profile** (Adobe Standard or camera Neutral)
2. **Cool the white balance** significantly (many digital images are too warm to begin with)
3. **Desaturate greens and shift them toward cyan**
4. Add **teal to shadows** via split toning or calibration
5. **Lift exposure** but pull highlights down — simulating overexposure latitude
6. Add **subtle magenta to skin tones** (HSL orange luminance +, magenta saturation −)
7. Apply **grain** last at low opacity

---

## 8. Critical Notes

1. **No single preset is definitive** — Pro 400H looks different on Frontier vs. Noritsu vs. Imacon scans. Choose your "reference 400H look" before tuning.
2. **Starting image matters enormously** — warm sunset images will never look like 400H without significant white balance correction.
3. **DCP profiles > presets** — for accurate highlight handling, you need a camera profile (DCP) that models the film's color response, not just slider moves.
4. **Overexposure is part of the look** — the film was shot at ISO 200 by almost everyone. If your digital image is exposed at 0EV, the 400H look won't fully engage.
5. **Scanning and lab interpretation vary wildly** — a Frontier SP-3000 scan of 400H is the "canonical" look most people mean when they talk about 400H's aesthetic.

---

## Sources

- [r/Lightroom — Mastin Fuji 400H preset thread](https://old.reddit.com/r/Lightroom/comments/5f15uu/)
- [r/Lightroom — Free Preset Fuji Pro Film](https://old.reddit.com/r/Lightroom/comments/50ol5r/)
- [r/Lightroom — Pro film emulsion presets](https://old.reddit.com/r/Lightroom/comments/ggjra/)
- [r/Lightroom — Cobalt vs RNI DCP profiles](https://old.reddit.com/r/Lightroom/comments/1s9111i/)
- [r/AnalogCommunity — Digitally archiving Pro 400H](https://old.reddit.com/r/AnalogCommunity/comments/ohjgma/)
- [r/AnalogCommunity — Thoughts on Pro 400H (scanning methodology)](https://old.reddit.com/r/AnalogCommunity/comments/1s0x532/)
- Lightroom Zen blog (archived, 2016)
- Aggregated YouTube tutorials on Pro 400H emulation (various creators, 2021–2024)
