"""Raw data loading entry points for events and 360 tables."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pandas as pd

from src.utils.io import resolve_repo_path

# TODO: Add schema normalization for raw columns once source files are pinned.


def build_raw_data_manifest(paths_config: Mapping[str, object]) -> dict[str, Path]:
    """Resolve raw input file locations from the paths config."""
    project_root = paths_config.get("project_root", ".")
    raw_files = paths_config.get("raw_files", {})
    return {
        "events_csv": resolve_repo_path(raw_files["events_csv"], project_root),
        "frames_360_csv": resolve_repo_path(raw_files["frames_360_csv"], project_root),
    }


def summarize_available_raw_inputs(manifest: Mapping[str, Path]) -> dict[str, bool]:
    """Summarize which expected raw inputs are currently available."""
    return {name: path.exists() for name, path in manifest.items()}


def load_events_csv(events_path: str | Path) -> pd.DataFrame:
    """Load the raw StatsBomb events CSV."""
    return pd.read_csv(events_path)


def load_frames_360_csv(frames_path: str | Path) -> pd.DataFrame:
    """Load the raw StatsBomb 360 CSV."""
    return pd.read_csv(frames_path)
