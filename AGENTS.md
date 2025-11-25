# Repository Guidelines

## Project Structure & Module Organization
- Core learning tracks live in `classifiers/`, `neural-networks/`, `rnns-lstm/`, `transformers/`, and `llm-from-scratch/`. Keep reusable helpers in `utils/`, runnable utilities in `scripts/`, and exploratory work in `notebooks/`.
- Benchmarks and kata-style tasks sit in `benchmarks/`; dataset drops and model artifacts belong in the gitignored `data/` and `models/` folders.
- Favor shared components in `utils/` and `scripts/` instead of duplicating logic inside individual track folders.

## Environment & Setup
- Create the Conda env once with `./setup.sh`, then activate with `conda activate dl-sandbox`. Verify core deps via `python scripts/verify_setup.py`.
- If dependencies change, run `conda env update -f environment.yml --prune`. Keep `environment.yml` as the single source of dependency truth.

## Build, Test, and Development Commands
- Run notebooks: `jupyter lab notebooks/00-getting-started.ipynb` (always inside the `dl-sandbox` env).
- Execute scripts: `python scripts/your_script.py` from the repo root to ensure imports resolve.
- Tests (pytest): `pytest benchmarks/tasks` to exercise the kata suites; add `-k <pattern>` for focused runs.

## Coding Style & Naming Conventions
- Python style: 4-space indentation, descriptive snake_case for functions/variables, PascalCase for classes, and module-level constants in UPPER_SNAKE.
- Formatting: prefer `black` (already listed in `environment.yml`); run `black .` before pushing if you change Python code. Use `pylint` selectively for deeper checks.
- Keep functions small and pure where possible; move shared math/nn utilities into `utils/` to avoid drift across tracks.

## Testing Guidelines
- Use `pytest` for new tests; mirror the existing pattern in `benchmarks/tasks/*/test_*.py`.
- Name tests after behavior (`test_handles_empty_input`) and place them alongside the code under test or in the relevant `benchmarks/tasks` subfolder.
- When adding notebook-driven features, extract core logic into a Python module and cover it with tests to keep notebooks lightweight.

## Commit & Pull Request Guidelines
- Commit messages: short, imperative, and scoped (e.g., `Add softmax utility`, `Refactor RNN training loop`). Avoid bundling unrelated changes.
- PRs should include: a brief summary of the change, how to reproduce results (commands, notebook paths), and any affected datasets or model files. Screenshots/metrics are helpful for training changes.
- Do not commit data or trained weights; keep them in `data/` or `models/` and document download paths or generation commands instead.

## Security & Configuration Tips
- Keep secrets out of the repo; rely on local `.env` files if needed and add paths to `.gitignore`.
- When introducing external datasets, prefer programmatic downloads in scripts with checksum validation rather than storing raw files.
