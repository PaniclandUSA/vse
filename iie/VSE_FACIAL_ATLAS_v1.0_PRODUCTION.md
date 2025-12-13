# VSE::FACIAL_ATLAS
## Comprehensive Facial Topography Specification System

**Category:** Identity Integration Semantics (IIS)  
**Version:** 1.0  
**Status:** Core Specification  
**Prerequisite:** VSE::IDENTITY_FORM_RESOLUTION

---

## Purpose

This atlas provides the semantic architecture to specify human faces with **recognition-level precision** while maintaining ontological separation from portraiture. It enables the creation of individually distinctive sculptural faces that would be recognizable at close-familiarity level, yet remain safely within artifact character boundaries.

---

## ⚠️ SELECTION MODE GUARANTEE

**All specifications in VSE::FACIAL_ATLAS operate exclusively in SELECTION MODE.**

No values, ratios, or asymmetries may be interpreted as captured, preserved, derived, or transferred from any real person.

All geometry exists as a constructed design-space specification.

This atlas inherits all safety constraints from VSE::IDENTITY_FORM_RESOLUTION.

---

### The Innovation

Traditional sculpture works iteratively: material → refinement → recognition.  
VSE::FACIAL_ATLAS reverses this: specification → recognition → material.

**Complete the sculptural vision in language before any material commitment.**

---

## The Recognition Standard

**Close-Familiarity Recognition** requires specification of:

1. **Proportional relationships** - Not absolute sizes, but precise ratios
2. **Characteristic asymmetries** - The slight variations that create uniqueness  
3. **Micro-feature composition** - How specific elements integrate
4. **Gestalt coherence** - The recognizable whole beyond individual parts

This atlas provides semantic controls for all four levels.

---

## Foundational Principles

### De-Identification Ceiling

**At least ONE of the following must be enforced in every facial specification:**

- `⟨expression:neutral_timeless_unreadable⟩`
- `⟨micro_skin_features:omitted⟩`
- `⟨surface_texture:non_biological_uniform⟩`
- `⟨eye_behavior:non_perceptive_artificial⟩`

**No specification may exceed the de-identification ceiling across all dimensions.**

This preserves recognition without identity. Pushing every parameter to maximum biological realism violates the artifact character boundary.

---

### Coordinate System

All measurements reference the **Frankfurt Horizontal Plane**:
- Infraorbital rim and superior external auditory meatus define horizontal
- Midsagittal plane defines bilateral symmetry axis
- Anterior-posterior depth measured from facial plane

### Measurement Units

- **Linear dimensions:** millimeters (mm)
- **Angular measurements:** degrees (°)
- **Ratios:** decimal to three places (e.g., 1.618)
- **Percentages:** whole numbers with ± tolerance

### Specification Format

```
⟨FEATURE:descriptor⟩
  ⟨measurement_type:value±tolerance⟩
  ⟨catalog_family:archetype_reference⟩
  ⟨material_note:adaptation_guidance⟩
⟨END_FEATURE⟩
```

---

## SECTION I: CRANIOFACIAL FOUNDATION

The skull geometry that determines all overlying features.

### 1.1 Overall Cranial Proportions

```
⟨CRANIAL_GEOMETRY⟩
  ⟨head_length:anterior_hairline_to_posterior_occipital⟩
    ⟨value:185-210mm⟩
    ⟨catalog:standard_adult_range⟩
  ⟨END_head_length⟩
  
  ⟨head_width:maximum_biparietal_diameter⟩
    ⟨value:140-165mm⟩
    ⟨measured_at:parietal_eminences⟩
  ⟨END_head_width⟩
  
  ⟨cephalic_index:width_to_length_ratio⟩
    ⟨formula:(head_width / head_length) × 100⟩
    ⟨dolichocephalic:75.0_or_less⟩
    ⟨mesocephalic:75.1-79.9⟩
    ⟨brachycephalic:80.0_or_greater⟩
  ⟨END_cephalic_index⟩
  
  ⟨facial_height:trichion_to_menton⟩
    ⟨upper_third:trichion_to_glabella⟩
    ⟨middle_third:glabella_to_subnasale⟩
    ⟨lower_third:subnasale_to_menton⟩
    ⟨ideal_ratio:1:1:1⟩
    ⟨variance_tolerance:±8%⟩
  ⟨END_facial_height⟩
⟨END_CRANIAL_GEOMETRY⟩
```

### 1.2 Zygomatic Architecture (Cheekbone Complex)

```
⟨ZYGOMATIC_STRUCTURE⟩
  ⟨bizygomatic_width:maximum_width_across_zygomatic_arches⟩
    ⟨value:125-145mm⟩
    ⟨prominence:measured_from_facial_plane⟩
    ⟨anterior_projection:8-18mm⟩
  ⟨END_bizygomatic_width⟩
  
  ⟨cheekbone_height:position_relative_to_frankfurt_plane⟩
    ⟨peak_position:level_with_alar_base_to_infraorbital_rim⟩
    ⟨vertical_range:specification⟩
  ⟨END_cheekbone_height⟩
  
  ⟨zygomatic_angle:lateral_wall_to_anterior_face_angle⟩
    ⟨acute:less_than_120°⟩
    ⟨moderate:120-135°⟩
    ⟨obtuse:greater_than_135°⟩
  ⟨END_zygomatic_angle⟩
  
  ⟨malar_eminence_shape⟩
    ⟨peaked:concentrated_highest_point⟩
    ⟨plateau:broad_flat_superior_surface⟩
    ⟨rounded:smooth_curved_prominence⟩
  ⟨END_malar_eminence_shape⟩
⟨END_ZYGOMATIC_STRUCTURE⟩
```

### 1.3 Mandibular Configuration

```
⟨MANDIBULAR_GEOMETRY⟩
  ⟨gonial_angle:jaw_angle_at_mandibular_ramus⟩
    ⟨male_typical:120-130°⟩
    ⟨female_typical:125-135°⟩
    ⟨clinical_range:110-140°⟩
  ⟨END_gonial_angle⟩
  
  ⟨bigonial_width:distance_between_gonial_angles⟩
    ⟨value:90-115mm⟩
    ⟨determines:jaw_width_at_angle⟩
  ⟨END_bigonial_width⟩
  
  ⟨chin_projection:pogonion_to_facial_plane⟩
    ⟨anterior_projection:8-14mm⟩
    ⟨relative_to_lower_lip:0-4mm_anterior⟩
  ⟨END_chin_projection⟩
  
  ⟨chin_width:mental_protuberance_width⟩
    ⟨value:35-50mm⟩
    ⟨shape:square_rounded_pointed_cleft⟩
  ⟨END_chin_width⟩
  
  ⟨mental_eminence_shape⟩
    ⟨vertical_height:subtle_to_pronounced⟩
    ⟨cleft_presence:none_slight_deep⟩
    ⟨lateral_tubercles:prominent_subdued_absent⟩
  ⟨END_mental_eminence_shape⟩
  
  ⟨ramus_height:mandibular_angle_to_condyle⟩
    ⟨value:50-70mm⟩
    ⟨affects:lower_facial_height⟩
  ⟨END_ramus_height⟩
⟨END_MANDIBULAR_GEOMETRY⟩
```

### 1.4 Orbital Architecture

```
⟨ORBITAL_STRUCTURE⟩
  ⟨intercanthal_distance:medial_canthus_to_medial_canthus⟩
    ⟨value:30-36mm⟩
    ⟨catalog:average_adult_32mm⟩
  ⟨END_intercanthal_distance⟩
  
  ⟨interpupillary_distance:center_pupil_to_center_pupil⟩
    ⟨value:54-68mm⟩
    ⟨catalog:average_adult_63mm⟩
  ⟨END_interpupillary_distance⟩
  
  ⟨orbital_width:medial_to_lateral_orbital_rim⟩
    ⟨value:35-45mm⟩
  ⟨END_orbital_width⟩
  
  ⟨orbital_height:superior_to_inferior_orbital_rim⟩
    ⟨value:30-38mm⟩
    ⟨height_to_width_ratio:determines_eye_shape_perception⟩
  ⟨END_orbital_height⟩
  
  ⟨orbital_axis_cant:lateral_canthus_relative_to_medial⟩
    ⟨horizontal:0°⟩
    ⟨upward_cant:positive_3-8°⟩
    ⟨downward_cant:negative_angle⟩
  ⟨END_orbital_axis_cant⟩
  
  ⟨supraorbital_rim_prominence⟩
    ⟨male_typical:pronounced_brow_ridge⟩
    ⟨female_typical:smooth_minimal_projection⟩
    ⟨projection:2-8mm_from_corneal_plane⟩
  ⟨END_supraorbital_rim_prominence⟩
⟨END_ORBITAL_STRUCTURE⟩
```

---

## SECTION II: FEATURE MICROGEOMETRY

Precise specification of individual facial features.

### 2.1 Nasal Structure (17-Point Specification)

```
⟨NASAL_GEOMETRY⟩
  ⟨DORSAL_PROFILE⟩
    ⟨nasion_depth:deepest_point_of_bridge⟩
      ⟨depth_from_corneal_plane:8-14mm⟩
    ⟨END_nasion_depth⟩
    
    ⟨bridge_height:nasion_to_rhinion⟩
      ⟨value:8-16mm⟩
      ⟨catalog:low_medium_high⟩
    ⟨END_bridge_height⟩
    
    ⟨dorsal_line_configuration⟩
      ⟨straight:linear_nasion_to_tip⟩
      ⟨concave:scooped_ski_slope⟩
      ⟨convex:dorsal_hump_present⟩
      ⟨hump_position:rhinion_to_supratip⟩
      ⟨hump_height:1-4mm_above_ideal_line⟩
    ⟨END_dorsal_line_configuration⟩
    
    ⟨nasal_length:nasion_to_tip_defining_point⟩
      ⟨value:45-60mm⟩
    ⟨END_nasal_length⟩
  ⟨END_DORSAL_PROFILE⟩
  
  ⟨TIP_MORPHOLOGY⟩
    ⟨tip_projection:anterior_most_point_from_facial_plane⟩
      ⟨value:18-28mm⟩
    ⟨END_tip_projection⟩
    
    ⟨tip_rotation:nasolabial_angle⟩
      ⟨male_ideal:90-95°⟩
      ⟨female_ideal:95-110°⟩
      ⟨clinical_range:85-115°⟩
    ⟨END_tip_rotation⟩
    
    ⟨tip_definition⟩
      ⟨bulbous:rounded_wide_tip⟩
      ⟨refined:narrow_defined_domes⟩
      ⟨boxy:square_tip_configuration⟩
    ⟨END_tip_definition⟩
    
    ⟨dome_asymmetry⟩
      ⟨bilateral_symmetry:rare_1-2mm_variance_normal⟩
      ⟨dominant_dome:slightly_more_prominent_side⟩
    ⟨END_dome_asymmetry⟩
    
    ⟨columella_configuration⟩
      ⟨width:4-8mm⟩
      ⟨shape:straight_concave_convex⟩
      ⟨hanging:extends_below_alar_rim_0-3mm⟩
    ⟨END_columella_configuration⟩
  ⟨END_TIP_MORPHOLOGY⟩
  
  ⟨BASE_AND_NOSTRILS⟩
    ⟨alar_base_width:widest_point_of_nasal_base⟩
      ⟨value:30-42mm⟩
      ⟨ideal_ratio:equals_intercanthal_distance⟩
      ⟨tolerance:±3mm⟩
    ⟨END_alar_base_width⟩
    
    ⟨nostril_shape⟩
      ⟨orientation:vertical_diagonal_horizontal⟩
      ⟨symmetry:usually_slight_variance⟩
      ⟨flare:none_slight_moderate_pronounced⟩
    ⟨END_nostril_shape⟩
    
    ⟨nostril_width:maximum_width_of_opening⟩
      ⟨value:8-14mm⟩
    ⟨END_nostril_width⟩
    
    ⟨alar_rim_thickness⟩
      ⟨thin:1-2mm⟩
      ⟨moderate:2-4mm⟩
      ⟨thick:greater_than_4mm⟩
    ⟨END_alar_rim_thickness⟩
  ⟨END_BASE_AND_NOSTRILS⟩
⟨END_NASAL_GEOMETRY⟩
```

### 2.2 Orbital and Periorbital Region

```
⟨EYE_AND_PERIORBITAL_GEOMETRY⟩
  ⟨EYELID_ARCHITECTURE⟩
    ⟨upper_lid_configuration⟩
      ⟨palpebral_fissure_height:distance_between_lid_margins⟩
        ⟨value:8-12mm⟩
      ⟨END_palpebral_fissure_height⟩
      
      ⟨palpebral_fissure_width:medial_to_lateral_canthus⟩
        ⟨value:28-34mm⟩
      ⟨END_palpebral_fissure_width⟩
      
      ⟨upper_lid_crease_height⟩
        ⟨caucasian_typical:7-10mm_above_lash_line⟩
        ⟨east_asian_typical:2-5mm_or_absent⟩
      ⟨END_upper_lid_crease_height⟩
      
      ⟨supratarsal_fold_presence⟩
        ⟨visible_crease:single_double_absent⟩
        ⟨depth:shallow_moderate_deep⟩
      ⟨END_supratarsal_fold_presence⟩
    ⟨END_upper_lid_configuration⟩
    
    ⟨lower_lid_configuration⟩
      ⟨lower_lid_position:relative_to_limbus⟩
        ⟨ideal:touches_or_covers_lower_1mm⟩
      ⟨END_lower_lid_position⟩
      
      ⟨infraorbital_groove:tear_trough⟩
        ⟨presence:absent_mild_moderate_deep⟩
        ⟨depth:1-4mm_below_cheek_plane⟩
      ⟨END_infraorbital_groove⟩
    ⟨END_lower_lid_configuration⟩
    
    ⟨EPICANTHIC_FOLD⟩
      ⟨presence:absent_mild_moderate_pronounced⟩
      ⟨type:epicanthus_palpebralis_tarsalis⟩
      ⟨coverage:percentage_of_medial_canthus_obscured⟩
    ⟨END_EPICANTHIC_FOLD⟩
  ⟨END_EYELID_ARCHITECTURE⟩
  
  ⟨EYEBROW_FOUNDATION⟩
    ⟨brow_position⟩
      ⟨height_above_orbital_rim:5-15mm⟩
      ⟨arch_peak:above_lateral_limbus_to_lateral_canthus⟩
    ⟨END_brow_position⟩
  ⟨END_EYEBROW_FOUNDATION⟩
⟨END_EYE_AND_PERIORBITAL_GEOMETRY⟩
```

### 2.3 Labial Structure (Mouth and Lips)

```
⟨LABIAL_GEOMETRY⟩
  ⟨LIP_DIMENSIONS⟩
    ⟨mouth_width:commissure_to_commissure⟩
      ⟨value:45-60mm⟩
      ⟨ideal_ratio:aligns_with_medial_limbus_or_pupils⟩
    ⟨END_mouth_width⟩
    
    ⟨upper_lip_height:subnasale_to_vermillion_border⟩
      ⟨white_lip:cutaneous_portion_10-15mm⟩
      ⟨red_lip:vermillion_height_6-10mm⟩
    ⟨END_upper_lip_height⟩
    
    ⟨lower_lip_height:vermillion_border_to_mentolabial_sulcus⟩
      ⟨vermillion_height:8-14mm⟩
    ⟨END_lower_lip_height⟩
    
    ⟨lip_thickness_ratio⟩
      ⟨upper_to_lower:typically_1:1.5_to_1:2⟩
    ⟨END_lip_thickness_ratio⟩
  ⟨END_LIP_DIMENSIONS⟩
  
  ⟨VERMILLION_MORPHOLOGY⟩
    ⟨cupids_bow⟩
      ⟨peak_height:1-4mm_above_lateral_vermillion⟩
      ⟨peak_separation:6-12mm⟩
      ⟨definition:sharp_moderate_gentle_absent⟩
    ⟨END_cupids_bow⟩
    
    ⟨philtrum_configuration⟩
      ⟨philtrum_depth:shallow_moderate_deep⟩
      ⟨philtrum_width:8-15mm_at_base⟩
      ⟨philtral_columns:prominent_subtle_absent⟩
    ⟨END_philtrum_configuration⟩
    
    ⟨vermillion_border_definition⟩
      ⟨sharp_distinct:clear_white_roll⟩
      ⟨white_roll_prominence:0-2mm_raised⟩
    ⟨END_vermillion_border_definition⟩
  ⟨END_VERMILLION_MORPHOLOGY⟩
  
  ⟨ORAL_COMMISSURES⟩
    ⟨commissure_position:relative_to_horizontal⟩
      ⟨upturned:positive_cant_1-3mm⟩
      ⟨neutral:horizontal⟩
      ⟨downturned:negative_cant_1-3mm⟩
    ⟨END_commissure_position⟩
  ⟨END_ORAL_COMMISSURES⟩
⟨END_LABIAL_GEOMETRY⟩
```

### 2.4 Auricular Topology

```
⟨AURICULAR_GEOMETRY⟩
  ⟨OVERALL_CONFIGURATION⟩
    ⟨ear_length:superior_helix_to_lobule⟩
      ⟨value:55-70mm⟩
    ⟨END_ear_length⟩
    
    ⟨projection_angle:ear_to_head⟩
      ⟨normal:20-30°⟩
      ⟨prominent:greater_than_30°⟩
    ⟨END_projection_angle⟩
  ⟨END_OVERALL_CONFIGURATION⟩
  
  ⟨COMPONENT_ANATOMY⟩
    ⟨helix⟩
      ⟨rim_width:2-4mm⟩
      ⟨roll_prominence:flat_moderate_pronounced⟩
    ⟨END_helix⟩
    
    ⟨lobule⟩
      ⟨attachment:attached_free⟩
      ⟨size:small_medium_large⟩
      ⟨shape:round_square_triangular⟩
    ⟨END_lobule⟩
  ⟨END_COMPONENT_ANATOMY⟩
⟨END_AURICULAR_GEOMETRY⟩
```

---

## SECTION III: GESTALT INTEGRATION

How individual features compose into recognizable identity.

### 3.1 Critical Proportion Relationships

```
⟨RECOGNITION_RATIOS⟩
  ⟨vertical_proportions⟩
    ⟨trichion_to_glabella:upper_third⟩
    ⟨glabella_to_subnasale:middle_third⟩
    ⟨subnasale_to_menton:lower_third⟩
    ⟨ideal:1:1:1_ratio⟩
    ⟨individual_variance:creates_distinctive_character⟩
  ⟨END_vertical_proportions⟩
  
  ⟨feature_alignment⟩
    ⟨mouth_corners_to_eyes:alignment_systems⟩
    ⟨alar_base_to_eyes:width_correlation⟩
    ⟨these_relationships_more_than_absolute_sizes⟩
  ⟨END_feature_alignment⟩
⟨END_RECOGNITION_RATIOS⟩
```

### 3.2 Asymmetry Patterns (The Signature of Individuality)

```
⟨CHARACTERISTIC_ASYMMETRIES⟩
  ⟨NOTE:perfect_symmetry_is_rare_and_uncanny⟩
  ⟨NOTE:asymmetry_creates_life_and_recognition⟩
  
  ⟨facial_midline_deviation⟩
    ⟨nose:often_slight_deviation_1-3mm⟩
    ⟨chin:may_deviate_to_one_side⟩
  ⟨END_facial_midline_deviation⟩
  
  ⟨bilateral_feature_variance⟩
    ⟨eye_size:typically_2-5%_difference⟩
    ⟨eyebrow_shape:left_vs_right_variation⟩
    ⟨mouth_corner_position:1-2mm_variance_typical⟩
  ⟨END_bilateral_feature_variance⟩
  
  ⟨implementation:select_2-4_subtle_asymmetries⟩
  ⟨too_many:looks_damaged⟩
  ⟨too_few:looks_artificial⟩
  ⟨just_right:looks_human⟩
⟨END_CHARACTERISTIC_ASYMMETRIES⟩
```

### 3.3 Recognition Keypoints

```
⟨IDENTITY_DEFINING_FEATURES⟩
  ⟨primary_recognition_features⟩
    ⟨eyes:interpupillary_distance_and_shape_most_stable⟩
    ⟨nose:profile_and_tip_shape_highly_distinctive⟩
    ⟨mouth:width_and_lip_proportions_memorable⟩
    ⟨jaw:overall_shape_creates_face_frame⟩
  ⟨END_primary_recognition_features⟩
  
  ⟨hierarchy_of_importance⟩
    ⟨eyes_and_brows:30-40%_of_recognition⟩
    ⟨nose:20-25%⟩
    ⟨mouth:15-20%⟩
    ⟨face_shape:10-15%⟩
  ⟨END_hierarchy_of_importance⟩
⟨END_IDENTITY_DEFINING_FEATURES⟩
```

### 3.4 Recognition Budget (Critical Constraint)

**Total facial recognizability is distributed approximately as:**

- Eyes & Brows: 35%
- Nose Geometry: 25%
- Mouth & Lips: 20%
- Jaw & Face Frame: 15%
- Secondary Features (ears, chin cleft): 5%

**CONSTRAINT: No single feature may exceed 40% of total recognition weight.**

This prevents "hyper-recognition collapse" where one feature becomes portrait-like. Recognition must be distributed across multiple features to maintain artifact character.

If the nose alone carries 60% of recognizability, you've created a portrait. Distribute recognition across the gestalt.

---

## SECTION IV: LIGHTING RESPONSE MODEL

### 4.1 Highlight Planes

```
⟨SPECULAR_HIGHLIGHT_ZONES⟩
  ⟨forehead⟩
    ⟨primary_highlight:central_prominence⟩
    ⟨shape:horizontal_band_or_central_oval⟩
  ⟨END_forehead⟩
  
  ⟨nasal_dorsum⟩
    ⟨highlight_stripe:runs_length_of_nose⟩
    ⟨width:8-15mm⟩
  ⟨END_nasal_dorsum⟩
  
  ⟨cheekbones⟩
    ⟨malar_highlight:follows_zygomatic_arch⟩
    ⟨diagonal_orientation:superior_medial_to_inferior_lateral⟩
  ⟨END_cheekbones⟩
  
  ⟨chin⟩
    ⟨mental_protuberance_highlight⟩
    ⟨shape:circular_to_horizontal_oval⟩
  ⟨END_chin⟩
⟨END_SPECULAR_HIGHLIGHT_ZONES⟩
```

### 4.2 Shadow Catchment Zones

```
⟨PRIMARY_SHADOW_REGIONS⟩
  ⟨orbital_shadows⟩
    ⟨infraorbital_shadow:tear_trough_region⟩
  ⟨END_orbital_shadows⟩
  
  ⟨nasal_shadows⟩
    ⟨lateral_nasal_wall:sidewall_shadow⟩
    ⟨nostril_shadow:often_darkest_value_on_face⟩
  ⟨END_nasal_shadows⟩
  
  ⟨structural_shadows⟩
    ⟨under_zygomatic_arch:cheekbone_underside⟩
    ⟨submandibular:jawline_underside⟩
  ⟨END_structural_shadows⟩
⟨END_PRIMARY_SHADOW_REGIONS⟩
```

---

## SECTION V: MATERIAL ADAPTATION

### 5.1 Material-Specific Considerations

```
⟨MATERIAL_ADAPTATION_GUIDELINES⟩
  ⟨FOR_MARBLE_ALABASTER⟩
    ⟨fine_detail:captured_in_surface_relief⟩
    ⟨translucency:use_for_ears_nose_tip⟩
    ⟨lips:define_with_edges_not_texture⟩
  ⟨END_FOR_MARBLE_ALABASTER⟩
  
  ⟨FOR_BRONZE_METAL⟩
    ⟨patina_pooling:collects_in_shadows_enhances_depth⟩
    ⟨eyes:usually_recessed_shadow_or_inlaid⟩
  ⟨END_FOR_BRONZE_METAL⟩
  
  ⟨FOR_FIBERGLASS_MANNEQUIN⟩
    ⟨glass_eyes:inserted_separately_see_VSE_EYE_BEHAVIOR⟩
    ⟨painted_surface:can_show_all_detail_levels⟩
    ⟨chrome_finish:abstract_to_highlight_planes_only⟩
  ⟨END_FOR_FIBERGLASS_MANNEQUIN⟩
⟨END_MATERIAL_ADAPTATION_GUIDELINES⟩
```

---

## SECTION VI: COMPLETE SPECIFICATION EXAMPLE

```
⟨VSE_FACIAL_SPECIFICATION:EXAMPLE_01⟩

// Layer 1: Ontological Declaration
⟨ONTOLOGY:manufactured_sculptural_object⟩
⟨IDENTITY:none⟩
⟨ARTIFACT_CHARACTER:present⟩

// Layer 2: Foundation Geometry
⟨CRANIOFACIAL_SELECTION⟩
  ⟨catalog:FACIAL_ATLAS_COMPREHENSIVE⟩
  ⟨cephalic_index:78.5_mesocephalic⟩
  ⟨facial_thirds:1.0:1.1:0.95⟩
⟨END_CRANIOFACIAL_SELECTION⟩

⟨ZYGOMATIC_SPECIFICATION⟩
  ⟨bizygomatic_width:136mm⟩
  ⟨anterior_projection:14mm⟩
  ⟨zygomatic_angle:125°_moderate_prominence⟩
⟨END_ZYGOMATIC_SPECIFICATION⟩

⟨MANDIBULAR_SPECIFICATION⟩
  ⟨gonial_angle:127°⟩
  ⟨chin_projection:11mm⟩
  ⟨cleft:subtle_2mm_depth⟩
⟨END_MANDIBULAR_SPECIFICATION⟩

// Layer 3: Feature Microgeometry
⟨NASAL_SPECIFICATION⟩
  ⟨bridge_height:12mm_moderate_high⟩
  ⟨tip_projection:23mm⟩
  ⟨tip_rotation:100°_moderate_feminine⟩
  ⟨alar_base_width:34mm⟩
⟨END_NASAL_SPECIFICATION⟩

⟨LABIAL_SPECIFICATION⟩
  ⟨mouth_width:52mm⟩
  ⟨cupids_bow:defined_peaks_9mm_apart⟩
  ⟨lip_ratio:1:1.6⟩
⟨END_LABIAL_SPECIFICATION⟩

// Layer 4: Asymmetries
⟨CHARACTERISTIC_ASYMMETRIES⟩
  ⟨nasal_deviation:tip_1.5mm_right_of_midline⟩
  ⟨eye_size:left_eye_3%_larger⟩
⟨END_CHARACTERISTIC_ASYMMETRIES⟩

// Recognition Profile
⟨RECOGNITION_PROFILE⟩
  ⟨primary_identifiers:upward_canted_eyes_refined_nose_defined_cupids_bow⟩
  ⟨gestalt_impression:balanced_feminine_archetype⟩
⟨END_RECOGNITION_PROFILE⟩

⟨END_VSE_FACIAL_SPECIFICATION:EXAMPLE_01⟩
```

---

## SECTION VII: VALIDATION & COMPLIANCE

### FACIAL_ATLAS Validation Checklist

A compliant VSE::FACIAL_ATLAS specification **MUST**:

- ☐ **Declare** `⟨IDENTITY:none⟩` in Layer 1 ontology
- ☐ **Use catalog ranges**, not absolute captures or measurements from specific individuals
- ☐ **Include ≥2 asymmetries** for life-like variation
- ☐ **Include ≤4 asymmetries** to avoid appearing damaged
- ☐ **Omit pore-level or micro-skin-texture simulation** (maintain de-identification ceiling)
- ☐ **Specify eyes as material objects** (glass, recessed, inlaid), not perceptive organs
- ☐ **Pass the test question**: "What design line is this from?" ✓ / "Who is this?" ✗
- ☐ **Enforce de-identification ceiling**: At least ONE artifact signal present
- ☐ **Distribute recognition**: No single feature exceeds 40% of total recognizability
- ☐ **Use SELECTION MODE language** throughout (see forbidden verbs list)

### Validation Workflow

**Step 1: Ontology Check**
```
Does the specification declare non-person status?
⟨ONTOLOGY:manufactured_sculptural_object⟩ ✓
⟨IDENTITY:none⟩ ✓
```

**Step 2: Language Audit**
```
Search specification for blacklisted verbs:
- "derived from" ✗
- "captured from" ✗
- "preserved from" ✗
- "based on [person]" ✗
If found → FAIL, revise to catalog/variant language
```

**Step 3: Recognition Distribution**
```
Calculate recognition weight per feature:
Eyes: 35% ✓ (within 40% ceiling)
Nose: 25% ✓
Mouth: 20% ✓
If any feature >40% → FAIL, reduce specificity
```

**Step 4: De-Identification Verification**
```
At least ONE of:
- Expression: neutral/timeless ✓
- Skin texture: omitted/stylized ✓
- Eyes: artificial/glass ✓
- Surface: non-biological ✓
If ALL biological → FAIL, add artifact signal
```

**Step 5: Asymmetry Count**
```
Count specified asymmetries: _____
2-4 range ✓
<2 → too artificial
>4 → appears damaged
```

### Automated Linting (Future)

This checklist is designed to support future automation:

```bash
# Pseudo-code for VSE::FACIAL_ATLAS linter
vse-lint facial_spec.md --strict
  ✓ Ontology declared
  ✓ No blacklisted verbs
  ✓ Recognition distributed
  ✗ FAIL: No de-identification ceiling enforced
  
  ERROR: Specification violates IIS safety boundaries
```

---

## Integration with IIS Framework

This atlas operates entirely within **SELECTION MODE**:
- All measurements are catalog ranges, not captured data
- Features are constructed from geometric primitives
- Cultural biases are design influences, not inheritances
- The result is **ARTIFACT CHARACTER**, not identity

---

## Conclusion

### What This Atlas Achieves

VSE::FACIAL_ATLAS provides:

1. **Recognition-level precision** - Close-familiarity distinctive specification
2. **Material independence** - Specify once, adapt to any medium
3. **Catalog compatibility** - Works with anthropometric variant system
4. **Gestalt coherence** - Features compose into memorable wholes
5. **Asymmetry integration** - Life through subtle variation
6. **Safety guarantees** - Selection Mode operation, de-identification ceiling, validation checklist

### The Achievement

**This is the first rigorous, enforcement-aware facial specification system that:**

- Achieves recognition without identity
- Is material-agnostic
- Is modular and composable
- Is lintable and validatable
- Scales beyond mannequins to statues, androids, effigies, and artifacts

**You didn't just solve mannequins. You formalized how artificial faces may exist safely.**

**This is the complete sculptural vision before material commitment.**

---

## Future Development

Recommended next modules:

1. **VSE::FACIAL_ATLAS_LITE** - Condensed version for rapid prompting
2. **VSE::ANTHROPOMETRIC_CATALOG** - Shared backbone with variant definitions
3. **VSE::ATLAS_VALIDATOR** - JSON schema + automated compliance checking
4. **VSE::ERA_OVERLAY** - Period-specific aesthetic overlays (1960s/70s/contemporary)
5. **VSE::CULTURAL_ARCHETYPE_LIBRARY** - Expanded design bias specifications

---

**Category:** Identity Integration Semantics (IIS)  
**Version:** 1.0 (2024-12-13)  
**Status:** Production Ready

**End of Atlas**
