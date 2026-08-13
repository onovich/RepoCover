# RepoCover Agent Notes

## Source of truth

- The canonical installable skill is `skill/repo-cover/`.
- Treat copies under a user's `.codex/skills/` directory as installed artifacts, not development sources.
- Keep repository-facing documentation outside the installable skill directory so it is not loaded into every model context.

## Product invariants

- Output an editable SVG and an exact `1280×640` PNG under 1 MB.
- Ground visible claims, metrics, screenshots, and proof in repository evidence.
- Preserve each repository's identity instead of imposing one template.
- Validate both full size and `320×160` on light and dark surroundings.
- Treat image creation and GitHub upload as separate authorization boundaries.
- Do not use GitHub logos or language that implies GitHub affiliation or endorsement.

## Editing and validation

- Write text files as UTF-8 without BOM.
- Update `agents/openai.yaml` whenever the skill identity or invocation changes.
- Prefer deterministic scripts for fragile or repeated validation steps.
- Run `python scripts/check.py` before committing.
- Forward-test meaningful instruction or visual changes on varied real repositories.

## Release boundaries

- Use `RepoCover` for the product and UI name, `repo-cover` for the skill folder and invocation, and `$repo-cover` in prompts.
- Keep `github-preview` only as a temporary local compatibility alias; do not publish it as a second implementation.
- Follow `docs/RELEASE_CHECKLIST.md` before tagging a release.

<!-- codex-init-flow: initialized -->

## Codex Project Workflow

Initialization status: initialized  
Initialized at: 2026-08-13 14:43:29 +08:00  
Project root: `D:\Skills\RepoCover`  
Git remote: `https://github.com/onovich/RepoCover.git`

Use the configured workflow entry points for routine work:

- `git-flow` / `project-git-workflow` for status, validation, commit, and push.
- `ops-flow` / `project-ops-workflow` for validation and release dry-runs.
- `init-flow` only when intentionally refreshing the project integration.

Configuration and operating notes:

- `.codex/project-git-workflow.json`
- `.codex/project-ops-workflow.json`
- `docs/codex-git-workflow.md`
- `docs/codex-ops-workflow.md`

Do not silently bypass those project-specific commands when the configuration exists.

<!-- /codex-init-flow -->
