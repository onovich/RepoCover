# Research cover design ledger

## Repository identity

- Repository: `onovich/Research`
- What it does: provides AI skills and a publishing workflow for evidence-backed industry research and bilingual web reports.
- Supported promise: evidence-backed research published as clear English and Simplified Chinese reports.
- Public sources checked: repository description and topics, `README.md`, `docs/visual-system.md`, and the existing website-derived RepoCover variants.

## Material diagnosis

- Product interface: visually distinctive, but the catalog, navigation, controls, and long editorial copy become clutter at Social Preview size.
- Brand system: strong. The project documents a mist-green paper surface, dark green ink, serif display type, bilingual controls, and a research ledger as its signature device.
- Standalone hero artwork: none required; the visual system itself is sufficient source material.
- Chosen route: level 2 material-aware reconstruction. Reuse the documented identity and report structure without reproducing the webpage.

## Direction contract

- Must keep: calm green palette, editorial serif headings, English and Simplified Chinese, and the observable signal → constraint → bounded result ledger.
- May simplify: site navigation, report catalog, theme controls, report counts, detailed body copy, and page chrome.
- Must exclude: raw webpage crops, invented metrics, decorative connectors, and any claim not supported by the repository.
- Thumbnail priority: `Research`, the bilingual spread, and the three-part ledger must remain legible at `320×160`.

## Regression hypothesis

- Baseline: `social-preview-v5-directed`, whose right side still reads as a cropped webpage.
- Expected gain: faster recognition as an intentional cover; stronger bilingual and research identity; no screenshot edge, clipped UI, or unexplained line.
- Main risk: the reconstructed report could become a generic dashboard. The composition therefore uses one editorial spread and one documented ledger instead of unrelated cards or charts.

## Acceptance record

- Editable source: `examples/research.svg`
- Website raster: `examples/research.png`
- Exact size: pass (`1280×640`)
- Under 1 MB: pass (`38,827` bytes)
- Full-size review: pass; title, bilingual spread, and ledger are separated without clipping or overlap.
- `320×160` light review: pass; repository name and overall bilingual composition remain recognizable.
- `320×160` dark review: pass; the preview keeps a clear outer edge and does not disappear into the surround.
