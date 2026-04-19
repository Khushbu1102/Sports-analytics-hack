"""Progression-oriented feature family builder."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Define territory gain, speed, and progression shape features.


def progression_features_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for progression features."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["progression_features"]


def build_progression_features(possessions: pd.DataFrame, cleaned_events: pd.DataFrame) -> pd.DataFrame:
    """Create progression-oriented features for downstream models."""
    raise NotImplementedError("TODO: implement progression feature extraction.")
