"""Possession construction utilities built from cleaned event data."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pandas as pd

from src.utils.io import resolve_repo_path

# TODO: Implement possession-level aggregation and `shot_label` assignment.


def build_possession_job(paths_config: Mapping[str, object]) -> dict[str, Path]:
    """Return the input/output contract for possession table creation."""
    project_root = paths_config.get("project_root", ".")
    intermediate_files = paths_config.get("intermediate_files", {})
    return {
        "cleaned_events": resolve_repo_path(intermediate_files["cleaned_events"], project_root),
        "possessions_base": resolve_repo_path(intermediate_files["possessions_base"], project_root),
    }


def build_possessions_base(cleaned_events: pd.DataFrame) -> pd.DataFrame:
    """Aggregate event-level data into one row per possession."""
    raise NotImplementedError("TODO: implement possession grouping and base aggregations.")


def write_possessions_base(possessions: pd.DataFrame, output_path: str | Path) -> None:
    """Persist the possession base table to parquet."""
    possessions.to_parquet(output_path, index=False)
