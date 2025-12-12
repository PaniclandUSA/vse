# VSE::EYE_BEHAVIOR v1.0

## Overview

Eyes are a **cross-cutting semantic fault line** in material transformations. Models have overwhelming training bias toward biological eye rendering, creating semantic collisions when subjects undergo material transformation (petrification, metallization, vitrification).

This module provides explicit sculptural eye regimes that **override biological defaults**.

## Core Problem: Wet Eye Regression

**Failure pattern observed across models:**
- Subject transforms to marble/stone/chrome
- Body geometry follows material logic correctly
- Eyes revert to biological rendering (corneal moisture, iris gradients, soft blending)
- Result: semantic collision between sculptural body and living eyes

**Root cause:** Models treat eyes as biological_feature → stylized rather than optical_suggestion → geometric_only

**VSE solution:** Explicit eye_fate declaration with prohibition system

---

## The Three Sculptural Eye Regimes

Observed in art-historical sculpture, not theoretical constructs.

### 1. Chiseled Illusion
**"Looks alive, but isn't"**

- Iris/pupil appear present through geometry alone
- No actual lens, moisture, or biological shading
- Readability from faceted planes, rim depth, directional lighting
- Art-historical: Late Renaissance funerary, High Baroque portraits, Michelangelo pupils

### 2. Structural Focus
**"Eyes as directional instruments"**

- No iris/pupil depiction
- Direction implied through eyelid geometry and socket asymmetry
- Upper lid thickness signals gaze
- Art-historical: Greek Classical, Roman copies, minimalist abstraction

### 3. Blank Orb
**"The eternal statue"**

- Smooth convex spheres
- No iris, no pupil, no implied optics
- Expression carried by lids, brows, head tilt only
- Art-historical: Archaic Greek kouroi, Neoclassical marble, museum-grade Roman busts

---

## VSE Specification

```xml
⟨VSE::MATERIAL_BEHAVIOR scope="eyes"⟩
  
  eye_fate = [chiseled_illusion | structural_focus | blank_orb | biological]
  
  <!-- ================================ -->
  <!--    MODE 1: CHISELED ILLUSION     -->
  <!-- ================================ -->
  ⟨if eye_fate="chiseled_illusion"⟩
    iris_method = carved_basin       # concave depression, not color
    iris_depth_mm = 0.3–1.0
    pupil_method = shadow_well       # depth-based darkness, not pigment
    pupil_depth_mm = 0.5–2.0
    
    cornea_treatment = faceted       # angular planes, NOT gloss dome
    catchlight_type = geometric      # sharp edge reflection, not wet highlight
    catchlight_intensity = 0.3–0.7
    
    eyelid_definition = sharp        # crisp plane breaks
    eyelid_thickness_mm = 1.0–3.0
    
    sclera_finish = matte_stone      # never glossy
    optical_illusion = high          # maximize "looks alive" through geometry alone
    
    <!-- CRITICAL PROHIBITIONS -->
    prohibit_corneal_moisture = true
    prohibit_iris_gradient = true    # no color fade, only depth
    prohibit_soft_blending = true    # hard plane transitions only
  ⟨/if⟩
  
  <!-- ================================ -->
  <!--   MODE 2: STRUCTURAL FOCUS       -->
  <!-- ================================ -->
  ⟨if eye_fate="structural_focus"⟩
    iris_method = omitted
    pupil_method = omitted
    
    direction_via = [lid_geometry | socket_asymmetry | ridge_flow]
    upper_lid_prominence = 0.5–1.0   # thickness signals gaze direction
    canthus_depth_asymmetry = 0.3–0.8 # inner/outer corner depth difference
    orbital_rim_dominance = high
    
    abstraction_level = 0.3–0.7      # 0=realistic, 1=minimalist
    sclera_finish = smooth_convex
    
    <!-- CRITICAL PROHIBITIONS -->
    prohibit_iris_suggestion = true
    prohibit_pupil_suggestion = true
    prohibit_biological_detail = true
  ⟨/if⟩
  
  <!-- ================================ -->
  <!--      MODE 3: BLANK ORB           -->
  <!-- ================================ -->
  ⟨if eye_fate="blank_orb"⟩
    orb_geometry = perfect_sphere
    orb_curvature = continuous       # no faceting
    
    iris_method = omitted
    pupil_method = omitted
    
    surface_finish = [matte | satin | polished]
    shadow_location = socket_only    # never within the orb itself
    
    expression_via = [lids | brows | head_tilt]
    
    <!-- CRITICAL PROHIBITIONS -->
    prohibit_iris = true
    prohibit_pupil = true
    prohibit_corneal_detail = true
    prohibit_internal_shadow = true  # orb must be uniform
  ⟨/if⟩
  
  <!-- ================================ -->
  <!--     MODE 0: BIOLOGICAL           -->
  <!-- ================================ -->
  ⟨if eye_fate="biological"⟩
    <!-- Explicit opt-in for living/hybrid subjects -->
    <!-- Use ONLY when wet eyes are intentional -->
    corneal_moisture = true
    iris_gradient = true
    sclera_vascular = partial
  ⟨/if⟩

⟨/VSE::MATERIAL_BEHAVIOR⟩
Art-Historical Presets
⟨preset name="renaissance_funerary"⟩
  eye_fate = chiseled_illusion
  iris_depth_mm = 0.5
  pupil_depth_mm = 1.2
  catchlight_intensity = 0.4
  eyelid_definition = sharp
⟨/preset⟩

⟨preset name="classical_greek"⟩
  eye_fate = structural_focus
  direction_via = lid_geometry
  orbital_rim_dominance = high
  abstraction_level = 0.4
⟨/preset⟩

⟨preset name="neoclassical_marble"⟩
  eye_fate = blank_orb
  orb_geometry = perfect_sphere
  surface_finish = matte
  expression_via = lids
⟨/preset⟩

⟨preset name="baroque_portrait"⟩
  eye_fate = chiseled_illusion
  iris_depth_mm = 0.8
  catchlight_type = geometric
  optical_illusion = high
⟨/preset⟩
Implementation Rules
For Renderers:
Eye fate MUST be explicitly declared in any material transformation involving eyes
Biological is an explicit opt-in, NOT a default fallback
Prohibitions take absolute precedence over model training bias
If eye_fate is omitted, renderer MUST surface an error, not assume biological
For Compositors:
Eyes inherit base material properties (reflectivity, translucency, finish) unless explicitly overridden
Catchlights in sculptural modes are geometric reflections, not biological moisture highlights
Shadow behavior follows material physics, not organic shading
Semantic Collision Detection:
If the following combination is detected, flag as error:
body_material = [stone | metal | glass | crystal]
+ eye_fate = biological
= SEMANTIC COLLISION (unless hybrid_form = true)
Real-World Material References
Chiseled illusion depth calibration:
Pewter engraving: 0.05-0.2mm (shallow, crisp)
Marble bas-relief: 0.5-2.0mm (moderate, reads at distance)
Deep stone carving: 1.5-3.0mm (dramatic, high contrast)
Why prohibitions matter:
prohibit_corneal_moisture prevents wet highlight on stone
prohibit_iris_gradient forces carved depression logic
prohibit_soft_blending maintains sculptural plane breaks
Module Status
Version: 1.0
Stability: Canonical
Dependencies: None (standalone)
Referenced by: VSE_identity_features.md, VSE_material_behavior.md, statue/petrification presets
