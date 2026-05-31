# Fuji Natura 1600 — Reference & Emulation Packs

## Mastin Labs Fuji Natura 1600 Preset Pack

### Status: DISCONTINUED

Mastin Labs produced a dedicated **Fuji Natura 1600 Lightroom Preset Pack** as part of their earlier product line. This was separate from their "Fuji Original" and "Fuji Pro" packs.

**What's known about the pack:**
- Included multiple variants (likely: Standard, Hard, Soft, and maybe B&W versions)
- Based on actual scans of Natura 1600 negatives, profiled to Frontoor and Noritsu scanner output
- Used Mastin's proprietary tone curve mapping from film to digital profiles
- Part of Mastin's earlier "film-specific" approach before they consolidated into broader "Original/Pro/Adventure" packs

**Current status:**
- The pack has been removed from mastinlabs.com (returns 404)
- Not available for purchase since Mastin restructured their product line (~2023)
- Existing owners who purchased before retirement may still have access
- The Wayback Machine/Archive.org does not have a cached copy of the product page

### Where to find it now:

**Official channels**: None. Discontinued.

**Secondary market**: Occasionally mentioned in preset trading communities and forums. Use caution — these are copyrighted commercial products.

**Mastin Labs current offerings** (as of 2026) that are closest:
- **Fuji Original** — Based on Fuji 400H, not Natura 1600. Warmer, more pastel.
- **Portra 800** — Different manufacturer but similar speed class. Warmer than Natura.

### Why Mastin discontinued it:

Mastin Labs simplified their product line from many individual film-specific packs to a smaller number of broader packs. Lesser-known/discontinued film stocks were the first to go. Natura 1600 was niche even when available — a Japan-only film with a cult following, not mass-market recognition.

---

## Other Commercial Preset Packs

### VSCO Film (Discontinued)
- VSCO's film packs included Fuji 1600 profiles (possibly based on Superia 1600 or Natura)
- VSCO exited the preset market entirely; packs no longer sold
- The VSCO 00–07 packs that included film profiles are now abandonware

### RNI (Really Nice Images) — Partial
- RNI's "All Films 5" pack includes Fuji Superia profiles
- No dedicated Natura 1600 profile, but Superia 1600C / 1600N variants may exist in their library
- Available as of 2026

### Cobalt Image
- Fuji film profiles available for Capture One and Lightroom
- No dedicated Natura 1600 profile confirmed
- Closest: Superia 1600 profile (if available)

### Dehancer
- Film grain and color emulation plugin (DaVinci Resolve, Photoshop, Lightroom)
- Does NOT include Natura 1600 specifically
- Includes Fuji Superia 800 and Fujicolor Pro 400H

---

## Free / Community Profiles

### No dedicated Natura 1600 profiles found from these sources:
- Fuji X Weekly (Fujifilm digital camera recipes) — no Natura 1600 recipe
- Preset galleries (PresetLove, FilterGrade, etc.) — none specific to Natura 1600
- r/LightroomPresets — no Natura 1600 shared

### DIY Approach (community discussion on r/AnalogCommunity)
Some users have discussed building custom camera calibration profiles by:
1. Scanning actual Natura 1600 negatives on calibrated scanners
2. Shooting a color chart (X-Rite ColorChecker) on both Natura 1600 and digital
3. Using Adobe DNG Profile Editor to match the digital profile to the film scan
4. This is labor-intensive and requires owning/access to Natura 1600 negatives

---

## YouTube & Video References

### "Extinct Emulsions: Fujifilm Natura/Superia 1600"
- Channel: grainydays (Jason Kummerfeldt) — former channel name was different
- Posted to r/AnalogCommunity by u/XieXun, Nov 2018
- URL: https://www.youtube.com/watch?v=mOyMaSNP2KU
- One of the earliest video retrospectives on Natura 1600 after discontinuation

### Flickr
- Search: "Fuji Natura 1600" — 17,000+ photos as of 2026
- URL: https://www.flickr.com/search/?text=fuji+natura+1600
- Excellent visual reference for the film's color signature across different lighting conditions

### Reddit r/analog
- Search: "Natura 1600" sorted by Top — dozens of high-quality examples
- Top post: "Valhalla" (Nikon FE, double exposure) — 3,324 points
- Second: "Nana Banana" (Fuji Natura Black camera, Superia 1600) — 3,103 points
- Third: "Konica Hexar AF | South Korea" — 2,820 points
- Provides the best cross-section of what the film actually looked like in users' hands

---

## Recommendations for Building Your Own Emulation

1. **Reference library**: Download high-resolution Natura 1600 scans from Flickr and r/analog. Focus on:
   - Night street photography (the film's strongest use case)
   - Portraits under mixed artificial light
   - Daylight shots at EI 400 (to see the overexposed palette)

2. **Base profile**: Start from a neutral/"flat" camera profile, not a baked-in Fuji simulation. The Fuji digital simulations (Classic Neg, etc.) impose their own color shifts that interfere with matching.

3. **Key targets to match**:
   - Skin tones under sodium vapor / warm street lights (the hardest thing to get right digitally)
   - Blue-channel behavior (the cool-neutral sky shift)
   - Shadow color — Natura shadows have subtle color information, not pure black or muddy brown
   - Highlight roll-off on point light sources
