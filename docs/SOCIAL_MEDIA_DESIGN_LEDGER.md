# RepoCover social media design ledger

## Scope

This ledger covers the public launch mosaic and its social-platform variants. These are promotional assets, not replacement GitHub Social Preview files; the canonical repository cover remains `docs/social-preview.svg` and `docs/social-preview.png`.

## Source and claim boundaries

```yaml
repository:
  name: RepoCover
  url: https://github.com/onovich/RepoCover
  visibility: public
  default_branch: main
  local_checkout: D:\Skills\RepoCover

evidence:
  mode: local-static
  inspected:
    - path_or_url: README.md
      proves: RepoCover reads a project before creating a repository cover.
    - path_or_url: skill/repo-cover/SKILL.md
      proves: The accepted output includes an editable SVG and a validated 1280×640 PNG.
    - path_or_url: site/examples/index.html
      proves: Eight public examples cover interfaces, main visuals, workflows, libraries, and Skills.
    - path_or_url: examples/*.png
      proves: The eight displayed covers are actual RepoCover outputs.
  claim_boundaries:
    - Do not imply that every AI coding tool supports Skills.
    - Do not imply GitHub affiliation or endorsement.
    - Do not use repository counts, adoption counts, ratings, or performance claims.

content:
  promise: RepoCover reads the project first, then creates a distinctive repository cover.
  proof:
    - Eight visibly different repository covers.
    - Existing interfaces and project visuals can be preserved and recomposed.
    - Projects without a suitable image can still receive an honest visual direction.
  exclude:
    - Internal terms such as cold start, semantic topology, bounded reconstruction, and evidence mode.
    - Installation detail, upload permissions, and validation implementation.
    - Decorative connectors or diagrams that are not part of the eight real covers.
```

## Source-material diagnosis

The existing `assets/launch-mosaic.png` is a strong deliberate collage: it shows eight complete covers, preserves their different visual identities, and remains readable as a gallery. Its weaknesses are public-facing terminology and a footer that describes internal process language more than user value.

| Source | Role | Identity | Beauty | Ready | Noise | Deficit |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `assets/launch-mosaic.png` | complete artifact | 3 | 3 | 3 | 1 | 1 |
| `assets/plugin-showcase.png` | older brand and workflow summary | 3 | 3 | 1 | 0 | 3 |
| `examples/*.png` | eight complete product examples | 3 | 3 | 2 | 0 | 0 |

### Intervention map

- **Keep:** dark navy field, RepoCover mark, eight complete covers, repository names, two-row gallery, cyan/coral palette.
- **Remove:** `cold start`, `semantic topology`, `bounded reconstruction`, and other internal labels.
- **Repair:** shorten the headline, make every label understandable without knowing RepoCover's internal workflow, simplify the footer.
- **Supplement:** no invented imagery; platform variants may reframe the same gallery and brand elements.
- **Interpretation level:** 1 — clean and reframe.
- **Continuity model:** deliberate collage.

`assets/plugin-showcase.png` was reviewed but not promoted. Its layout is strong, but labels such as `evidence-first` and `one visual language` no longer match the plain public product language.

## Composition and version contract

```yaml
composition:
  production_route: source-hybrid
  regions:
    - name: headline
      purpose: Explain the value in one short sentence.
    - name: example gallery
      purpose: Prove that different repositories receive different covers.
    - name: footer
      purpose: Point to the project and summarize the output.
  line_ledger: []

version:
  baseline: assets/launch-mosaic.png
  candidate: assets/social/repocover-launch-landscape.png
  preservation_contract:
    identity_anchors:
      - RepoCover mark and navy/cyan/coral palette
      - Eight real cover images
      - Deliberate two-row collage
    protected_strengths:
      - Immediate visual variety
      - Complete, uncropped example covers
      - Clear hierarchy at landscape size
    allowed_changes:
      - Plain-language headline, labels, and footer
      - Reflow for square and portrait formats
    forbidden_changes:
      - Replacing real covers with generated approximations
      - Cropping repository names or primary cover subjects
      - Adding unsupported metrics, ratings, or decorative lines
```

## Final outputs

| Asset | Use | Target |
| --- | --- | --- |
| `assets/social/repocover-launch-landscape.png` | Website, X, LinkedIn, launch posts | 1600×1000 source composition |
| `assets/social/repocover-x-en.png` | X native image | 1280×640 |
| `assets/social/repocover-linkedin-en.png` | English LinkedIn and Open Graph image | 1200×627 |
| `assets/social/repocover-linkedin-zh.png` | Chinese Open Graph image | 1200×627 |
| `assets/social/repocover-square-en.png` | English square social post | 1080×1080 |
| `assets/social/repocover-square-zh.png` | Chinese square social post | 1080×1080 |
| `assets/social/repocover-portrait-en.png` | English portrait social post | 1080×1350 |
| `assets/social/repocover-portrait-zh.png` | Chinese portrait social post | 1080×1350 |
| `assets/social/repocover-product-hunt-gallery.png` | Product Hunt gallery | 1270×760 |
| `assets/social/repocover-product-hunt-thumbnail.png` | Product Hunt thumbnail | 240×240 |

## Inspection verdict

- All ten candidate assets were inspected at their full target dimensions and in reduced previews.
- Repository names, headlines, and primary subjects remain visible; the source covers use `contain` placement, so no example is cropped to fill a mismatched card.
- Adobe platform checks returned `resize-only` with no crop and no tradeoffs for the X, LinkedIn, square, and portrait variants that were checked there.
- The Chinese and English type both render correctly, and no decorative connectors or unsupported claims were introduced.
- **Promote:** every file listed in the planned outputs table.
- **Retain but do not promote:** `assets/plugin-showcase.png`.
