# Reference Packs — Mastin Labs T-Max 3200 & Competitor Breakdown

## Key Finding: No Current Dedicated T-Max 3200 Pack from Mastin Labs

As of May 2026, **Mastin Labs does not offer a dedicated Kodak T-Max 3200 preset pack.** Their current B&W offering is:

### Mastin Labs — Artisan B&W (formerly "Ilford Original")

| Detail | Value |
|---|---|
| **Product name** | Artisan B&W Lightroom Desktop Presets |
| **Price** | $99 MSRP (frequently $49 on sale) |
| **Film presets included** | Pan F, HP5, Delta 3200 |
| **T-Max 3200** | **NOT included** |
| **Platforms** | Lightroom Classic, Lightroom CC, Capture One, Mobile Profiles |
| **Also includes** | Mastin Magic Toolkit (18 AI tools, grain presets, tone profiles) |

### Artisan B&W Preset Breakdown

| Preset | Film Emulated | Character Description (per Mastin) |
|---|---|---|
| **Pan F** | Ilford Pan F Plus (ISO 50) | Rich black and white, moody tones, low grain |
| **HP5** | Ilford HP5 Plus (ISO 400) | Versatile, medium contrast and grain |
| **Delta 3200** | Ilford Delta 3200 (EI 3200) | Glowing highlights, thick expressive grain |

### Why No T-Max 3200 in Mastin Labs?

Possible reasons for the absence:
1. Mastin's B&W line was originally branded "Ilford Original" — they partnered with/emulated Ilford films specifically
2. The rebrand to "Artisan B&W" retained the Ilford portfolio (Pan F, HP5, Delta 3200)
3. Kodak-branded presets may involve licensing/commercial considerations
4. Mastin Labs' color presets focus on Fuji and Kodak color films (Portra, Fuji 400H, etc.) — their B&W strategy favored the Ilford ecosystem

### Historical Note

There is **no evidence** that Mastin Labs ever sold a standalone "T-Max 3200" pack, either under that name or under a broader Kodak B&W pack. The Mastin B&W line has been Ilford-focused since inception. If a "T-Max 3200 pack" existed from Mastin, it may have been:
- A very early limited release (pre-2019)
- A custom profile within another pack
- Confused with another vendor's offering

---

## Competitor & Alternative T-Max 3200 Presets

### 1. RNI Films (Really Nice Images)
| Detail | Value |
|---|---|
| **Product** | RNI All Films 5 / RNI BW Films |
| **Includes T-Max 3200?** | RNI BW Films includes Kodak T-Max 3200 profile |
| **Platform** | Lightroom, Capture One, ACR |
| **Approach** | Lab-scanned reference film profiles |

**RNI Kodak T-Max 3200 profiles include:**
- T-Max 3200 (normal)
- T-Max 3200 (pushed +1)
- T-Max 3200 (pushed +2)
- T-Max 3200 (expired)
- Often includes grain as part of the profile

### 2. Nik Silver Efex Pro (DxO)
| Detail | Value |
|---|---|
| **Product** | Nik Collection — Silver Efex Pro |
| **Includes T-Max 3200?** | Yes — built-in film type selector |
| **Platform** | Photoshop, Lightroom (plugin), standalone |
| **Approach** | Grain + tone curve simulation |

Silver Efex Pro includes **Kodak T-Max 3200** as a selectable film type in the "Film Types" dropdown. It adjusts:
- Tonal response curve
- Grain structure (amount, size, hardness)
- Spectral sensitivity approximation
- Adjustable "Grain per ISO" slider to simulate different EI ratings

### 3. Dehancer
| Detail | Value |
|---|---|
| **Product** | Dehancer Film Plugin |
| **Includes T-Max 3200?** | **No** — only T-Max 100 and T-Max 400 |
| **Workaround** | Use T-Max 400 + push/grain adjustments |
| **Platform** | Lightroom Classic, Photoshop, DaVinci Resolve |

### 4. FilmConvert / CineMatch
| Detail | Value |
|---|---|
| **Product** | FilmConvert Nitrate |
| **Includes T-Max 3200?** | **No** — Kodak B&W limited to T-Max 100/400, Tri-X |
| **Platform** | Premiere Pro, DaVinci, Final Cut, Photoshop |

### 5. VSCO (Discontinued)
| Detail | Value |
|---|---|
| **Product** | VSCO Film 01–07 (discontinued 2019) |
| **Includes T-Max 3200?** | **Yes** — VSCO Film 01 (B&W) included a T-Max 3200 preset |
| **Status** | No longer sold; existing owners can still use |
| **Character** | VSCO's T-Max 3200 was known for heavy, crisp grain and high contrast |

### 6. Mastin Labs Alternatives for T-Max 3200 Aesthetic

If using Mastin Labs specifically, the closest approximation within their ecosystem:

#### Option A: Artisan B&W — Delta 3200 with Adjustments
- Start with Mastin Delta 3200 preset
- Increase contrast (+15 to +25)
- Change grain setting to a sharper profile (use a 35mm grain preset and increase roughness)
- Adjust B&W mix toward red sensitivity (+15 red, +10 orange)
- Clone/heal settings from a reference T-Max 3200 scan

#### Option B: Mastin Magic Toolkit Workaround
- Use a neutral base
- Apply "Dark & Moody Assist" AI tool
- Layer grain from 35mm grain preset at higher roughness
- Custom tone curve to mimic TMZ push characteristics

---

## Detailed RNI T-Max 3200 Profile Reference

RNI BW Films (v5) is the most comprehensive commercially available T-Max 3200 preset. Their approach:

### RNI T-Max 3200 — What's In the Profile
- **Base curve:** Modeled from drum-scanned TMZ negatives developed in XTOL
- **Grain:** Texture-based grain emulation (not simple noise overlay)
- **Spectral mapping:** Camera-specific B&W conversion that accounts for T-Max's extended red sensitivity
- **Push variants:** Different curve/contrast profiles for different EIs
- **Fade profiles:** "Expired" and "vintage" variants with adjusted fog + contrast

### Strengths
- Highly accurate to lab-scanned reference
- Push variants cover the full EI range
- Camera profiling improves consistency across sensors

### Weaknesses
- No native grain amount slider (grain is baked into profile intensity)
- Profiles can be heavy-handed — less flexible than manual approach
- Pricing: Premium product, not subscription-based

---

## DIY T-Max 3200 Preset Building Checklist

For users who want to build their own preset from scratch (in Lightroom or Capture One):

### Step-by-Step T-Max 3200 Reference Build

1. **Start with neutral B&W conversion** (zeroed B&W mix)
2. **Set spectral response:**
   - Reds: +15 to +25
   - Orange: +10 to +20
   - Blue: -15 to -30
   - (Adjust per reference scan)
3. **Set contrast curve:**
   - Point curve: Medium to Strong Contrast
   - Blacks: -30, Shadows: -20, Highlights: -15
4. **Add grain:**
   - Amount: 50, Size: 40, Roughness: 65
   - (Increase amount/size for higher EI, increase roughness for T-grain character)
5. **Fine-tune:**
   - Clarity: +10 to +15 (T-grain acutance)
   - Dehaze: +5 to +10 (midtone snap)
   - Vignette: -10 post-crop
6. **Test and iterate:**
   - Test on faces (check skin tone rendering)
   - Test on landscapes (check sky/foliage balance)
   - Test on low-light images (where TMZ is actually used)

---

## Reference Image Sources for T-Max 3200

For building or validating presets, refer to these sources for authentic T-Max 3200 scans:

1. **Flickr:** Search "Kodak T-Max 3200" + developer name (e.g., "XTOL", "D-76")
2. **r/analog on Reddit:** Filter by "T-Max 3200" or "TMZ" flair — many posts include development notes
3. **Lomography community:** Tag "kodak-tmax-3200"
4. **FilmDev account (community dev resource):** Aggregated scan results by film + developer combination
5. **Richard Photo Lab / Carmencita Film Lab / Indie Film Lab:** Lab scans visible on their blogs/social media

---

## Summary Table: Where to Get T-Max 3200 Presets

| Provider | Dedicated TMZ 3200? | Quality | Price | Notes |
|---|---|---|---|---|
| **RNI Films** | Yes (BW Films pack) | High | $$$ | Best commercial option |
| **Nik Silver Efex** | Yes (built-in) | High | $$$ | Part of Nik Collection |
| **VSCO** | Yes (Film 01, discontinued) | High | N/A | No longer available |
| **Mastin Labs** | No | — | — | Delta 3200 only |
| **Dehancer** | No (T-Max 100/400 only) | — | — | Use 400 + push |
| **FilmConvert** | No | — | — | Use Tri-X or T-Max 400 |
| **DIY (Lightroom)** | Build your own | Variable | Free | Research required |

---

## Sources

- MastinLabs.com — Artisan B&W product page (accessed May 2026)
- RNI Films product documentation
- Nik Collection by DxO — Silver Efex Pro documentation
- VSCO Film legacy documentation / Internet Archive
- Dehancer and FilmConvert film lists
- Community discussion on Photrio, Reddit r/Lightroom, r/analog
