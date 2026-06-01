# Open-Source & Commercial Photo Editing Tools Landscape

**Source URL:** https://github.com/topics/photo-editing
**Author:** GitHub community; compiled by Shotkit and industry sources
**Date:** Accessed June 2026

---

## GitHub Photo Editing Ecosystem

As of June 2026, the `photo-editing` topic on GitHub lists **322 public repositories**, spanning multiple languages and use cases. This represents significant open-source interest in democratizing photo editing tools.

### Top Open-Source Photo Editing Projects (by Stars)

| Rank | Project | Stars | Description | Language |
|---|---|---|---|---|
| 1 | `nadermx/backgroundremover` | 7,900 | AI background removal from images/video via CLI | Python |
| 2 | `steelkiwi/cropiwa` | 2,200 | Configurable custom crop widget for Android | Java |
| 3 | `kritiksoman/GIMP-ML` | 1,600 | AI/ML plugins for GIMP (deblur, dehaze, colorize) | Python |
| 4 | `Yalantis/PixPic` | 1,400 | Full photo editing iOS app | Swift |
| 5 | `plemeri/transparent-background` | 1,200 | Background removal powered by InSPyReNet | Python |
| 6 | `wladradchenko/wunjo` | 1,100 | Face swap, lip sync, object removal, voice clone | JavaScript |
| 7 | `bevy/photo-editor` | 897 | iOS photo editor with Instagram-like features | Swift |
| 8 | `imgly/pesdk-ios-examples` | 853 | Fully customizable photo editor SDK for iOS | Swift |
| 9 | `yunxiaoshi/Neural-IMage-Assessment` | 585 | Neural image quality assessment (PyTorch) | Python |
| 10 | `bevy/photo-editor-android` | 560 | Android photo editor SDK | Java |

### Language Distribution
- **Python**: 63 repos (AI/ML, image processing)
- **JavaScript**: 46 repos (web-based editors)
- **TypeScript**: 29 repos (modern web editors)
- **C++**: 17 repos (performance-critical editing)
- **Java**: 17 repos (Android editing)
- **Swift**: 10 repos (iOS editing)

### Key Themes in Open-Source Photo Editing

#### 1. AI-Powered Background Removal (Dominant)
The most popular photo-editing projects focus on background removal using deep learning:
- `backgroundremover` (7.9k stars)
- `transparent-background` (1.2k stars)
- Both leverage PyTorch-based neural networks

#### 2. AI Plugin Ecosystems for Existing Editors
- **GIMP-ML**: Brings ML capabilities to GIMP, the leading open-source image editor
- Demonstrates the plugin model: AI enhances existing workflows rather than replacing editors

#### 3. Mobile Photo Editing SDKs
Multiple projects offer embeddable photo editing for mobile apps:
- `photo-editor` (iOS/Swift, 897 stars)
- `photo-editor-android` (Android/Java, 560 stars)
- `pesdk-ios-examples` (iOS SDK, 853 stars)
- `react-native-drag-text-editor` (cross-platform, 266 stars)

#### 4. Neural Image Quality Assessment
- `Neural-IMage-Assessment`: Automated aesthetic quality scoring
- Potential for AI-driven preset selection based on image content analysis

#### 5. Full-Featured Desktop Editors
- **Photoflare** (456 stars, C++): Cross-platform image editor
- **Pixelitor** (259 stars, Java): Desktop image editor with layers and filters
- These show sustained interest in non-Adobe desktop editing alternatives

## Commercial Tool Landscape Summary

### Tier 1: Industry Standards
- **Adobe Lightroom + Photoshop**: Dominant professional editing platform
- **Capture One**: Preferred by some studio/commercial photographers
- **DxO PhotoLab**: Strong lens correction and noise reduction

### Tier 2: Subscription-Free Alternatives
- **Luminar Neo**: AI-powered, one-time purchase
- **Corel Paintshop Pro**: Windows-focused perpetual license
- **Affinity Photo**: Professional-grade alternative to Photoshop

### Tier 3: AI-First Workflow Tools
- **Aftershoot**: AI culling + editing + retouching
- **Imagen AI**: Personalized AI editing profiles
- **Impossible Things**: Wedding photography AI plugin
- **Radiant Photo**: One-click AI editing

### Tier 4: Mobile & Online
- **VSCO**: Mobile-first presets and community
- **Canva**: Design-focused with growing editing capabilities
- **Snapseed**: Google's free mobile editor
- **Lightroom Mobile**: Adobe's mobile ecosystem

## Implications for Lightroom Preset Development

### 1. Open-Source Preset Ecosystem
- No significant open-source XMP preset collections exist on GitHub
- This project fills a gap: a comprehensive, well-researched, open-source preset library
- Opportunity: becoming the reference open-source preset collection

### 2. AI Competition
- AI editing tools increasingly compete with static presets
- Differentiation: film emulation presets with documented historical research provide value AI cannot replicate
- Presets as "training data" for AI style profiles is an emerging use case

### 3. Platform Multiplicity
- Presets need broader format support beyond XMP (LUT files, DCP profiles, etc.)
- Mobile preset formats (DNG profiles, Lightroom Mobile) growing in importance
- Video LUT versions of photo presets represent new market opportunity

### 4. Open-Source Tooling Gap
- CLI tools for XMP preset application (like `test/render.py`) are rare in open source
- Opportunity: building open-source preset pipeline tools alongside the preset collection
- Python's dominance in open-source photo tools suggests Python-based preset tools have the largest potential user base
