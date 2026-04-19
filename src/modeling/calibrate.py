"""Calibration utilities for probability outputs."""

from __future__ import annotations

import pandas as pd

# TODO: Add train-fold-safe calibration flows and artifact persistence.


def build_calibration_spec(model_name: str, method: str = "isotonic") -> dict[str, str]:
    """Create a lightweight calibration spec."""
    return {"model_name": model_name, "method": method}


def calibrate_predictions(y_true: pd.Series, y_pred: pd.Series, method: str = "isotonic") -> pd.Series:
    """Calibrate raw probability predictions."""
    raise NotImplementedError("TODO: implement post-hoc calibration.")
