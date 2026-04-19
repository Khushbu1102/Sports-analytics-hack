"""Event cleaning stage for the possession modeling pipeline."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pandas as pd

from src.utils.io import resolve_repo_path

# TODO: Implement column selection, dtype fixes, and 360 joins needed downstream.


def build_cleaning_job(paths_config: Mapping[str, object]) -> dict[str, Path]:
    """Return the input/output contract for the cleaning stage."""
    project_root = paths_config.get("project_root", ".")
    raw_files = paths_config.get("raw_files", {})
    intermediate_files = paths_config.get("intermediate_files", {})
    return {
        "events_csv": resolve_repo_path(raw_files["events_csv"], project_root),
        "frames_360_csv": resolve_repo_path(raw_files["frames_360_csv"], project_root),
        "cleaned_events": resolve_repo_path(intermediate_files["cleaned_events"], project_root),
    }


def clean_events_table(
    events: pd.DataFrame,
    frames_360: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Build the cleaned event table used by possession and feature pipelines."""
    raise NotImplementedError("TODO: implement event cleaning and optional 360 enrichment.")


def write_cleaned_events(cleaned_events: pd.DataFrame, output_path: str | Path) -> None:
    """Persist cleaned events to parquet."""
    cleaned_events.to_parquet(output_path, index=False)
