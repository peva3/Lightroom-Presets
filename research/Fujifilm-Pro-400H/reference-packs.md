# Fujifilm Pro 400H — Reference Packs & Commercial Preset Documentation

> What Mastin Labs, RNI, VSCO, and other commercial preset makers document about Pro 400H in their products.

---

## 1. Mastin Labs — Fujicolor Pushed Pack

### Product Context

Mastin Labs released the **Fujicolor Pushed** preset pack as part of their Fujicolor lineup, which included:
- **Fujicolor Original** — standard Fuji stock emulations (Pro 400H, Pro 160NS/160C)
- **Fujicolor Pushed** — pushed/overexposed variants designed to replicate the "shot at ISO 200" look that defined the wedding photography aesthetic

### What Mastin Documented About Pro 400H

Mastin's presets were specifically designed to work with their **3-step workflow**:
1. Apply the **base preset** (Fuji 400H or Fuji 400H Pushed)
2. Adjust **exposure** (Mastin required manual exposure adjustment, not auto)
3. Apply **tone profile** (hard/soft — for contrast adjustment)

#### Key Characteristics of the Mastin Pro 400H Preset:

| Property | Implementation |
|---|---|
| **White balance** | Cooled from neutral, slight magenta bias |
| **Contrast** | Low — softer than Mastin's Portra presets |
| **Highlight rolloff** | Soft, filmic shoulder — no hard clip |
| **Shadow color** | Cool — teal/cyan cast in deep shadows |
| **Green rendering** | Cool, desaturated, shifted toward cyan |
| **Skin tones** | Pink-magenta undertone, cool-neutral base |
| **Saturation** | Low overall, with color-specific desaturation in greens and blues |
| **Grain** | Profile-specific grain emulation (matched to real Pro 400H grain scans) |

#### Mastin's Pushed Variant:

The "Pushed" preset specifically targeted the **overexposed Pro 400H look** that wedding photographers used:
- Exposure set higher by default (+0.5 to +1.0 EV equivalent in the preset)
- Further reduced contrast
- More pronounced pastel bloom
- Even softer highlight rolloff
- Lifted shadows into the mint range more aggressively

### Community Feedback on Mastin Pro 400H (from r/Lightroom)

From the 2016 thread on the Mastin Fuji 400H preset:

> *"Presets are starting points, not end points."* — u/ApatheticAbsurdist

Users consistently found:
- The preset was "too bright" out of the box — accurate to the overexposed 400H look but needed pulling back for some images
- It was "mostly just flat" — some users wanted deeper shadows than the preset default
- Adding vibrance helped "bring life back" after the desaturation
- Manual exposure adjustment was essential — the preset didn't work as a one-click solution

### Mastin's Philosophy

Mastin presets were designed to **replicate the film look, not the film itself** — meaning they targeted how 400H looked when professionally scanned on a Frontier SP-3000, not the raw negative characteristics. This is an important distinction for anyone trying to compare preset makers.

---

## 2. RNI (Really Nice Images) — All Films 5 Pro

### Product Context

RNI All Films 5 Pro is a comprehensive film simulation pack containing **DCP camera profiles** (not just slider presets) for Lightroom and Capture One. It includes Fujifilm Pro 400H emulations.

### Pro 400H Variants in RNI

RNI typically provides **multiple variants** of each film stock, reflecting different scanning/development interpretations:

#### Typical RNI Pro 400H Variants:
| Variant | Description |
|---|---|
| **Pro 400H (Standard)** | "Box speed" neutral interpretation |
| **Pro 400H (Faded)** | Overexposed/pastel look, lower contrast |
| **Pro 400H (Frontier)** | Emulates Frontier SP-3000 scanner interpretation |
| **Pro 400H (Noritsu)** | Emulates Noritsu HS-1800 scanner interpretation |

### RNI's Methodology

RNI uses **DCP (Digital Camera Profile) technology** rather than pure slider presets:
- DCP profiles modify the raw demosaicing/color rendering at a fundamental level
- Provides more accurate highlight handling than slider-only presets
- Camera-native color science is transformed to match film response
- More consistent across different lighting conditions

### Community Reception (from r/Lightroom)

From the 2025 thread comparing Cobalt vs RNI:

> *"RNI seems like a mystery box haha"* — u/Fickle-Jellyfish-287

> *"RNI seems easy to install and straightforward, but do they hold up for professional work where consistency matters?"*

RNI was generally considered:
- More accessible/approachable than Cobalt Image
- Good enough for professional work
- Less sensor-specific than Cobalt (broader compatibility but potentially less accurate)
- Somewhat opaque about methodology
- Well-regarded for Fujifilm emulations specifically

---

## 3. VSCO Film Packs

### Product Context

VSCO Film was the original commercial film emulation preset system for Lightroom (discontinued as standalone, later integrated into VSCO's mobile app). VSCO's film packs included Fuji Pro 400H emulations.

### Pro 400H in VSCO Film

VSCO Film Pack 02 and/or 06 typically included Fujifilm emulations. The Pro 400H emulation was characterized by:

#### VSCO's Pro 400H Profile:
| Property | Behavior |
|---|---|
| **Color profile** | Cooler than VSCO's Portra profiles |
| **Skin tones** | Neutral-cool with subtle pink |
| **Contrast** | Lowered via custom tone curve |
| **Shadow tint** | Cool/teal bias |
| **Grain** | Subtle, fine grain pattern |

#### VSCO's Approach vs. Mastin/RNI:
- VSCO used a combination of camera profiles and slider adjustments
- Less sensor-accurate than Cobalt/DCP-based solutions
- More of a "vibe" emulation than a technical match
- Targeted the "Instagram-ready" look rather than print accuracy
- Historically significant as the first mainstream film preset system

### VSCO's Discontinuation

VSCO discontinued their desktop film presets in the late 2010s, transitioning to a mobile-first subscription model. The original Lightroom presets are no longer sold but remain in use by photographers who purchased them.

---

## 4. Cobalt Image

### Product Context

Cobalt Image produces **sensor-specific DCP camera profiles** for accurate film emulation. They are considered the most technically rigorous commercial option.

### Pro 400H in Cobalt

Cobalt Image's approach:
- **Sensor-specific profiles** — different DCP for Sony vs. Canon vs. Nikon vs. Fujifilm sensors
- Profiles model the actual **spectral response** of the film on the target sensor
- Claims to handle **highlight color accuracy** better than slider-based presets
- Best-in-class for avoiding clipping artifacts at high exposure
- Complex documentation, harder to set up

### Community Assessment (from r/Lightroom, 2025):

> *"Cobalt seems technically superior with their sensor specific profiles, but their site and documentation are a bit of a maze."*

Cobalt was recommended for:
- Professional work requiring consistency across shoots
- Print-critical work where color accuracy matters
- Users willing to invest time in setup for superior results

---

## 5. Other Notable Pro 400H Emulations

### PresetPane / PresetLove / FilterGrade

Various preset marketplaces sell "Fuji Pro 400H" presets, but these are typically:
- Generic, slider-only adjustments
- Not based on real film measurements
- Inconsistent quality
- Often just a desaturated + cooled + lifted-shadows formula

### DXO FilmPack

DXO FilmPack includes a Fuji Pro 400H emulation that:
- Uses DXO's lens/sensor correction database
- Models grain based on real film samples
- Less popular than Mastin/RNI but technically competent
- Windows/Mac standalone + Lightroom/Photoshop plugin

### Dehancer (DaVinci Resolve / Photoshop)

Dehancer, primarily a film emulation plugin for video, includes Pro 400H as a color profile:
- Built on spectral modeling of real film stocks
- Includes grain, halation, bloom, and film damage emulation
- Available for Resolve, Final Cut Pro, Premiere, and Photoshop
- Well-regarded in the video/filmmaking community

### FilmConvert / CinePrint16

FilmConvert's film stock library includes Pro 400H:
- Targeted at video colorists
- Uses camera-specific input transforms
- Less popular than Dehancer for stills

### Negative Lab Pro (Lightroom)

NLP is the dominant tool for converting film scans, but it does not provide Pro 400H presets for digital images. However, understanding NLP's rendering of real Pro 400H scans can inform what a digital emulation should target:
- NLP's "Frontier" mode + Pro 400H scans produce the canonical pastel look
- NLP's "Noritsu" mode + Pro 400H scans produce a warmer, more contrasty look
- The difference between modes illustrates how much scanner interpretation defines "the Pro 400H look"

---

## 6. The Mastin Fuji Pushed Pack — Historical Significance

Mastin Labs' Fuji Pushed pack was notable because it explicitly acknowledged that the community was **not shooting Pro 400H at box speed**. The "Pushed" branding reflected real-world usage:

- Wedding photographers shot Pro 400H at ISO 100–200 (1–2 stops over)
- Mastin created a dedicated variant for this specific practice
- No other preset maker explicitly segmented their product this way
- This made Mastin's Fuji presets the closest-to-reality for the "overexposed pastel wedding look"

The Mastin Fuji Pushed pack was eventually folded into the broader Mastin Fujicolor lineup and is no longer sold separately.

---

## 7. Comparison Matrix: Commercial Pro 400H Emulations

| Product | Type | Methodology | Accuracy | Ease of Use | Still Available? |
|---|---|---|---|---|---|
| **Mastin Fujicolor (incl. Pushed)** | LR Presets | Real film profiling + manual tuning | Good | Easy | Yes (Fujicolor pack) |
| **RNI All Films 5 Pro** | DCP Profiles + Presets | Real film, multiple scanner interpretations | Very Good | Easy | Yes |
| **Cobalt Image** | DCP Profiles | Sensor-specific spectral modeling | Excellent | Complex | Yes |
| **VSCO Film (discontinued)** | LR Presets | Real film profiling | Good (for its era) | Easy | No (desktop) |
| **DXO FilmPack** | Plugin + LR Presets | Real film samples | Good | Moderate | Yes |
| **Dehancer** | Plugin (video/stills) | Spectral modeling | Very Good | Moderate | Yes |

---

## 8. Key Takeaway for Preset Development

Commercial preset makers converge on several consistent choices for Pro 400H emulation:

1. **Cooler white balance with magenta bias** — universal across all makers
2. **Low contrast with soft highlight rolloff** — the most important tonal characteristic
3. **Desaturated, cyan-shifted greens** — the defining color move
4. **Cool/teal shadow tinting** — simulates the 4th layer's shadow signature
5. **Subtle, fine grain** — finer than Portra emulations
6. **Multiple variants for different scanner/exposure interpretations** — no single "correct" 400H look

The most significant divergence between makers is:
- **DCP/lab-profile based** (Cobalt, RNI) vs. **slider-preset based** (Mastin, VSCO)
- **Sensor-specific calibration** vs. **universal profiles**
- **Frontier-biased interpretation** (pastel, cool) vs. **Noritsu-biased** (warmer, more contrast)
- **Box-speed calibration** vs. **overexposure-biased** ("Pushed")

---

## Sources

- [Mastin Labs — Fujicolor presets product page](https://mastinlabs.com/) (archived references)
- [r/Lightroom — Mastin Fuji 400H preset discussion](https://old.reddit.com/r/Lightroom/comments/5f15uu/)
- [r/Lightroom — Cobalt vs RNI DCP profiles](https://old.reddit.com/r/Lightroom/comments/1s9111i/)
- [r/Lightroom — RNI All Pro 5 preset compatibility](https://old.reddit.com/r/Lightroom/comments/120tjsy/)
- VSCO Film documentation (archived)
- Cobalt Image product documentation
- Dehancer Pro film profiles documentation
- DXO FilmPack film stock list
- Negative Lab Pro documentation
- [r/AnalogCommunity — DIY Pro 400H digital archiving methodology](https://old.reddit.com/r/AnalogCommunity/comments/ohjgma/)
