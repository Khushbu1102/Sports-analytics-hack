"""Full descriptive possession feature table builder."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Combine benchmark-safe feature families into the full descriptive table.


def full_features_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for the full descriptive feature table."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["full_features"]


def build_full_features(
    possessions: pd.DataFrame,
    start_features: pd.DataFrame,
    early_features: pd.DataFrame,
    pressure_features: pd.DataFrame | None = None,
    progression_features: pd.DataFrame | None = None,
    features_360: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Create the full descriptive benchmark feature table."""
    raise NotImplementedError("TODO: merge benchmark-safe feature families into one table.")
