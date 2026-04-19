"""XGBoost training entry points for benchmark models."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# TODO: Define grouped CV, parameter search, and model persistence for XGBoost.


def build_xgb_run_spec(feature_view: str, feature_path: str | Path) -> dict[str, str]:
    """Create a lightweight run spec for an XGBoost benchmark."""
    return {"model_name": "xgb", "feature_view": feature_view, "feature_path": str(feature_path)}


def train_xgb_model(feature_table: pd.DataFrame, target_column: str = "shot_label") -> object:
    """Train the XGBoost benchmark model."""
    raise NotImplementedError("TODO: implement grouped XGBoost training.")
