"""Validation utilities for shared dataset contracts."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

# TODO: Add domain-specific checks for possession uniqueness and leakage audits.


def assert_required_columns(
    frame: pd.DataFrame,
    required_columns: Iterable[str],
    table_name: str,
) -> None:
    """Raise an error if a dataframe is missing required columns."""
    missing = [column for column in required_columns if column not in frame.columns]
    if missing:
        raise ValueError(f"{table_name} is missing required columns: {missing}")


def assert_group_disjoint(
    train_groups: Iterable[object],
    test_groups: Iterable[object],
    group_name: str = "match_id",
) -> None:
    """Raise an error if train and test groups overlap."""
    overlap = set(train_groups).intersection(test_groups)
    if overlap:
        raise ValueError(f"Overlapping {group_name} values found: {sorted(overlap)[:5]}")
