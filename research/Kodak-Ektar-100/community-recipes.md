# Community Recipes — Kodak Ektar 100 Lightroom Settings

> Sourced from Reddit (r/analog, r/AnalogCommunity, r/Lightroom), YouTube tutorials, and photography forums

## Community Consensus

The Ektar 100 look in Lightroom is defined by **high saturation + high contrast + zero grain + warm color bias**. The community generally agrees on these core characteristics, though specific slider values vary by creator.

## Recipe 1: "Classic Ektar Punch" (Reddit/YouTube consensus)

### Basic Panel
| Setting | Value | Notes |
|---|---|---|
| Profile | Adobe Color / Adobe Standard | NOT Apple/smartphone profile; start neutral |
| Temp | +5 to +15 (warmer) | Ektar runs warm; slight yellow-red bias |
| Tint | +5 to +10 (magenta) | Counteracts green from digital sensors |
| Exposure | 0 to +0.30 | Slight overexposure mimics film latitude |
| Contrast | +25 to +40 | Ektar is high-contrast film |
| Highlights | –20 to –40 | Tame digital clipping; film compresses highlights |
| Shadows | +15 to +30 | Lift shadows slightly (but Ektar shadows block fast) |
| Whites | 0 to +15 | |
| Blacks | –10 to –25 | Deepen blacks for contrast punch |

### Tone Curve
- **Point Curve:** Medium Contrast or Strong Contrast
- **Custom point curve:** S-curve with lifted blacks (crushed black point ~5–10%) and pulled highlights (~90–95%)
- Typical Reddit recipe: "Start with Medium Contrast curve, then pull the shadow point up to ~10% and the highlight point down to ~95%"

### HSL / Color
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +5 to +15 | +15 to +30 | –5 to –15 |
| Orange | –5 to 0 | +10 to +25 | 0 to –10 |
| Yellow | –5 to +5 | +10 to +25 | +5 to +15 |
| Green | +10 to +25 | +15 to +35 | –10 to –20 |
| Aqua | 0 to +10 | +10 to +20 | –5 to +5 |
| Blue | –5 to +5 | +10 to +25 | –10 to –20 |
| Purple | 0 to +10 | 0 to +15 | 0 |
| Magenta | 0 to +10 | 0 to +15 | 0 |

**Key HSL insights from community:**
- **Reds:** Shift slightly orange, increase saturation, darken — Ektar reds are deep and warm, not neon
- **Greens:** Shift toward yellow-green, heavily saturate, darken — creates the "Ektar landscape look"
- **Blues:** Deepen (darken) while saturating — for that intense sky blue
- **Skin tones note:** Orange luminance may need +5 to +10 instead of –5 to prevent ruddy skin

### Color Grading
| Range | Hue | Saturation | Notes |
|---|---|---|---|
| Shadows | 200–220° (blue-cyan) | 5–15 | Ektar has a cool-blue shadow tint |
| Midtones | 30–50° (warm yellow-orange) | 5–15 | Warm earth-tone midtones |
| Highlights | 30–50° (warm) | 3–8 | Subtle warmth in highlights |

### Detail
| Setting | Value | Notes |
|---|---|---|
| Sharpening | 40–60 | Ektar is very sharp; emulate with moderate sharpening |
| Masking | 30–50 | Edge-only sharpening |
| Noise Reduction | 0–5 | Ektar has essentially no grain at 100 |
| Grain | OFF or Amount 5 / Size 10 / Roughness 50 | Most community recipes ADD NO GRAIN; it's about the clean look |

### Calibration
| Channel | Hue | Saturation |
|---|---|---|
| Red Primary | +5 to +15 | +10 to +20 |
| Green Primary | –5 to +10 | +5 to +15 |
| Blue Primary | –5 to +5 | +10 to +20 |

## Recipe 2: "Ektar Skin-Safe" (from r/AnalogCommunity)

For portraits where the standard Ektar look is too harsh on skin:

- **Reduce Orange Saturation** to +5 (not +25)
- **Orange Luminance to +10** (not –10)
- **Calibration Red Primary Hue to +20, Saturation to –5**
- **Reduce overall Contrast to +15**
- **Add very slight negative Clarity** (–5 to –10) to soften skin

## Recipe 3: Luke Taylor's Free Preset Approach

Luke Taylor (lukeptaylor.com) created a free Ektar 100 XMP preset. His approach:

- Designed as a "final edit" — minimal further tweaking needed
- Strong warm bias with elevated reds and yellows
- Moderate contrast curve with compressed highlights
- Zero added grain (respects Ektar's clean signature)
- Works across cameras: tested on Sigma FP, Ricoh GR III, Sony a7s
- No additional editing after preset application in sample images

## Recipe 4: YouTube Tutorial Approaches

Based on "How to Create the KODAK EKTAR 100 Look in Lightroom Classic" and similar videos:

### Base Adjustments
- Start with **Adobe Color** or **Adobe Neutral** profile
- **White Balance:** Adjust warmer — ~5600–6200K daylight scenes

### Critical Curve Move
- **Red channel curve:** Lift shadow reds slightly, pull highlight reds down — creates the warm shadows/cooler highlights crossover
- **Blue channel curve:** Boost blue in highlights (sky), slightly crush blue in shadows
- **Green channel curve:** Neutral to slight S-curve

### Split Toning (old method) / Color Grading (new)
- Shadows: Blue at ~210–225°, saturation ~10
- Highlights: Yellow-orange at ~40–55°, saturation ~10

## Red Flags from Community

1. **Do NOT add grain.** Ektar 100 is about the clean, virtually grain-free look. Adding grain defeats the purpose.
2. **Skin tones are the biggest challenge.** Many community members note Ektar renders Caucasian skin ruddy/red. Use local adjustments or reduce orange/red saturation for portraits.
3. **Don't crush blacks completely.** Ektar has tight shadow latitude; lifted shadows + slightly lifted blacks better represent the film's actual behavior.
4. **Blue shadows are authentic.** The characteristic cool-blue shadow tint is a real Ektar trait, especially visible in scans.
5. **Low light = weird.** Multiple Reddit reports: Ektar in low light produces "strange dark blue hues" and "unnatural shadow colors."

## Community Discussion Highlights

From r/analog post (1h03xp9):
> "After a few rolls of Ektar, I realized Ektar is not friendly for low light condition. Unlike Portra, the image is very likely to have weird dark blue hue in low light condition, and post adjustment will be needed."

From RyanHK on r/AnalogCommunity:
> "Ektar produces reds and greens that are impossibly vivid. It's like slide film went through C-41. But if you have any red in your skin you look sunburned."

From #film-photography Discord:
> "Rate Ektar at 80. Always overexpose by 1/3 to 2/3 stop. The box speed is optimistic and the shadows are unforgiving."

## Paid Products That Offer Free Samples

- **Seim Effects Filmist Sampler** (free Classic Negative + Portra 160 presets; full Ektar in paid Filmist pack)
- **Luke Taylor** — free Ektar 100 .xmp preset
- **PresetLove** — free Forrest Lane Ektar 100 preset
- **PSD Stack** — free Kodak Ektar 100 preset (DNG + XMP + LRTEMPLATE)
- **Presetpro.com** — Ektar 100 emulation profile (in paid collection)
- **Eli Hendrickson on Gumroad** — free Ektar 100 LR preset
