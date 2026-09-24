# Contributing to DHARĀ

## Branch & PR Workflow

1. **No direct commits to `main`.** All changes come through pull requests.
2. Create a feature branch: `git checkout -b feat/p1.1-coverage-verification`
3. Branch naming: `feat/<task-id>-<short-description>`, `fix/<issue-number>-<description>`, `docs/<what>`
4. Open a PR against `main`. The PR description must reference the task ID (e.g. `Closes #5 — P1.1 AOI coverage verification`).
5. **PRs cannot merge unless the CI check is green.** See `.github/workflows/ci.yml`.
6. Every PR must have at least one reviewer approval before merge.

## Code Standards

- Python: formatted with `ruff format`, linted with `ruff check`. Type hints required on all public functions.
- TypeScript: `eslint` + `prettier` must pass. No `any` types without a comment justifying why.
- All scientific constants (thresholds, weights) must be named constants in a dedicated config file — never magic numbers.

## Acceptance Criteria

Every issue in this repo has a written acceptance criterion. A PR is not "done" until its acceptance criterion is demonstrably met and documented in the PR description.

## Data Policy

- **Never commit raw data files** (`.tif`, `.h5`, `.nc`, `.hdf5`). The `.gitignore` enforces this.
- All data is stored in `data-pipeline/data/` and referenced via the manifest pattern defined in P1.2.
- The `data-pipeline/data/.gitkeep` exists only to hold the directory structure in git.
