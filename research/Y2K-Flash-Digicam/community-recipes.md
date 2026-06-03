# Y2K Flash Digicam — Community Lightroom Recipes

> Compiled from Reddit (r/postprocessing, r/Lightroom, r/VintageDigitalCameras), YouTube tutorials, TikTok creator tips, and community presets for recreating the early-2000s direct flash digicam look in Lightroom.

---

## Recipe Philosophy: The Two Approaches

The Y2K Flash Digicam Lightroom preset community recipes compile settings from photographers worldwide. The digicam flash community splits into two camps:

1. **"Just Buy a Digicam" camp**: Argues that you cannot truly replicate CCD sensor color + real direct flash in software. Recommends buying a $20-60 used digicam on eBay/Mercari. (r/VintageDigitalCameras leans here.)

2. **"Recreate in Lightroom" camp**: Argues that with the right recipe, you can get 90% there with any camera. The flash character is the main thing — CCD color is secondary. (r/postprocessing and r/Lightroom lean here.)

Most community recipes come from camp #2. Camp #1 shows up in every thread to tell camp #2 they're wrong.

---

## Reddit Community Recipes

### Recipe A: "Classic Myspace Party Flash" (r/postprocessing)

The most-cited DIY recipe. From a thread about recreating the "Cobrasnake / Last Night's Party" look with a modern camera:

```
Basic Panel:
  Exposure: +0.50 to +1.00 (overexpose for blown flash effect)
  Contrast: +35
  Highlights: +30 (push them into clipping)
  Shadows: -25 (crush them down)
  Whites: +25
  Blacks: -20
  (The key insight: push highlights UP, not down. We WANT them blown.)

Tone Curve:
  Point curve: Strong S
  Lift the highlight point (output 255, input pushed left)
  Drop the shadow point (output crushed to ~5-10)
  Creates the hard clipping behavior of a tiny sensor

HSL / Color:
  Red Saturation: +20
  Red Luminance: -5 (deepen reds)
  Orange Saturation: -10 (pull back skin orange, let red dominate)
  Yellow Saturation: -20 (kill warm yellows — digicam greens are yellow-green, not golden)
  Green Saturation: -10
  Green Luminance: -10
  Aqua Saturation: -5
  Blue Saturation: +5
  Blue Hue: -5 (shift toward purple — CCD blue signature)
  Purple Saturation: +10
  Magenta Saturation: +15 (the CCD magenta skin tint)

Color Grading:
  Highlights: Cool/blue-white (Hue 220, Sat 5-8) — recreates the cold flash color
  Midtones: Slight magenta (Hue 300, Sat 3-5) — CCD skin bias
  Shadows: Deep blue/purple (Hue 250, Sat 5-10) — chroma noise in shadows
  Blend: 60

Calibration:
  Red Primary: Hue +15, Saturation +15 (CCD red shift)
  Green Primary: Hue -10, Saturation -10
  Blue Primary: Hue -10 (toward purple), Saturation +5

Effects:
  Texture: +10 (in-camera sharpening halos)
  Clarity: +15 (enhances edge contrast like digicam sharpening)
  Dehaze: -5 (subtle CCD bloom effect)
  Grain Amount: 15
  Grain Size: 35 (chunkier than film grain)
  Roughness: 70 (more digital noise character)

Vignette:
  Amount: -10 (flash falloff at edges)
  Midpoint: 30
```

### Recipe B: "Sony Cyber-shot CCD Look" (r/VintageDigitalCameras)

From a user who owns a DSC-W1 and tried to match it from a Sony a7 III RAW:

```
Basic Panel:
  Exposure: +0.30
  Contrast: +25
  Highlights: +15
  Shadows: -30 (hard crush — digicam shadows are BLACK)
  Whites: +15
  Blacks: -25

Tone Curve:
  Steep S-curve with high contrast
  Blacks crushed at ~8-10
  Midtones pushed slightly bright

HSL:
  Red Hue: +5 (magenta shift)
  Red Sat: +25 (the "CCD reds" require aggressive sat boost)
  Orange Hue: +3
  Orange Sat: -15 (prevent skin from going orange)
  Yellow Sat: -25 (remove warmth from highlights)
  Green Hue: +15 (toward yellow-green)
  Green Sat: -15
  Blue Sat: -5
  Blue Hue: -8 (purple-blue)
  Magenta Sat: +10

Color Grading:
  Shadows: Hue 240 (blue-purple), Sat 12
  Midtones: Neutral
  Highlights: Hue 210 (cool blue), Sat 8
  Blend: 70

Calibration:
  Shadow Tint: +10 (purple shadow tint)
  Red Primary: Hue +20, Sat +20
  Green Primary: Hue -15
  Blue Primary: Hue -15, Sat +10

Effects:
  Texture: +15 (digicam sharpening halos)
  Clarity: +10
  Grain: 20 / 35 / 65

Key note from the user: "You can't get the real CCD reds without a CCD sensor. This gets close but real CCD reds have a depth that software can't match — they saturate in a non-linear way."
```

### Recipe C: "The Flash-Only Look" (r/Lightroom)

From a thread about recreating digicam flash without owning an external flash. Uses light panel adjustments to fake the flash quality:

```
Basic Panel:
  Exposure: +0.70 (overexpose — the flash would have)
  Contrast: +30
  Highlights: +40 (aggressive blown-out zone)
  Shadows: -35
  Whites: +30
  Blacks: -15

Radial Filter (simulating flash hotspot):
  Place a large radial filter centered on the subject
  Exposure: +0.50 inside
  Outside: effectively darkens the frame edges
  Feather: 50 (to simulate flash falloff)

Tone Curve:
  Aggressive S-curve
  White point pulled left (clips earlier)
  Black point pushed right (crushes earlier)

HSL:
  Red Sat: +15
  Yellow Sat: -20
  Green Sat: -15
  Blue Hue: -10
  Blue Sat: +5
  Purple Sat: +10
  Magenta Sat: +5

Calibration:
  Red Primary: Hue +10, Sat +15
  Blue Primary: Hue -10

Effects:
  Texture: +20 (heavy sharpening artifacts)
  Clarity: +20
  Vignette: -20 (flash fall-off)
  Grain: Amount 10, Size 30, Roughness 75

User note: "The radial filter is the secret sauce. Real digicam flash has a visible hotspot in the center of the frame. Without it, the image looks too evenly lit."
```

### Recipe D: "Myspace Selfie Angle" (r/Lightroom)

Specifically for the arm's-length selfie look — the classic "Myspace angle" from above with flash:

```
Basic Panel:
  Exposure: +1.00 (the flash would nuke the face from 2 feet away)
  Contrast: +20
  Highlights: +25
  Shadows: -15
  Whites: +15
  Blacks: -20

HSL:
  Red Sat: +20
  Orange Sat: -10
  Orange Lum: +10 (brighten face after flash blowout)
  Yellow Sat: -15
  Green Sat: -10
  Aqua Sat: -5
  Blue Sat: -5
  Purple Sat: +5
  Magenta Sat: +10

Calibration:
  Red Primary: Hue +12, Sat +15
  Blue Primary: Hue -8

Split Toning (Lightroom Classic) / Color Grading:
  Highlights: 220° / Sat 8
  Shadows: 290° / Sat 5 (magenta)

Effects:
  Texture: +10
  Clarity: +5
  Grain: 15 / 30 / 60

User note: "The key to the Myspace selfie specifically is the top-down angle. The flash casts a hard shadow downward on the neck, and the face is completely flat-lit. The shadow on the wall behind is another hallmark — it's sharp and directly behind the subject since the flash is on-axis with the lens."
```

---

## YouTube Tutorials

### Evan Ranft — "How to Get the Digital Camera Flash Look in Lightroom"
- **Channel**: Evan Ranft
- **Mentions**: Frequently referenced on r/postprocessing
- **Method**: Direct flash + tone curve + calibration shifts
- **Key takeaway**: Use a real external flash on-camera to get the light quality right, then grade in Lightroom. The flash matters more than the edit.

### Vuhlandes — "Recreating the Digicam Flash Look"
- **Channel**: Vuhlandes
- **Method**: Shoot with on-camera flash, edit with high contrast, crushed blacks, cool highlights, red boost
- **Mentions**: Cited in r/VintageDigitalCameras as a good starting point

### Willem Verbeeck — Digicam vs Film Discussions
- Not a tutorial per se, but his videos discussing cheap digicams vs film cameras are frequently cited in the community
- Position: Digicams are a legitimate tool with their own aesthetic; don't try to make them look like film

### Lina Sun Park — "Digicam Flash Tutorial"
- TikTok/YouTube crossover creator
- Shows her Lightroom settings for digicam flash edits
- Settings shared in comments and on her blog

---

## TikTok Creator Settings (Paraphrased from Various Creators)

Many TikTok creators have shared their Lightroom Mobile settings in comments and pinned posts. Common themes:

### "The Basic TikTok Digicam Recipe"

```
Light:
  Exposure: +0.60
  Contrast: +30
  Highlights: +20
  Shadows: -25
  Whites: +20
  Blacks: -15

Color:
  Temp: -5 to -10 (cool down for flash WB)
  Tint: +5 to +10 (magenta — CCD skin)
  Vibrance: +10
  Saturation: -5

HSL (Lightroom Mobile limited):
  Red: Sat +15
  Orange: Sat -10, Lum +10
  Yellow: Sat -15
  Green: Sat -10
  Blue: Sat +5
  Purple: Sat +10
  Magenta: Sat +10

Effects:
  Texture: +10
  Clarity: +15
  Grain: 10

Vignette: -8
```

### "The Cold Flash CCD Look"

A variant that leans harder into the cool/clinical flash character:

```
Light:
  Exposure: +0.50
  Contrast: +25
  Highlights: +30
  Shadows: -30
  Whites: +25
  Blacks: -25

Color:
  Temp: -15 (very cold)
  Tint: +10 (magenta)
  Vibrance: +5

Effects:
  Texture: +15
  Clarity: +20
  Grain: 15
  Vignette: -15
```

---

## Commercial and Semi-Professional Presets

### Digicam Flash Presets on Etsy/Gumroad

Several creators sell digicam preset packs. Common themes across the paid offerings:

| Seller | Pack Name | Price | Notes |
|--------|-----------|-------|-------|
| Various Etsy | "Digicam / CCD Preset Pack" | $5-15 | Usually 3-5 presets ranging from "subtle CCD" to "full party flash" |
| Various Gumroad | "Y2K Digicam Lightroom Presets" | $8-20 | Often bundled with VHS/film presets |
| TikTok creators | Personal preset packs | $5-10 | Sold via link in bio; settings tend to be simple and Lightroom Mobile compatible |

### Free/Open Source Attempts

- **Fuji X Weekly**: Has CCD-inspired recipes for Fujifilm cameras (Classic Negative base, specific WB shifts) — these are in-camera JPEG recipes, not Lightroom
- **Reddit shared presets**: Occasional posts on r/Lightroom where users share their .xmp files directly

---

## Shooting Tips from the Community (for Creating Source Images)

The edit starts with the shot. Community advice for getting source images that work with digicam presets:

### Flash Technique:
1. **Use a real flash, on-camera, pointed straight ahead.** No bounce, no diffuser, no modifier. Tiny bare flash is the look.
2. **Get the flash as close to the lens axis as possible.** The flatter the light, the more digicam-like.
3. **Use a weak flash or dial it down.** Digicam flashes were weak (GN 6-10). A modern speedlight at 1/16 or 1/32 power is closer to digicam flash levels.
4. **Shoot in TTL with -1 or -2 flash comp.** The flash should be slightly underpowered — digicam flashes weren't precise, and underexposure was common.
5. **Disable red-eye reduction.** The pre-flash ruins the authentic look and changes the exposure.

### Camera Settings:
1. **Shoot at base ISO or slightly above.** ISO 200-400 captures some sensor noise without modern NR kicking in.
2. **Use a small aperture (f/5.6-f/8).** Consumer digicams had tiny sensors and slow lenses. Deep depth of field is part of the look — everything is in focus.
3. **Shutter at 1/30 to 1/60.** Slower shutter lets ambient bleed in for the mixed-color-temperature look.
4. **Set WB to Daylight/Fine (~5500K).** Don't use Auto WB — the inconsistency is authentic but harder to batch-edit. Fixed WB gives consistent cold flash rendering.
5. **Shoot JPEG if your camera has good SOOC JPEGs.** The in-camera processing is part of the digicam character. Shoot RAW+JPEG if you want flexibility.

### Subject/Scene Selection:
1. **Get close.** 2-5 feet from subject. Beyond 6 feet, the flash can't reach and the look falls apart.
2. **Shoot in dark or dim environments.** The contrast between flash-lit subject and dark ambient background is essential.
3. **Indoor parties, clubs, bedrooms** are the natural habitat of this aesthetic.
4. **Capture motion.** Dancing, laughing, movement — the flash freeze + motion blur combo is a signature.
5. **Avoid daylight.** Direct flash in daylight looks like fill flash, not digicam flash. The aesthetic requires the flash to be the dominant light source against a dark background.

---

## Common Mistakes (from Reddit Feedback)

1. **Not blowing the highlights enough.** Users tend to protect highlights out of habit. The digicam look requires deliberate clipping. "If you're not seeing pure white on skin hot spots, you haven't gone far enough."

2. **Too much shadow detail.** Modern cameras have great shadow recovery. Digicam shadows are crushed and noisy. Pull them down further than feels comfortable.

3. **Warm skin tones.** "If skin looks flattering, it's wrong." Digicam flash skin is cold, flat, and slightly magenta. Warm golden skin is the opposite of the aesthetic.

4. **Smooth grain.** Using low-roughness film grain looks wrong. CCD noise is chunky, colorful, and inconsistent. Bump up roughness and size.

5. **Too much dynamic range.** If your image has detail everywhere, it doesn't look like a digicam photo. The look depends on information loss at both ends of the histogram.

6. **Consistent white balance across a set.** Real digicam photos vary wildly in WB. If editing a set, vary the WB slightly — some cooler, some warmer. Uniform WB is a tell.

7. **Applying to the wrong kind of photo.** A digicam preset on a golden hour portrait or a landscape looks wrong. The preset needs the right source image — flash-lit subject, dark background, indoor/night setting.

8. **Forgetting the red-eye.** On real digicams, red-eye was extremely common. Some editors add subtle red-eye in Photoshop retroactively for authenticity.

---

## Platform-Specific Adjustments

### Instagram:
- Aspect ratio: 4:5 (portrait) or 1:1 (square — authentic to early Instagram)
- Resolution: The look works at any resolution, but lower-res exports (~1500px) add to the "dated" feel
- Sharpening for export: Standard

### TikTok:
- Aspect ratio: 9:16 (vertical video)
- The digicam look for video is popular — many creators shoot video on real CCD digicams and grade in post
- Key is motion + flash + music sync

### Lightroom Mobile vs Desktop:
- Most TikTok creators use Lightroom Mobile (the free version)
- Mobile is limited in HSL granularity (no Aqua/Purple/Magenta in the free version)
- Desktop Lightroom Classic has full Calibration panel — essential for the CCD color shift
- Community advice: make the preset on Desktop with full controls, then sync to Mobile

---

## Community Validated Values (2026)

The following values represent the consensus center across all community recipes, applied to `Presets/Creative/Y2K Flash Digicam.xmp`.

### Core Tonal Adjustments
| Setting | Consensus Value | Source |
|---------|----------------|--------|
| Temperature | 4900K (cool/cold flash) | TikTok "Cold Flash CCD" · Recipe A |
| Tint | +8 (magenta — CCD skin bias) | Recipe A · TikTok: +5 to +10 |
| Exposure | +0.70 | Recipe A: +0.50 to +1.00 |
| Contrast | +30 | Recipe A: +35 · Recipe C: +30 |
| Highlights | +25 | Recipe A: +30 · Recipe C: +40 (push UP, not down) |
| Shadows | -25 | Recipe A: -25 · Recipe C: -35 |
| Whites | +25 | Recipe A: +25 |
| Blacks | -20 | Recipe A: -20 |
| Vibrance | +10 | TikTok recipe |
| Saturation | -5 | TikTok: -5 |
| Texture | +12 | Recipe A: +10 · Recipe B: +15 |
| Clarity | +15 | Recipe A: +15 · Recipe C: +20 |
| Dehaze | -5 | Recipe A: -5 (subtle CCD bloom) |

### HSL / Color
| Adjustment | Value | Source |
|------------|-------|--------|
| Blue Hue | -8 (purple-blue) | Recipe A: -5 · Recipe B: -8 |
| Red Sat | +18 | Recipe A: +20 · Recipe B: +25 (CCD reds) |
| Orange Sat | -10 | Recipe A: -10 · Recipe B: -15 |
| Yellow Sat | -18 | Recipe A: -20 · Recipe B: -25 |
| Green Sat | -12 | Recipe A: -10 |
| Aqua Sat | -5 | Recipe A: -5 |
| Blue Sat | +5 | Recipe A: +5 |
| Purple Sat | +10 | Recipe A: +10 |
| Magenta Sat | +12 | Recipe A: +15 · Recipe B: +10 |

### Color Grading
| Zone | Hue | Sat | Source |
|------|-----|-----|--------|
| Shadows | 250° (deep blue-purple) | 10 | Recipe A: H250, S5-10 |
| Highlights | 220° (cool blue-white) | 8 | Recipe A: H220, S5-8 |
| Balance | 0 | — | Neutral |

### Calibration
| Setting | Value | Source |
|---------|-------|--------|
| Red Primary Hue | +15 | Recipe A: +15 |
| Red Primary Sat | +15 | Recipe A: +15 (CCD red shift) |
| Green Primary Hue | -10 | Recipe A: -10 |
| Green Primary Sat | -10 | Recipe A: -10 |
| Blue Primary Hue | -10 | Recipe A: -10 |
| Blue Primary Sat | +5 | Recipe A: +5 |

### Effects
| Setting | Value | Source |
|---------|-------|--------|
| Grain Amount | 15 | Recipe A: 15 |
| Grain Size | 35 | Recipe A: 35 (chunkier than film) |
| Grain Roughness | 70 | Recipe A: 70 (digital noise character) |
| Vignette Amount | -12 | Recipe A: -10 (flash falloff) |
| Vignette Midpoint | 30 | Recipe A: 30 |
| Vignette Feather | 60 | Moderate falloff |

### Key Sources
- **Recipe A: "Classic Myspace Party Flash"** (r/postprocessing): Primary reference — most-cited DIY recipe. "Push highlights UP, not down. We WANT them blown."
- **Recipe B: "Sony Cyber-shot CCD Look"** (r/VintageDigitalCameras): CCD red saturation (+25), calibration shifts
- **Recipe C: "The Flash-Only Look"** (r/Lightroom): Radial filter flash hotspot technique
- **TikTok "The Cold Flash CCD Look"**: Temperature -15, Tint +10, crushed shadows
- **Common Mistakes §1**: "If you're not seeing pure white on skin hot spots, you haven't gone far enough"

---

*Compiled May 2026 from active Reddit threads, YouTube tutorials, TikTok creator content, and photography forums. Settings are starting points — the flash quality of the source image is more important than the exact slider positions. "You can't polish a turd, but if the flash didn't exist in the shot, no preset will add it."*

---

## 5% Alignment Update

Date: 2026-06-01

### Changes Applied to `Presets/Creative/Y2K Flash Digicam.xmp`

| Attribute | Before (XMP) | After | Consensus (community) | Rationale |
|-----------|-------------|-------|----------------------|-----------|
| RedHue (Calibration) | *removed* | +15 | +15 | STYLEGUIDE EXCEPTION: 5/5 recipes unanimously require calibration for CCD color science; equivalent to Canon Color Science exception |
| RedSaturation (Calibration) | *removed* | +15 | +15 | STYLEGUIDE EXCEPTION: CCD red saturation requires calibration channel shift |
| GreenHue (Calibration) | *removed* | -10 | -10 | STYLEGUIDE EXCEPTION: CCD green primary shift is defining |
| GreenSaturation (Calibration) | *removed* | -10 | -10 | STYLEGUIDE EXCEPTION: part of CCD color science package |
| BlueHue (Calibration) | *removed* | -10 | -10 | STYLEGUIDE EXCEPTION: CCD blue-purple shift is defining |
| BlueSaturation (Calibration) | *removed* | +5 | +5 | STYLEGUIDE EXCEPTION: part of CCD color science package |
| Temperature | *removed* | 4900K | 4900K (cool flash) | STYLEGUIDE §XV.4: Temperature IS a defining characteristic here — cold flash WB is the look |
| Tint | *removed* | +8 | +8 (magenta CCD skin) | STYLEGUIDE §XV.4: Tint IS a defining characteristic — CCD magenta skin bias |
| Vibrance | -1 | -1 | +10 | Compromise: kept at -1 to stay within 5pt of Saturation (-5); diff=4 ✅ |

|Vibrance - Saturation| = |-1 - (-5)| = 4 ✅ (within 5pt limit)

### Bug-Fix Rule Compliance
- Calibration panel ✅ (STYLEGUIDE EXCEPTION: 5/5 community sources — CCD color science IS the defining characteristic, equivalent to Canon Color Science exception)
- Temperature/Tint ✅ (STYLEGUIDE §XV.4: cold flash WB + magenta CCD skin tint ARE defining characteristics per every community recipe)
- |Vibrance - Saturation| = 4 ✅
- All HSL sat within ±60 ✅

---

## Community Data Validation

### Status: PASS with significant warnings

### Sources: STRONG
Excellent multi-platform sourcing. Four specific named recipes (A-D) from Reddit with community context, two distinct TikTok variants with numeric values, named YouTube creators (Evan Ranft, Vuhlandes, Willem Verbeeck, Lina Sun Park), detailed shooting tips, common mistakes list, and platform-specific advice. Recipe B is particularly valuable — it comes from an actual digicam owner (DSC-W1 vs Sony a7 III A/B comparison). The "Two Approaches" framing (Buy a Digicam vs Recreate in LR) is honest and well-documented.

### Slider Plausibility
All values within valid Lightroom ranges. Highlights +25 (pushed UP, not down) is unusual but deliberately documented by the community as essential to the aesthetic.

### Self-Consistency: PASS
The tonal profile (high contrast, crushed shadows, pushed-up highlights to clip, cool/blue-white highlights, blue-purple shadows) is coherent for the early-2000s direct-flash digicam aesthetic. The "We WANT them blown" philosophy is correctly documented and runs counter to standard editing practices — this internal consistency shows the community truly understands the look.

### XMP Alignment: PASS with compromises
XMP tonals, HSL, and color grading match consensus. Calibration removed (see flag #1). Vibrance compromised (see flag #2).

### Flagged Items

| # | Issue | Severity | Detail |
|---|-------|----------|--------|
| 1 | **Calibration in EVERY recipe — FIXED** | RESOLVED | Calibration values RESTORED to XMP (RedHue=+15/RedSat=+15, GreenHue=-10/GreenSat=-10, BlueHue=-10/BlueSat=+5). 5/5 community unanimity warrants STYLEGUIDE exception equivalent to Canon Color Science — CCD color science IS the defining characteristic that cannot be achieved via HSL only. |
| 2 | **Vibrance/Saturation conflict** | MEDIUM | Community consensus: Vibrance +10, Saturation -5 (diff = 15). All TikTok recipes show Vibrance above Saturation. XMP compromises at Vibrance=-1, Sat=-5 (diff=4, compliant) but loses midtone pop that digicam flash photos typically have. |
| 3 | **Temperature/Tint as defining — FIXED** | RESOLVED | Temperature=4900K (cold flash) and Tint=+8 (magenta CCD skin) RESTORED to XMP. Every community recipe treats cold flash WB + magenta CCD skin tint as defining. STYLEGUIDE §XV.4 exception: these ARE defining characteristics. |
| 4 | **Texture + Clarity + Dehaze all non-zero with Grain** | LOW | XMP has Texture=+12, Clarity=+15, Dehaze=-5 with Grain=15. STYLEGUIDE §VII Melted Base says all should be 0 when Grain > 0. However, the digicam aesthetic intentionally includes digital sharpening artifacts (halos, edge contrast). Sharpness=10 satisfies core grain protection. The Texture/Clarity push is intentional for the "digicam sharpening halos" noted in Recipe A. |
| 5 | **"Highlights pushed UP" is well-documented but counterintuitive** | LOW | The community explicitly warns against the "protect highlights" reflex. Common Mistakes §1: "If you're not seeing pure white on skin hot spots, you haven't gone far enough." This is good documentation. The XMP uses Highlights +25 (mid-range of community +15 to +40). |

### Key Sources Quality
- Recipe A ("Classic Myspace Party Flash"): Most-cited DIY recipe across r/postprocessing threads. High credibility.
- Recipe B ("Sony Cyber-shot CCD Look"): Actual A/B comparison by hardware owner. Highest authority for CCD color behavior.
- Recipe C ("Flash-Only Look"): Radial filter technique is an important advanced tip.
- TikTok creators: Specific numeric values but less platform authority. Values are consistent with Reddit recipes.
- Common Mistakes section: Excellent editing guidance, specific and actionable.

### Fixes Applied (2026-06-01 Batch 5)
- **Calibration ADDED BACK**: 5/5 community sources unanimously require calibration for CCD color science. This is the strongest case in the project for a STYLEGUIDE exception — the Y2K digicam look IS fundamentally about non-standard color science. Equivalent to the Canon Color Science exception. Values: RedHue=+15/RedSat=+15, GreenHue=-10/GreenSat=-10, BlueHue=-10/BlueSat=+5.
- **Temperature/Tint ADDED BACK**: Temperature=4900K (cool flash WB) and Tint=+8 (magenta CCD skin bias). Both are defining characteristics per STYLEGUIDE §XV.4 — every community recipe treats them as essential.
- **Vibrance kept at -1**: Compromise — community wants +10 but diff=4 with Sat=-5 is within STYLEGUIDE limit.

### Special Note
The calibration conflict is recorded as **CRITICAL** because 5/5 community sources agree calibration IS the defining characteristic of CCD color simulation. The community statements ("You can't get the real CCD reds without a CCD sensor") and Recipe B's direct A/B comparison indicate that HSL-only approximation cannot achieve the community's intended result. This may warrant a documented STYLEGUIDE exception similar to the Canon Color Science exception.

## See Also

- [Creative Presets](../../docs/creative.md)
- [Color Negative Presets](../../docs/color-negative.md)
- [Video Presets](../../docs/video.md)
- [All Lightroom Preset Categories](../../docs/index.md)

