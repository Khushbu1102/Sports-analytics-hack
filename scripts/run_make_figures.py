"""Lightweight runner for figure-generation scaffolding."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.visualization.eda_plots import eda_figure_path
from src.visualization.model_plots import model_figure_path
from src.visualization.pitch_plots import pitch_figure_path
from src.utils.io import load_yaml


def main() -> None:
    """Print canonical figure locations for EDA, model, and pitch outputs."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    figures_dir = paths_config["outputs"]["figures_dir"]

    print("Figure scaffold")
    print(f"EDA figure example: {eda_figure_path(figures_dir, 'eda_audit.png')}")
    print(f"Model figure example: {model_figure_path(figures_dir, 'benchmark_comparison.png')}")
    print(f"Pitch figure example: {pitch_figure_path(figures_dir, 'example_possession.png')}")
    print("TODO: wire saved tables and trained models into plotting functions.")


if __name__ == "__main__":
    main()
