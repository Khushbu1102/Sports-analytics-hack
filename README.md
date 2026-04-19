# Soccer Possession-to-Shot Probability

Minimal repository scaffolding for a team project that predicts whether a possession ends in a shot using StatsBomb World Cup 2022 event and 360 data.

## Project Goal

The modeling target is whether a possession ends in a shot. The repository is organized so teammates can work in parallel on:

- preprocessing and possession construction
- feature engineering
- benchmark modeling and evaluation
- visualization and slides

The focus of this scaffold is stable file contracts and clean module boundaries, not a finished implementation.

## Core Data Contract

- Possession key: `match_id`, `possession`, `possession_team`
- Target label: `shot_label`
- Grouped validation unit: `match_id`

These identifiers should stay consistent across cleaned events, possession tables, feature tables, and model outputs.

## Benchmark Views

The initial benchmark modeling work should support three views of the possession:

1. `start-only`
2. `early first-3-events`
3. `full descriptive`

These views should be built into separate feature tables so modelers can compare them without changing upstream preprocessing logic.

## Leakage Rules

Predictive feature sets must exclude direct or indirect shot outcome leakage. In particular:

- no `shot_*`
- no `pass_shot_assist`
- no `pass_goal_assist`
- no shot-derived fields in predictive models

If a field is only known because the possession ultimately resulted in a shot, it should not enter training data.

## Expected File Flow

The intended pipeline contract is:

`raw csv -> cleaned_events.parquet -> possessions_base.parquet -> feature tables -> models -> outputs`

Canonical filenames are defined in [src/utils/schemas.py](/c:/Users/rohan/Documents/Sports-analytics-hack/src/utils/schemas.py).

## Repository Layout

- `config/`: path, feature, and modeling contracts
- `data/`: raw, interim, and processed datasets
- `notebooks/`: analysis notebooks by stage
- `src/data/`: ingestion, cleaning, possession logic, and data splits
- `src/features/`: benchmark and feature-family builders
- `src/modeling/`: preprocessing, training, evaluation, calibration, interpretation
- `src/visualization/`: EDA, model, and pitch-specific plotting
- `scripts/`: lightweight runners for reproducible stage entry points
- `outputs/`: generated tables, figures, and logs
- `slides/`: presentation assets

## Team Parallelization Guidance

- Preprocessing owner: `src/data/`, `src/utils/validation.py`, `config/paths.yaml`
- Feature owner: `src/features/`, `config/features.yaml`
- Modeling owner: `src/modeling/`, `config/modeling.yaml`
- Visualization/slides owner: `src/visualization/`, `notebooks/05_final_figures.ipynb`, `slides/`

The key unblockers for everyone else are:

- `config/paths.yaml`
- `src/utils/schemas.py`
- `src/data/clean_events.py`
- `src/data/build_possessions.py`

## Getting Started

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Put raw StatsBomb files in `data/raw/`.
4. Use the runner scripts in `scripts/` as stage entry points while modules are implemented.

The existing exploratory notebook in `code/Khush_EDA.ipynb` is left untouched and can be migrated later if useful.
