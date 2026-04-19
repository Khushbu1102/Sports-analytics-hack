"""EDA plotting entry points for raw and cleaned datasets."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# TODO: Add audit plots for missingness, distributions, and possession counts.


def eda_figure_path(figures_dir: str | Path, figure_name: str) -> Path:
    """Build a figure path inside the outputs directory."""
    return Path(figures_dir) / figure_name


def plot_data_audit_summary(cleaned_events: pd.DataFrame) -> object:
    """Generate a high-level audit plot from cleaned events."""
    raise NotImplementedError("TODO: implement EDA audit figures.")
