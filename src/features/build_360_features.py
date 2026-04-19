"""StatsBomb 360-specific feature family builder."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Define off-ball structure and spatial control features from 360 data.


def features_360_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for 360-based features."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["features_360"]


def build_360_features(cleaned_events: pd.DataFrame, frames_360: pd.DataFrame) -> pd.DataFrame:
    """Create 360-derived feature families aligned to possession keys."""
    raise NotImplementedError("TODO: implement 360 feature extraction.")
