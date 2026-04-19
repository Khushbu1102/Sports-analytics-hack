"""Grouped data split helpers for model development."""

from __future__ import annotations

from typing import Iterator

import pandas as pd
from sklearn.model_selection import GroupKFold

from src.utils.schemas import MATCH_GROUP_COLUMN

# TODO: Add temporal or tournament-aware evaluation variants if needed.


def build_group_folds(
    feature_table: pd.DataFrame,
    group_column: str = MATCH_GROUP_COLUMN,
    n_splits: int = 5,
) -> Iterator[tuple[list[int], list[int]]]:
    """Yield grouped train/test indices keyed by match."""
    splitter = GroupKFold(n_splits=n_splits)
    groups = feature_table[group_column]
    return splitter.split(feature_table, groups=groups)
