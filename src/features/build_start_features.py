"""Start-of-possession feature table builder."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Implement features derived only from the initial possession state.


def start_features_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for start-only features."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["start_features"]


def build_start_features(possessions: pd.DataFrame, cleaned_events: pd.DataFrame) -> pd.DataFrame:
    """Create the start-only benchmark feature table."""
    raise NotImplementedError("TODO: implement start-only possession features.")
