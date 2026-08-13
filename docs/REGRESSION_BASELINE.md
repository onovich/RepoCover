# Regression baseline

This document records the public, privacy-safe regression contract for meaningful RepoCover changes. It does not bundle private repository names, source trees, screenshots, or credentials.

## Current accepted baseline

- Acceptance date: 2026-08-14
- Owner-run portfolio size: 63 accessible public and private repositories
- Accepted unit: the latest selected cover for each repository, not one globally shared version number
- Result: 63 of 63 latest selected covers accepted by the project owner
- Public portable evidence: eight example PNGs plus the RepoCover product preview
- External independence: none claimed; this is owner acceptance testing

The internal portfolio covered games, web projects, developer tools, libraries, utilities, and skills. Evidence modes included remote-static inspection, local runtime captures, repository-owned art and UI assets, weak visual references, and repositories with no usable primary visual.

## Failure families the baseline must protect

1. **Template drift:** unrelated repositories converge on the same left-card/right-image split, glass panels, palette, or diagram grammar.
2. **Over-reconstruction:** attractive native subjects, 3D depth, materials, characters, or UI identity are replaced with a cleaner but different product.
3. **Under-interpretation:** whole screenshots retain redundant headings, setup UI, debug text, empty space, or weak captured states.
4. **Fragment tearing:** crops expose partial text, half controls, orphaned borders, or ambiguous screenshot-to-reconstruction seams.
5. **Meaningless lines:** connectors, curves, paths, axes, or graph edges have no evidenced role or valid endpoints.
6. **Topology loss:** parallel, branching, merging, nested, sequential, or independent relations are flattened or overlapped for layout convenience.
7. **Material regression:** meaningful grids, restrained tonal ranges, or project-native surfaces become generic white cards, dark navy panels, or preset gradients.
8. **Literalization:** mathematical, sonic, geometric, or workflow identities become generic cubes, controllers, panels, or tutorial props.
9. **Asset-role misuse:** masks, textures, backgrounds, empty frames, glyphs, or component sprites are presented as finished product visuals.
10. **Pseudo-evidence:** inferred covers invent translated names, product aliases, features, scores, room identifiers, telemetry, status, or benchmarks.

## Portable regression examples

| Artifact | Route and protected behavior |
|---|---|
| `examples/prismdraft.png` | Preserve faceted 3D product identity. |
| `examples/littlepng.png` | Present a local-first browser product without generic code imagery. |
| `examples/deskmochi.png` | Preserve character and desktop-companion identity. |
| `examples/audiotrim.png` | Keep waveform and editor proof bounded and legible. |
| `examples/beat.png` | Cold-start symbolic abstraction retains frequency-band and beat-event semantics. |
| `examples/justgoal-skill.png` | Branches, parallel reviews, merge, gate, main path, and fix loop remain visible. |
| `examples/knot.png` | Genuine geometry overlap and projection relations use a purposeful drafting material. |
| `examples/ping.png` | Weak runtime evidence becomes a bounded game artifact without fabricated score or telemetry. |

These artifacts test transferable rules; they are not layouts to reproduce.

## Review protocol for meaningful changes

For instruction changes that affect visual judgment:

1. Run `python scripts/check.py`.
2. Forward-test varied repositories without revealing the desired output or suspected failure to the generator.
3. Inspect each candidate at full size and exact `320×160` on light and dark surroundings.
4. When a previous cover exists, compare source, preferred baseline, and candidate; use the ten-dimension no-regression review.
5. For batches, inspect a contact sheet for repeated layout or material grammar.
6. Record `promote`, `retain-baseline`, or `reject` only after visual inspection.
7. Update this document only when the accepted regression contract or public evidence changes.

Do not claim that the owner-run 63-repository set was rerun unless it actually was. A smaller forward test can validate a scoped change when its limitations are stated.
