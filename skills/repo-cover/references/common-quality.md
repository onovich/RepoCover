# Common RepoCover quality gates

Apply this reference to every cover, regardless of evidence route.

## Canvas and hierarchy

- Canvas: exact `1280×640`, ratio `2:1`.
- Outer safe area: roughly `72–96` px.
- Primary title: commonly `64–96` px; value statement: `26–38` px; supporting copy: `17–24` px.
- Give the primary product proof at least one third of the canvas.
- Allocate separate regions for copy, product proof, captions, and signature before adding detail.
- Use a restrained palette unless repository evidence requires more colors.
- Test at `640×320` and `320×160`; remove details that become noise.

## Product relevance

1. State the primary user task in one line.
2. Select one product artifact and at most three facts that prove it.
3. List true but secondary facts to exclude.
4. Remove every element that cannot be mapped to the promise or proof.

A factual feature can still be wrong for the cover. Do not foreground telemetry, architecture internals, integrations, badges, or implementation trivia unless they are central to why someone would choose the project.

## Composition recipes

Choose one dominant recipe; do not combine every recipe into one canvas.

- **Brand plus product proof:** name and value statement beside a faithful chart, terminal result, UI artifact, diagram, or code-native proof.
- **Product-first artifact:** one complete, self-contained application, scene, board, editor, or interface artifact owns most of the canvas.
- **System diagram:** one short, evidence-bound flow with three to five nodes; emphasize transformation or output rather than implementation detail.
- **Typographic identity:** strong repository name plus one grounded token, glyph, notation system, or geometric relation when a product artifact would be dishonest.

Code-native SVG is the default for developer tools, libraries, diagrams, charts, and inferred systems. Source pixels or generated illustration are production choices, not design identities.

## Visual-system extraction

When the repository already has a design system:

1. Take colors from actual tokens or assets.
2. Reuse border radii, stroke weights, spacing rhythm, and type hierarchy.
3. Recreate charts and diagrams with the same primitives and data semantics.
4. Use the repository name as the brand; do not introduce a second logo language.

When no system exists, derive a restrained material and palette from the product domain. Avoid default purple gradients, glowing glass panels, random blobs, terminal wallpaper, or stock-code aesthetics unless the repository itself supports them.

## Line semantics

Assign every visible line one role: connector, path, trajectory, boundary, axis, waveform, character skeleton, or inherited source geometry.

- Connectors terminate on visible nodes or ports.
- Paths and trajectories have defensible starts, ends, and direction.
- Boundaries are closed or visibly bounded by the region they define.
- Axes and waveforms remain inside labeled plots.
- Character skeletons connect actual joints and preserve plausible poses.
- Inherited geometry remains only when it belongs to the real scene.
- Decorative lines are prohibited by default; prefer mass, spacing, color, type, texture, or bounded patterns.

Record element, role, endpoints or bounds, and evidence in the line ledger. Remove any line that cannot be explained in one concrete sentence.

## Charts and waveforms

- Define plot bounds and use an SVG `clipPath` when marks may cross them.
- Reserve roughly 10–15% vertical breathing room; aim for 70–80% maximum occupied plot height unless real data requires otherwise.
- Keep marks, labels, playheads, and screenshots inside the owning plot.
- Prefer a representative silhouette over theatrical spikes.
- At `320×160`, the chart should read as one product artifact, not dense texture.

## Copy

- Prefer a concrete outcome over vague praise.
- Use verified proof instead of fake social proof, invented counts, or unsupported speed claims.
- Keep important text as exact vector typography; do not depend on generated-image text.
- Preserve the repository's actual name. Do not invent a translation, alias, branded subtitle, feature, score, room identifier, telemetry value, benchmark, or status.
- Keep the promise understandable in one sentence.

## Universal rejection checks

Reject or revise a design when:

- changing only the name could make it represent an unrelated repository;
- the product proof is too small or the image reads like a README screenshot;
- decoration is stronger than the repository name or primary task;
- text, captions, marks, URLs, or decoration collide or clip;
- a chart escapes its plot or dominates the cover without evidence;
- a line lacks a semantic role, visible endpoints or bounds, or repository evidence;
- a connector ends in empty space or implies an unsupported relationship;
- a background, texture, mask, glyph, component, or empty frame is presented as a finished artifact;
- pure white, near-black, darker panels, glass, gradients, or another preset replace a more suitable material without reason;
- multiple repositories receive the same motif, panel grammar, palette, or layout without product evidence;
- transparency creates unpredictable results on different sharing surfaces.

GitHub's documented baseline is PNG, JPG, or GIF under 1 MB, at least `640×320`, with `1280×640` recommended: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview>.
