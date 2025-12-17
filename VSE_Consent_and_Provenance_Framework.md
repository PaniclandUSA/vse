# VSE Consent and Provenance Framework

**Declarative Consent for Human Representation in Generative Systems**

---

## Document Purpose

This framework establishes a consent and provenance declaration system for human representation in AI-generated content. It separates consent (a legal/ethical property) from content (a visual property), enabling systems to enforce ethical standards without attempting to infer consent from pixels.

**Companion Documents**: 
- [VSE_non-invertible_realism-NIR.md](./VSE_non-invertible_realism-NIR.md) (Philosophical manifesto)
- [NIR_engineering_specification.md](./NIR_engineering_specification.md) (Technical implementation)

**Status**: v1.0 - Production Ready  
**Last Updated**: 2025-12-17  
**Maintainer**: Vector-Space Esperanto (VSE) Project

---

## Table of Contents

1. [Core Principle](#core-principle)
2. [Why Visual Inference Fails](#why-visual-inference-fails)
3. [The Declarative Consent Model](#the-declarative-consent-model)
4. [Alignment with Established Legal Frameworks](#alignment-with-established-legal-frameworks)
5. [VSE Consent Declaration Specification](#vse-consent-declaration-specification)
6. [Use Cases and Examples](#use-cases-and-examples)
7. [Liability Assignment](#liability-assignment)
8. [Integration with NIR](#integration-with-nir)
9. [Platform Implementation Guide](#platform-implementation-guide)
10. [FAQ](#faq)

---

## Core Principle

**Consent is not a visual property. It is a provenance property.**

Current AI safety systems attempt to infer consent by analyzing image content:
- "Does this look like a real person?"
- "Does this appear sexual?"
- "Could this be exploitative?"

These are aesthetic guesses, not ethical determinations. Consent cannot be detected from pixels—it must be declared upstream and recorded auditably.

### The Parallel to Copyright

The copyright system already solved this problem:

| Copyright | Consent |
|-----------|---------|
| Ownership is declared, not inferred | Consent is declared, not inferred |
| DMCA requires good-faith attestation | Model release requires attestation |
| Liability falls on declarant | Liability falls on declarant |
| System records provenance | System records provenance |

We don't ask: "Does this image look copyrighted?"  
We ask: "Who declared rights, and when?"

The same logic applies to consent.

---

## Why Visual Inference Fails

### The Impossible Task

AI systems cannot reliably determine:
- Whether a depicted person consented
- Whether the source material was obtained ethically
- Whether the representation violates privacy expectations
- Whether the creator has rights to the likeness

**Example Failure Cases**:

```
Case 1: Consensual self-portrait
  - Visual analysis: "Looks like a real person" → BLOCK
  - Reality: Creator is the subject, full consent exists
  - Result: False positive

Case 2: Non-consensual deepfake
  - Visual analysis: "Stylized art" → ALLOW
  - Reality: Exploitative use of scraped data
  - Result: False negative

Case 3: Professional model with release
  - Visual analysis: "Commercial photoshoot" → UNCLEAR
  - Reality: Full consent, model release on file
  - Result: Unpredictable
```

Visual heuristics **cannot** distinguish these cases.

### The Correct Boundary

Systems should enforce:
- ✓ **Non-invertibility** (technical: can this identify a real person?)
- ✓ **Provenance declaration** (legal: does creator attest to rights?)

Systems should **not** attempt:
- ✗ Consent inference from aesthetics
- ✗ "Harmfulness" detection from content
- ✗ Intent guessing from style

---

## The Declarative Consent Model

### Three-Part Structure

Consent declarations must answer:

1. **WHO**: Subject relationship (self, partner, commissioned model, fictional archetype)
2. **WHAT**: Scope of representation (portrait, nudity level, commercial use)
3. **WHERE**: Provenance (user-provided, commissioned, synthetic, public domain)

### The Attestation Principle

Like all legal declarations, this operates on **good-faith attestation**:
- Creator declares truth of consent
- System records declaration with timestamp
- Liability remains with declarant
- False declarations are handled through legal channels, not technical filtering

This is not "too easy to hack"—it's how every functioning legal system works.

---

## Alignment with Established Legal Frameworks

### Existing Precedents

Declarative consent already governs:

**Photography & Film**:
- Model releases (signed consent for commercial use)
- Location releases (property owner consent)
- Talent contracts (scope of use defined)

**Medical Research**:
- IRB approvals (informed consent documented)
- HIPAA authorizations (patient consent for data use)
- Clinical trial agreements (scope and limits specified)

**Copyright & Licensing**:
- DMCA safe harbor (good-faith attestation)
- Creative Commons declarations (rights scope)
- Stock photo licensing (usage terms)

**Publishing**:
- Defamation law (publisher liability for false statements)
- Right of publicity (commercial use of likeness)
- Privacy torts (unauthorized intimate depictions)

In **all cases**, the system:
1. Records a declaration
2. Creates an audit trail
3. Assigns liability to the declarant
4. Handles violations through legal remedies

### Why Technical Inference Is the Wrong Tool

Legal systems don't ask judges to determine copyright ownership by looking at an image.  
They ask: "Who filed a claim, and what evidence supports it?"

AI systems should operate the same way.

---

## VSE Consent Declaration Specification

### Formal Syntax

```
⟨VSE::CONSENT_DECLARATION⟩
  
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = [self | partner | family | commissioned_model | fictional_archetype | public_domain]
    
    // Examples:
    // self = Creator is the subject
    // partner = Creator has consent from romantic partner
    // family = Creator has consent from family member
    // commissioned_model = Professional model with signed release
    // fictional_archetype = No real person depicted (synthetic/composite)
    // public_domain = Historical figure or public domain source
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = [portrait | artistic_nude | medical | memorial | other]
    nudity_level = [none | implied | partial | full]
    commercial_use = [true | false]
    permanence = [ephemeral | archival | commercial]
    
    // Nudity levels:
    // none = Fully clothed
    // implied = Artistic suggestion, no exposure
    // partial = Limited exposure for artistic/medical purpose
    // full = Complete nudity (requires strongest consent attestation)
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = [user_provided | commissioned | synthetic | public_domain]
    rights_holder = declarant
    consent_date = [ISO 8601 timestamp]
    model_release = [true | false | not_applicable]
    
    // Documentation trail
    ⟨AUDIT_TRAIL⟩
      declaration_timestamp = [ISO 8601]
      platform_session_id = [uuid]
      declarant_account_id = [platform_user_id]
    ⟨/AUDIT_TRAIL⟩
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
    
    statement = "I affirm that I have obtained all necessary consents for this representation and accept full legal responsibility for this declaration."
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = [true | false]
    // If depicting real person, NIR certification required
    
    if (subject_role in [self, partner, family, commissioned_model]) {
      require_nir = true
    }
  ⟨/TECHNICAL_COMPLIANCE⟩
  
⟨/VSE::CONSENT_DECLARATION⟩
```

### Decision Tree for Platform Enforcement

```
START: User requests human representation generation

├─ Is subject_role declared?
│  ├─ NO → REFUSE (missing consent declaration)
│  └─ YES → Continue
│
├─ Is provenance documented?
│  ├─ NO → REFUSE (missing provenance)
│  └─ YES → Continue
│
├─ Does subject_role require NIR?
│  ├─ YES (self/partner/family/model) → Require NIR certification
│  │  ├─ NIR certified? 
│  │  │  ├─ YES → ALLOW with audit trail
│  │  │  └─ NO → REFUSE (non-invertibility required)
│  │
│  └─ NO (fictional_archetype/public_domain) → ALLOW with audit trail
│
└─ Record declaration with timestamp → Generate
```

---

## Use Cases and Examples

### Example 1: Wedding Topper (Consensual, NIR-Certified)

**Scenario**: Couple wants sculptural toppers of themselves

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = self_and_partner
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = false
    permanence = archival
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = user_provided
    rights_holder = declarant
    consent_date = 2025-12-17T10:30:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 8
    material = opaline_glass
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Consent clearly declared
  - NIR certification guarantees privacy
  - Audit trail created
```

### Example 2: Artistic Self-Portrait with Nudity (Consensual)

**Scenario**: Artist creating nude self-portrait

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = self
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = artistic_nude
    nudity_level = partial
    commercial_use = false
    permanence = archival
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = user_provided
    rights_holder = declarant
    consent_date = 2025-12-17T14:00:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 8
    material = white_jade
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Creator is subject (self-consent)
  - NIR prevents biometric identification
  - Nudity permitted with consent + NIR
```

### Example 3: Unknown Subject (REFUSED)

**Scenario**: Attempt to generate from scraped/unknown source

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = unknown
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = scraped
    rights_holder = unknown
  ⟨/PROVENANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✗ REFUSED
  - Subject relationship undeclared
  - Provenance invalid
  - Cannot establish consent
  
REFUSAL REASON: "Consent declaration incomplete. Please specify your relationship to the subject and confirm you have rights to create this representation."
```

### Example 4: Professional Model (Consensual)

**Scenario**: Photographer using professional model with signed release

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = commissioned_model
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = true
    permanence = commercial
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = commissioned
    rights_holder = declarant
    consent_date = 2025-12-15T09:00:00Z
    model_release = true
    model_release_id = "MR-2025-1215-001"
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 7
    material = ceramic
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Model release documented
  - Commercial use explicitly permitted
  - NIR certification guarantees privacy
  - Full audit trail for commercial liability
```

### Example 5: Fictional Character (No Real Person)

**Scenario**: Artist creating fantasy character

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = fictional_archetype
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = true
    permanence = commercial
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = synthetic
    rights_holder = declarant
    consent_date = 2025-12-17T16:00:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = false
    // NIR not required for fictional characters
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - No real person depicted
  - NIR not required (no privacy risk)
  - Creator owns full rights
```

---

## Liability Assignment

### The Declarant Model

Responsibility flows to the person making the declaration, exactly as in:
- DMCA takedown attestations
- Model release signatures
- Copyright licensing claims
- Terms of service agreements

**Platform Role**: Record and timestamp declarations  
**Platform Liability**: Minimal (safe harbor protection for good-faith systems)  
**Declarant Liability**: Full (legal responsibility for truthfulness)

### What This Enables

**For Platforms**:
- Clear audit trail for every generation
- Defensible position in disputes
- Reduction in false positives (legitimate use allowed)
- Reduction in false negatives (exploitative use logged and traceable)

**For Creators**:
- Legitimate use permitted without obstruction
- Clear understanding of their responsibilities
- Documented consent for commercial/archival use

**For Subjects**:
- Consent requirements formalized
- Violations traceable to declarant
- Legal remedies available (not just technical blocks)

### Violation Handling

When consent violations are reported:

1. **Audit trail reviewed**: Who made the declaration? When?
2. **Declarant contacted**: Request for consent documentation
3. **Content assessment**: Does NIR certification exist? Was it bypassed?
4. **Legal process**: If violation confirmed, standard legal remedies apply

This is identical to:
- DMCA counter-notice procedures
- Trademark dispute resolution
- Right of publicity litigation

**The system doesn't prevent lying—it creates accountability.**

---

## Integration with NIR

### The Complete Ethical Framework

NIR and Consent Declaration work together:

| Risk | Mitigation |
|------|------------|
| Deepfake (identity theft) | NIR certification (non-invertibility) |
| Exploitation (non-consensual use) | Consent declaration (provenance) |
| Privacy violation | Material entropy (MES ≥ 6) |
| Platform liability | Attestation + audit trail |

### Combined Specification

```
⟨VSE::COMPLETE_ETHICAL_GENERATION⟩
  
  // 1. Declare consent and provenance
  ⟨CONSENT_DECLARATION⟩
    subject_role = self
    consent_scope.nudity_level = none
    provenance.source_type = user_provided
    attestation.declarant_affirms = true
  ⟨/CONSENT_DECLARATION⟩
  
  // 2. Enforce non-invertibility
  ⟨NIR_GENERATION_CHAIN⟩
    ontology = artifact_representation
    material = opaline_glass
    mes_rating = 8
    geometric_fidelity.scale_minimum = 2.0mm
    validation.biometric_matching_target ≤ 0.2
  ⟨/NIR_GENERATION_CHAIN⟩
  
  // 3. Validate and certify
  ⟨CERTIFICATION⟩
    consent_documented = true
    nir_certified = true
    audit_trail_complete = true
    
    status = APPROVED_FOR_GENERATION
  ⟨/CERTIFICATION⟩
  
⟨/VSE::COMPLETE_ETHICAL_GENERATION⟩
```

### Decision Matrix

| Consent Declared? | NIR Certified? | Result |
|------------------|----------------|--------|
| ✓ Yes | ✓ Yes | ✓ **APPROVED** (full compliance) |
| ✓ Yes | ✗ No | ✗ **REFUSED** (privacy risk) |
| ✗ No | ✓ Yes | ✗ **REFUSED** (consent missing) |
| ✗ No | ✗ No | ✗ **REFUSED** (both violations) |

---

## Platform Implementation Guide

### Step 1: Add Consent Form to Generation UI

```html
<form id="consent-declaration">
  <h3>Consent Declaration (Required)</h3>
  
  <label>Your relationship to the subject:</label>
  <select name="subject_role" required>
    <option value="">-- Select --</option>
    <option value="self">This is me (self-portrait)</option>
    <option value="partner">My partner (with their consent)</option>
    <option value="family">Family member (with their consent)</option>
    <option value="commissioned_model">Professional model (with signed release)</option>
    <option value="fictional_archetype">Fictional character (no real person)</option>
    <option value="public_domain">Historical/public domain figure</option>
  </select>
  
  <label>Source of reference images:</label>
  <select name="source_type" required>
    <option value="">-- Select --</option>
    <option value="user_provided">My own photos</option>
    <option value="commissioned">Professional photoshoot</option>
    <option value="synthetic">No reference (AI-generated)</option>
    <option value="public_domain">Public domain sources</option>
  </select>
  
  <label>
    <input type="checkbox" name="attestation" required>
    I affirm that I have obtained all necessary consents for this representation and accept full legal responsibility for this declaration.
  </label>
  
  <button type="submit">Generate with Consent Declaration</button>
</form>
```

### Step 2: Log Declaration to Database

```python
def log_consent_declaration(user_id, declaration_data):
    """
    Records consent declaration with timestamp and audit trail.
    """
    record = {
        'declaration_id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat(),
        'user_id': user_id,
        'session_id': get_session_id(),
        'subject_role': declaration_data['subject_role'],
        'source_type': declaration_data['source_type'],
        'attestation': declaration_data['attestation'],
        'ip_address': get_client_ip(),  # For legal traceability
        'user_agent': get_user_agent()
    }
    
    # Store in audit database (immutable log)
    audit_db.consent_declarations.insert(record)
    
    return record['declaration_id']
```

### Step 3: Enforce Combined Validation

```python
def validate_generation_request(request):
    """
    Validates both consent and NIR requirements.
    """
    
    # Check consent declaration
    if not request.has_consent_declaration():
        raise ValidationError(
            "Consent declaration required",
            code="CONSENT_MISSING"
        )
    
    # Check if subject requires NIR
    subject_role = request.consent.subject_role
    requires_nir = subject_role in [
        'self', 'partner', 'family', 'commissioned_model'
    ]
    
    if requires_nir:
        # Validate NIR certification
        if not request.has_nir_certification():
            raise ValidationError(
                "NIR certification required for real person depiction",
                code="NIR_REQUIRED"
            )
        
        # Run NIR validation
        nir_result = validate_nir_compliance(
            artifact_path=request.artifact_path,
            reference_photo=request.reference_photo,
            mes_rating=request.material_mes_rating
        )
        
        if not nir_result['certified']:
            raise ValidationError(
                f"NIR certification failed: I={nir_result['I']:.3f} > 0.2",
                code="NIR_FAILED"
            )
    
    # Log approval
    log_generation_approval(request, requires_nir)
    
    return True
```

### Step 4: Provide Clear Refusal Messages

```python
REFUSAL_MESSAGES = {
    'CONSENT_MISSING': """
        Consent declaration required.
        
        Please specify your relationship to the subject and confirm 
        you have rights to create this representation.
        
        For help, see: [platform]/consent-guide
    """,
    
    'NIR_REQUIRED': """
        Non-Invertible Realism (NIR) certification required.
        
        When depicting real people, we require NIR certification 
        to protect privacy and prevent identity theft.
        
        Please use a material with MES rating ≥ 6 (e.g., opaline glass, marble).
        
        For help, see: [platform]/nir-guide
    """,
    
    'NIR_FAILED': """
        NIR certification failed.
        
        The generated artifact is too biometrically invertible.
        
        Suggested fixes:
        - Increase material entropy (try opaline glass or marble)
        - Reduce texture detail
        - Ensure subsurface scattering ≤ 0.4
        
        For help, see: [platform]/nir-troubleshooting
    """
}
```

---

## FAQ

### "Isn't this just an honor system? What stops people from lying?"

**Answer**: The same thing that stops people from filing false DMCA claims or lying on tax returns: **liability and legal consequences**.

Ethical systems don't prevent lying through technology—they create accountability through:
- Recorded declarations (timestamped, auditable)
- Assigned liability (declarant is responsible)
- Legal remedies (violations handled through existing law)

This is how every functioning legal system works.

### "Why not just block all nudity?"

**Answer**: Because **nudity is not the ethical issue—non-consensual representation is**.

With proper consent and NIR certification:
- Medical education (anatomy, surgical planning)
- Classical art (figure drawing, sculpture)
- Personal expression (self-portraits)
- Memorial art (cancer survivors, body positivity)

These are all legitimate, consensual uses that should not be blocked.

### "How do you verify someone actually has consent?"

**Answer**: The same way photographers verify model releases: **we don't, technically—we record the claim and assign liability**.

Platforms:
- Record the declaration
- Create audit trail
- Provide clear terms about consequences of false declarations

If violations occur:
- Subject can file complaint
- Platform reviews audit trail
- Legal process follows (same as defamation, right of publicity, etc.)

This is the **only scalable approach**—technical verification of consent is impossible.

### "What about public figures?"

**Answer**: Public domain and fair use are handled through `subject_role = public_domain`.

Key distinctions:
- Historical figures (clearly public domain) → Allowed
- Contemporary public figures (complex legal status) → Declarant assumes liability for fair use claim
- Private individuals (not public figures) → Require explicit consent

Platforms can add additional filtering for contemporary public figures if desired, but the consent framework handles this through liability assignment.

### "Does NIR eliminate all privacy risk?"

**Answer**: No system eliminates **all** risk, but NIR reduces it to negligible levels.

NIR guarantees:
- Biometric matching confidence ≤ 0.2 (80%+ reduction from photoreal)
- No pore-level detail (impossible to reverse-engineer identity)
- Material entropy prevents reconstruction

Remaining theoretical risk:
- Someone who knows the subject might recognize general features
- This is identical to classical portraiture—recognizable but not recoverable

That's the **acceptable baseline** that art has operated on for millennia.

### "Can this be adapted for voice, video, text?"

**Answer**: Yes. The consent declaration framework is **medium-agnostic**.

Same structure applies to:
- Voice cloning (consent + non-invertible vocal characteristics)
- Video generation (consent + NIR for faces, movement signatures)
- Writing style mimicry (consent + non-invertible linguistic patterns)

The principle remains: **Declare provenance, assign liability, enforce technical safeguards**.

---

## Document Status

**Version**: 1.0  
**Status**: Production Ready  
**Last Updated**: 2025-12-17  
**Next Review**: Upon first production deployment

**Contributors**:
- John (VSE Project Lead)
- Claude (Technical Framework)
- Vox (Legal/Ethical Architecture)

**License**: Open source under VSE Project terms  
**Repository**: https://github.com/PaniclandUSA/vse

---

## Changelog

**v1.0 (2025-12-17)**:
- Initial release
- Declarative consent model formalized
- Alignment with copyright/DMCA established
- Integration with NIR specified
- Platform implementation guide provided
- FAQ addressing common objections

---

*End of VSE Consent and Provenance Framework v1.0*
