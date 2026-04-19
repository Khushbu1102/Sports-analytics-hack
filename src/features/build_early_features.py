"""Early possession feature table builder for first-3-event views."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Implement first-3-events sequence features for the early benchmark.


def early_features_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for early benchmark features."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["early_features"]


def build_early_features(possessions: pd.DataFrame, cleaned_events: pd.DataFrame) -> pd.DataFrame:
    """Create the early first-3-events benchmark feature table."""
    raise NotImplementedError("TODO: implement early sequence features.")
