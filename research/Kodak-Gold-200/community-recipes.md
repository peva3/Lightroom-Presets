# Kodak Gold 200 — Community Lightroom Recipes

> **Compiled from:** Reddit (r/analog, r/Lightroom, r/postprocessing), YouTube creators (Jamie Windsor, Willem Verbeeck, grainydays, Kyle McDougall, NATE Cam), Mastin Labs, VSCO, RNI Films, and various photography forums. Settings are approximate starting points — fine-tune per image.

---

## 1. Core Philosophy

Community consensus on emulating Gold 200 in Lightroom centers on five pillars:

1. **Warm golden-white balance** (5800–6200K with slight green tint offset)
2. **Moderate S-curve** with lifted blacks and soft highlights
3. **HSL shifts**: boost warm tones, cool the blues, yellow the greens
4. **Teal shadow split-tone** to create warm/cool color contrast
5. **Visible grain** — moderate amount, rougher texture

---

## 2. Baseline Settings

### Recipe A: "Starting Point" (most-cited community average)

This is a synthesis of the most commonly shared settings across Reddit and YouTube. Use this as your starting point and adjust.

```
BASIC PANEL
├── WB Temp: 5900–6100K (warmer than default)
├── WB Tint: -5 to -10 (toward green, counteracts digital magenta)
├── Exposure: 0 to +0.30 (slight overexposure mimics consumer film)
├── Contrast: -10 to -15 (flatten for filmic look)
├── Highlights: -40 to -60 (gentle highlight roll-off)
├── Shadows: +20 to +35 (lift shadows, reveal detail)
├── Whites: -15 to -25
├── Blacks: +15 to +25 (crushed blacks are NOT Gold 200)
├── Clarity: -5 to -10 (light halation/softness)

TONE CURVE
├── Point Curve: Medium Contrast
├── Custom RGB curves:
│   ├── All channels: slight S-curve
│   ├── Lift black point: output ~8-12 (milky blacks)
│   ├── Lower white point: output ~245-250 (soft highlights)
│   └── Add slight midtone bump for contrast

HSL / COLOR
├── Red Hue: +5 to +10 (toward orange)
├── Orange Hue: 0 to -5
├── Yellow Hue: -10 to -15 (toward orange/gold)
├── Green Hue: +15 to +30 (toward yellow)
├── Aqua Hue: -10 to -15 (toward cyan/teal)
├── Blue Hue: -5 to -15 (toward aqua for shadows)
├── Purple/Magenta: -10 to -20 (suppress magenta)
│
├── Red Saturation: +5 to +15
├── Orange Saturation: +10 to +20
├── Yellow Saturation: +15 to +25 (GOLD signature)
├── Green Saturation: -10 to -20 (desaturate greens)
├── Aqua Saturation: 0 to -10
├── Blue Saturation: -10 to -20 (muted blues)
├── Purple/Magenta Saturation: -15 to -30
│
├── Orange Luminance: +10 to +20 (brighten skin tones)
├── Yellow Luminance: +5 to +15
├── Green Luminance: -5 to -10
├── Blue Luminance: -5 to -15 (deepen sky slightly)

SPLIT TONING
├── Highlights: Hue 45–55 (warm yellow-orange), Saturation 10–20
├── Shadows: Hue 200–215 (teal/cyan-blue), Saturation 10–25
├── Balance: -20 to -40 (favor shadow toning over highlights)
└── (This creates the warm highlight / cool shadow dynamic)

CALIBRATION
├── Red Primary: Hue +15 to +25, Sat +10 to +20 (warm reds)
├── Green Primary: Hue -10 to -20, Sat 0 to -10
├── Blue Primary: Hue -5 to -15, Sat -5 to +5
└── (These shifts are critical — they affect color globally)

EFFECTS
├── Grain Amount: 25–40
├── Grain Size: 25–35
├── Grain Roughness: 40–60 (consumer film, not ultra-fine)
├── Vignette: -5 to -10 (subtle, not heavy)
├── Dehaze: 0 (or slight negative for halation simulation)

DETAIL
├── Sharpening: 40–60 (standard)
├── Masking: 40–60 (avoid sharpening grain)
└── No luminance NR (preserve grain texture)
```

---

## 3. Alternative Community Recipes

### Recipe B: "Overexposed Gold" (Dreamy / Pastel Look)

Popular on r/analog for the "golden hour portrait" look. Based on overexposing Gold 200 by +1 to +2 stops.

```
Use Recipe A as base, then modify:
├── Exposure: +0.50 to +0.75
├── Highlights: -70 to -80
├── Contrast: -20 to -25
├── Blacks: +25 to +35
├── Yellow Saturation: +25 to +35
├── Green Saturation: -25 to -30
├── Split Toning Highlights: Saturation 15–25
├── Grain Amount: 30–45
└── Clarity: -10 to -20
```

This produces the soft, warm, slightly washed-out dreamy look popular on Instagram.

### Recipe C: "Moody Gold" (Darker, Contrastier)

For overcast or moody scenes. Less common but favored by some YouTubers.

```
Use Recipe A as base, then modify:
├── Exposure: -0.15 to -0.30
├── Contrast: 0 to +10
├── Shadows: +10 to +15
├── Blacks: 0 to +10
├── Highlights: -30 to -40
├── Orange Saturation: +5 to +10
├── Split Toning Shadows: Saturation 20–30 (stronger teal)
├── Grain Amount: 35–50
└── Dehaze: +5 to +10
```

### Recipe D: "120 Gold" (Medium Format Emulation)

For when you want the smoother Gold 200 120-format look with less apparent grain.

```
Use Recipe A as base, then modify:
├── Grain Amount: 10–20
├── Grain Size: 15–25
├── Grain Roughness: 30–40
├── Clarity: 0 to -5 (medium format is sharper)
├── Sharpening: 50–70
└── (Keep all other settings the same — the color palette is identical between 35mm and 120)
```

---

## 4. Tone Curve Deep Dive

The tone curve is arguably the most important element after white balance. Gold 200 has a distinctive S-curve.

### Recommended Point Curve

```
Points (approximate):
├── (0, 10)    — lifted black point (~4% output)
├── (25, 30)   — slight shadow lift
├── (50, 55)   — midtone contrast boost
├── (75, 72)   — highlight compression begins
├── (100, 95)  — soft white point (~95% output)
```

### Per-Channel Adjustments

**Red Channel** (slight S, to boost warm contrast):
```
├── (0, 8), (50, 52), (100, 95)
```

**Green Channel** (flatter, preserves natural luminance):
```
├── (0, 10), (50, 50), (100, 96)
```

**Blue Channel** (lifted shadows for teal, compressed highlights for warmth):
```
├── (0, 14), (50, 48), (100, 94)
```

---

## 5. HSL Deep Dive — The "Gold" Palette

### Critical HSL Shifts

These are the shifts that most differentiate a Gold 200 emulation from a generic warm preset:

| Adjustment | Value | Why |
|---|---|---|
| **Green Hue → +20** | Shifts greens toward yellow | Gold 200 greens are yellowish, not blue-green |
| **Yellow Hue → -15** | Shifts yellows toward orange | Creates the "golden" signature |
| **Blue Hue → -10** | Shifts blues toward aqua | Shadows take on cyan/teal quality |
| **Orange Sat → +15** | Boosts warm skin/earth tones | Gold 200 amplifies warm tones |
| **Yellow Sat → +20** | Boosts golden cast | The namesake characteristic |
| **Green Sat → -15** | Desaturates greens | Consumer film greens are subdued |
| **Blue Sat → -15** | Mutes blue saturation | Skies are pleasant, not hyper-blue |
| **Magenta Sat → -25** | Suppresses magenta | Distinguishes from Fuji films |

### Skin Tone Protection

Gold 200 renders skin warmly but not orange. Critical to get this right:
- Orange Luminance +15 brightens skin
- Orange Saturation kept moderate (+10 to +15 max)
- Red Hue slight shift toward orange prevents lipstick-red cast

---

## 6. Split Toning — The Teal Shadow Secret

The warm highlight / cool shadow interplay is what gives Gold 200 its characteristic depth. Without split toning, emulations often look flat or generically warm.

### Community Consensus Values

```
Highlights: Hue 45–52 (yellow-orange), Saturation 8–20
Shadows:   Hue 205–215 (cyan-blue / teal), Saturation 12–25
Balance:   -25 to -35 (significant bias toward shadow toning)

Critical note: The shadow teal should be SUBTLE — if your shadows
are obviously teal, reduce saturation. Gold 200 is not a teal-and-
orange Instagram filter. The effect should look natural.
```

### Why Balance Matters

A negative balance (-25 to -35) means the shadow hue/saturation affect a wider tonal range. This creates a gentle cool transition from midtones into shadows, rather than a harsh split at the 50% luminance mark. This matches Gold 200's natural gradual cooling toward shadows.

---

## 7. Grain — Critical for Authenticity

Gold 200's grain is part of the aesthetic. Clean digital files with Gold 200 color but no grain read as "warm digital" rather than "film."

### Recommended Lightroom Grain Settings

```
Amount:    30–40   (visible but not overwhelming)
Size:      25–30   (matches 35mm consumer emulsion)
Roughness: 45–55   (consumer film has rougher grain than pro films)
```

### Format Considerations

- **35mm emulation**: Higher grain amount (35–45), rougher texture (50–60)
- **120 emulation**: Lower grain amount (10–20), slightly smoother (40–45)
- **Instragram/web**: Slightly higher grain (it compresses out)
- **Prints**: Slightly lower grain (it's more visible in print)

---

## 8. Scene-Specific Tuning

### Golden Hour / Sunset

Gold 200 + golden hour = double warmth. Watch out for excessive yellow.
```
├── Reduce WB Temp by 200–300K from baseline
├── Increase Orange Saturation +5
├── Reduce Yellow Saturation -5 (compensate for scene warmth)
├── Increase highlight split tone saturation
└── Reduce shadow split tone (teal competes with warm light)
```

### Beach / Ocean Scenes

Gold 200 loves the beach — this is where it shines.
```
├── Aqua Saturation +5 to +10 (ocean color)
├── Blue Hue -5 (slightly teal water)
├── Yellow Saturation +15 (sand warmth)
├── Reduce shadow split tone slightly (beach shadows are warm)
```

### Overcast / Flat Light

Gold 200 loses character in overcast. Boost warmth artificially.
```
├── WB Temp +300 to +500K from baseline
├── Contrast +5 to +10 (compensate for flat light)
├── Reduce highlight compression (-40 instead of -60)
├── Increase grain slightly (flat light reveals grain more)
└── Green Saturation: don't desaturate as much
```

### Indoor / Flash

Gold 200 with flash was the standard family-photo setup.
```
├── WB Temp: 5600–5800K (flash is ~5500K, Gold adds warmth)
├── Orange Saturation: +10 (skin tones with flash)
├── Reduce shadows lift (+10 instead of +25)
├── Reduce split toning (flash lit scenes are more uniform)
```

---

## 9. Known Commercial Presets

### Jamie Windsor — JW Gold 200

Jamie Windsor's Gold 200 preset is one of the most referenced in the community. Key characteristics (reverse-engineered from community discussion):

- Moderate warmth with green tint offset
- S-curve with lifted blacks
- Desaturated greens, boosted yellows
- Subtle teal shadow toning
- Light grain application
- Calibration shifts: red toward orange, blue toward cyan

### Mastin Labs — Kodak Gold (Original Pack)

Mastin Labs' original Kodak pack included a Gold preset. Community notes:
- Profile-based (not just settings)
- More neutral than community DIY recipes
- Designed for professional wedding/portrait work
- Less heavy-handed on the warm cast
- Cleaner grain structure (pro use case)

### VSCO — Film 02 (Kodak Gold 100)

Now discontinued but settings live on in community knowledge:
- VSCO 02: Kodak Gold 100 base
- Warmer than neutral, moderate contrast
- Desaturated greens, boosted warm tones
- Slight fade in shadows
- Fade amount applied for highlight attenuation

### RNI Films — Kodak Gold 200

RNI All Films 5 includes a Kodak Gold 200 profile:
- Camera profile-based (ICC/DCP)
- More accurate color reproduction than generic HSL recipes
- Subtle grain simulation
- Available for Lightroom and Capture One

---

## 10. Common Mistakes to Avoid

Based on community feedback on "bad" Gold 200 emulations:

1. **Too orange** — Gold is warm-golden, not orange. Watch the orange/red balance.

2. **Crushed blacks** — Gold 200 has lifted, slightly milky blacks. Crushing to pure black kills the film look.

3. **Overdone teal shadows** — The teal cast is subtle. If your shadows look like a cross-processed movie still, reduce split toning by 50%.

4. **Too much contrast** — Gold 200 has moderate contrast. Heavy S-curves make it look like slide film (Ektachrome), not Gold.

5. **No grain** — A clean digital file with warm tones is not a film emulation. Add grain or it reads as "warm digital preset."

6. **Green greens** — Gold 200 greens are yellow-leaning. If your greens look like Fuji Velvia, desaturate and shift hue toward yellow.

7. **Blue skies** — Gold 200 renders skies as slightly muted/milky blue, not deep saturated blue. Reduce blue saturation.

8. **Magenta presence** — If there's noticeable magenta in your image, you've lost the Gold look. Kill magenta saturation and shift its hue.

9. **Overdone halation** — Some YouTubers add bloom/halation. Gold 200 has mild halation in the red channel only. Don't overdo it.

10. **Too much clarity** — Negative clarity (-5 to -10) softens the digital edge. Positive clarity makes it look like digital sharpening.

---

## 11. Quick-Apply Checklist

When applying a Gold 200 emulation to a new image, check:

- [ ] White balance: ~6000K, tint -8 (warm, slight green offset)
- [ ] Blacks lifted (+15 to +25)
- [ ] Highlights softly compressed (-45 to -60)
- [ ] S-curve on tone curve (mild)
- [ ] Greens: shifted toward yellow, desaturated
- [ ] Yellows: boosted saturation, shifted toward orange
- [ ] Blues: shifted toward aqua, slightly desaturated
- [ ] Oranges: boosted saturation and luminance
- [ ] Magenta: desaturated heavily
- [ ] Split tone: warm highlights, teal shadows (subtle)
- [ ] Calibration: red +20 hue, blue -10 hue
- [ ] Grain: amount 30–40, size 25–30, roughness 45–55
- [ ] Clarity: -5 to -10
- [ ] No heavy vignette (subtle -5 to -10 ok)

---

## 12. Community Source References

- **r/analog** — Primary community for Gold 200 shooters; extensive discussions on color characteristics and scanning
- **r/Lightroom** — Multiple preset-sharing threads; Gold 200 is one of the most requested
- **r/postprocessing** — Technical discussions on emulation accuracy; film color science analysis
- **Jamie Windsor** (YouTube) — Gold 200 preset tutorial and philosophy; emphasis on warm/cool dynamic
- **Willem Verbeeck** (YouTube) — Extensive Gold 200 shooting; scanning and color correction approach
- **grainydays** (YouTube) — Gold 200 review and shooting tips; film characteristic analysis
- **Kyle McDougall** (YouTube) — Analog film breakdowns; Gold 200 scanning and color philosophy
- **NATE Cam** (YouTube) — Lightroom film emulation tutorials including Gold 200
- **Mastin Labs** — Commercial preset reference; profile-based approach
- **VSCO** — Historical Film 02 pack; film-accurate starting point
- **RNI Films** — Most accurate profile-based Gold 200 emulation available

---

*Last updated: May 2026 — Community recipes evolve. Always test against real Gold 200 scans for your specific camera/sensor combination.*
