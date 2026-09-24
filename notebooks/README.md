# Notebooks

Exploratory Jupyter notebooks live here. They are **NOT part of the production pipeline**.

Purpose: prototyping, visualization, ad-hoc investigation.
Production code lives in `data-pipeline/src/dhara/`.

Guidelines:
- Notebook filenames: `NB{number}_{short_description}.ipynb` (e.g. `NB01_coverage_check.ipynb`)
- Every notebook must have a clear markdown cell at the top explaining its purpose and what it produces.
- Notebooks are NOT run in CI. They are for human exploration only.
- If you write something worth keeping, refactor it into `data-pipeline/src/dhara/` as a proper tested module, then reference it from the notebook.
