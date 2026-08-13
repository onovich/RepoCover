# Source-material route

Use this route when the repository provides screenshots, runtime captures, logos, illustrations, SVGs, sprites, textures, or other meaningful visual evidence.

## Contents

- [Assess the source](#assess-the-source)
- [Set the reconstruction radius](#set-the-reconstruction-radius)
- [Write the intervention map](#write-the-intervention-map)
- [Choose an interpretation level](#choose-an-interpretation-level)
- [Extract and recompose](#extract-and-recompose)
- [Protect fragments and seams](#protect-fragments-and-seams)
- [Preserve dimensional identity](#preserve-dimensional-identity)

## Assess the source

Inventory the strongest artifacts and identify the project's recognizable anchors: subject silhouette, camera, dimensionality, material, lighting, palette, spatial topology, UI rhythm, or character design.

Score each source from `0` to `3` on:

- **Identity value:** recognizable project identity.
- **Intrinsic beauty:** subject, palette, material, lighting, rhythm, and authorship.
- **Composition readiness:** focal point, balance, scale, and negative space for `2:1`.
- **Noise burden:** browser chrome, headings, setup UI, debug text, empty state, duplicated copy, or incidental HUD.
- **Information deficit:** the mechanic, transformation, result, or state missing from the frame.

Do not average these into an automatic route. High identity plus high noise calls for selective extraction, not direct screenshot use or total reconstruction.

## Set the reconstruction radius

- **Strong source:** preserve the primary subject and visual medium; crop, mask, rebalance, simplify surrounding UI, and add typography.
- **Moderate source:** preserve the strongest subject or mechanic and rebuild weak framing, empty space, or secondary UI only.
- **Weak but relevant source:** construct a bounded product artifact from repository evidence and state what was observed versus inferred.

The stronger the identity, the smaller the redesign radius. Do not use a screenshot as a loose prompt for unrelated artwork. Map protected regions before placing copy, and keep overlays outside characters, gameplay targets, controls, chart marks, and existing headings.

## Write the intervention map

- **Keep:** exact subjects or regions that must remain recognizable.
- **Remove:** redundant or unattractive regions removed by crop, mask, replacement field, or omission.
- **Repair:** hierarchy, crop, balance, contrast, spacing, scale, or focal separation defects.
- **Supplement:** the minimum missing cue required to understand the product, with its evidence source.

If `Remove` and `Supplement` are empty, explain why the source is genuinely cover-ready. Omit any supplement that cannot be traced to code, assets, documentation, another observed state, or an established mechanic.

## Choose an interpretation level

| Level | Treatment | Appropriate use |
|---:|---|---|
| 0 | Cover-ready crop | Rare, self-contained source with strong composition and no harmful clutter |
| 1 | Clean and reframe | Strong focal subject; remove only incidental composition |
| 2 | Selective extraction and recomposition | Distinctive source with both attractive and weak regions; preferred middle route |
| 3 | Bounded reconstruction | Mechanic is proven but the observed state is empty, cluttered, or unreadable |

The level is a budget, not a target to exhaust. Prefer level 1 or 2 when project-native material can remain recognizable. Record expected gains before rendering and verify them afterward.

## Extract and recompose

1. Capture or select a representative state. When safe, interact past empty landing, loading, or setup states to reveal the primary task.
2. Treat the source as evidence and a visual dictionary, not automatically as the final canvas.
3. Extract protected subjects, palette, mechanic, signature shapes, useful UI fragments, typographic rhythm, and dimensional cues.
4. Remove page headings, browser layout, empty regions, secondary controls, and incidental UI that do not prove the promise.
5. Preserve semantic relationships rather than original pixel positions.
6. Embed raw pixels only when a faithful, self-contained crop remains the clearest proof; record whether pixels were embedded.
7. When Pages is unavailable, prefer a safe local runtime capture from an existing checkout and record the checkout and validation boundary. Do not present localhost as a durable product URL.

Use masks, cutouts, tonal grading, depth fields, and typography to create a poster composition. Avoid repeatedly placing a left information card beside a rectangular screenshot.

## Protect fragments and seams

Choose exactly one continuity model before combining source and reconstructed material:

1. **One continuous scene:** perspective, scale, grid, background, borders, lighting, and information density agree across every seam.
2. **Isolated complete artifact:** a device, panel, card, character, board, chart, or scene has an unambiguous visible or masked boundary.
3. **Deliberate collage:** heterogeneous regions use a real gap, frame, material change, overlap, or bounded silhouette that makes discontinuity intentional.

Never leave an accidental strip that looks like the top of a reconstructed interface.

For every fragment check:

- **Semantic closure:** do not cut words, title bars, toolbar groups, cards, buttons, counters, status rows, bodies, boards, or other expected units.
- **Edge closure:** end at a natural object, viewport, mask, panel, or background boundary; no orphaned border, half icon, clipped label, or unexplained rule.
- **Adjacency truth:** touching regions that look continuous must describe the same spatial or UI state.
- **Duplication:** remove headings, HUD, or controls repeated by cover typography or reconstruction.
- **Thumbnail integrity:** the seam remains coherent or intentionally separated at `320×160`.

If a fragment cannot pass, extract its palette, material, signature shapes, or non-text subject and reconstruct a bounded artifact instead of embedding the pixels.

## Preserve dimensional identity

Do not flatten a 3D or 3D-to-2D project into generic 2D illustration unless the user explicitly requests a new art direction. Preserve perspective, volume, material, lighting, depth cues, camera, and scene geometry with source pixels or technically faithful reconstruction.

Do not replace a distinctive character, game world, diagram topology, or interface language with a cleaner but different-looking product.

Reject or revise the source route when a strong screenshot is used almost whole despite removable noise, a reconstruction adds beauty without fixing a diagnosed deficit, a crop exposes a partial semantic unit, or a source-to-reconstruction boundary still reads as a rendering tear.
