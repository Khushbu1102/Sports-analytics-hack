"""Interpretability entry points for trained benchmark models."""

from __future__ import annotations

import pandas as pd

# TODO: Add coefficient summaries, SHAP hooks, and report-ready artifacts.


def build_interpretation_spec(model_name: str, feature_view: str) -> dict[str, str]:
    """Create a lightweight interpretation spec."""
    return {"model_name": model_name, "feature_view": feature_view}


def summarize_model_behavior(model: object, feature_table: pd.DataFrame) -> pd.DataFrame:
    """Create a model-interpretation summary table."""
    raise NotImplementedError("TODO: implement interpretation outputs.")
