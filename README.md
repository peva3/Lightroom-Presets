# Lightroom Presets — Film Simulations & Creative Looks

A collection of 30 hand-tuned Lightroom presets inspired by classic film stocks, iconic camera profiles, and trending social media aesthetics. Each preset was reverse-engineered from real photography shared on Reddit and Instagram, then dialed in against reference photos to match the original emulsion or style as closely as possible.

## Contents

- [Installation](#installation)
- [Usage Tips](#usage-tips)
- Classic Color Negative Film
  - [Fujifilm Classic Chrome](#fujifilm-classic-chrome)
  - [Kodak Portra 400](#kodak-portra-400)
  - [Kodak Portra 160](#kodak-portra-160)
  - [Kodak Gold 200](#kodak-gold-200)
  - [Fuji Superia X-TRA 400](#fuji-superia-x-tra-400)
  - [Fujifilm Pro 400H](#fujifilm-pro-400h)
  - [Agfa Vista 200](#agfa-vista-200)
  - [Kodak Ektar 100](#kodak-ektar-100)
  - [Fuji Astia 100F](#fuji-astia-100f)
  - [Kodak Ektachrome E100](#kodak-ektachrome-e100)
- Classic Slide Film & Vintage
  - [Kodachrome 64](#kodachrome-64)
  - [Fuji Velvia 50](#fuji-velvia-50)
  - [Faded Summer / Expired Film](#faded-summer--expired-film)
- Black & White Film
  - [Ricoh High-Contrast Monochrome](#ricoh-high-contrast-monochrome)
  - [Ilford HP5 Plus](#ilford-hp5-plus)
  - [Kodak Tri-X 400](#kodak-tri-x-400)
  - [Ilford Delta 3200](#ilford-delta-3200)
- Night & Specialty Film
  - [Cinestill 800T](#cinestill-800t)
- Creative & Trending Looks
  - [Moody PNW](#moody-pnw)
  - [Cinematic Teal and Orange](#cinematic-teal-and-orange)
  - [Y2K Flash Digicam](#y2k-flash-digicam)
  - [Polaroid SX-70](#polaroid-sx-70)
  - [Cyberpunk Neon City](#cyberpunk-neon-city)
  - [Light and Airy Fine Art](#light-and-airy-fine-art)
  - [Bleach Bypass](#bleach-bypass)
  - [Lomography Cross-Processed](#lomography-cross-processed)
  - [Pastel Anime Aethereal](#pastel-anime-aethereal)
  - [Cinematic Dream / Pro-Mist Look](#cinematic-dream--pro-mist-look)
  - [Matte Fade](#matte-fade)
  - [Faux Infrared](#faux-infrared)
- [Preset Quick Reference](#preset-quick-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Download the `.xmp` files from the `Presets/` folder in this repo. Presets are organized into subfolders by category:
   - `Presets/Color-Negative/` — Film stock emulations
   - `Presets/Black-White/` — Monochrome film looks
   - `Presets/Slide/` — Slide/transparency film
   - `Presets/Creative/` — Trending, experimental, and non-film looks
2. Copy the `.xmp` files into your Lightroom Develop Presets folder:
   - **macOS:** `~/Library/Application Support/Adobe/Lightroom/Develop Presets/`
   - **Windows:** `%APPDATA%\Adobe\Lightroom\Develop Presets\`
3. Restart Lightroom. Presets will appear under the **Film Simulations** group in the Develop module.

## Usage Tips

- **White Balance is key.** Many film presets assume a specific temperature. If colors feel off, adjust WB first — Portra presets expect warmth, Cinestill expects cool/tungsten.
- **Exposure varies.** Apply the preset, then tweak the Exposure slider. These are starting points calibrated for well-exposed RAW files.
- **Grain scales with resolution.** The grain settings were tuned for 24MP images. Reduce Grain Amount for lower-res shots or increase for film-scanner authenticity.
- **Stack 'em.** Try applying a film preset for color, then adding a creative preset (like Matte Fade or Cinematic Dream) on top as a second pass.

---

## Classic Color Negative Film

### Fujifilm Classic Chrome

*Documentary-street look with muted tones, subdued blues, and deep punchy shadows.*

Mimics Fujifilm's beloved in-camera simulation. Colors feel restrained and journalistic — blues drop back, greens recede, but reds hold their presence. Great for urban landscapes, travel reportage, and overcast days.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +15, Highlights -15, Shadows +10, Whites +10, Blacks -15 |
| Color | Vibrance +10, Saturation -15 |
| HSL | Red Sat +10, Blue Sat -20 / Lum -10, Green Sat -15 |
| Effects | Clarity +5 |

---

### Kodak Portra 400

*Warm, flattering skin tones with soft contrast and lifted matte blacks.*

The gold standard for portraiture. Portra 400 wraps subjects in a warm glow with gentle highlight roll-off and a signature lifted shadow that reads as a subtle matte. Perfect for golden hour, window light, and environmental portraits.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.15, Contrast -10, Highlights -20, Shadows +20, Whites +10, Blacks +15 |
| Color | WB push warmer (+300K to +500K) |
| HSL | Orange Lum +10, Green Hue +15 / Sat -20 |
| Effects | Grain 25 / 25 / 25 |

---

### Kodak Portra 160

*Ultra-soft contrast with wide dynamic range and pastel-flawless skin.*

The softer sibling of Portra 400. It flattens contrast further, pulls highlights way down, and lifts shadows into a creamy matte. Skin looks airbrushed and foliage shifts to a warm yellow-green.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -15, Highlights -30, Shadows +25, Whites -10, Blacks +20 |
| Color | WB slightly warm, Vibrance +5, Saturation -15 |
| HSL | Orange Sat -5 / Lum +15, Green Hue +10 |
| Effects | Grain 15 / 20 |

---

### Kodak Gold 200

*Sunny nostalgia — the quintessential 90s family-vacation consumer film.*

Gold 200 leans hard into warm, golden hues with a distinct yellow-orange cast on skin. Blues pull back so the warmth dominates. It feels like scanning a shoebox full of drugstore prints from childhood road trips.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +5, Highlights -15, Shadows +15, Blacks +10 |
| Color | WB warm (+400K to +600K), Tint +5 Magenta, Saturation +5 |
| HSL | Yellow + Orange Sat +15, Blue Sat -10 |
| Color Grading | Shadows: Hue 45, Sat 10 |
| Effects | Grain 25, Roughness 40 |

---

### Fuji Superia X-TRA 400

*Gritty street staple with murky greenish shadows and punchy magenta-reds.*

Superia was the cheap 4-pack you grabbed at the drugstore before a trip. It renders shadows with a sickly green cast and cranks red tones toward magenta. Perfect for flash street photography and skate shots.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +15, Highlights -20, Shadows +10, Blacks +5 |
| Color | Tint push Green (-10) |
| HSL | Red Sat +20 / Hue -10, Green Hue -10 |
| Color Grading | Shadows: Hue 170, Sat 15 |
| Effects | Grain 30, Roughness 45 |

---

### Fujifilm Pro 400H

*Light, airy, pastel-driven wedding and lifestyle look.*

Pushes greens toward a cooler minty-cyan and lifts overall exposure for that bright, ethereal wedding blog aesthetic. Contrast is dialed back heavily so nothing feels harsh.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.40, Contrast -15, Highlights -30, Shadows +30, Blacks +10 |
| Color | WB slightly cooler/blue |
| HSL | Green Hue +25 / Sat -20, Blue Hue -15 / Sat -10 |
| Effects | Clarity -5, Grain 20 |

---

### Agfa Vista 200

*Retro color pop that blasts primary colors, especially deep vibrant reds.*

Once sold cheaply in drugstores, Vista 200 is legendary for over-the-top saturation on a budget. Reds are massive, blues pack a punch, and there's a subtle cheap-film charm throughout.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +10, Highlights -10, Shadows +5, Whites +15, Blacks -5 |
| Color | Vibrance +20, Saturation +5 |
| HSL | Red Sat +25, Blue Sat +15, Yellow Hue +10 |
| Effects | Grain 20 |

---

### Kodak Ektar 100

*Clean, modern color with the finest grain and warm earth tones.*

Marketed as having the tightest grain of any color negative film. Ektar delivers big contrast, rich saturation, and a sky that shifts slightly toward teal — all while staying refined and never garish.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +20, Highlights -25, Shadows +10, Blacks -10 |
| Color | WB slightly warm, Saturation +15 |
| HSL | Red Sat +15, Yellow Sat +10, Blue Hue -10 |
| Effects | Grain 15 / 15 / 15 |

---

### Fuji Astia 100F

*Soft fashion — Fuji's answer to portrait slide film.*

Astia tames the extreme contrast of other Fuji slide films. Muted saturation, smooth highlight roll-offs, and brilliant skin tones make it ideal for fashion editorials with natural light.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -5, Highlights -20, Shadows +15, Blacks +5 |
| Color | Vibrance +10, Saturation -10 |
| HSL | Orange Lum +15, Blue + Green Sat -15 |
| Effects | Texture -5, Grain 10 |

---

### Kodak Ektachrome E100

*Clean slide film with cool-leaning blues and crisp contrast.*

Ektachrome was recently resurrected by Kodak and delivers a clean, modern slide-film look. Strong contrast, deep cool blues, and punchy reds give it that unmistakable transparency-film character.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +25, Highlights -15, Shadows -10, Blacks -15 |
| Color | Vibrance +15 |
| HSL | Blue Sat +20 / Lum -10, Red Sat +15, Yellow Sat +10 |
| Effects | Clarity +10 |

---

## Classic Slide Film & Vintage

### Kodachrome 64

*Vibrant mid-century slide film with rich deep reds and warm nostalgic cast.*

The film that defined color photography for decades. Reds are deep and luminous, yellows pop off the page, and a warm orange tint lives in the shadows. It feels like a sunny 1960s postcard.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.10, Contrast +20, Highlights -10, Shadows -5 |
| Color | Vibrance +15, Saturation -5 |
| HSL | Red Sat +20 / Lum -10, Yellow Sat +15, Blue Hue -10 |
| Color Grading | Shadows: Hue 40, Sat 10 |
| Effects | Clarity +10, Grain 15 |

---

### Fuji Velvia 50

*Vivid landscape slide film with crushed shadows and hyper-saturated greens and blues.*

The most intense film in this collection. Velvia pushes greens and blues to almost unnatural levels, crushes blacks deep, and dials contrast high for that epic landscape-on-a-lightbox look. Keep grain at zero — slide film is pristine.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +25, Highlights -15, Shadows -10, Whites +15, Blacks -15 |
| Color | Vibrance +30, Saturation +10 |
| HSL | Green Sat +20, Blue Sat +20, Orange Sat +10 |
| Effects | Dehaze +10, Clarity +10, Grain 0 |

---

### Faded Summer / Expired Film

*What happens when cheap color film bakes in a hot attic for 15 years and gets overexposed two stops.*

Washed out, extremely warm, with muddy shadows and greens that turn to yellow-brown. The black point is so lifted it barely exists. Add heatwave haze and sun-bleached nostalgia.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.50, Contrast -30, Highlights -40, Shadows +40, Blacks +40 |
| Color | WB extremely warm (+800K), Saturation -20 |
| HSL | Green Hue +30 / Sat -30, Blue Sat -40 |
| Color Grading | Shadows: Hue 40, Sat 25 |
| Effects | Grain 40 |

---

## Black & White Film

### Ricoh High-Contrast Monochrome

*Daido Moriyama aggression — pure black shadows, blooming highlights, and heavy grit.*

Inspired by the Ricoh GR series' legendary JPEG profile and Moriyama's prowling street work. Shadows get crushed to near-pure black, highlights bloom with intensity, and enormous grain coats everything. This preset converts to B&W automatically.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +45, Highlights +30, Shadows -40, Whites +25, Blacks -50 |
| B&W Mixer | Red -10, Blue -20 |
| Effects | Clarity +35, Dehaze +10, Grain 60 / 50 / 60 |
| Profile | Adobe Monochrome (auto-conversion) |

---

### Ilford HP5 Plus

*Versatile classic B&W with wide tonal range and pleasing mid-tone contrast.*

The workhorse of black-and-white film. HP5 preserves detail from shadow to highlight without crushing either end. Mid-tones get a gentle push and the grain is present but never overwhelming.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +10, Highlights -20, Shadows +15, Whites +15, Blacks -10 |
| B&W Mixer | Yellow +15, Green +10, Blue -15 |
| Effects | Texture +10, Clarity +10, Grain 35 / 30 / 40 |
| Profile | Adobe Monochrome |

---

### Kodak Tri-X 400

*The undisputed king of photojournalism B&W — crisp whites, aggressive mid-tones, and gorgeous grain.*

Tri-X defined documentary photography from the 1950s onward. It pushes mid-tone contrast hard, keeps whites crisp, and covers everything in that unmistakable sharp-but-organic grain that editors at LIFE Magazine knew by sight.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +35, Highlights -10, Shadows -15, Whites +20, Blacks -30 |
| B&W Mixer | Yellow +15, Green +20, Blue -15 |
| Effects | Clarity +15, Grain 55 / 40 / 50 |
| Profile | Adobe Monochrome |

---

### Ilford Delta 3200

*Ultra-high-speed concert and night-street B&W with massive, golf-ball-sized grain.*

Shot at ISO 3200 in dark clubs and alleys. Low contrast, soft textures, lifted blacks, and grain so large it becomes the subject. This is the look of a dimly lit punk show captured on film.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -10, Highlights -30, Shadows +25, Whites -10, Blacks +20 |
| Effects | Texture -10, Clarity -15, Grain 75 / 60 / 75 |
| Profile | Adobe Monochrome |

---

## Night & Specialty Film

### Cinestill 800T

*Tungsten-balanced cinema film for night photography with red halation glow around bright lights.*

Repurposed motion picture stock — a Reddit night-photography favorite. The cool tungsten balance turns skies deep teal while warm highlights bloom orange. Edges soften with negative clarity and texture to mimic the halation effect.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.10, Contrast +10, Highlights -20, Shadows +15, Whites +10, Blacks +10 |
| Color | WB push cooler/blue, Vibrance +10, Saturation -10 |
| HSL | Red + Orange Lum +10, Blue Hue -15 |
| Color Grading | Shadows: Hue 220 / Sat 15, Highlights: Hue 25 / Sat 15 |
| Effects | Texture -10, Clarity -10, Grain 25 |

---

## Creative & Trending Looks

### Moody PNW

*Dark, brooding Pacific Northwest evergreen vibes with crushed greens and atmospheric haze.*

Inspired by the moody forest and coastal photography dominant in the Pacific Northwest scene. Greens and yellows are heavily desaturated and darkened, blues are muted, and the overall exposure sits about 1/3 stop under to deepen the gloom.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure -0.20, Contrast +10, Highlights -30, Shadows -10, Blacks +15 |
| Color | Vibrance -10, Saturation -10 |
| HSL | Green Sat -50 / Lum -30, Yellow Sat -40 / Lum -20, Blue Sat -20 |
| Effects | Clarity +15, Dehaze +10 |

---

### Cinematic Teal and Orange

*The defining color palette of modern blockbuster color grading.*

Deep teal shadows push cool while warm orange highlights separate skin tones from the background. Boosted blue saturation plus the split-toning combo creates that instantly recognizable trailer-grade look. Works on almost everything.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +15, Highlights -20, Shadows +10, Whites +10, Blacks -10 |
| HSL | Orange Sat +10 / Lum +10, Blue Hue -15 / Sat +20 |
| Color Grading | Shadows: Hue 220 / Sat 25, Highlights: Hue 35 / Sat 15 |
| Effects | Clarity +10 |

---

### Y2K Flash Digicam

*Blown-out direct flash and crushed shadows straight from a 2003 point-and-shoot.*

Recreates the look of early digital compacts — a Sony Cyber-shot or Canon PowerShot with the flash forced on. Highlights are aggressive and blown, shadows push darker, reds get a slight boost while yellows are pulled back to avoid an overly warm cast.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.30, Contrast +25, Highlights +20, Shadows -20, Whites +20, Blacks -15 |
| HSL | Red Sat +15, Yellow Sat -15 |
| Effects | Clarity +15, Texture +10 |

---

### Polaroid SX-70

*Soft, low-contrast instant film with creamy shadows and a heavy vignette.*

Emulates the original Polaroid SX-70 integral film — low contrast, lifted blacks, desaturated blues, and a warm highlight cast meeting cool shadows. The heavy vignette and texture softening complete the instant-print feel.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -20, Highlights -10, Shadows +30, Blacks +40 |
| HSL | Green Hue +20, Blue Sat -20 |
| Color Grading | Shadows: Hue 300 / Sat 15, Highlights: Hue 50 / Sat 20 |
| Effects | Texture -15, Clarity -10, Grain 20, Vignette -35 |

---

### Cyberpunk Neon City

*Neon-drenched night cityscape with boosted magenta/pinks and crushed natural tones.*

Dialed for Blade Runner cityscapes and rainy night streets. Magenta and red channels get massive boosts while yellows and greens are nearly eliminated. High clarity and dehaze cut through mist for that razor-sharp neon glow.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +25, Highlights -20, Shadows +15, Blacks -25 |
| HSL | Red Sat +40, Magenta Sat +40, Blue Hue -25 / Sat +30, Yellow Sat -80, Green Sat -80 |
| Effects | Clarity +20, Dehaze +15 |

---

### Light and Airy Fine Art

*Bright, ethereal, high-key look with soft greens and glowing skin.*

A favorite among Instagram fine-art and newborn photographers. Exposure is pushed over half a stop, contrast is heavily reduced, greens are desaturated and brightened for that dreamy aesthetic, and skin tones get a luminance boost for a porcelain finish.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.60, Contrast -25, Highlights -40, Shadows +30, Whites -10, Blacks +15 |
| Color | Vibrance +10, Saturation -10 |
| HSL | Orange Lum +20, Green Hue +15 / Sat -30 / Lum +20 |
| Effects | Texture -10, Clarity -15 |

---

### Bleach Bypass

*Silver-retention film processing — ultra-high contrast with severely stripped saturation.*

A darkroom technique where the bleach step is skipped during development, leaving silver in the emulsion. The result: massive contrast, crushed blacks, and color that's been beaten down to near-monochrome with just a ghost of hue remaining.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +40, Highlights -20, Shadows -25, Whites +20, Blacks -35 |
| Color | Vibrance -30, Saturation -25 |
| Effects | Texture +15, Clarity +35, Dehaze +10, Grain 30 / Roughness 50 |

---

### Lomography Cross-Processed

*Wild, unpredictable color shifts with heavy vignette — the Holga/Diana aesthetic.*

Replicates cross-processing slide film in C-41 chemistry. Shadows shift toward purple, highlights go yellow-green, saturation jumps off the charts, and a heavy vignette frames the chaos. Every shot comes out different. That's the point.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +35, Highlights +10, Shadows -15 |
| Color | Saturation +20 |
| Color Grading | Shadows: Hue 280 / Sat 25, Highlights: Hue 75 / Sat 30 |
| Effects | Grain 35, Vignette -50 / Midpoint 25 / Feather 50 |

---

### Pastel Anime Aethereal

*Dreamy pastel look with teal-shifted skies and subtle pink-purple shadows.*

Inspired by anime key visuals and aethereal portrait trends. Blues shift heavily toward cyan, greens toward mint, and a subtle pink tone in the shadows adds warmth without breaking the pastel palette. Bright and soft throughout.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Exposure +0.30, Contrast -10, Highlights -25, Shadows +25, Whites +15 |
| Color | Vibrance +20 |
| HSL | Blue Hue -25 / Lum +15, Green Hue +20 |
| Color Grading | Shadows: Hue 320 / Sat 15 |
| Effects | Clarity -5 |

---

### Cinematic Dream / Pro-Mist Look

*Bloomed highlights, negative clarity, and lifted blacks for a milky, diffused aesthetic.*

Recreates the effect of physical diffusion filters like the Tiffen Pro-Mist. Highlights bloom outward, clarity is crushed, dehaze is pulled negative, and blacks lift for a soft matte fade. Throw some grain on top and you get that dreamy film-set haze.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -20, Highlights -40, Shadows +30, Whites -20, Blacks +30 |
| Color Grading | Shadows: Hue 210 / Sat 15, Highlights: Hue 35 / Sat 15 |
| Effects | Texture -20, Clarity -30, Dehaze -10, Grain 20 |

---

### Matte Fade

*Clean, low-contrast matte look with warm shadow tint and heavy black-point lift.*

A straightforward matte fade — contrast is pulled way down, the black point is raised high, and warm orange tints the shadows for a subtle vintage warmth. Saturation is lowered just enough to keep colors from fighting the fade. Great for editorial and lifestyle.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast -30, Highlights -20, Shadows +30, Whites -10, Blacks +50 |
| Color | Saturation -15 |
| Color Grading | Shadows: Hue 40 / Sat 15 |
| Effects | Grain 15 |

---

### Faux Infrared

*Simulated infrared film — glowing white foliage against dark dramatic skies.*

Reproduces the surreal look of infrared photography. Greenery and foliage (green and yellow channels) are pushed to near-pure white, while blue and aqua channels are slammed to black to darken skies and water. B&W conversion is automatic to complete the effect.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | Contrast +35, Highlights +20, Shadows -20, Whites +30, Blacks -30 |
| B&W Mixer | Green +100, Yellow +80, Blue -100, Aqua -80 |
| Effects | Clarity +20, Grain 40 / Roughness 50 |
| Profile | Adobe Monochrome |

---

## Preset Quick Reference

| Category | Preset | Type | Key Vibe |
|---|---|---|---|---|
| Color-Negative | Fujifilm Classic Chrome | Color Neg | Muted, documentary, punchy shadows |
| Color-Negative | Kodak Portra 400 | Color Neg | Warm skin, soft contrast, lifted blacks |
| Color-Negative | Kodak Portra 160 | Color Neg | Ultra-soft, matte pastel skin |
| Color-Negative | Kodak Gold 200 | Color Neg | 90s nostalgia, warm golden cast |
| Color-Negative | Fuji Superia X-TRA 400 | Color Neg | Gritty street, green shadows |
| Color-Negative | Fujifilm Pro 400H | Color Neg | Airy, pastel, minty greens |
| Color-Negative | Agfa Vista 200 | Color Neg | Retro color pop, cheap film charm |
| Color-Negative | Kodak Ektar 100 | Color Neg | Clean, modern, fine grain |
| Black-White | Ricoh High-Contrast Monochrome | B&W | Aggressive, gritty, Moriyama-style |
| Black-White | Ilford HP5 Plus | B&W | Classic mid-tone contrast, versatile |
| Black-White | Kodak Tri-X 400 | B&W | Photojournalism, crisp grain |
| Black-White | Ilford Delta 3200 | B&W | Extreme grain, concert nights |
| Slide | Kodachrome 64 | Slide | Rich reds, warm nostalgic cast |
| Slide | Fuji Velvia 50 | Slide | Hyper-saturated landscapes |
| Slide | Fuji Astia 100F | Slide | Soft fashion, muted saturation |
| Slide | Kodak Ektachrome E100 | Slide | Clean slide, cool blues |
| Creative | Cinestill 800T | Specialty | Tungsten night, red halation glow |
| Creative | Cinematic Dream / Pro-Mist | Creative | Bloomed highlights, milky haze |
| Creative | Faded Summer / Expired Film | Creative | Sun-bleached, heat-damaged film |
| Creative | Moody PNW | Creative | Dark forests, atmospheric gloom |
| Creative | Cinematic Teal and Orange | Creative | Blockbuster color grading |
| Creative | Y2K Flash Digicam | Creative | Early-2000s direct flash |
| Creative | Polaroid SX-70 | Creative | Soft instant film, heavy vignette |
| Creative | Cyberpunk Neon City | Creative | Neon magenta/pink, Blade Runner |
| Creative | Light and Airy Fine Art | Creative | High-key, dreamy, bright |
| Creative | Bleach Bypass | Creative | Ultra-contrast, stripped color |
| Creative | Lomography Cross-Processed | Creative | Wild color shifts, heavy vignette |
| Creative | Pastel Anime Aethereal | Creative | Dreamy pastel, cyan skies |
| Creative | Matte Fade | Creative | Low contrast, warm black lift |
| Creative | Faux Infrared | B&W/Creative | Glowing white foliage, dark skies |

---

## Contributing

New presets, tweaks to existing settings, and documentation improvements are welcome. The full guide — including how to export `.xmp` files, naming conventions, and PR guidelines — is in [CONTRIBUTING.md](CONTRIBUTING.md).

Quick overview:

1. **Fork** this repo and create a branch.
2. **Add or edit** an `.xmp` preset file and update the README.
3. **Open a pull request** with a description of the look and your reference photo.

---

## License

MIT — see [LICENSE](LICENSE) for the full text. Basically: use these presets however you want, just keep the copyright notice intact.

---

*Presets tuned by [@peva3](https://github.com/peva3) against real-world reference photos shared on Reddit, Instagram, and photography forums.*
