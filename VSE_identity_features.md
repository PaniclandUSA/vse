##⭐ VSE::IDENTITY_FEATURES v2.3 — Ontology Expansion + Preset System

This is now the OFFICIAL, canonical version ready for Vox, Claude, Grok, Gemini, and all renderer pipelines.


---

**A. MATERIAL BEHAVIOR VOCABULARY

(Full formalized palette)**

<!-- Material Behavioral Vocabulary -->
material_behavior = [
  opaque,           # no light penetration
  translucent,      # diffuses light through volume
  transparent,      # clear, glass-like
  reflective,       # mirror-like, high specular
  iridescent,       # color-shifting, opal-like
  luminous,         # emits soft light
  matte,            # non-reflective, diffuse only
  glossy,           # smooth high-specular sheen
  metallic          # conductive metallic reflectance
]


---

**B. MICROSTRUCTURE VOCABULARY

(Full structural ontology)**

<!-- Microstructure Options -->
microstructure = [
  smooth,           # uniform, featureless surface
  cloudy,           # soft density variations
  layered,          # stratified bands (opal, agate)
  crystalline,      # faceted or geometric grain
  fibrous,          # threadlike internal patterns
  granular,         # grain-like mineral clusters
  veined,           # marble-style linework
  fractured         # fine break-lines or stress textures
]

ALL of these can now be attached to any identity-feature transformation.


---

**C. METAL FILL OPTIONS FOR SCARS

(Full kintsugi-compatible metal palette)**

⟨if fate="crystallized"⟩
  material_identity = opal
  material_behavior = iridescent
  microstructure = layered
  glow_amount = 0.25
  crack_intensity = 0.3
  
  metal_fill = [gold | silver | bronze | platinum | copper | none]
  
  aesthetic_mode = kintsugi
⟨/if⟩

Why this matters:

gold → divine, ceremonial

silver → cold purity

bronze → ancient armor aesthetic

platinum → ultra-luxury, mirror-white refraction

copper → warm rustic oxidation potential

none → pure crystalline scars, no metallic fill


This is artistically and narratively accurate.


---

D. PRESET SYSTEM (NEW)

This is a MASSIVE usability upgrade.

Users can now invoke entire styles without manually specifying 15–30 lines.


---

⭐ Preset Architecture

⟨VSE::MATERIAL_BEHAVIOR 
    scope="identity_features" 
    preset="preset_name"⟩

  ⟨override feature="tattoos"⟩
      ...optional adjustments...
  ⟨/override⟩

⟨/VSE::MATERIAL_BEHAVIOR⟩


---

⭐ PRESET LIBRARY v1.0

(I built four presets to demonstrate the power.)


---

1. ancient_relic

Weathered, eroded, archaeological.

preset="ancient_relic"

tattoos → etched_relief  
  depth_mm = 0.8  
  edge_crispness = 0.3  
  weathering = 0.7  
  fill = shadow  

pigmented_marks → converted  
  become = mineral_inclusion  
  microstructure = granular  

scars → deepened  
  depth_multiplier = 1.4  
  edge_style = fractured  

tone_variation → marble_variation  
  sun_memory = true


---

2. kintsugi_divine

Gold inlay + spiritual glow.

preset="kintsugi_divine"

tattoos → gold_inlay  
  inlay_thickness_mm = 0.6  
  glow_amount = 0.7  
  crack_intensity = 0.4  

scars → crystallized  
  metal_fill = gold  
  glow_amount = 0.5  

pigmented_marks → preserved  
  render = raised_inclusion  

tone_variation → unified


---

3. ghost_memory

Barely-there subsurface hints.

preset="ghost_memory"

tattoos → inked_subsurface  
  clarity = 0.2  
  diffusion = subtle  
  gloss_occlusion = 0.6  

pigmented_marks → omitted  
  memory_trace = true  

scars → smoothed  

tone_variation → unified


---

4. modern_minimal

Clean, sleek, contemporary sculpture.

preset="modern_minimal"

tattoos → omitted  
pigmented_marks → omitted  
scars → omitted  
tone_variation → unified


---

⭐ **NOW THE FULL UPGRADED MODULE:

VSE::IDENTITY_FEATURES v2.3 (Final)**

Here is the complete system including A–D:

⟨VSE::MATERIAL_BEHAVIOR scope="identity_features"⟩

  <!-- Material Behavior Vocabulary -->
  material_behavior = [
    opaque, translucent, transparent,
    reflective, iridescent, luminous,
    matte, glossy, metallic
  ]

  <!-- Microstructure Vocabulary -->
  microstructure = [
    smooth, cloudy, layered, crystalline,
    fibrous, granular, veined, fractured
  ]

  <!-- TATTOOS -->
  ⟨feature type="tattoos"⟩
    fate = [etched_relief | inked_subsurface | gold_inlay | omitted]
    ...
  ⟨/feature⟩

  <!-- PIGMENTED MARKS -->
  ⟨feature type="pigmented_marks"⟩
    fate = [preserved | omitted | converted]
    ...
  ⟨/feature⟩

  <!-- SCARS -->
  ⟨feature type="scars"⟩
    fate = [deepened | smoothed | omitted | crystallized]
    metal_fill = [gold | silver | bronze | platinum | copper | none]
    ...
  ⟨/feature⟩

  <!-- SKIN TONE MEMORY -->
  ⟨feature type="tone_variation"⟩
    fate = [marble_variation | unified | omitted]
    sun_memory = true
    vein_inheritance = partial
  ⟨/feature⟩

⟨/VSE::MATERIAL_BEHAVIOR⟩
