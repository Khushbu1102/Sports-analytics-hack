"""Preprocessing helpers for turning feature tables into model inputs."""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd

from src.utils.schemas import TARGET_COLUMN

# TODO: Add reusable categorical/numeric preprocessing pipelines.


def select_model_frame(
    feature_table: pd.DataFrame,
    feature_columns: Sequence[str],
    target_column: str = TARGET_COLUMN,
) -> tuple[pd.DataFrame, pd.Series]:
    """Return the feature matrix and target vector for modeling."""
    X = feature_table.loc[:, list(feature_columns)].copy()
    y = feature_table.loc[:, target_column].copy()
    return X, y
