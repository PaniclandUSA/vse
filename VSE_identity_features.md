⟨VSE::MATERIAL_BEHAVIOR scope="identity_features"⟩

  <!-- ========================= -->
  <!--        TATTOOS            -->
  <!-- ========================= -->
  ⟨feature type="tattoos"⟩
    fate = [etched_relief | inked_subsurface | gold_inlay | omitted]

    ⟨if fate="etched_relief"⟩
      depth_mm = 0.05–2.0
      edge_crispness = 0.0–1.0
      fill = [shadow | gold | enamel | void]
      continuity = smooth
      weathering = 0.0–1.0
    ⟨/if⟩

    ⟨if fate="inked_subsurface"⟩
      depth_below_surface_mm = 0.5–3.0
      clarity = 0.0–1.0
      diffusion = [none | subtle | moderate | heavy]
      diffusion_mm = 0.0–0.5            # expert override
      hue_shift = neutral
      sss_interaction = true
      vein_overlap = partial
      gloss_occlusion = 0.0–1.0
    ⟨/if⟩

    ⟨if fate="gold_inlay"⟩
      inlay_thickness_mm = 0.1–1.0
      glow_amount = 0.0–1.0
      crack_intensity = 0.0–1.0
      metal_fill = gold
      aesthetic_mode = kintsugi
    ⟨/if⟩

    ⟨if fate="omitted"⟩
      removal = 1.0
      memory_trace = false
    ⟨/if⟩
  ⟨/feature⟩


  <!-- ========================= -->
  <!-- FRECKLES / MOLES / MARKS -->
  <!-- ========================= -->
  ⟨feature type="pigmented_marks"⟩
    fate = [preserved | omitted | converted]

    ⟨if fate="preserved"⟩
      render = [surface_spot | subsurface_impurity | raised_inclusion]
      scale = 1.0
      color_inherit = partial
    ⟨/if⟩

    ⟨if fate="converted"⟩
      become = [mineral_inclusion | vein_node | micro_crystal | air_pocket]
      material_identity = quartz        # conceptual
      material_behavior = translucent   # behavioral
      microstructure = cloudy           # structural
      distribution = anchored
    ⟨/if⟩
  ⟨/feature⟩


  <!-- ========================= -->
  <!--          SCARS            -->
  <!-- ========================= -->
  ⟨feature type="scars"⟩
    fate = [deepened | smoothed | omitted | crystallized]

    ⟨if fate="deepened"⟩
      depth_multiplier = 1.0–2.0
      edge_style = [rough | clean | fractured]
    ⟨/if⟩

    ⟨if fate="crystallized"⟩
      material_identity = opal
      material_behavior = iridescent
      microstructure = layered
      glow_amount = 0.25
      crack_intensity = 0.3
      metal_fill = gold
      aesthetic_mode = kintsugi
    ⟨/if⟩
  ⟨/feature⟩


  <!-- ========================= -->
  <!--     SKIN TONE MEMORY      -->
  <!-- ========================= -->
  ⟨feature type="tone_variation"⟩
    fate = [marble_variation | unified | omitted]
    sun_memory = true
    vein_inheritance = partial
  ⟨/feature⟩

⟨/VSE::MATERIAL_BEHAVIOR⟩