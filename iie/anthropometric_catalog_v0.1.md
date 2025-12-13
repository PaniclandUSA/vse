# VSE::ANTHROPOMETRIC_CATALOG
## Human Form Variant Library

**Version:** 0.1 (Framework)  
**Status:** Foundational Structure  
**Parent Spec:** VSE::IDENTITY_FORM_RESOLUTION

---

## Purpose

This catalog provides **named archetypes** for human form selection in VSE applications. Each variant represents a point in anthropometric design space - not a person, but a **typological coordinate**.

---

## Catalog Structure

Each variant includes:

```
⟨VARIANT_ID:unique_identifier⟩
  ⟨catalog:library_name⟩
  ⟨archetype_name:descriptive_label⟩
  
  ⟨PROPORTIONS⟩
    ⟨height_range:min_max_cm⟩
    ⟨shoulder_hip_ratio:numeric⟩
    ⟨limb_proportions:descriptor⟩
  ⟨END_PROPORTIONS⟩
  
  ⟨FACIAL_GEOMETRY⟩
    ⟨jaw_width:descriptor⟩
    ⟨cheekbone_prominence:descriptor⟩
    ⟨nose_bridge:descriptor⟩
    ⟨orbital_spacing:descriptor⟩
  ⟨END_FACIAL_GEOMETRY⟩
  
  ⟨CULTURAL_DESIGN_BIAS⟩
    ⟨influence:archetype_family⟩
    ⟨application:structural_only⟩
  ⟨END_CULTURAL_DESIGN_BIAS⟩
  
  ⟨TYPICAL_APPLICATIONS⟩
    ⟨use_cases:list⟩
  ⟨END_TYPICAL_APPLICATIONS⟩
⟨END_VARIANT_ID⟩
```

---

## Variant Families

### LUXURY_DISPLAY_VARIANTS_V3

High-end fashion mannequin archetypes

**LDV3-A: Classic Elegance**
```
⟨VARIANT_ID:LDV3-A⟩
  ⟨archetype_name:classic_elegance⟩
  
  ⟨PROPORTIONS⟩
    ⟨height_range:175-182cm⟩
    ⟨shoulder_hip_ratio:0.95⟩
    ⟨limb_proportions:elongated_graceful⟩
  ⟨END_PROPORTIONS⟩
  
  ⟨FACIAL_GEOMETRY⟩
    ⟨jaw_width:moderate_refined⟩
    ⟨cheekbone_prominence:subtle_defined⟩
    ⟨nose_bridge:straight_moderate⟩
    ⟨orbital_spacing:balanced⟩
  ⟨END_FACIAL_GEOMETRY⟩
  
  ⟨CULTURAL_DESIGN_BIAS⟩
    ⟨influence:pan_european_fashion_archetype⟩
    ⟨application:proportional_bias_only⟩
  ⟨END_CULTURAL_DESIGN_BIAS⟩
  
  ⟨TYPICAL_APPLICATIONS⟩
    ⟨use_cases:evening_wear_couture_formal_display⟩
  ⟨END_TYPICAL_APPLICATIONS⟩
⟨END_VARIANT_ID⟩
```

**LDV3-B: Athletic Contemporary**
```
⟨VARIANT_ID:LDV3-B⟩
  ⟨archetype_name:athletic_contemporary⟩
  
  ⟨PROPORTIONS⟩
    ⟨height_range:168-175cm⟩
    ⟨shoulder_hip_ratio:1.05⟩
    ⟨limb_proportions:balanced_muscular_suggestion⟩
  ⟨END_PROPORTIONS⟩
  
  ⟨FACIAL_GEOMETRY⟩
    ⟨jaw_width:strong_angular⟩
    ⟨cheekbone_prominence:pronounced⟩
    ⟨nose_bridge:straight_bold⟩
    ⟨orbital_spacing:wide_set⟩
  ⟨END_FACIAL_GEOMETRY⟩
  
  ⟨CULTURAL_DESIGN_BIAS⟩
    ⟨influence:pan_latina_fashion_archetype⟩
    ⟨application:proportional_bias_only⟩
  ⟨END_CULTURAL_DESIGN_BIAS⟩
  
  ⟨TYPICAL_APPLICATIONS⟩
    ⟨use_cases:sportswear_contemporary_casual_streetwear⟩
  ⟨END_TYPICAL_APPLICATIONS⟩
⟨END_VARIANT_ID⟩
```

**LDV3-C: Delicate Minimalist**
```
⟨VARIANT_ID:LDV3-C⟩
  ⟨archetype_name:delicate_minimalist⟩
  
  ⟨PROPORTIONS⟩
    ⟨height_range:165-172cm⟩
    ⟨shoulder_hip_ratio:0.88⟩
    ⟨limb_proportions:slender_refined⟩
  ⟨END_PROPORTIONS⟩
  
  ⟨FACIAL_GEOMETRY⟩
    ⟨jaw_width:narrow_soft⟩
    ⟨cheekbone_prominence:delicate_high⟩
    ⟨nose_bridge:gentle_refined⟩
    ⟨orbital_spacing:close_set⟩
  ⟨END_FACIAL_GEOMETRY⟩
  
  ⟨CULTURAL_DESIGN_BIAS⟩
    ⟨influence:east_asian_fashion_archetype⟩
    ⟨application:proportional_bias_only⟩
  ⟨END_CULTURAL_DESIGN_BIAS⟩
  
  ⟨TYPICAL_APPLICATIONS⟩
    ⟨use_cases:minimalist_fashion_contemporary_asian_markets⟩
  ⟨END_TYPICAL_APPLICATIONS⟩
⟨END_VARIANT_ID⟩
```

---

## Usage in VSE Scripts

```
⟨ANTHROPOMETRIC_SELECTION⟩
  ⟨catalog:LUXURY_DISPLAY_VARIANTS_V3⟩
  ⟨variant:LDV3-B⟩
  ⟨variation:within_specified_range⟩
⟨END_ANTHROPOMETRIC_SELECTION⟩
```

This syntax:
1. ✓ References a catalog (not a person)
2. ✓ Selects from design space
3. ✓ Allows variation within type
4. ✓ Maintains SELECTION MODE semantics

---

## Expansion Framework

### Adding New Variants

When creating new catalog entries:

1. **Never reference source people** - describe geometry abstractly
2. **Use proportional ranges** - not exact measurements
3. **Cultural bias is stylistic** - not ancestral
4. **Name descriptively** - avoid proper names
5. **Test against blacklist** - no derivation verbs

### Planned Variant Families

- **MUSEUM_RECONSTRUCTION_VARIANTS** - Historical period archetypes
- **THEATRICAL_DISPLAY_VARIANTS** - Stage and performance forms
- **MEDICAL_TRAINING_VARIANTS** - Anatomical education forms
- **SCULPTURE_BASE_VARIANTS** - Fine art foundation forms

---

## Relationship to Other Modules

- **VSE::IDENTITY_FORM_RESOLUTION** - Parent specification, defines legal framework
- **VSE::FACIAL_CONSTRUCTION_MODEL** - Provides geometric assembly rules
- **VSE::CULTURAL_FORM_TUNING** - Defines how bias is applied
- **VSE::UNCANNY_CALIBRATION** - Controls realism level per variant

---

## Development Notes

**v0.1** provides:
- Framework structure
- Three example variants
- Usage syntax
- Expansion guidelines

**Future versions will add:**
- 20+ variants across families
- Detailed proportion specifications
- Visual reference guides (generated examples)
- Cross-compatibility matrices
- Era-specific styling overlays

---

**End of Catalog Framework**
