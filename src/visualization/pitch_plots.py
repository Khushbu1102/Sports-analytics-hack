"""Pitch-level plotting entry points for soccer possession examples."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# TODO: Add possession-path, pressure, and freeze-frame visualizations.


def pitch_figure_path(figures_dir: str | Path, figure_name: str) -> Path:
    """Build a pitch-plot figure path inside the outputs directory."""
    return Path(figures_dir) / figure_name


def plot_example_possession(cleaned_events: pd.DataFrame, possession_id: tuple[int, int, str]) -> object:
    """Generate a pitch plot for one example possession."""
    raise NotImplementedError("TODO: implement pitch plots for slide-ready examples.")
