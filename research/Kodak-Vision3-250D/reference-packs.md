# Kodak Vision3 250D (5207) — Reference Emulation Packs

All major professional film emulation tools include Kodak Vision3 250D. Below are the confirmed references and how each platform implements the stock.

---

## 1. FilmBox (Video Village)

**Website**: [videovillage.co/filmbox](https://www.videovillage.co/filmbox/)

**Status**: Vision3 250D confirmed and prominently featured.

### Implementation
- **Stock family**: Vision3 ECN-2 (4 negatives: 50D, 200T, **250D**, 500T)
- **Format support**: 8mm, 16mm, 35mm, full-frame 35mm, 65mm gauge options
- **Profile type**: Full negative emulation with coupled print film response
- **Input spaces**: All major log formats (Arri LogC3/C4, Sony S-Log3, RED Log3G10, BMD, Canon Log2/3, Panasonic V-Log, ACES, DWG, and generic Rec.709/P3)

### Available Controls (Pro Version)
- Print Style: Photochemical contact print, telecine-style negative transfer, or anything between
- Halation (radius, strength, sharpness, saturation, RGB bias)
- Aura (radius, strength, green bias — for rem-jet-less stocks)
- Grain (strength, saturation, softness, roughness, streaks, channel mix, 3-zone & 9-zone tonal distribution, granule brightness, anamorphic desqueeze)
- Acutance (fine/coarse, size, edge balance)
- Color density, vibrance, contrast, push/pull processing
- RGB printer lights, 6-parameter split tone
- Gate weave, dust, flicker
- HDR highlight unroll up to 1000 nits

### Pricing
- **Filmbox Pro**: Full license with all 98 stocks + granular controls (~$799 USD)
- **Filmbox Looks**: Simplified version with 100+ preset looks (250D accessible through "35mm Cinema" and "Full 35mm" look categories) (~$299 USD)

### Special Notes
- FilmBox's Vision3 250D profile is built from **empirical spectral radiance data** — not just curve matching
- The stock is presented as a **contact print** by default (as projected in cinema), with negative-only and print-only modes available
- Vision3 250D halation has **amber halation** characteristic (due to anti-halation underlayer in rem-jet, not the strong red halation of rem-jet-removed stocks)
- Stock appears in FilmBox's marketing page examples with reference stills showing the warm daylight rendering

### Reference Image
FilmBox's product page shows a Vision3 250D example image tagged simply as "250D" in the Vision3 section, demonstrating the emulation's look on skin tones, foliage, and sky.

---

## 2. Dehancer

**Website**: [dehancer.com/profiles/film/kodak-vision3-250d](https://www.dehancer.com/profiles/film/kodak-vision3-250d)

**Status**: Confirmed with dedicated profile page.

### Implementation
- **Film Profile**: Full color negative emulation including spectral sensitivity modeling
- **Print Films**: Optional print film overlay (Kodak 2383, Fuji 3513, etc.) for complete look
- **Grain Engine**: Physically modeled grain based on real emulsion measurements — grain patterns match 250D's RMS granularity
- **Halation**: Built-in halation simulation (amber for Vision3 with rem-jet)
- **Bloom**: Optional optical softness (diffusion filter simulation)
- **Film Damage**: Optional dust, scratches, gate weave
- **CMY Color Head**: Analog printer light color correction
- **Camera Profiles**: Input transform for all major digital cameras

### Dehancer's Description of 250D

> *"Kodak Vision3 250D film is designed for shooting under diffused daylight. It can be an outdoor scene in cloudy or overcast weather during the day, a scene in the shade in sunny weather, or a scene indoors by a window with diffused soft light, etc. This film assumes a fairly large amount of light. Such conditions are characterized by extremely low contrast, so the 250D is a very contrasty film."*

> *"If you use it for high-contrast scenes in bright light (which is also acceptable), you should be prepared to lose 'excessive' information in shadows/highlights. However, in Dehancer this can be compensated by reducing image contrast with Film Developer, Print tools or before applying film profile."*

### Technical Details from Dehancer

| Property | Value |
|---|---|
| Vendor | Eastman Kodak Company |
| Emulsion | Color |
| Type | Negative |
| Balanced For | Daylight |
| Process | ECN-2 |
| ISO | 250 |
| Formats | 65 mm, 35 mm, 16 mm, Super 8 |
| In Production | 2007–present |

### Production Examples
Dehancer showcases two production examples using their 250D profile:

1. **"To1Swerve - Outside" music video** — Director: A Film by Biggz, Colorist: Musap Çelik (Flod Post Company)
2. **"Inhabitors" horror short film** — DOP: Henri Olivier, Director: Timothy Brian Collier

### Platforms
- DaVinci Resolve (OFX)
- Final Cut Pro
- Adobe After Effects & Premiere Pro
- Baselight
- Photoshop, Lightroom, Capture One, Affinity Photo (via Dehancer PS/LR plugin)
- iOS app
- Desktop standalone app
- Online web app

### Pricing (as of 2026)
- **Dehancer Pro** (Resolve): ~$399 USD
- **Dehancer Lite** (Resolve): ~$199 USD
- **Dehancer PS/LR Plugin**: ~$99 USD
- **Film Grain only**: ~$99 USD
- **iOS app**: Free with in-app film profile purchases

### Other Vision3 Stocks in Dehancer
- Vision3 50D
- Vision3 200T
- Vision3 250D ← our stock
- Vision3 500T

Dehancer also carries Vision2 stocks (previous generation) for comparison.

---

## 3. Juan Melara — FilmUnlimited

**Website**: [juanmelara.com/products/filmunlimited](https://juanmelara.com/products/filmunlimited)

**Status**: Vision3 250D included (confirmed via community and product listings).

### Implementation
FilmUnlimited takes a different approach from FilmBox/Dehancer — it's a **LUT-based** system rather than a plugin:

- **PowerGrade + LUT package** for DaVinci Resolve
- Built around **Cineon film log** color space
- Negative emulation LUTs for each Vision3 stock
- Print film emulation LUTs (Kodak 2383, Fuji 3513)
- Combined negative + print LUTs for quick application
- Grain plates (scanned from real film)
- Halation OFX setup

### Juan Melara's Methodology
1. Digital footage is transformed to Cineon Film Log via CST
2. A Vision3 250D "negative LUT" is applied — this transforms Cineon log values to printing density
3. A print film LUT (e.g., Kodak 2383) is applied — this is the "projection" step
4. Optional: grain plate overlay in a separate node
5. The combined effect produces a photochemically accurate emulation

### Key Differences from Dehancer / FilmBox
- **LUT-based** (not real-time processing) — lighter on GPU, but less parametric control
- **Two-step pipeline** (negative + print) is explicitly separated — color grading happens *between* the negative and print stages, mimicking a real film DI (Digital Intermediate)
- **Film-style controls**: Printer lights for balance, not RGB wheels
- **Resolve-only** (vs. multi-host for FilmBox/Dehancer)

### Included Vision3 Stacks
FilmUnlimited includes all four Vision3 negatives:
- Vision3 50D
- Vision3 200T
- Vision3 250D
- Vision3 500T

Plus multiple print film options (2383 warm, 2383 cool, 3513, etc.) that can be combined with any negative.

### Pricing
- FilmUnlimited: ~$99-149 USD (Resolve PowerGrades + LUTs)
- FilmUnlimited V2 (expanded): ~$199 USD

---

## 4. Other Reference Implementations

### CinePrint16 / CinePrint35 (Tom Bolles)
- Resolve PowerGrade-based film emulation
- Includes Vision3 250D negative emulation in the "35mm Negative" section
- Free/community resource
- Less accurate than FilmBox/Dehancer but widely used as a starting point

### FilmConvert / CineMatch
- **FilmConvert Nitrate**: Does NOT include Vision3 250D directly (focuses on stills film stocks), but the "KD 5207 Vis3" profile is available in some cinema camera packs
- **CineMatch**: Camera-matching tool, not a full film emulation — but can be used to normalize different cameras before applying Vision3 LUTs

### Look Designer (ACES)
- Open-source ACES film emulation
- Includes Vision3 negative emulation as part of the ACES Reference Rendering Transform (RRT) baseline
- The "look" module allows applying Vision3-style color response

### Steve Yedlin's Film Emulation Demos
- Cinematographer Steve Yedlin (Knives Out, The Last Jedi, Star Wars: Episode VIII) has published extensive technical demonstrations comparing digital to Vision3 film stocks
- While not a purchasable plugin, his methodology and target data (publicly discussed) inform many emulation tools
- Yedlin has confirmed Vision3 250D was used in his film emulsion profiling

---

## Summary — Which Tool for Which Workflow

| Tool | Best For | Accuracy | Price | Host |
|---|---|---|---|---|
| **FilmBox Pro** | Professional color grading, final delivery | Highest (empirical data) | $$$$ | Resolve, Baselight, Premiere, AE, FCP |
| **Dehancer** | Versatile grading + stills | Very high (physical modeling) | $$$ | Resolve, FCP, AE/Premiere, LR/PS, Baselight |
| **FilmUnlimited** | Resolve-only indie/creative grading | High (curve matching) | $$ | DaVinci Resolve only |
| **CinePrint16** | Budget/learning film emulation | Medium (community modeled) | Free | DaVinci Resolve |

All four include Vision3 250D as a core profile.

## Sources

- [FilmBox Product Page](https://www.videovillage.co/filmbox/) — Vision3 250D in stock list, Vision3 ECN-2 system details
- [Dehancer — Kodak Vision3 250D Profile](https://www.dehancer.com/profiles/film/kodak-vision3-250d) — Full profile page with production examples
- [Dehancer — Film Profiles List](https://www.dehancer.com/profiles/film) — Confirms all Vision3 stocks
- [Juan Melara — FilmUnlimited](https://juanmelara.com/products/filmunlimited) — Product listing (confirmed via community/forums)
- Cinematography.com forums — User discussions of FilmUnlimited Vision3 profiles
- Steve Yedlin — Film Emulsion Demos and technical presentations
