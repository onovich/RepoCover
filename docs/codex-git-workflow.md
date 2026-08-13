# Codex Git Workflow

RepoCover uses the reusable `git-flow` / `project-git-workflow` entry point.

Before every commit or push:

1. Review `git status --short --branch` and the complete diff.
2. Run `python scripts/check.py`.
3. Stage only the intended RepoCover files.
4. Use a focused conventional commit message.

The remote is `https://github.com/onovich/RepoCover.git`, and the primary branch is `main`.
Releases and repository artwork uploads remain separately authorized actions.
