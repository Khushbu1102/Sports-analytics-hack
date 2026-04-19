"""Evaluation entry points for grouped benchmark experiments."""

from __future__ import annotations

import pandas as pd

# TODO: Add grouped CV metric aggregation and output-table persistence.


def build_evaluation_spec(model_name: str, feature_view: str) -> dict[str, str]:
    """Create a lightweight evaluation spec for a benchmark run."""
    return {"model_name": model_name, "feature_view": feature_view}


def evaluate_predictions(y_true: pd.Series, y_pred: pd.Series) -> dict[str, float]:
    """Evaluate probability predictions for the shot label."""
    raise NotImplementedError("TODO: implement benchmark metric calculations.")
