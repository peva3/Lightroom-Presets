# Kodachrome 64 — Reference Packs & Emulation Products

A survey of commercially available and community-developed film emulation packs that include Kodachrome or Kodachrome-inspired looks. Organized by format and approach.

---

## Profile-Based Emulations (Most Accurate Approach)

These products use **ICC profiles / DCP camera profiles / LUTs** rather than slider adjustments. Profiles remap color at the raw processing level, which generally produces more accurate film emulation than HSL/tone curve manipulation.

### RNI (Really Nice Images) — All Films 5

**Website**: reallyniceimages.com  
**Format**: Lightroom/ACR profiles, Capture One styles, iOS app  
**Pricing**: Lite $96 / Pro $192 / Demo (free)  
**Kodachrome inclusion**: Yes — includes multiple Kodachrome variants

RNI is widely considered the **gold standard** for digital film emulation. Their profiles are derived from actual film scans and calibrated per-camera. All Films 5 uses profile-based rendering (Generation 5) which doesn't touch the adjustment sliders, leaving you a clean starting point.

Reported Kodachrome variants in All Films 5:
- Kodachrome 64 (Standard)
- Kodachrome 64 (Faded)
- Kodachrome 200
- Kodachrome 25

RNI also offers All Films 4 (Generation 4), which uses adjustment-based presets — less accurate for color but allows slider modification after application.

**Community consensus**: Best Kodachrome blue rendering among commercial packs. Slightly warm midtone rendition. The Gen 5 profiles are the most sophisticated approach available.

### RNI — All Films 5 for Capture One

Same film library, implemented as Capture One Styles (ICC-based). Note that Capture One cannot use camera-specific DCP profiles, so the implementation differs from the Lightroom version.

---

## Adjustment-Based Preset Packs

### Alex Ruskman — Kodachrome Preset Pack

**Website**: alexruskman.com  
**Format**: Lightroom presets + DCP camera profiles  
**Pricing**: ~$25-45 estimated  
**Kodachrome inclusion**: Dedicated pack

Alex Ruskman is frequently cited on Reddit (r/Lightroom, r/analog) and YouTube for having one of the most accurate community-developed Kodachrome preset collections. His approach uses a custom DCP camera profile as the color foundation, then builds presets on top for specific lighting conditions.

Reported contents:
- Kodachrome 64 (Direct Sun)
- Kodachrome 64 (Overcast)
- Kodachrome 64 (Flash/Studio)
- Kodachrome 64 (Tungsten)
- Kodachrome 64 Faded (simulating age)
- Kodachrome 25 (lower contrast, finer grain)
- Kodachrome 200 (higher contrast, more grain)
- Adjustment brushes for local Kodachrome effects

**Community consensus**: Excellent red rendering. Strong blue-to-cyan shift. Skin tones can skew slightly magenta in some lighting. Requires the DCP profile to be installed correctly — without it, results are inconsistent.

---

### Mastin Labs — Not Confirmed

Mastin Labs (mastinlabs.com) produces high-end presets profiled to specific cameras. As of 2024-2025, they primarily focus on Portra, Fuji, and Ilford emulations. They do not have a dedicated Kodachrome pack, but their "Vintage" or "Adventure" packs may approximate the palette.

---

### VSCO Film Packs — Discontinued

VSCO's desktop film presets (VSCO Film 01-07) were discontinued in 2019, but they remain in use by photographers who purchased them before delisting. VSCO Film included Kodachrome 64 in certain packs, and community archives of slider values from VSCO's Kodachrome presets circulate on forums.

---

## Scanner-Based ICC Profiles (for scanning actual Kodachrome)

### SilverFast — Kodachrome Mode

**Website**: silverfast.com  
**Format**: Scanner software with dedicated ICC profiles  
**Available in**: SilverFast SE Plus, Ai Studio, Archive Suite

SilverFast includes custom Kodachrome ICC profiles for most supported film scanners. These profiles compensate for Kodachrome's notorious blue color cast during scanning and optimize color reproduction. They also offer Multi-Exposure to handle Kodachrome's extreme dynamic range (up to 3.8D for K25).

This is the tool for digitizing actual Kodachrome slides, not for emulation.

---

## Video / Motion LUTs

### FilmConvert / Dehancer

- **Dehancer** (dehancer.com) — Includes Kodachrome 64 as a film stock in their OFX plugin for DaVinci Resolve, Premiere, Final Cut. Uses a combination of color transform + halation + grain. Highly regarded for video.
- **FilmConvert Nitrate** — Includes "KD 5207" (Kodak Vision3) but does not have a dedicated Kodachrome reversal stock. Some users modify the KD profile to approximate Kodachrome.

### RNI All Films — Video (Coming Soon / Available)

RNI has announced a video LUT version of their film library for DaVinci Resolve, Premiere Pro, and After Effects.

---

## Mobile Apps

### RNI Films (iOS)

Real film simulation app for iPhone. Includes Kodachrome 64 among its film profiles. Uses the same profile engine as the desktop version.

### VSCO (iOS/Android)

The VSCO mobile app includes Kodachrome-inspired filters (labeled with coded names like C1-C9, A4-A6, etc.). The exact Kodachrome filter name changes with app updates; community forums track which filter codes correspond to which film stocks.

---

## DIY / Open-Source Approaches

### RawTherapee Film Simulation (HaldCLUT)

RawTherapee's HaldCLUT system allows loading of film simulation color lookup tables. Community-generated Kodachrome HaldCLUTs are available on:
- GitHub (search: "Kodachrome HaldCLUT")
- RawTherapee forums
- The Film Simulation database (film.photography)

Quality varies widely — these are community contributions without professional calibration.

### Darktable — Film Module

Darktable includes a "color look up table" module and "filmic" tone mapping. Community style files for Kodachrome exist but require manual installation.

---

## Summary Table

| Product | Type | Kodachrome Variants | Pricing | Rating (Community) |
|---|---|---|---|---|
| **RNI All Films 5** | Profile-based presets | K25, K64, K200, K64 Faded | $96-$192 | ★★★★★ |
| **RNI All Films 4** | Adjustment-based presets | K25, K64 | $82-$164 | ★★★★☆ |
| **Alex Ruskman Kodachrome Pack** | DCP + presets | Multiple K64 variants, K25, K200 | ~$25-45 | ★★★★☆ |
| **SilverFast Kodachrome Mode** | Scanner ICC profiles | N/A (for scanning) | $ included in SE Plus+ | ★★★★★ |
| **Dehancer** | Video OFX plugin | K64 | Subscription or perpetual | ★★★★☆ |
| **RNI Films (iOS)** | Mobile app profiles | K64 | Free + IAP | ★★★★☆ |
| **VSCO (discontinued desktop)** | Presets | K64 (historic) | Discontinued | ★★★☆☆ |
| **HaldCLUT (DIY)** | Open-source CLUT files | Varies | Free | ★★☆☆☆ to ★★★★☆ |

---

## Notes on Purchasing

1. **RNI offers a free demo** of All Films 5 with a limited subset of films. Check if Kodachrome is included before purchasing the full pack.
2. **Alex Ruskman's pack** is sold through his personal site. Verify current availability; smaller creators sometimes discontinue products.
3. **Capture One vs. Lightroom** — RNI sells separate licenses. The visual output differs slightly between platforms due to different rendering engines.
4. **All products listed** are third-party; none are officially licensed by Kodak (the Kodachrome trademark is owned by Eastman Kodak).

---

## Sources

- RNI product pages (reallyniceimages.com/store)
- Alex Ruskman website (alexruskman.com)
- SilverFast Kodachrome page (silverfast.com)
- Community reviews: r/Lightroom, r/analog, fredmiranda.com, dpreview.com
- Dehancer product documentation (dehancer.com)
