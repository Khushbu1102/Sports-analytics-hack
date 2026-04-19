"""Pressure-oriented feature family builder."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.schemas import CANONICAL_PROCESSED_FEATURE_FILENAMES

# TODO: Define pressure, nearby-defender, and contest-state features.


def pressure_features_output_path(processed_dir: str | Path) -> Path:
    """Return the canonical output path for pressure features."""
    return Path(processed_dir) / CANONICAL_PROCESSED_FEATURE_FILENAMES["pressure_features"]


def build_pressure_features(cleaned_events: pd.DataFrame, frames_360: pd.DataFrame | None = None) -> pd.DataFrame:
    """Create pressure-oriented features that can feed ablation studies."""
    raise NotImplementedError("TODO: implement pressure feature extraction.")
