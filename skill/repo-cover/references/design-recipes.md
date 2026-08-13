# GitHub social preview design recipes

Use the repository's visual evidence to choose one recipe. Do not combine every recipe into one canvas.

## Shared grid

- Canvas: `1280×640`, ratio `2:1`.
- Outer safe area: about `72–96` px.
- Primary title: commonly `64–96` px.
- Value statement: commonly `26–38` px.
- Supporting copy: commonly `17–24` px.
- Limit the palette to a background, an ink color, one accent, and a small supporting range unless the product itself requires more colors.
- Give the primary subject at least one third of the canvas.
- Test at `640×320` and `320×160`; remove details that become noise.
- Allocate separate rectangles for copy, product proof, captions, and signatures. Do not let two text regions share the same lower edge or compete for the same corner.

## Product relevance filter

Choose visuals by relevance, not merely by factual availability.

1. State the primary user task in one line.
2. Select one product artifact and at most three facts that prove that task.
3. List secondary features and integrations to exclude.
4. Remove any visible element that does not map to the selected promise or proof.

A real feature can still be the wrong feature for a social preview. Do not foreground telemetry, Git events, architecture internals, or ancillary integrations unless they are central to why a user would choose the project.

## Recipe A: Brand plus product proof

Best for developer tools, Actions, libraries, dashboards, and data products.

- Put the name and value statement on one side.
- Put a faithful chart, terminal result, UI card, or code-native product artifact on the other.
- Use two or three concise proof points only when they distinguish the product.
- Let the product visual carry detail; keep copy calm.

This is the default when a real product artifact is visually legible.

## Recipe B: Product-first crop

Best for applications whose interface is the product.

- Use a real screenshot or a faithful crop across roughly 60–75% of the canvas.
- Protect important UI from edge cropping.
- Place the repository name and one statement in a quiet overlay or adjacent panel.
- Remove browser chrome unless it conveys necessary context.
- Do not shrink an entire desktop screenshot until nothing is readable.

## Recipe C: System diagram

Best for infrastructure, automation, APIs, pipelines, and architecture tools.

- Show one short left-to-right flow with three to five nodes.
- Use repository-native icons or simple labeled shapes.
- Emphasize the transformation or output, not implementation trivia.
- Avoid a dense architecture poster; the diagram must work at thumbnail size.

## Recipe D: Typographic identity

Best for libraries, CLIs, standards, and projects without a meaningful screenshot.

- Use a strong wordmark or repository name as the main visual.
- Add one distinctive code token, command, glyph, pattern, or geometric motif from the project.
- Use whitespace and deliberate alignment instead of decorative filler.
- Do not substitute generic GitHub, terminal, or code imagery for product identity.

## Visual-system extraction

When the project already has a design system:

1. Take colors from actual tokens or assets.
2. Reuse border radii, stroke weights, spacing rhythm, and type hierarchy.
3. Recreate charts or diagrams with the same primitives and data semantics.
4. Use the project name as the brand; avoid introducing a second logo language.

When no system exists, derive a restrained palette from the product domain and choose one clear accent. Avoid default purple gradients, glowing glass panels, random blobs, and stock-code aesthetics unless the repository itself uses them.

## Charts and waveforms

- Define explicit plot bounds and apply an SVG `clipPath` when marks, paths, or screenshots could cross them.
- Reserve about 10–15% vertical breathing room above and below the largest mark; target roughly 70–80% maximum occupied plot height.
- Keep strokes, nodes, labels, and playheads inside the plot that owns them. Never let one chart bleed into a title, neighboring chart, caption, or control row.
- Prefer a representative, calm silhouette over theatrical spikes. Extreme amplitude is appropriate only when it represents real, important data.
- At `320×160`, the chart should read as one recognizable product artifact rather than dense texture.

## Copy rules

- Prefer a concrete outcome: “Validated SVG charts saved in your repository.”
- Avoid vague praise: “The ultimate next-generation developer experience.”
- Prefer proof: “10 layouts · exact percentages · auditable data.”
- Avoid fake social proof, invented usage counts, or unsupported speed claims.
- Keep important text as vector typography; never depend on generated-image text.

## Final rejection checks

Reject or revise a design when:

- it could represent any unrelated GitHub repository after changing only the name;
- the product proof is too small to recognize;
- the image reads like a README screenshot;
- decoration is visually stronger than the repository name;
- a true but secondary feature distracts from the primary user task;
- any text, caption, URL, chart mark, or decoration overlaps another region;
- a chart or waveform touches its panel edge, escapes its plot, or visually dominates the whole card;
- more than one sentence is required to understand the promise;
- transparency causes unpredictable results on different sharing surfaces.

GitHub's documented baseline is PNG, JPG, or GIF under 1 MB, at least `640×320`, with `1280×640` recommended for best display: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview>.
