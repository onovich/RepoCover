# RepoCover design ledger template

## Contents

- [Use the ledger](#use-the-ledger)
- [Template](#template)
- [Portfolio extension](#portfolio-extension)

## Use the ledger

Create one ledger entry per repository. Store it beside the batch or output artifacts in Markdown, JSON, or both. Keep paths and URLs durable; do not place the only record in a temporary directory.

Omit route-specific sections that do not apply. Never fill an empty field with invented evidence.

## Template

```yaml
repository:
  name: ""
  url: ""
  visibility: public | private | unknown
  default_branch: ""
  local_checkout: ""

evidence:
  mode: remote-static | local-static | build-tested | runtime-tested
  inspected:
    - path_or_url: ""
      proves: ""
  claim_boundaries:
    - ""

content:
  promise: ""
  proof:
    - ""
  exclude:
    - ""

source_route:
  artifacts:
    - path_or_url: ""
      role: complete-artifact | brand | subject | component | glyph | mask | texture | background | weak-reference
      identity_value: 0
      intrinsic_beauty: 0
      composition_readiness: 0
      noise_burden: 0
      information_deficit: 0
  intervention:
    keep: []
    remove: []
    repair: []
    supplement:
      - cue: ""
        provenance: ""
  interpretation_level: 0 | 1 | 2 | 3
  continuity_model: continuous-scene | isolated-artifact | deliberate-collage
  aspect_fit:
    source_bounds: ""
    target_bounds: ""
    method: cover | contain | explicit-crop | extracted-recomposition
    unused_area: ""
    verdict: pass | fail
  fragment_ledger:
    - source_region: ""
      semantic_unit: ""
      crop_boundary: ""
      adjacency: ""
      thumbnail_verdict: pass | fail

cold_start_route:
  semantic_skeleton:
    objects: []
    actions: []
    topology: ""
    outcome: ""
  representation: symbolic-abstraction | structural-diagram | product-form-illustration | typographic-identity
  material_plan:
    background_surface_relation: ""
    character: ""
    semantic_texture_or_grid: ""
    contrast_and_focus: ""
    region_separation: ""
  direction_hypotheses:
    chosen: ""
    rejected: ""
    rejection_reason: ""

composition:
  production_route: code-native-svg | source-hybrid | illustration-hybrid
  regions:
    - name: ""
      bounds: ""
      purpose: ""
  line_ledger:
    - element: ""
      role: ""
      endpoints_or_bounds: ""
      evidence: ""

version:
  baseline: ""
  candidate: ""
  preservation_contract:
    identity_anchors: []
    protected_strengths: []
    allowed_changes: []
    forbidden_changes: []
  comparison_scores: {}
  vetoes: []
  verdict: promote | retain-baseline | reject | not-applicable
  reason: ""

output:
  svg: ""
  png: ""
  review_sheet: ""
  width: 1280
  height: 640
  bytes: 0
  mechanical_validation: pass | fail
  full_size_review: pass | fail
  thumbnail_light_review: pass | fail
  thumbnail_dark_review: pass | fail
  batch_contact_review: pass | fail | not-applicable

authorization:
  readme_modified: false
  github_uploaded: false
  upload_verification: not-requested | pending | publicly-verified
```

## Portfolio extension

For portfolio triage, add `maturity`, `cover_worthiness`, `confidence`, and a plain-language explanation before creating a design entry. For a skipped repository, record the evidence and reason but do not fabricate a cover ledger.
