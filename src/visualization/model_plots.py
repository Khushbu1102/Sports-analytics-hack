"""Model-result plotting entry points."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# TODO: Add ROC, calibration, lift, and benchmark comparison plots.


def model_figure_path(figures_dir: str | Path, figure_name: str) -> Path:
    """Build a model-figure path inside the outputs directory."""
    return Path(figures_dir) / figure_name


def plot_benchmark_comparison(results_table: pd.DataFrame) -> object:
    """Generate a benchmark comparison figure."""
    raise NotImplementedError("TODO: implement benchmark model plots.")
