# Reference Packs — Commercial Tri-X 400 Lightroom Preset Documentation

> What paid preset packs (VSCO, Mastin Labs, RNI, DxO, Nik, etc.) document about their Tri-X 400 emulations.

---

## VSCO Film 01 — "Tri-X" (Discontinued but Widely Documented)

VSCO Film 01 was the industry-standard Lightroom preset pack for film emulation (2011–2022). The Tri-X presets were:

### Presets in the VSCO Tri-X Family

1. **Kodak Tri-X (+1)** — Tri-X at box speed. Moderate grain, strong contrast, open shadows.
2. **Kodak Tri-X (+2)** — Pushed Tri-X. Heavier grain, elevated contrast, deeper blacks.
3. **Kodak Tri-X (+3)** — Tri-X pushed 2+ stops. Extreme grain, very heavy contrast, aggressive crush.
4. **Kodak Tri-X 400 -** — Low contrast variant. Pulled look.
5. **Kodak Tri-X 400 +** — High contrast variant.
6. **Kodak Tri-X 400 ++** — Maximum contrast variant.

### VSCO Tri-X Characteristics (Documented by Community Analysis)

| Property | VSCO Behavior |
|----------|---------------|
| Tone Curve | Custom S-curve with lifted black point (RGB ~12-15 at black) and slightly rolled-off whites |
| Contrast | High — same "family feel" across all + variants |
| Grain | Tri-X grain is "larger and more pronounced" than their HP5 emulation — VSCO described it as "coarse but structured" |
| B&W Mix | Custom channel mixer weights — heavy red sensitivity (skin brightening) paired with blue darkening |
| Split Tone | Subtle warm tone in highlights (255, 248, 240) — very slight sepia shift in the highlights only |
| Sharpening | VSCO applies camera-specific sharpening profiles — Tri-X preset adds more sharpening than their Delta/T-Max presets |

### Notable VSCO Tri-X Design Philosophy

VSCO's blog (archived) documented their Tri-X approach:
- They profiled a Noritsu HS-1800 scanner output with Kodak Tri-X 400 developed in D-76
- The "reference negative" was shot at EI 320 (not 400) for better shadow detail
- Grain size and structure were modeled from actual Tri-X scans at 100% magnification
- The +, ++ variants use the same base profile with progressively stronger tone curve and grain intensity
- They explicitly noted Tri-X has identifiable grain even at web resolutions (unlike HP5 or T-Max)

---

## Mastin Labs — "Ilford Original" Pack (Tri-X as "Push" Variant)

Mastin Labs doesn't have a dedicated "Tri-X" preset pack; their B&W film emulations live primarily in the **Ilford Original** pack.

### How Mastin Approaches B&W Emulation

Mastin uses a different philosophy from VSCO:
- Base presets are "neutral" (HP5/FP4 look)
- Tone curves are less aggressive — Mastin prefers "printable" tonal range
- Grain is applied uniformly across the pack — less nuance per film stock
- The "Push" variants in their pack correspond loosely to pushed Tri-X

### Mastin Preset Family Mapping

| Mastin Preset | Approximate Film Stock Emulation |
|---------------|----------------------------------|
| Ilford HP5 | HP5+ at box speed (softer, smoother) |
| Ilford HP5 Push | HP5+ or Tri-X pushed to 800-1600 |
| Ilford FP4 | FP4+ at box speed (finer grain) |
| Ilford FP4 Push | FP4+ pushed |

### Community Notes on Mastin Ilford Original

- Users on r/WeddingPhotography report Mastin's B&W presets work well for portraits but "don't have the grain character" of real Tri-X
- The "Push" variant produces higher contrast and more aggressive grain — closest to pushed Tri-X
- Mastin presets are designed to work with their "Tone" profiles, which apply per-camera-sensor color rendering
- Split-toning: Subtle warm highlights / cool shadows (classic B&W selenium-toned print look)

---

## RNI (Really Nice Images) — "All Films 5" Pack

RNI All Films is the most comprehensive commercial film preset pack available (2019–present). Their B&W film emulations are highly regarded for grain accuracy.

### RNI Tri-X Preset Family

RNI offers the following Tri-X variants in All Films 5:

| RNI Preset | Description |
|------------|-------------|
| Kodak Tri-X 400 | Box speed, D-76 development emulation |
| Kodak Tri-X 400 (HC-110) | HC-110 developer emulation — higher acutance, more grain |
| Kodak Tri-X 400 (Rodinal) | Rodinal developer emulation — maximal grain and edge sharpness |
| Kodak Tri-X 400 Push +1 | Pushed to 800 |
| Kodak Tri-X 400 Push +2 | Pushed to 1600 |
| Kodak Tri-X 400 Faded | Simulating expired or processed Tri-X |

### RNI Grain Technology

RNI uses a proprietary "real grain" engine (vs. Lightroom's synthetic grain):
- Grain is sampled from actual Tri-X scans at multiple luminance levels
- Grain varies in size, shape, and intensity based on tonal zone (highlights = less visible grain, shadows = less visible, mid-tones = most visible)
- This replicates the real-world behavior of silver grain "clumping" in mid-tones
- RNI grain is widely considered the closest to real film grain available in Lightroom

### RNI Tri-X Tone Curve Characteristics

- Blacks at RGB ~10-12 (not fully crushed — Tri-X has "open" shadows even at high contrast)
- Mid-tone "push" — the curve steepens through zone V-VII (aggressive mid-tones)
- Gentle shoulder roll-off in highlights (maintains highlight separation)
- Contrast Index target: ~0.60-0.65 (confirmed by RNI documentation)

---

## DxO FilmPack — Tri-X Emulation

DxO FilmPack includes a scientifically modeled Tri-X 400 emulation.

### DxO Tri-X Model Parameters

DxO models film using actual sensitometric data:
- Uses real characteristic curves from Kodak datasheets
- Models the Callier Effect (condenser vs diffuse enlarger differences)
- Grain structure is derived from real Tri-X microdensitometer traces

### DxO Tri-X Grain Character

DxO's Tri-X grain is documented as:
- RMS 17 (matching official Kodak data)
- "Salt and pepper" distribution with ~3-5 micrometer average grain diameter in mid-tones
- Grain becomes more directional (apparent "clumping") above zone VI
- Real grain varies across luminance — DxO calls this "zone-dependent grain modeling"

---

## Nik Silver Efex Pro — Tri-X Emulation

Nik Silver Efex Pro (now owned by DxO) has a built-in "Film Types" section with Tri-X emulation.

### Nik Silver Efex Tri-X Settings (Default)

| Parameter | Default Value |
|-----------|---------------|
| Brightness | 0% |
| Contrast | +25% |
| Structure | +30% |
| Film Type | "Tri-X 400" |
| Grain per ISO | 1000 (their scale) |
| Grain Hardness | Soft (adjustable) |

### Nik vs Lightroom Grain Quality

Nik's grain engine is superior to Lightroom's:
- Nik uses per-luminance-zone grain modulation
- Grain transitions smoothly from shadows to mid-tones to highlights
- Nik's "Soft" vs "Hard" grain toggle maps to different Tri-X development regimes (fine-grain developer vs acutance developer)
- Users on r/postprocessing widely prefer Nik's grain to Lightroom's for Tri-X work

---

## Comparison Table: Paid Packs Tri-X Rendering

| Feature | VSCO Film 01 | RNI All Films 5 | DxO FilmPack | Mastin Ilford | Nik Silver Efex |
|---------|-------------|-----------------|--------------|---------------|-----------------|
| Grain realism | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Tone accuracy | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Developer variants | No | Yes (HC-110, Rodinal) | Partial | No | No |
| Push variants | +, ++, +++ | +1, +2 | Manual | "Push" | Manual |
| Currently available | No (discontinued) | Yes | Yes | Yes | Yes |
| Price | N/A | ~$120 | ~$80 | ~$100 | ~$150 |

---

## Key Takeaways for Tri-X Emulation Development

1. **The gold standard (VSCO) is gone** — RNI and DxO are the best current alternatives for grain accuracy.

2. **Grain authenticity separates the good from the great** — Lightroom's built-in grain is widely criticized as inadequate for Tri-X. Any serious emulation needs an external grain solution or the RNI/DxO engine.

3. **Developer matters more than preset makers admit** — The difference between Tri-X in D-76 vs Rodinal vs HC-110 is dramatic. RNI is the only major pack that models developer choice.

4. **Almost all paid packs model Tri-X at EI 250-320** — Even when labeled "400," the characteristic curve used for modeling typically assumes the film was exposed at ~EI 320 (the "real" speed for good shadow detail) and developed for higher contrast.

5. **Split-toning is universal in paid packs** — Every major Tri-X emulation applies subtle warm highlights (simulating selenium-toned silver prints) and neutral-to-cool shadows. VSCO's approach: highlight warmth was 255,248,240 at ~2% opacity in L*a*b* space.
