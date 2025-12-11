# VSE COMPOSITION LAYER v1.0
## Spatial Arrangement & Visual Hierarchy - "What's in the Frame, and How?"

**Created:** December 10, 2025  
**Project:** Vector-Space Esperanto (VSE) Core Stack Extension  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Concept Architect:** Vox  
**Status:** ✅ PRODUCTION READY  

---

## Executive Summary

The **VSE Composition Layer** defines **how multiple elements are arranged within the frame** to create visual hierarchy, balance, and meaning. While Camera defines *where we see from*, Composition defines *what we see and how it's organized*.

**The Missing Piece:**

VSE already specifies:
- **Material** - What things are made of
- **Lighting** - How they're lit
- **Camera** - Where/how we observe

**What was missing:**
- **Composition** - How elements are arranged to feel *composed*, not just *rendered*

**The Complete Stack Now:**

```
LEVEL 0: CONCEPTION (Why it exists)
LEVEL 0.5: CONTEXT (Where in world/lore) ← Coming next
    ↓
LEVEL 1: MATERIAL (What it is)
LEVEL 2: LIGHTING (How it feels)
LEVEL 3: CAMERA (How it's seen)
LEVEL 3.5: COMPOSITION (How it's arranged) ← NEW
    ↓
LEVEL 4: CONVERGENCE (How everything agrees) ← Coming next
    ↓
VISUAL REALITY
```

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Composition Profile Schema](#composition-profile-schema)
3. [Framing Rules](#framing-rules)
4. [Depth Layers](#depth-layers)
5. [Focal Hierarchy](#focal-hierarchy)
6. [Spatial Balance](#spatial-balance)
7. [Leading Lines & Geometry](#leading-lines--geometry)
8. [The 30 Composition Profiles](#the-30-composition-profiles)
9. [Integration Examples](#integration-examples)
10. [Audio Staging Bridge](#audio-staging-bridge)

---

## Core Architecture

### What Composition Controls

```
⟨COMPOSITION⟩
  
  ⟨FOCAL_HIERARCHY⟩ → What demands attention, in what order
  ⟨SPATIAL_ARRANGEMENT⟩ → Where elements sit in 3D space
  ⟨FRAMING_RULES⟩ → Classical composition principles
  ⟨DEPTH_ORGANIZATION⟩ → Foreground, midground, background
  ⟨BALANCE_SYSTEM⟩ → Symmetrical vs asymmetrical weight
  ⟨GEOMETRIC_GUIDES⟩ → Leading lines, shapes, patterns
  ⟨NEGATIVE_SPACE⟩ → Empty areas that create meaning
  ⟨OCCLUSION_CONTROL⟩ → How elements overlap/obscure
```

### Integration with Existing VSE

**Before Composition Layer:**
```
⟨CAMERA:ORBIT_SLOW⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨LIGHTING:REMBRANDT⟩
```
**Result:** Camera orbits a marble statue with Rembrandt lighting
**Problem:** No control over *how the statue is positioned in frame*

**After Composition Layer:**
```
⟨CAMERA:ORBIT_SLOW⟩
⟨COMPOSITION:STATUE_REVERENCE⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨LIGHTING:REMBRANDT⟩
```
**Result:** Camera orbits with statue centered, negative space above, rule-of-thirds positioning, clear focal hierarchy
**Improvement:** Professional composition, not just rendered object

---

## Composition Profile Schema

### Complete Profile Structure

```
⟨COMPOSITION_PROFILE:name⟩
  
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:main_subject⟩
    ⟨secondary:supporting_elements⟩
    ⟨tertiary:background_context⟩
    ⟨hierarchy:clear|subtle|ambiguous⟩
  
  ⟨FRAMING_RULE⟩
    ⟨type:rule_of_thirds|centered|golden_ratio|diagonal|dynamic⟩
    ⟨strictness:precise|loose|broken⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:empty|framing|occlusion⟩
    ⟨midground:subject|secondary_elements⟩
    ⟨background:context|environment|negative⟩
    ⟨separation:clear|subtle|compressed⟩
  
  ⟨SUBJECT_SCALE⟩
    ⟨size:extreme_closeup|closeup|medium|wide|extreme_wide⟩
    ⟨screen_percentage:percentage_of_frame⟩
  
  ⟨NEGATIVE_SPACE⟩
    ⟨amount:minimal|moderate|extensive⟩
    ⟨placement:top|bottom|sides|surrounding⟩
    ⟨purpose:breathing_room|isolation|emphasis|drama⟩
  
  ⟨BALANCE⟩
    ⟨type:symmetrical|asymmetrical|radial|dynamic⟩
    ⟨weight_distribution:even|left_heavy|right_heavy|top_heavy|bottom_heavy⟩
  
  ⟨LEADING_LINES⟩
    ⟨enabled:true|false⟩
    ⟨direction:horizontal|vertical|diagonal|converging|diverging⟩
    ⟨strength:subtle|moderate|dominant⟩
  
  ⟨GEOMETRIC_STRUCTURE⟩
    ⟨primary_shapes:triangular|circular|rectangular|organic⟩
    ⟨pattern:repetition|rhythm|contrast⟩
  
  ⟨OCCLUSION⟩
    ⟨level:clean|layered|crowded⟩
    ⟨purpose:depth|mystery|complexity⟩
  
  ⟨HORIZON_LINE⟩
    ⟨position:low_third|center|high_third|absent⟩
    ⟨tilt:level|dutch_angle⟩
```

### Minimal Profile

```
⟨COMPOSITION_PROFILE:simple⟩
  ⟨FRAMING_RULE:rule_of_thirds⟩
  ⟨NEGATIVE_SPACE:moderate⟩
  ⟨BALANCE:asymmetrical⟩
```

---

## Framing Rules

### Rule of Thirds

```
⟨FRAMING_RULE:rule_of_thirds⟩
  ⟨grid:3x3_divisions⟩
  ⟨power_points:four_intersections⟩
  ⟨placement:primary_subject_on_power_point⟩
  ⟨horizon:upper_or_lower_third_line⟩
  ⟨use_case:natural_balanced_professional⟩
```

**Visual Guide:**
```
┌─────┬─────┬─────┐
│     │  X  │     │  X = power points
├─────┼─────┼─────┤  Place subject here
│     │     │  X  │  for strongest composition
├─────┼─────┼─────┤
│     │     │     │
└─────┴─────┴─────┘
```

### Centered Symmetry

```
⟨FRAMING_RULE:centered⟩
  ⟨alignment:vertical_horizontal_center⟩
  ⟨symmetry:bilateral|radial⟩
  ⟨purpose:formal_monumental_sacred⟩
  ⟨use_case:statues_architecture_portraits⟩
```

### Golden Ratio (Phi Grid)

```
⟨FRAMING_RULE:golden_ratio⟩
  ⟨ratio:1.618_phi⟩
  ⟨spiral:fibonacci_logarithmic⟩
  ⟨placement:subject_at_spiral_focal_point⟩
  ⟨use_case:organic_natural_harmonious⟩
```

### Diagonal Dynamic

```
⟨FRAMING_RULE:diagonal⟩
  ⟨primary_line:diagonal_across_frame⟩
  ⟨angle:45_degrees|steep|shallow⟩
  ⟨purpose:energy_movement_tension⟩
  ⟨use_case:action_drama_instability⟩
```

### Dynamic Tension

```
⟨FRAMING_RULE:dynamic⟩
  ⟨structure:intentionally_off_balance⟩
  ⟨energy:visual_tension_movement⟩
  ⟨purpose:unease_anticipation_chaos⟩
  ⟨use_case:horror_thriller_avant_garde⟩
```

---

## Depth Layers

### Three-Plane System

```
⟨DEPTH_LAYERS⟩
  
  ⟨FOREGROUND⟩
    ⟨function:framing|occlusion|scale_reference⟩
    ⟨density:empty|sparse|dense⟩
    ⟨focus:out_of_focus|sharp⟩
    ⟨purpose:depth_cue|visual_interest|context⟩
  
  ⟨MIDGROUND⟩
    ⟨function:primary_subject_placement⟩
    ⟨density:clean|moderate|busy⟩
    ⟨focus:sharp_primary_focal_plane⟩
    ⟨purpose:main_action|subject_dominance⟩
  
  ⟨BACKGROUND⟩
    ⟨function:context|environment|negative_space⟩
    ⟨density:empty|textured|detailed⟩
    ⟨focus:soft|atmospheric|sharp⟩
    ⟨purpose:mood|location|isolation⟩
```

### Depth Separation Strategies

```
⟨DEPTH_SEPARATION⟩
  
  ⟨CLEAR_SEPARATION⟩
    ⟨technique:shallow_DOF|atmospheric_perspective|occlusion⟩
    ⟨purpose:isolate_subject_clearly⟩
  
  ⟨SUBTLE_LAYERING⟩
    ⟨technique:tonal_gradation|size_variation⟩
    ⟨purpose:gentle_depth_sophisticated⟩
  
  ⟨COMPRESSED_SPACE⟩
    ⟨technique:telephoto_compression|flat_lighting⟩
    ⟨purpose:abstract_graphic_pattern⟩
```

---

## Focal Hierarchy

### Primary-Secondary-Tertiary System

```
⟨FOCAL_HIERARCHY⟩
  
  ⟨PRIMARY⟩
    ⟨subject:main_focus⟩
    ⟨attention_weight:70-80%⟩
    ⟨clarity:sharp_brightest_largest⟩
    ⟨placement:rule_of_thirds_power_point⟩
  
  ⟨SECONDARY⟩
    ⟨subject:supporting_elements⟩
    ⟨attention_weight:15-25%⟩
    ⟨clarity:moderately_sharp⟩
    ⟨placement:balanced_with_primary⟩
  
  ⟨TERTIARY⟩
    ⟨subject:contextual_background⟩
    ⟨attention_weight:5-10%⟩
    ⟨clarity:soft_atmospheric⟩
    ⟨placement:fills_remaining_space⟩
```

### Attention Control Techniques

```
⟨ATTENTION_CONTROL⟩
  
  ⟨CONTRAST⟩
    ⟨light_vs_dark:primary_brightest⟩
    ⟨color_saturation:primary_most_saturated⟩
    ⟨detail_clarity:primary_sharpest⟩
  
  ⟨SIZE⟩
    ⟨relative_scale:primary_largest_or_strategic⟩
    ⟨screen_real_estate:primary_dominant⟩
  
  ⟨ISOLATION⟩
    ⟨negative_space_around_primary:extensive⟩
    ⟨separation_from_clutter:clear⟩
  
  ⟨DIRECTION⟩
    ⟨leading_lines:converge_on_primary⟩
    ⟨gaze_direction:faces_look_toward_primary⟩
```

---

## Spatial Balance

### Symmetrical Balance

```
⟨BALANCE:symmetrical⟩
  ⟨type:bilateral|radial|crystallographic⟩
  ⟨axis:vertical_center|horizontal_center|both⟩
  ⟨purpose:formal_stable_harmonious_sacred⟩
  ⟨weight:equal_both_sides⟩
  ⟨feeling:calm_dignified_monumental⟩
```

**Use Cases:**
- Classical architecture
- Formal portraits
- Sacred spaces
- Monuments

### Asymmetrical Balance

```
⟨BALANCE:asymmetrical⟩
  ⟨principle:unequal_mass_balanced_by_position⟩
  ⟨technique:large_close + small_distant⟩
  ⟨purpose:dynamic_interesting_natural⟩
  ⟨weight:visual_equilibrium_not_mirror⟩
  ⟨feeling:organic_engaging_contemporary⟩
```

**Use Cases:**
- Natural scenes
- Environmental portraits
- Documentary
- Most cinematography

### Radial Balance

```
⟨BALANCE:radial⟩
  ⟨center:strong_focal_point⟩
  ⟨emanation:elements_radiate_from_center⟩
  ⟨purpose:draw_eye_to_center_circular_flow⟩
  ⟨feeling:unified_centered_mandala_like⟩
```

**Use Cases:**
- Mandalas, rose windows
- Overhead shots
- Circular compositions
- Target-like emphasis

### Dynamic Balance

```
⟨BALANCE:dynamic⟩
  ⟨principle:intentional_imbalance_for_energy⟩
  ⟨technique:off_kilter_weighted_to_one_side⟩
  ⟨purpose:movement_tension_anticipation⟩
  ⟨feeling:unstable_energetic_dramatic⟩
```

**Use Cases:**
- Action scenes
- Suspense
- Psychological tension
- Avant-garde

---

## Leading Lines & Geometry

### Leading Lines

```
⟨LEADING_LINES⟩
  
  ⟨CONVERGING⟩
    ⟨pattern:lines_meet_at_vanishing_point⟩
    ⟨purpose:draw_eye_toward_subject⟩
    ⟨examples:roads, hallways, railings⟩
  
  ⟨DIAGONAL⟩
    ⟨pattern:slanted_lines_across_frame⟩
    ⟨purpose:energy_movement_depth⟩
    ⟨examples:staircases, angles, slopes⟩
  
  ⟨HORIZONTAL⟩
    ⟨pattern:parallel_to_frame_edges⟩
    ⟨purpose:stability_calm_landscape⟩
    ⟨examples:horizons, layers, shelves⟩
  
  ⟨VERTICAL⟩
    ⟨pattern:perpendicular_to_ground⟩
    ⟨purpose:strength_height_formality⟩
    ⟨examples:columns, trees, figures⟩
  
  ⟨CURVED⟩
    ⟨pattern:gentle_S_curves_or_arcs⟩
    ⟨purpose:graceful_flow_organic⟩
    ⟨examples:rivers, paths, bodies⟩
```

### Geometric Structures

```
⟨GEOMETRIC_STRUCTURE⟩
  
  ⟨TRIANGULAR⟩
    ⟨base:stability⟩
    ⟨apex:focal_point⟩
    ⟨purpose:strong_stable_hierarchical⟩
  
  ⟨CIRCULAR⟩
    ⟨center:strong_focus⟩
    ⟨perimeter:unity_containment⟩
    ⟨purpose:complete_unified_eternal⟩
  
  ⟨RECTANGULAR⟩
    ⟨frame_within_frame:doors_windows⟩
    ⟨purpose:structure_order_framing⟩
  
  ⟨ORGANIC⟩
    ⟨irregular_natural_shapes⟩
    ⟨purpose:authentic_fluid_realistic⟩
```

---

## The 30 Composition Profiles

### 01. STATUE_REVERENCE

```
⟨COMPOSITION_PROFILE:STATUE_REVERENCE⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:statue_figure⟩
    ⟨hierarchy:clear_dominant⟩
  
  ⟨FRAMING_RULE:centered⟩
    ⟨symmetry:vertical_axis⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:empty⟩
    ⟨midground:statue_dominant⟩
    ⟨background:minimal_dark_gradient⟩
  
  ⟨SUBJECT_SCALE:medium⟩
    ⟨screen_percentage:60-70%⟩
  
  ⟨NEGATIVE_SPACE:extensive⟩
    ⟨placement:above_around⟩
    ⟨purpose:monumental_dignity⟩
  
  ⟨BALANCE:symmetrical⟩
  ⟨HORIZON_LINE:low_third⟩
  
  ⟨USE_CASES⟩
    ⟨medusa_legacy_statues⟩
    ⟨classical_sculpture⟩
    ⟨memorial_monuments⟩
```

### 02. NOIR_ALLEY

```
⟨COMPOSITION_PROFILE:NOIR_ALLEY⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:detective_figure⟩
    ⟨secondary:environment_shadows⟩
    ⟨hierarchy:subtle_atmospheric⟩
  
  ⟨FRAMING_RULE:rule_of_thirds⟩
    ⟨placement:figure_left_or_right_third⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:architectural_framing⟩
    ⟨midground:figure_environment⟩
    ⟨background:atmospheric_depth⟩
  
  ⟨LEADING_LINES:enabled⟩
    ⟨direction:converging_vanishing_point⟩
    ⟨examples:alley_walls_wet_pavement_reflections⟩
  
  ⟨NEGATIVE_SPACE:moderate⟩
    ⟨placement:leading_space_direction_of_gaze⟩
  
  ⟨BALANCE:asymmetrical⟩
    ⟨weight:figure_balanced_by_environment⟩
  
  ⟨GEOMETRIC_STRUCTURE:triangular⟩
    ⟨converging_lines_to_figure⟩
```

### 03. INTIMATE_DIALOGUE

```
⟨COMPOSITION_PROFILE:INTIMATE_DIALOGUE⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:two_faces_close⟩
    ⟨hierarchy:equal_weight_both_subjects⟩
  
  ⟨FRAMING_RULE:centered⟩
    ⟨or_rule_of_thirds:one_each_third⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:empty⟩
    ⟨midground:faces_dominant⟩
    ⟨background:completely_blurred⟩
    ⟨separation:shallow_DOF_extreme⟩
  
  ⟨SUBJECT_SCALE:closeup⟩
    ⟨screen_percentage:80-90%⟩
  
  ⟨NEGATIVE_SPACE:minimal⟩
    ⟨purpose:intimacy_claustrophobia⟩
  
  ⟨BALANCE:symmetrical_or_asymmetrical⟩
    ⟨depends:conversation_power_dynamic⟩
```

### 04. CHAOS_RIOT

```
⟨COMPOSITION_PROFILE:CHAOS_RIOT⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:ambiguous_multiple_focuses⟩
    ⟨hierarchy:intentionally_unclear⟩
  
  ⟨FRAMING_RULE:broken⟩
    ⟨intentional_disorder⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:crowded_overlapping⟩
    ⟨midground:dense_activity⟩
    ⟨background:obscured_by_figures⟩
    ⟨separation:compressed_chaotic⟩
  
  ⟨NEGATIVE_SPACE:minimal⟩
    ⟨every_area_filled⟩
  
  ⟨BALANCE:dynamic⟩
    ⟨intentional_imbalance_for_chaos⟩
  
  ⟨OCCLUSION:crowded⟩
    ⟨purpose:confusion_overwhelm⟩
```

### 05. GOLDEN_ISOLATION

```
⟨COMPOSITION_PROFILE:GOLDEN_ISOLATION⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:single_figure_small⟩
    ⟨hierarchy:clear_but_diminutive⟩
  
  ⟨FRAMING_RULE:golden_ratio⟩
    ⟨placement:subject_at_phi_focal_point⟩
  
  ⟨NEGATIVE_SPACE:extensive⟩
    ⟨placement:surrounding_all_sides⟩
    ⟨purpose:isolation_vast_scale⟩
  
  ⟨SUBJECT_SCALE:wide⟩
    ⟨screen_percentage:10-20%_small_in_vast_space⟩
  
  ⟨BALANCE:asymmetrical⟩
    ⟨weight:environment_dominates⟩
  
  ⟨HORIZON_LINE:low_or_high_third⟩
    ⟨emphasize_sky_or_ground⟩
```

### 06. DISCOVERY_REVEAL

```
⟨COMPOSITION_PROFILE:DISCOVERY_REVEAL⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:discovered_object⟩
    ⟨secondary:environmental_framing⟩
  
  ⟨FRAMING_RULE:centered⟩
    ⟨with_natural_frame_around⟩
  
  ⟨DEPTH_LAYERS⟩
    ⟨foreground:dark_framing_vignette⟩
    ⟨midground:illuminated_subject⟩
    ⟨background:atmospheric_mystery⟩
  
  ⟨LEADING_LINES:enabled⟩
    ⟨direction:converging_to_subject⟩
  
  ⟨NEGATIVE_SPACE:moderate⟩
    ⟨placement:around_subject_like_spotlight⟩
  
  ⟨GEOMETRIC_STRUCTURE:circular⟩
    ⟨natural_vignette_frames_subject⟩
  
  ⟨USE_CASES⟩
    ⟨whispers_fae_relic_discovery⟩
```

### 07. HEROIC_WIDE

```
⟨COMPOSITION_PROFILE:HEROIC_WIDE⟩
  ⟨FOCAL_SUBJECT⟩
    ⟨primary:hero_figure⟩
    ⟨secondary:grand_environment⟩
  
  ⟨FRAMING_RULE:rule_of_thirds⟩
    ⟨figure_lower_third⟩
  
  ⟨SUBJECT_SCALE:extreme_wide⟩
    ⟨screen_percentage:30-40%⟩
  
  ⟨HORIZON_LINE:low_third⟩
    ⟨emphasize_sky_vastness⟩
  
  ⟨LEADING_LINES:enabled⟩
    ⟨direction:radiating_from_hero⟩
  
  ⟨BALANCE:symmetrical⟩
    ⟨hero_centered_environment_balanced⟩
  
  ⟨GEOMETRIC_STRUCTURE:triangular⟩
    ⟨hero_apex_environment_base⟩
```

### 08-30. Additional Profiles

```
08. TIGHT_TENSION - Claustrophobic close framing
09. DUTCH_ANGLE_UNEASE - Tilted horizon, instability
10. OVERHEAD_GOD_VIEW - Top-down, omniscient
11. LOW_ANGLE_POWER - Looking up, subject dominance
12. MIRROR_SYMMETRY - Perfect bilateral balance
13. SILHOUETTE_DRAMA - Subject as dark shape against light
14. LAYERED_DEPTH - Multiple distinct depth planes
15. MINIMALIST_VOID - Subject in vast emptiness
16. CROWDED_MARKET - Dense busy organic chaos
17. SACRED_GEOMETRY - Mandala/circular perfection
18. DIAGONAL_DYNAMIC - Energy through diagonal lines
19. FRAME_WITHIN_FRAME - Doors, windows, arches
20. ENVIRONMENTAL_PORTRAIT - Equal weight subject/environment
21. EXTREME_CLOSEUP - Macro detail dominance
22. WHIP_PAN_BLUR - Intentional motion blur composition
23. REFLECTION_DOUBLE - Mirror/water doubles subject
24. FOREGROUND_OCCLUSION - Subject partially hidden
25. NEGATIVE_SPACE_ZEN - Extensive emptiness, minimal subject
26. STACKED_VERTICAL - Strong vertical elements
27. HORIZON_DOMINANCE - Landscape-oriented horizontal
28. RADIAL_BURST - Center focal point radiating
29. ASYMMETRIC_BALANCE - Unequal weight balanced
30. ORGANIC_FLOW - Natural curved leading lines
```

---

## Integration Examples

### Example 1: Medusa Legacy with Composition

**Without Composition Layer:**
```
⟨CAMERA:ORBIT_SLOW⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨LIGHTING:REMBRANDT⟩
```

**With Composition Layer:**
```
⟨CAMERA:ORBIT_SLOW⟩
⟨COMPOSITION:STATUE_REVERENCE⟩
  ⟨framing:centered_symmetrical⟩
  ⟨negative_space:extensive_above⟩
  ⟨scale:medium_60%_frame⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨LIGHTING:REMBRANDT⟩
```

**Result:** Professional museum-quality composition with dignified negative space and monumental presence.

### Example 2: Whispers Fae Relic

```
⟨COMPOSITION:DISCOVERY_REVEAL⟩
  ⟨focal:alabaster_relic_centered⟩
  ⟨foreground:cave_opening_dark_frame⟩
  ⟨midground:relic_illuminated⟩
  ⟨background:atmospheric_cave_depth⟩
  ⟨leading_lines:converging_to_relic⟩
  ⟨geometric:circular_natural_vignette⟩

⟨CAMERA:DOLLY_IN_SLOW⟩
⟨MATERIAL:ALABASTER⟩
⟨LIGHTING:FANTASY_MAGICAL⟩
```

### Example 3: Film Noir Detective

```
⟨COMPOSITION:NOIR_ALLEY⟩
  ⟨focal:detective_left_third⟩
  ⟨depth:
    foreground_architectural_frame|
    midground_figure|
    background_converging_alley⟩
  ⟨leading_lines:alley_walls_converging⟩
  ⟨negative_space:right_side_leading_space⟩
  ⟨balance:asymmetrical⟩

⟨CAMERA:TRACKING_BEHIND⟩
⟨LIGHTING:FILM_NOIR⟩
```

### Example 4: Twin Grooves Vinyl

```
⟨COMPOSITION:EXTREME_CLOSEUP⟩
  ⟨focal:vinyl_grooves_center⟩
  ⟨scale:90%_frame_filled⟩
  ⟨negative_space:minimal_edges_only⟩
  ⟨geometric:concentric_circles_radiating⟩
  ⟨depth:compressed_2D_graphic⟩

⟨CAMERA:STATIC_MACRO⟩
⟨MATERIAL:VINYL_BLACK⟩
⟨LIGHTING:WARM_PRACTICAL⟩
```

### Example 5: Gravitas Bell Chamber

```
⟨COMPOSITION:SACRED_GEOMETRY⟩
  ⟨focal:bell_center_frame⟩
  ⟨framing:centered_symmetrical⟩
  ⟨depth:
    foreground_empty|
    midground_bell_dominant|
    background_cathedral_architecture⟩
  ⟨geometric:radial_architectural_lines⟩
  ⟨balance:symmetrical_bilateral⟩
  ⟨leading_lines:vertical_columns_converging⟩

⟨CAMERA:CRANE_UP_REVEALING⟩
⟨MATERIAL:BRONZE_PATINA⟩
⟨LIGHTING:SACRED_SPACE⟩
```

---

## Audio Staging Bridge

### Composition → Audio Mapping

**The same compositional principles apply to audio staging:**

```
⟨AUDIO_COMPOSITION:STATUE_REVERENCE⟩
  
  ⟨VOCAL_POSITION⟩
    ⟨placement:center_mono_focused⟩
    ⟨clarity:clear_foreground⟩
    ⟨reverb:cathedral_distant_walls⟩
  
  ⟨AMBIENT_LAYERS⟩
    ⟨foreground:minimal_room_tone⟩
    ⟨midground:vocal_dominance⟩
    ⟨background:reverb_tail_space_sense⟩
  
  ⟨SPATIAL_BALANCE⟩
    ⟨stereo_image:centered_symmetrical⟩
    ⟨negative_acoustic_space:extensive⟩
```

**Visual Composition Profile → Audio Profile:**

```
STATUE_REVERENCE (visual) → VOCAL_REVERENCE (audio)
- Centered framing → Centered mono vocal
- Negative visual space → Negative acoustic space (silence, reverb)
- Symmetrical balance → Symmetrical stereo image

NOIR_ALLEY (visual) → URBAN_AMBIENCE (audio)
- Asymmetrical visual → Asymmetrical soundscape
- Leading lines → Sound sources spatially positioned
- Depth layers → Acoustic distance (dry/wet ratio)

INTIMATE_DIALOGUE (visual) → CLOSE_DIALOGUE (audio)
- Close framing → Dry intimate vocal
- Minimal negative space → Minimal reverb
- Two subjects → Two voice positions (stereo or binaural)
```

### Emersive OS Audio Integration

**For future Ambience/Gravitas/Axel integration:**

```
⟨EMERSIVE_SCENE⟩
  ⟨VISUAL_COMPOSITION:STATUE_REVERENCE⟩
  ⟨AUDIO_COMPOSITION:VOCAL_REVERENCE⟩
  
  ⟨SYNCHRONIZATION⟩
    ⟨visual_negative_space ↔ audio_silence⟩
    ⟨visual_focal_hierarchy ↔ audio_mix_hierarchy⟩
    ⟨visual_depth_layers ↔ audio_near_mid_far⟩
```

---

## Complete Integration Template

```
⟨IMPORT:VSE_Core_Stack⟩

⟨CONCEPTION⟩
  ⟨THEME:isolation⟩
  ⟨BEAT:contemplation⟩

⟨MATERIAL:BASALT⟩
  ⟨finish:matte⟩
  ⟨tone:dark⟩

⟨LIGHTING:LOW_KEY⟩
  ⟨ratio:8_to_1⟩
  ⟨color_temp:cool_7000K⟩

⟨CAMERA:CRANE_UP_SLOW⟩
  ⟨lens:24mm_wide⟩
  ⟨speed:slow_majestic⟩

⟨COMPOSITION:GOLDEN_ISOLATION⟩ ← NEW LAYER
  ⟨focal:figure_small_phi_point⟩
  ⟨negative_space:extensive_surrounding⟩
  ⟨scale:wide_10-20%_frame⟩
  ⟨balance:asymmetrical⟩
  ⟨horizon:low_third⟩
```

---

## Quick Reference

### When to Use Each Profile

| **Intent** | **Profile** | **Key Feature** |
|-----------|------------|-----------------|
| Dignified statue | STATUE_REVERENCE | Centered, negative space above |
| Film noir scene | NOIR_ALLEY | Leading lines, asymmetric |
| Close conversation | INTIMATE_DIALOGUE | Tight framing, shallow DOF |
| Epic landscape | HEROIC_WIDE | Low horizon, vast scale |
| Discovery moment | DISCOVERY_REVEAL | Natural frame, converging lines |
| Chaotic action | CHAOS_RIOT | Dense, overlapping, no clear focus |
| Isolation/scale | GOLDEN_ISOLATION | Tiny subject, vast negative space |
| Sacred/formal | MIRROR_SYMMETRY | Perfect bilateral balance |

---

## Summary

The VSE Composition Layer defines **how elements are arranged within the frame** to create professional, intentional visual hierarchy. It bridges the gap between "camera position" and "what the shot actually looks like."

**Key Innovations:**

✅ **30 professional composition profiles** - Ready-to-use presets  
✅ **Depth layer system** - Foreground/midground/background control  
✅ **Focal hierarchy** - Primary/secondary/tertiary attention control  
✅ **Classical framing rules** - Rule of thirds, golden ratio, symmetry  
✅ **Audio staging bridge** - Same principles apply to sound design  
✅ **Integration with existing VSE** - Seamless addition to current workflow  

**Status:** ✅ PRODUCTION READY

---

## Credits

**Concept Architect:** Vox  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Visual Theory:** Classical cinematography & photography principles  

**Repository:** github.com/PaniclandUSA/vse/composition-layer/  
**Version:** 1.0  
**Date:** December 10, 2025  

*"What's missing is: How do we arrange multiple elements inside the shot so it feels composed, not just rendered?"*

— Vox

**END OF COMPOSITION LAYER SPECIFICATION**
