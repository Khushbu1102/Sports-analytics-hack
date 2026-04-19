"""Logistic-regression training entry points for benchmark models."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# TODO: Define grouped CV, preprocessing pipeline, and regularization search.


def build_logreg_run_spec(feature_view: str, feature_path: str | Path) -> dict[str, str]:
    """Create a lightweight run spec for a logistic-regression benchmark."""
    return {"model_name": "logreg", "feature_view": feature_view, "feature_path": str(feature_path)}


def train_logistic_regression(feature_table: pd.DataFrame, target_column: str = "shot_label") -> object:
    """Train the logistic-regression benchmark model."""
    raise NotImplementedError("TODO: implement grouped logistic-regression training.")
