# Community Recipes — Lightroom B&W Presets for Tri-X 400 Emulation

> Compiled from Reddit (r/Lightroom, r/analog, r/postprocessing, r/photography), YouTube tutorials, photography forums, and community blogs. These are community-developed settings — not official Kodak data.

---

## Recipe A: "Classic Tri-X at Box Speed" (D-76 Look)

Goal: Moderate grain, deep blacks, open shadows, strong mid-tone contrast. Emulates Tri-X at ISO 400 in D-76 1:1.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | 0 (adjust per image) |
| Contrast | +35 to +45 |
| Highlights | -15 |
| Shadows | +20 to +30 |
| Whites | +15 |
| Blacks | -25 to -35 |

### Tone Curve
```
Parametric:
  Highlights: -10
  Lights: +10
  Darks: -20
  Shadows: -5

Point Curve: Medium Contrast
```
Custom point curve (optional): Two-point S-curve with a slight lift in the deep shadows (crushed-but-not-blocked blacks).

### B&W Mix (HSL / Black & White)
| Color Channel | Value | Notes |
|---------------|-------|-------|
| Red | +25 to +35 | Lightens skin, darkens skies slightly |
| Orange | +15 to +25 | Key skin tone channel |
| Yellow | -10 to 0 | Preserves highlight separation |
| Green | -20 to -30 | Darkens foliage — Tri-X is panchromatic with red sensitivity |
| Aqua | 0 |
| Blue | -30 to -50 | Darkens skies — dramatic Tri-X sky look |
| Purple | 0 |
| Magenta | -10 to 0 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +20 to +35 |
| Dehaze | +5 to +15 |
| Texture | +10 to +20 |

### Grain (Critical for Tri-X emulation)
| Setting | Value | Notes |
|---------|-------|-------|
| Amount | 55 to 70 | Visible at 100% zoom on 24MP |
| Size | 35 to 45 | Tri-X grain is medium-coarse, not fine |
| Roughness | 65 to 80 | Key! High roughness creates "salt-and-pepper" texture |

### Vignette
| Setting | Value |
|---------|-------|
| Post-Crop Vignette | -10 to -15 |
| Midpoint | 35 |
| Feather | 50 |

---

## Recipe B: "Pushed Tri-X at 1600" (HC-110 Look)

Goal: Heavy, aggressive grain. Crushed blacks. High contrast with dramatic mid-tone separation. The classic 1970s war photographer / Daido Moriyama look.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | -0.3 to 0 |
| Contrast | +60 to +80 |
| Highlights | -30 |
| Shadows | +10 to +15 |
| Whites | +30 |
| Blacks | -40 to -55 |

### Tone Curve
```
Parametric:
  Highlights: -30
  Lights: +15
  Darks: -30
  Shadows: -15

Point Curve: Strong Contrast
```
Custom: Deep S-curve. Lift the toe slightly (RGB value ~8 at black), then steep drop.

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +30 |
| Orange | +20 |
| Yellow | -5 |
| Green | -35 |
| Aqua | 0 |
| Blue | -50 to -60 |
| Purple | -10 |
| Magenta | -10 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +40 to +60 |
| Dehaze | +15 to +25 |
| Texture | +20 to +30 |

### Grain (Heavy)
| Setting | Value |
|---------|-------|
| Amount | 75 to 100 |
| Size | 45 to 55 |
| Roughness | 80 to 95 |

### Vignette
| Setting | Value |
|---------|-------|
| Post-Crop Vignette | -20 to -30 |
| Midpoint | 25 |
| Feather | 40 |

---

## Recipe C: "Tri-X in Rodinal" (Maximal Grain/Acutance)

Goal: Pronounced grain with enhanced edge sharpness. Tri-X's true "grain texture" on full display. Favored by fine art / street photographers wanting aggressive texture.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | 0 |
| Contrast | +50 |
| Highlights | -20 |
| Shadows | +25 |
| Whites | +10 |
| Blacks | -30 |

### Tone Curve
- Strong S-curve with a sharp toe (blacks clip faster)
- Slightly lifted mid-point for more brightness in the mid-tones

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +20 |
| Orange | +15 |
| Yellow | -15 |
| Green | -25 |
| Blue | -40 |
| (Others at 0) |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +50 to +70 |
| Dehaze | +10 |
| Texture | +25 to +35 |

### Grain
| Setting | Value |
|---------|-------|
| Amount | 80 to 100 |
| Size | 40 to 50 |
| Roughness | 85 to 100 |

### Sharpening (Rodinal = high acutance)
| Setting | Value |
|---------|-------|
| Amount | 60 to 80 |
| Radius | 1.0 to 1.4 |
| Detail | 35 to 50 |
| Masking | 10 to 30 (to avoid sharpening grain in skies) |

---

## Recipe D: "Tri-X XP2 / Low Contrast Pull" (Tri-X @ 200)

Goal: Fine grain, long tonal scale, open shadows. Emulates Tri-X pulled to 200 in XTOL or D-76 1:3. Suitable for portraits with smoother skin.

### Basic Panel
| Setting | Value |
|---------|-------|
| Exposure | +0.3 to +0.5 |
| Contrast | +15 to +25 |
| Highlights | -25 |
| Shadows | +40 to +50 |
| Whites | +5 |
| Blacks | -15 to -20 |

### Tone Curve
- Gentle S-curve
- Shadow end NOT crushed — keep detail at RGB ~15

### B&W Mix
| Color Channel | Value |
|---------------|-------|
| Red | +20 |
| Orange | +10 |
| Yellow | -10 |
| Green | -15 |
| Blue | -25 |

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +10 to +20 |
| Dehaze | +5 |
| Texture | +10 |

### Grain (Fine)
| Setting | Value |
|---------|-------|
| Amount | 30 to 45 |
| Size | 30 to 35 |
| Roughness | 50 to 60 |

---

## Recipe E: "Newspaper / Magazine Tri-X" (High-Contrast Repro)

Goal: Extremely punchy. Heavy black crush. The photojournalism look on newsprint.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +70 to +90 |
| Highlights | -40 |
| Shadows | -10 to -20 |
| Whites | +40 |
| Blacks | -60 |

### Tone Curve
- Aggressive S-curve
- Blacks at RGB 0-5 (full crush)
- Whites pushed to RGB 248+

### B&W Mix
- Heavy red/orange boost (+30 to +40)
- Blue heavy darken (-50 to -70)

### Presence
| Setting | Value |
|---------|-------|
| Clarity | +60 to +80 |

### Grain
| Setting | Value |
|---------|-------|
| Amount | 70 to 90 |
| Size | 40 to 50 |
| Roughness | 75 to 90 |

---

## Key Insights from Community Research

### From Reddit (r/Lightroom, r/analog, r/postprocessing):

1. **"The B&W Mix is everything"** — Multiple Reddit threads emphasize that Tri-X's unique look comes from its spectral sensitivity (panchromatic with extended red). The red/orange channel boost is the single most important setting. Without it, B&W conversions look "generic."

2. **Grain roughness matters more than amount** — Lightroom's grain at 100 amount but 25 roughness looks like fine-grain Delta/T-Max, NOT Tri-X. Roughness at 70+ is essential for the "salt and pepper" character.

3. **Clarity is your friend, but don't overdo it** — Clarity above 60 produces "haloing" that looks digital, not like film edge sharpness (acutance). Use Clarity +30 to +45 and supplement with Texture for a more authentic "edge effect."

4. **The "woven grain" phenomenon on r/analog (565 points)** — A major thread discussed "woven" or "reticulated" grain pattern on Tri-X. Community consensus: this is RETICULATION from harsh temperature changes during development (specifically monobath developers or cold water stop), NOT inherent to Tri-X. Properly developed Tri-X has a random "salt and pepper" pattern, not a directional/reticulated one.

5. **"HP5 has smooth grain like sand, Tri-X has sharp grain like broken glass"** — Common community characterization from u/throwaway comment on r/analog.

### From YouTube:

Popular Tri-X emulation tutorials emphasize:
- Using the B&W Profile (not desaturation) as the foundation
- Heavy negative Blue and Cyan in the B&W mixer for dramatic skies
- Lightroom's built-in grain engine is considered "acceptable but not great" — many recommend using third-party grain overlays (like RNI or DxO FilmPack) for more authentic grain structure
- VSCO Film 01's Tri-X preset was widely considered the gold standard until discontinuation

### From Photography Forums:

- **FredMiranda.com** threads suggest Tri-X at EI 200-250 yields the "true" shadow detail, with the characteristic curve showing ~2 stops of underexposure latitude and 5+ stops overexposure latitude
- **Photrio (APUG)** consensus: D-76 1:1 at 9.75 min is the "reference standard" for Tri-X development against which all other developer/film combinations are judged
- **RangeFinderForum** recommendation: Pair Tri-X with a yellow filter (K2/Y48) for classic street photography look, or orange filter for dramatic skies

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Black-White/Kodak Tri-X 400.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Highlights2012 | -12.5 | -13.8 | Averaged (community -15) |
| Shadows2012 | -17.5 | +25 | Replaced (community +20 to +30) |
| Whites2012 | +22.5 | +15 | Replaced (community +15) |
| Blacks2012 | -35 | -32.5 | Averaged (community -25 to -35) |
| Clarity2012 | +20 | +27.5 | Replaced (community +20 to +35) |
| Texture | +7.5 | +15 | Replaced (community +10 to +20) |
| Dehaze | (none) | +10 | Added (community +5 to +15) |
| GrayMixerRed | +2.5 | +30 | Replaced (community +25 to +35) |
| GrayMixerOrange | +5 | +20 | Replaced (community +15 to +25) |
| GrayMixerYellow | +17.5 | -5 | Replaced (community -10 to 0) |
| GrayMixerGreen | +22.5 | -25 | Replaced (community -20 to -30) |
| GrayMixerAqua | +2.5 | 0 | Replaced (community 0) |
| GrayMixerBlue | -17.5 | -40 | Replaced (community -30 to -50) |
| GrayMixerPurple | -5 | 0 | Replaced (community 0) |
| GrayMixerMagenta | -2.5 | -5 | Replaced (community -10 to 0) |
| GrainAmount | +57.5 | +60 | Averaged (community 55-70) |
| GrainFrequency | +52.5 | +72.5 | Replaced (community 65-80) |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Black-White/Kodak Tri-X 400.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | +35 | +35 to +45 | Recipe A (box speed) |
| Highlights2012 | -13.8 | -15 | Averaged |
| Shadows2012 | +25 | +20 to +30 | Midpoint |
| Whites2012 | +15 | +15 | Recipe A |
| Blacks2012 | -32.5 | -25 to -35 | Averaged |
| Clarity2012 | +27.5 | +20 to +35 | Midpoint |
| Dehaze | +10 | +5 to +15 | Midpoint |
| Texture | +15 | +10 to +20 | Midpoint |
| **B&W Mix** | | | |
| Red | +30 | +25 to +35 | Key: panchromatic red sensitivity |
| Orange | +20 | +15 to +25 | Midpoint |
| Yellow | -5 | -10 to 0 | Midpoint |
| Green | -25 | -20 to -30 | Darken foliage |
| Aqua | 0 | 0 | Recipe A |
| Blue | -40 | -30 to -50 | Dramatic sky darkening |
| Purple | 0 | 0 | Recipe A |
| Magenta | -5 | -10 to 0 | Midpoint |
| **Grain** | | | |
| Amount | 60 | 55-70 | Averaged |
| Size | 40 | 35-45 | Midpoint |
| Frequency | 72.5 | 65-80 | High roughness = salt-and-pepper |

> **Note:** Values in the table above reflect community consensus before STYLEGUIDE v2.1 alignment. The actual XMP supersedes several values per grain protection rules, grain table caps, and Blacks floor. See [STYLEGUIDE v2.1 Alignment](#styleguide-v21-alignment) below for final XMP values. Specifically: Blacks -32.5→-30 (floor), Clarity +27.5→0, Dehaze +10→0, Texture +15→0, GrainAmount 60→55, GrainSize 40→35, GrainFrequency 72.5→65.

**Key sources:** r/Lightroom, r/analog, r/postprocessing, FredMiranda forums, Photrio (APUG), VSCO Film 01 reference, YouTube tutorials.

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01 to `Presets/Black-White/Kodak Tri-X 400.xmp`:

| Parameter | Before | After | Rule |
|-----------|--------|-------|------|
| Blacks2012 | -32.5 | -30 | Blacks floor -30 |
| GrainAmount | 60 | 55 | STYLEGUIDE Tri-X grain table: Amount 40-55 |
| GrainSize | 40 | 35 | STYLEGUIDE Tri-X grain table: Size 25-35 |
| GrainFrequency | 72.5 | 65 | STYLEGUIDE Tri-X grain table: Roughness 50-65 |

No other violations. Clarity=0, Texture=0, Dehaze=0 already compliant. Sharpness=10, calibration ban, B&W curve neutral all pass.

## Community Data Validation

### Validity Assessment: GOOD

**Overall Status**: Well-sourced with 5 distinct recipes covering different development chemistries (D-76, HC-110, Rodinal, XTOL pull, newspaper repro). The community understanding of Tri-X's panchromatic red sensitivity and the importance of grain roughness over amount is accurate and well-documented. However, community recipes advocate Clarity/Texture/Dehaze values incompatible with grain protection rules.

### Flagged Bogus Data

| # | Severity | Claim | Source | Issue |
|---|----------|-------|--------|-------|
| 1 | **MODERATE** | Clarity +20 to +35, Texture +10 to +20, Dehaze +5 to +15 recommended simultaneously with grain (GrainAmount 55-70) | Recipe A, r/Lightroom (community-recipes.md:47-50) | STYLEGUIDE §VII.2: sharpening of any kind sees grain as "detail" and amplifies it into jagged digital noise. Clarity (30-100px radius) directly boosts midtone grain clusters. The community "Contrast layering" approach (adding small amounts of Clarity, Texture, and Dehaze) is valid for grain-free images but breaks with heavy Tri-X grain. XMP correctly sets all three to 0. |
| 2 | **MODERATE** | Recipe C (Rodinal): Sharpening Amount 60-80, Radius 1.0-1.4, Detail 35-50 with GrainAmount 80-100 | Community recipe (community-recipes.md:171-177) | STYLEGUIDE §VII.2: Sharpening ≤ 10 when GrainAmount > 0. Community Rodinal recipe would produce extreme jagged noise — each grain particle treated as an edge by the USM kernel. This is a legitimate Rodinal aesthetic for darkroom prints but fails in digital grain simulation. XMP correctly uses Sharpness=10. |
| 3 | **MODERATE** | Recipe B (Pushed 1600): Contrast +60 to +80 | HC-110 look (community-recipes.md:76) | While pushed Tri-X at 1600 in HC-110 does exhibit very high contrast, Contrast +60 to +80 in Lightroom's Basic panel risks total shadow/highlight clipping on anything except perfectly exposed images. The community recipe acknowledges this is an aggressive look, but users should understand the extreme slider range. |
| 4 | **MINOR** | "Lift the toe slightly (RGB value ~8 at black)" | Recipe B point curve description (community-recipes.md:92) | This is a point curve technique recommendation. The XMP uses neutral 0,0 → 255,255 curves (per STYLEGUIDE §IV for B&W). Point curve lifts are image-specific and should not be in a general preset. Correctly excluded. |
| 5 | **NONE** | "HP5 has smooth grain like sand, Tri-X has sharp grain like broken glass" | r/analog u/throwaway (community-recipes.md:272) | Legitimate subjective characterization. Not a slider recommendation — useful aesthetic guide. |

### Slider Range Check

All XMP values within valid ranges:
- Contrast +35 (0..100) ✓
- Highlights -13.8 (-100..100) ✓
- Shadows +25 (-100..100) ✓
- Whites +15 (-100..100) ✓
- Blacks -30 (at floor) ✓
- B&W Mix: all values within -100..+100 ✓
- GrainAmount 55 ≤ STYLEGUIDE Tri-X max 55 ✓
- GrainSize 35 = STYLEGUIDE Tri-X max 35 ✓
- GrainFrequency 65 = STYLEGUIDE Tri-X max 65 ✓

### Self-Consistency Check

| Check | Result |
|-------|--------|
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0, Dehaze=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| B&W Mix values within ±100 | ✓ (Blue -40 max) |
| Blacks ≥ -30 | ✓ |
| B&W neutral tone curves (0,0 → 255,255) | ✓ |

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| r/analog, r/Lightroom | High (archived) | High — extensive Tri-X discussion |
| FredMiranda.com | Medium | High — detailed EI and development discussions |
| Photrio (APUG) | High (archive) | High — D-76 1:1 reference standard documented |
| VSCO Film 01 reference | Medium (discontinued) | High — was gold standard |
| Community characterization ("woven grain" thread) | High (565 upvotes) | Medium — reticulation correctly identified as processing artifact |

### Film Stock Behavior Check

| Behavior | Community Claim | XMP Implementation | Verdict |
|----------|----------------|-------------------|---------|
| Extended red sensitivity (panchromatic) | Red +30, Orange +20 | Applied ✓ | The single most important B&W Mix setting for Tri-X |
| Deep dramatic skies | Blue -40 | Applied ✓ | Orange/red filter equivalent for sky darkening |
| Darkened foliage | Green -25 | Applied ✓ | Tri-X's red sensitivity darkens greens |
| Salt-and-pepper grain | Roughness 65, Size 35, Amount 55 | Applied ✓ | High roughness = irregular grain pattern |
| Moderate-to-strong midtone contrast | Contrast +35, Blacks -30 | Applied ✓ | D-76 box speed reference |
| Preserve highlight separation | Yellow -5 | Applied ✓ | Subtle yellow channel restraint |

### Validation Status: ✅ PASS (3 moderate flags documented; XMP correctly disregards them; documentation corrected)

The community recipe collection is excellent as a historical reference for Tri-X's different looks across developers and EI ratings. However, two of five recipes (Rodinal and pushed HC-110) recommend sharpening and clarity values that would produce jagged digital artifacts when combined with Lightroom's grain engine. The XMP correctly applies STYLEGUIDE grain protection rules. The "woven grain/reticulation" discussion is properly identified as a processing artifact, not inherent film behavior — this demonstrates good community knowledge quality.

**Documentation fix (2026-06-01):** Added note to Community Validated Values table clarifying values reflect pre-STYLEGUIDE consensus, not final XMP state. Actual XMP: Blacks=-30, Clarity=0, Dehaze=0, Texture=0, GrainAmount=55, GrainSize=35, GrainFrequency=65, Sharpness=10.

**Note**: The STYLEGUIDE grain table (Tri-X: Amount 40-55, Size 25-35, Roughness 50-65) is slightly more conservative than the community consensus (Amount 55-70, Size 35-45, Roughness 65-80). The XMP follows STYLEGUIDE caps at the upper boundary. Community values are not "bogus" — they reflect user preference for more prominent grain — but STYLEGUIDE's display-survivability concerns (§XIII) justify the conservative caps.
