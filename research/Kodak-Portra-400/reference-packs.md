# Kodak Portra 400 — Reference Preset Packs

> How Mastin Labs, RNI (Really Nice Images), VSCO, and other commercial products document and emulate Portra 400.

---

## Mastin Labs — Portra Original

### Product Info
- **Pack**: Mastin Labs Portra Original (replaced by "Portra Pushed" in 2023, but "Original" is the Portra 400/160/800 pack)
- **Price**: ~$99
- **Format**: Lightroom Presets + Profiles
- **Target**: Professional wedding/portrait photographers; batch-editing friendly

### Mastin's Portra 400 Philosophy
Mastin positions Portra as their **warmest, most flattering film emulation**. Their marketing copy emphasizes:
- "Warm, glowing skin tones"
- "Soft, forgiving contrast"
- "Signature pastel color palette"
- "True-to-analog film grain"

### What Mastin Documents About Portra 400:
- **Three strength variants per stock**: Each Portra emulation comes in 3 "flavors" — a standard version, a softer version, and a punchier version
- **Tone profiles**: Separate tone curves for "hard light" and "soft light" shooting conditions
- **Grain**: Emulated grain pattern based on real Portra 400 scans
- **Built-in white balance presets** for different lighting (daylight, tungsten, cloudy)

### Community Assessment (from Reddit):
- Praised as "gorgeous" and "batch-wedding ready"
- Some users find them too strong/saturated out of box
- The Tone Profile system is considered Mastin's strength — handles different lighting better than many competitors
- Less accurate to scanning profiles (doesn't distinguish Noritsu/Frontier) than RNI

---

## RNI (Really Nice Images) — All Films 5

### Product Info
- **Pack**: RNI All Films 5 (includes Portra 400 in the base library; also available in free Demo)
- **Price**: $149 (full), Free (demo with limited stocks)
- **Format**: Lightroom Profiles (.xmp camera profiles), Capture One Styles, iOS apps
- **Generations**: Gen 5 is the latest (2023+), uses profile-based approach

### RNI's Portra 400 Philosophy
RNI is explicitly a **colorimetric** approach — they build profiles from real film stock measurements and aim for technical accuracy. Unlike Mastin's "creative" approach, RNI tries to scientifically match the film.

### What RNI Documents About Portra 400:
- **Profile-based** (doesn't touch adjustment sliders — installed as camera profiles alongside "Adobe Color", "Adobe Standard", etc.)
- **Camera-profiled**: RNI profiles are calibrated per-camera-sensor (Sony, Canon, Nikon, Fuji, Leica all separate profiles)
- **Density-variant**: Some packs include different "development" variants (box speed, pushed, pulled)
- **Cross-platform**: Desktop profiles sync to Lightroom Mobile

### RNI Portra 400 — Community Observations (from Reddit):

**Strengths:**
- Most accurate color rendering of any commercial pack
- Smooth highlight compression (baked into profile — emulates film shoulder)
- Works well on skin tones
- Free demo lets you test Portra 400 before buying

**Weaknesses:**
- **Clips white and black points** — the profile prevents reaching true white (r/Lightroom comment: "Look at the histogram, their profile is preventing the image from getting true white")
- Shadow/highlight compression is baked into the profile and **cannot be adjusted** with sliders
- Whites can appear slightly gray/pinkish (noted as actually authentic to overexposed Portra behavior)
- Some users want the color science without the tonal compression

### RNI vs. Color Precision — Head-to-Head (from r/Lightroom):
- RNI: Better color rendering overall, smoother highlight transitions
- Color Precision: More flexible (can push whites brighter), but yellow shift in bright areas looks "weird"
- RNI highlight compression is divisive — some love it (filmic), others hate it (can't adjust)

---

## VSCO Film 06 (Discontinued)

### Product Info
- **Pack**: VSCO Film 06 — The Alternative Process Pack (also VSCO 01 has Portra 800)
- **Price**: Was ~$59 (discontinued 2019, no longer sold)
- **Format**: Lightroom Camera Profiles + Presets

### VSCO's Portra 400 Documentation
VSCO was the original benchmark. Film 06 included:
- **Portra 400** (standard)
- **Portra 400+** (pushed, more contrast/saturation)
- **Portra 400-** (pulled, flatter, more pastel)
- **Portra 400 HC** (high contrast variant)

### Legacy and Community Sentiment:
- Still sought after years after discontinuation (r/Lightroom has posts of users asking for old VSCO presets)
- Users switching to Canon R5 report VSCO profiles don't support newer cameras
- The "Portra 400+ preset" from VSCO 06 is the single most-referenced analog emulation in the history of Lightroom presets
- Many still consider VSCO the gold standard, especially for Portra 400

---

## Color Precision — Portra 400 (Noritsu)

### Product Info
- **Price**: ~$40
- **Format**: Lightroom Profiles
- **Target**: Noritsu HS-1800 scanner look specifically

### Community Assessment:
- Good Noritsu emulation but **yellow shift in highlights** criticized as unrealistic
- Requires manual highlight adjustment after applying the profile
- More flexible than RNI but less "polished" out of box

---

## Caleb Salvadori — Film Preset Collection

### Product Info
- **Price**: ~$60
- **Format**: Lightroom Profiles
- **Selection**: ~25 curated presets (not hundreds)

### Community Assessment (from Reddit):
- "Better than RNI" — mentioned in r/Lightroom RNI vs CP thread
- Narrower selection seen as advantage (less overwhelming)
- High quality sample images
- Relatively newer entrant compared to RNI/Mastin

---

## Other Notable Packs

### Jamie Windsor — Film Essentials / Portra Pack
- **Price**: ~$15-25
- **Format**: Lightroom Profiles
- Budget option, highly recommended on r/Lightroom
- Medium Format Stocks (Set 2) includes Portra 400

### Cobalt Image
- **Price**: ~$60 per individual film stock (expensive)
- **Format**: Profiles
- "VERY accurate" but "not fun or moody" — clinical, scientific approach
- Limited selection, expensive per-film

### ANDP Film Styles
- **Price**: ~$5 per stock
- **Format**: LUT-based profiles (.xmp)
- Cheapest option mentioned on r/postprocessing
- Works "fine out of the box, can be further tweaked"

### DxO FilmPack / Nik Collection
- **Format**: Integrated into DxO/Nik workflow
- Used as alternative to Lightroom-native presets
- Nik allows viewing and modifying every element of the recipe (curves, grain, color)

---

## The "Graded Scan vs Raw Negative" Divide (How Packs Differ)

### Mastin Labs approach:
- Models the **graded, lab-delivered scan** — the final look a client receives
- This means: built-in contrast, color grading, and density adjustments
- Less flexible, more "one-click wonder"

### RNI approach:
- Models the **film emulsion itself** as a color profile
- Leaves exposure/contrast adjustments to the user
- More flexible but requires more user skill

### VSCO approach (legacy):
- Multiple variants: standard, pushed, pulled
- Acknowledged that "Portra 400" doesn't have one single look
- The benchmark others are measured against

### Noritsu vs. Frontier split:
- **Mastin**: Doesn't explicitly target a scanner; their look is "graded Portra"
- **RNI**: Similarly doesn't specify scanner; their profile is "the film"
- **Color Precision**: Explicitly targets Noritsu HS-1800
- **Cobalt Image**: May offer scanner-specific variants
- Most community DIY recipes target one or the other implicitly

---

## Price Comparison (May 2026)

| Product | Price | Free Trial | Format |
|---------|-------|-----------|--------|
| RNI All Films 5 | $149 | Yes (demo) | Profiles |
| Mastin Labs Portra | $99 | No | Presets + Profiles |
| Caleb Salvadori | ~$60 | No | Profiles |
| Cobalt Image | ~$60/stock | No | Profiles |
| Color Precision | ~$40 | No | Profiles |
| Jamie Windsor | ~$15-25 | No | Profiles |
| ANDP Film Styles | ~$5 | No | LUT/Profiles |
| Filmis.fun Portra 400 | ~$5 | No | Presets |
| RNI Demo | Free | N/A | Profiles (Portra 400 included) |

---

## Which Pack for Which User?

| User Profile | Recommended Pack |
|-------------|-----------------|
| Wedding pro, batch editing | Mastin Labs Portra Original |
| Color accuracy obsessive | RNI All Films 5 (or Cobalt Image) |
| Budget hobbyist | RNI Demo (free Portra 400) or Jamie Windsor |
| Learning curve | Caleb Salvadori (fewer presets = less overwhelm) |
| Noritsu look specifically | Color Precision |
| "Just give me the old VSCO" | Community DIY recipes + profiles |
| Fuji camera owner | Fuji X Weekly in-camera recipe (free) |

---

*Compiled May 2026. Prices and availability subject to change. Product descriptions from marketing pages, Reddit discussions, and community reviews. Not affiliated with any product mentioned.*
