# Community Lightroom Recipes — ORWO NC 500

---

## Recipe Availability

**No dedicated Fuji X Weekly or t3mujinpack recipes exist for ORWO NC 500.**

This film was released in 2022-2023 and is still very new to the market. No established community Lightroom recipes have been compiled yet. Values must be derived from film characteristics documented in reviews, forum discussions, and scan analysis.

## Derived Values (from Film Characteristic Analysis)

### Approach
ORWO NC 500 has a distinctive color signature that must be reconstructed:
- **Unique color palette**: Terracotta reds, muted teal blues, warm olive greens
- **Halation**: The orange/red highlight bloom is a defining characteristic
- **Warm grain**: Visible grain with warm character
- **European muted palette**: Overall restrained saturation with selective warmth

### Key Derivation Rules
1. **Color palette reconstruction**: Red Hue +15 (toward orange/terracotta), Blue Hue -15 (toward teal), Green Hue +15 (toward olive)
2. **Muted saturation**: Global Sat -10, with selective channel boosts
3. **Warm shadow character**: ColorGrade Shadow Hue 30 (warm brown, not cool)
4. **Orange highlight bloom**: ColorGrade Highlight Hue 25 (orange), Sat 12
5. **Grain**: Visible vintage-style grain — Amount 35, Size 32, Roughness 58
6. **Contrast**: Moderate — +10

### Preset Values
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Contrast | +10 | Moderate contrast |
| Highlights | -25 | Preserve highlight detail for halation effect |
| Shadows | +20 | Lift shadows (ORWO shadow warmth) |
| Whites | 0 | Neutral whites |
| Blacks | -20 | Warm blacks |
| Saturation | -10 | Overall muted palette |
| Vibrance | -5 | Within 5 of Saturation (diff=5) |
| HSL Red Hue | +15 | Toward orange/terracotta |
| HSL Red Sat | -5 | Muted reds |
| HSL Orange Hue | +5 | Warm orange |
| HSL Orange Sat | +10 | Boost orange (terracotta signature) |
| HSL Yellow Hue | -5 | Toward orange |
| HSL Yellow Sat | -5 | Muted yellow |
| HSL Green Hue | +15 | Toward olive |
| HSL Green Sat | -15 | Muted olive greens |
| HSL Green Lum | -5 | Darker foliage |
| HSL Aqua Sat | -10 | Muted aqua |
| HSL Blue Hue | -15 | Toward teal (ORWO sky signature) |
| HSL Blue Sat | -10 | Muted blue |
| HSL Blue Lum | -5 | Slightly darker sky |
| ColorGrade Shadow Hue | 30 | Warm brown shadow |
| ColorGrade Shadow Sat | 10 | Present warm shadow |
| ColorGrade Midtone Hue | 35 | Warm midtone |
| ColorGrade Midtone Sat | 5 | Subtle |
| ColorGrade Highlight Hue | 25 | Orange bloom (halation simulation) |
| ColorGrade Highlight Sat | 12 | Noticeable orange glow |
| Grain Amount | 35 | Prominent grain (ORWO character) |
| Grain Size | 32 | Medium-large grain |
| Grain Roughness | 58 | Visible texture |
| Sharpness | 10 | Grain protection |

## References
- ORWO Wolfen NC 500 official product page
- 35mmc: "Orwo Wolfen NC500 – Pushed a stop" (Matt Murray, 2025-01-03)
- 35mmc: "5 frames with Orwo Wolfen NC500" (Vincent Nguyen, 2024-05-04)
- 35mmc: "Orwo Wolfen NC-500 – A Contrarian's Perspective" (Bob Prendergast, 2024-03-15)
- 35mmc: "Update from Orwo on New Colour C41 Cine Film!" (Molly Kate, 2022-07-11)
- r/analog: NC 500 examples, color analysis threads
- YouTube: grainydays, Kyle McDougall NC 500 reviews

## Community Data Validation

### Validity Assessment: FAIR (Derived)

**Overall Status**: No established community recipes exist. Film is very new (2022+). Values derived from multiple comprehensive reviews, scan analysis, and documented color characteristics. The ORWO palette is distinctive and well-documented in community discussions — terracotta reds, teal blues, olive greens, warm grain, and orange halation are consistently reported.

### Slider Range Check
All derived values within valid ranges per STYLEGUIDE §XV.

### Self-Consistency Check
| Check | Result |
|-------|--------|
| \|Vibrance − Saturation\| ≤ 5 | ✓ (-5 vs -10, diff=5) |
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| HSL Sat ≤ ±60 | ✓ (max +10/-15) |
| HSL Hue ≤ |±100| ✓ (max ±15) |
| Blacks ≥ -30 | ✓ (-20) |
| Color-Negative neutral curve | ✓ |

### Film Stock Behavior Check
| Behavior | Expected | XMP Implementation | Verdict |
|----------|---------|-------------------|---------|
| Terracotta reds | Yes | Red Hue +15, Orange Sat +10 | ✓ |
| Teal-muted blues | Yes | Blue Hue -15, Blue Sat -10 | ✓ |
| Olive greens | Yes | Green Hue +15, Green Sat -15 | ✓ |
| Visible grain | Yes | Grain 35, Size 32, Roughness 58 | ✓ |
| Warm shadows | Yes | Shadow Hue 30, Sat 10 | ✓ |
| Orange halation glow | Yes | Highlight Hue 25, Sat 12 | ✓ |
