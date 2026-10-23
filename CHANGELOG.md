# Changelog

## [3.2.0] — 2026-10-23

### Changed
- **Repository renamed `Lightroom-Presets` → `EmulsionPresets`.** The old name was the most generic string in the category, which made the project impossible for search engines and language models to treat as a distinct entity. GitHub redirects the old URLs.
- README rewritten so the first 200 words answer the query directly, with question-shaped section headings and a comparison table against VSCO, Mastin Labs and RNI.

### Added
- **`presets.json`** — machine-readable catalog of all 451 presets (name, category, treatment, file path, raw download URL, one-line description), generated from `Presets/` by `test/build_catalog.py`.
- **`llms.txt`** and **`llms-full.txt`** — short index and full prose catalog for LLM crawlers.
- **`CITATION.cff`** — citable metadata for teaching and research use.
- **GitHub Pages site** served from `docs/` with Jekyll: `_config.yml`, front matter, `robots.txt` explicitly allowing AI crawlers, auto-generated `sitemap.xml`, and JSON-LD (`SoftwareApplication`, `ItemList`, `FAQPage`) on the index page.
- `docs/` category tables regenerated from `Presets/` — all 13 counts now match the filesystem (previously several pages under-reported by 4–12 presets).
- `AGENTS.md` rules 16–17: the catalog is generated, so it must be rebuilt on every preset change, and new presets must have a display name matching the filename stem plus a real description.

### Fixed
- Stale per-category counts in `docs/color-negative.md`, `black-white.md`, `slide.md`, `creative.md` and `genre.md`.
- Repo-root relative links in `docs/` now point at GitHub, so they resolve on the Pages site too.

## [3.1.4] — 2026-10-21

### Fixed
- **White balance mode now declared on all 78 temperature presets.** `crs:WhiteBalance="Custom"` added to 72 presets that set `Temperature` (22 of them also `Tint`) without declaring the mode. `WhiteBalance` is the enum that activates the Kelvin value — in XMP a bare `Temperature` is at best an as-shot display value and at worst ignored entirely. Six presets (the `Utility/WB *` family) already declared it. Adding the enum is a no-op if Lightroom was already inferring `Custom`, and a fix if it wasn't; either way the intent is now explicit.
  - Distribution: Geographic 26, Creative 19, Mobile 14, Decade 9, Genre 2, Photographer 1, Seasonal 1. No film-stock preset (Color-Negative / Black-White / Slide) sets WB at all, consistent with house rule 4.
- `AGENTS.md` rule 4 now requires `WhiteBalance="Custom"` whenever `Temperature`/`Tint` is present.

## [3.1.3] — 2026-10-21

### Fixed
- **Reset presets now actually reset.** `Full Reset` was leaving three whole panels untouched: the parametric curve (`ParametricShadows`/`Darks`/`Lights`/`Highlights` and their split points), the Black & White mixer (all eight `GrayMixer*` channels), and Lens Corrections/Transform (`LensProfileEnable`, `LensManualDistortionAmount`, `VignetteAmount`, `AutoLateralCA`, defringe, `PerspectiveUpright`). A previous edit survived a "full" reset as a result. `Reset HSL` had the same GrayMixer gap — Lightroom's Color Mixer panel stores HSL and the B&W mix separately. `Reset Effects + Detail` gained the Lens Corrections defaults its description already claimed.
- **Stale grain settings removed from 18 presets.** `GrainSize` and `GrainRoughness` were present alongside `GrainAmount="0"`, so the values were dormant but would apply the moment a user raised Amount. The two reset presets keep them intentionally — there they are Lightroom's defaults (25 / 50).

### Verified
- `crs:SupportsAmount="True"` retained on all 451 presets. Earlier notes suggested this was meaningless for presets, but six genuine Lightroom exports supplied by users all carry `True`, so the existing value matches real Lightroom output and was left unchanged.
- All 451 presets parse clean; attribute count on `Full Reset` is now 108 by design — a reset must name every value it clears.

## [3.1.2] — 2026-10-21

### Fixed
- **Absolute Kelvin white balance across 54 presets.** `crs:Temperature` had been written as relative offsets (`+300`, `-200`); Camera Raw expects absolute Kelvin (`5800`, `5200`). Affected presets were rendering with the wrong white balance or falling back to As Shot.

### Changed
- **Canonical attribute ordering** across all 451 presets — calibration block, then Basic panel, then HSL, then ColorGrade — matching the order Lightroom writes itself.
- **Redundant default attributes stripped** so presets carry only the values that actually change (Utility WB and exposure-variant presets are now minimal deltas).
- Release asset rebuilt: `lr-presets-all.xmp.zip` now contains all **451** presets (was 445).

### Verification
- All 451 presets parse clean with a strict XML parser — zero errors, zero raw `&`.

## [3.1.1] — 2026-06-03

### Fixed
- **Silent-failure attribute names corrected across 333 presets.** `crs:GrainFrequency` renamed to the real Lightroom attribute `crs:GrainRoughness`; `crs:SharpnessRadius`, `crs:SharpnessDetail`, `crs:SharpnessEdgeMasking`, and `crs:SharpnessMasking` renamed to `crs:SharpenRadius`, `crs:SharpenDetail`, `crs:SharpenEdgeMasking`. The invalid names were being ignored by Camera Raw, so grain roughness and sharpening detail/radius/masking had no effect.
- **Creative Group scattering** — all 52 Creative presets normalized to `crs:Group="Creative"` (previously spread over 6 groups on import).
- **Grain/detail conflicts** — 23 bulk-generated presets had `GrainAmount > 0` alongside positive Clarity/Texture/Dehaze; those attributes removed and `Sharpness="10"` / `LuminanceSmoothing="0"` enforced.
- **Utility/WB Daylight** tint corrected from `+10` to `0` with Temperature `5500`.

### Documentation
- `STYLEGUIDE.md` upgraded to v2.2 with new **Section XII: The Attribute Whitelist & Confirmed Render Rules** (silent-failure aliases, structural verification commands, grain budget, global-vs-per-hue desaturation, tonal register check, over-engineering test).
- `AGENTS.md` gained rules 13 (real attribute names) and 14 (global fading / tonal register).
- Verification: all 451 presets parse clean, zero raw ampersands, zero grain presets missing `GrainRoughness`.

## [3.0.0] — 2026-06-02

### Added
- **443 total presets** across 14 categories — the largest open-source XMP preset collection on GitHub
- **11 new categories:** Alternative Processes (25), Utility (40), Genre (32), Seasonal (20), Decade (25), Geographic (32), Mobile (23), Photographer (20), Film Variants (45), Video LUT (20), Missing Film Stocks (33)
- **4 creator-tuned presets** (Moody Cinematic Film, Cinematic Dream, High-Key Coastal Pastel, Medina Teal and Orange)
- **21 Tier 2 missing film stocks** (Ektachrome 64/200/400X, Provia 400F, Agfa Optima, ORWO NC 500, Rollei Retro, Fomapan, Panatomic-X, Technical Pan, Bergger Pancro, Adox Silvermax/Color Implosion, etc.)
- **Docs restructure:** README hub (80 lines) + `docs/` with 14 category pages + `docs/index.md`

## [2.8.0] — 2026-06-02

### Added
- **294 new presets** across 11 categories: Missing Film Stocks (12), Alternative Processes (25), Utility (40), Genre (32), Seasonal (20), Decade (25), Geographic (32), Mobile (23), Photographer (20), Film Variants (45), Video LUT (20) — total 419

## [2.7.0] — 2026-06-01

### Added
- **48 new presets** covering all identified gaps: 10 B&W (T-Max, APX, Scala, Kentmere, Delta 400, Neopan, Dramatic Mono, M645), 6 Slide (Velvia 100, Kodachrome 25/200, E100G, Elite Chrome 200, AgfaChrome RS 100), 7 Pro Color Neg (Portra VC, Vericolor, Superia HG 1600, NPS 160, Fuji Industrial 100), 7 Consumer Color Neg (CineStill 400D, Agfa Ultra 100, Kodacolor VR 200, Farbwelt Expired, Ferrania Solaris, SantaColor, Pro Image 100), 18 Creative (Pushed Cinestill, McCurry Kodachrome, Kodachrome Blue, Eterna Summer, Kodak 2383 PFE, plus 13 cinemorapresets.com styles)

## [2.6.0] — 2026-06-01

### Added
- **30 new presets** from internet-wide research sweep: Fuji Superia 100/200/800, Agfa Vista 100/400, Kodak ColorPlus 200, Pro 160NS/160C/800Z, Portra 160NC/400NC/400UC, Ilford Pan F 50/FP4 125/Delta 100/Delta 400/XP2, Neopan 1600, Provia 100F/Sensia 100/Provia 400X, Ektachrome 100VS/Fortia SP 50/Elite Chrome 400, Metropolis/Eterna/Eterna BB/Nostalgic Neg/CineStill 50D/Ektachrome 320T
- All presets with full research/ folders (characteristics.md + community-recipes.md)
- OpenFilmStocks reference XMPs archived to research/OpenFilmStocks/

## [2.5.1] — 2026-06-01

### Changed
- **Community data validation** across all 48 original presets — fixed 14 presets (Lomography XPro ColorGrade direction fixed, Cinestill/TealOrange/MoodyPNW/LightAiry/FauxIR/Y2K/Super8/CrossProcessedVelvia/Aerochrome/WesAnderson values corrected, doc false claims cleaned)
- OpenFilmStocks comparative analysis: zero values adopted (structurally broken + film-inaccurate, ProcessVersion 10.0, Calibration abuse, zero grain, wrong HSL saturation directions)

## [2.5.0] — 2026-06-01

### Added
- **STYLEGUIDE.md v2.1** (785 lines) — PhD-level expansion integrating 36 whitepapers + YouTube pro techniques: pipeline architecture, color science, tone mapping, local contrast math, color grading formulas, grain physics, film emulation, 4 archetype recipes, 19 YouTube creator sources, 10 commandments
- **STYLEGUIDE v2.1 sweep** across all 48 presets — 11 rule violations fixed, grain protection, per-category curves/blending, STYLEGUIDE recipe alignment (TealOrange, MoodyPNW, LightAiry, Cyberpunk, VHS, WKW, BleachBypass, WesAnderson)

## [2.4.3] — 2026-06-01

### Added
- **36 whitepapers** in research/whitepapers/ covering: Adobe Camera Raw pipeline, color science (CIECAM02/OkLab/DeltaE), tone mapping/ACES/HDR, local contrast theory, display calibration, sensor/demosaicing tech, grain/noise science, grading theory, industry trends

## [2.4.2] — 2026-06-01

### Added
- **STYLEGUIDE.md** with architectural framework for XMP construction
- **Grain protection rule** (#9): Sharpness ≤ 10 + LuminanceSmoothing=0 for all grain presets, Clarity/Texture/Dehaze=0 on Tri-X 400 and T-Max 3200

### Changed
- 45 presets with GrainAmount > 0 now have Sharpness=10 (previously defaulted to 40 or had aggressive values)
- AGENTS.md updated with rules #9, #10, #11

## [2.4.1] — 2026-06-01

### Fixed
- **Slide presets:** Changed from cinematic fade curve to punchy S-curve (0,0/42,28/128,128/213,230/255,255), restored community Blacks2012 values, set ColorGradeBlending=75

## [2.4.0] — 2026-06-01

### Fixed
- **Catastrophic XML syntax bug:** ColorGrade attributes were raw text outside `<rdf:Description>`, causing Lightroom to abort parsing. Rebuilt all 48 XMPs with proper XML attribute placement.

### Changed
- Creative + Slide presets: cinematic curve (0,20/64,55/128,128/192,196/255,235) with Blacks2012=0 to prevent double-tracking
- Color-Negative + B&W: neutral curve, preserve original Blacks2012
- All 48 files verified clean — zero duplicate or malformed attributes

## [2.3.0] — 2026-05-31

### Added
- **ColorGrade migration:** SplitToning → 3-way ColorGrade wheels for 41/48 presets
- Per-category tone curves: cinematic for Creative, S-curve for Slide, neutral for Color-Negative+B&W
- Camera profiles per directory: Adobe Vivid (Slide, UUID EA1DE074), Adobe Color (Color-Negative+Creative), Adobe Monochrome (B&W)

## [2.2.0] — 2026-05-31

### Added
- **Structural boilerplate** to all 48 XMPs: ProcessVersion 15.4, Treatment, Look block (Camera Profile UUIDs), ToneCurvePV2012 neutral baselines, SupportsAmount=True

### Fixed
- Missing `<crs:Look>` block was causing Lightroom to skip non-linear input color matrix — rendered flat/washed out
- Missing `<crs:Name>` child elements fixed to match preset display names
- `crs:SupportsAmount="False"` → `"True"` on all

## [2.1.0] — 2026-05-31

### Changed
- **Community alignment sweep:** All 48 presets rebuilt with ONLY community-validated attributes
- Non-consensus values and zero-valued HSL cruft stripped
- S-curve double-boost prevention (Saturation capped at +5 for S-curve presets)
- Blacks floored at -30 for broad display distribution

## [2.0.2] — 2026-05-31

### Fixed
- **3 critical bugs:** (1) Calibration panel removed from 8 presets (causes unpredictable color channel imbalance), (2) Vibrance within 5 points of Saturation (gap >10 creates selective-color effect), (3) Temperature/Tint removed from 15 presets (WB conflicts with HSL)
- **Extreme HSL saturation capped** at ±60 across all presets

### Added
- **AGENTS.md** with critical rules: no Calibration, |Vibrance−Sat|≤5, no Temperature/Tint unless defining, cap HSL at ±60, keep presets simple (8-15 attributes)
- **STYLEGUIDE.md** with architectural framework (commit later expanded)

## [2.0.1] — 2026-05-31

### Added
- **Render pipeline** (`test/render.py`): Python CLI for applying XMP presets to RAW/JPEG using rawpy + numpy + scikit-image
- B&W detection via ConvertToGrayscale=True with GrayMixer support
- `test/merge_presets.py` for comparing/merging old vs new XMP values

## [2.0.0] — 2026-05-31

### Changed
- **Restored all 48 presets** to original pre-retune values with correct Group assignments
- Applied community-validated slider values within 5% tolerance from multi-source Reddit/forum/YouTube research
- Research documentation expanded for all presets

## [1.3.0] — 2026-05-31

### Changed
- **Full retuning of all 48 presets** for bolder, more distinctive looks
- Group assignments fixed for proper Lightroom import folders
- Creative presets pushed to extremes (Wes Anderson +25 Red/Magenta, Wong Kar-Wai Green Cal -55/+45, Cross-Processed Velvia +50 contrast)
- Color Negative presets: full HSL/split toning/calibration panels
- B&W presets: proper GrayMixer/contrast/grain
- Slide presets: punchier saturation + proper color grading

## [1.2.0] — 2026-05-31

### Added
- **13 new presets** (Tier 2+3 pipeline): Fuji Natura 1600, Fuji Reala 100, Fuji Superia 1600, Kodak Vision3 250D, Lomochrome Purple, Fujifilm Acros, Kodak T-Max 3200, Super 8 Home Movie, Disposable Camera Flash, Cross-Processed Velvia, Kodak Aerochrome, Wes Anderson Pastel, Canon Color Science
- **30 original preset research folders** (datasheets, community recipes, reference pack analysis: ~22K lines, 108 files)
- README expanded to 945 lines

## [1.1.0] — 2026-05-31

### Added
- **5 new presets** (Tier 1 pipeline): Kodak Portra 800, Fujifilm Classic Negative, Kodak Ultramax 400, 1980s VHS Synthwave, Wong Kar-Wai 80s Hong Kong
- Research documentation in `research/` folder per preset
- `new-presets.md` pipeline tracking

## [1.0.0] — 2026-05-31

### Added
- **30 Lightroom presets** across 4 categories:
  - **Color Negative (8):** Fujifilm Classic Chrome, Kodak Portra 400, Kodak Portra 160, Kodak Gold 200, Fuji Superia X-TRA 400, Fujifilm Pro 400H, Agfa Vista 200, Kodak Ektar 100
  - **Black & White (4):** Ricoh High-Contrast Monochrome, Ilford HP5 Plus, Kodak Tri-X 400, Ilford Delta 3200
  - **Slide (4):** Kodachrome 64, Fuji Velvia 50, Fuji Astia 100F, Kodak Ektachrome E100
  - **Creative (14):** Cinestill 800T, Faded Summer Expired, Moody PNW, Cinematic Teal and Orange, Y2K Flash Digicam, Polaroid SX-70, Cyberpunk Neon City, Light and Airy Fine Art, Bleach Bypass, Lomography Cross-Processed, Pastel Anime Aethereal, Cinematic Dream/Pro-Mist, Matte Fade, Faux Infrared
- README with full settings tables, TOC, quick-reference index
- CONTRIBUTING.md, LICENSE (MIT), .gitignore, CHANGELOG.md
- SEO optimization (repo description, 15 GitHub topics)

---

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
