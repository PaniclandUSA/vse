⭐ VSE::IDENTITY_FEATURES v2.3 — Ontology Expansion + Preset System

Official canonical version for Vox, Claude, Grok, Gemini, and all renderer pipelines.

This module governs identity-linked features during VSE material transformation:
tattoos, scars, freckles, moles, pigmentation, and surface microstructure.


---

## A. MATERIAL BEHAVIOR VOCABULARY

Full formalized palette

material_behavior = [
  opaque,            # no light penetration
  translucent,       # diffuses light through volume
  transparent,       # clear, glass-like
  reflective,        # mirror-like, high specular
  iridescent,        # color-shifting, opal-like
  luminous,          # emits soft light
  matte,             # non-reflective, diffuse
  glossy,            # smooth high-specular sheen
  metallic           # conductive metallic reflectance
]


---

## B. MICROSTRUCTURE VOCABULARY

Full microstructure spectrum

microstructure = [
  smooth,
  cloudy,
  layered,
  crystalline,
  fibrous,
  granular,
  veined,
  fractured
]


---

## C. IDENTITY FEATURE TYPES


---

1. Tattoos

<feature type="tattoos">
  fate = [ etched_relief | inked_subsurface | omitted ]
</feature>

Etched Relief Mode

depth_mm: 0.05–2.0
edge_definition: 0.0–1.0
fill_behavior: [ none | shadow | gold_inlay | pigment_inlay ]
weathering: 0.0–1.0
surface_continuity: [ smooth | textured | fractured ]

Inked Subsurface Mode

ink_depth_mm: 0.5–3.0
clarity: 0.0–1.0
diffusion: [ none | subtle | moderate | heavy ]
color_shift: [ neutral | warm | cool | desaturated | monochrome ]
interact_with_translucency: true/false
interact_with_veining: [ none | partial | full ]
gloss_interference: 0.0–1.0

Omitted Mode

removal_completeness: 0.0–1.0
surface_memory: true/false


---

2. Pigmented Marks (Freckles, Moles, Birthmarks)

<feature type="pigmented_marks">
  fate = [ preserved | omitted | converted_to_material_flaws ]
</feature>

Preserved Mode

render_as: [ subsurface_impurity | surface_spot | raised_inclusion ]
size_scaling: 0.5–2.0
color_inheritance: [ full | partial | none ]

Converted to Material Flaws

become: [ mineral_inclusion | vein_node | crystalline_flaw | air_pocket ]
distribution: match_original


---

3. Scars

<feature type="scars">
  fate = [ deepened | smoothed | omitted | crystallized ]
</feature>

Deepened Mode

depth_multiplier: 1.0–3.0
edge_character: [ rough | clean | fractured ]

Crystallized Mode

material_identity: opal
material_behavior: iridescent
microstructure: layered
glow_amount: 0.0–1.0
crack_intensity: 0.0–1.0
metal_fill: [ gold | silver | bronze | platinum | none ]
aesthetic_mode: kintsugi


---

4. Natural Discoloration (Skin Tone Memory)

<feature type="natural_discoloration">
  fate = [ preserved_as_marble_variation | unified_to_base_material | omitted ]
</feature>

Options

sun_exposure_memory: true/false
vein_color_inheritance: true/false


---

## D. PRESET SYSTEM

Simplifies authoring by grouping commonly used identity behaviors.


---

Preset: ancient_relic

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ancient_relic"/>

Loads:

Tattoos → etched_relief, weathering=0.7

Pigmented marks → mineral flaws

Scars → deepened

Discoloration → preserved_as_marble_variation



---

Preset: kintsugi_divine

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="kintsugi_divine"/>

Loads:

Tattoos → gold-inlay etched relief

Scars → crystallized opal + gold veins

Pigmented marks → subsurface impurities

Discoloration → unified



---

Preset: ghost_memory

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ghost_memory"/>

Loads:

Tattoos omitted → faint memory

Pigmented marks omitted

Scars smoothed

Discoloration removed



---

## E. OVERRIDE SYSTEM

Override any preset field inline.

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="kintsugi_divine">
  <override feature="tattoos">
    glow_amount = 0.9
    depth_mm = 1.2
  </override>
</VSE::MATERIAL_BEHAVIOR>


---

## F. FULL EXAMPLE

<VSE::material_transform>
  <material
    base="white_opal_marble"
    translucency="0.42"
    veining="warm_gold"
  />

  <VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ancient_relic">

    <override feature="scars">
      fate = crystallized
      glow_amount = 0.55
      metal_fill = gold
    </override>

  </VSE::MATERIAL_BEHAVIOR>
</VSE::material_transform>

## Eyes (Delegated Behavior)

Eye rendering is governed by the standalone module:

→ **[VSE_eye_behavior.md](./VSE_eye_behavior.md)**

### Integration Rule

Any identity transformation involving eyes MUST declare an `eye_fate` from the eye behavior module.

**Correct usage:**
```xml
⟨VSE::MATERIAL_BEHAVIOR scope="identity_features"⟩
  ⟨use module="VSE::EYE_BEHAVIOR"⟩
    eye_fate = chiseled_illusion
    iris_depth_mm = 0.6
  ⟨/use⟩
  
  ⟨feature type="tattoos"⟩
    fate = etched_relief
    depth_mm = 0.4
  ⟨/feature⟩
⟨/VSE::MATERIAL_BEHAVIOR⟩
Why eyes are not embedded here:
Eyes are a cross-cutting semantic fault line
They intersect material logic, perception logic, and training bias
They require prohibition system to override biological defaults
See eye behavior module for full specification
Default Behavior Warning
If eye_fate is omitted during material transformation, renderers MUST NOT assume biological defaults. This will cause "wet eye regression" (semantic collision between sculptural body and living eyes).
Failure mode example:
marble body + (implicit biological eyes) = semantic collision
Correct approach:
marble body + eye_fate=blank_orb = consistent sculptural logic
