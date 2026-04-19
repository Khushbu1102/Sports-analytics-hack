"""Lightweight runner for benchmark model scaffolding."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.modeling.train_logreg import build_logreg_run_spec
from src.modeling.train_xgb import build_xgb_run_spec
from src.utils.io import load_yaml


def main() -> None:
    """Print the training specs for start, early, and full benchmark views."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    processed_files = paths_config["processed_files"]

    run_specs = [
        build_logreg_run_spec("start_only", processed_files["start_features"]),
        build_logreg_run_spec("early_first3", processed_files["early_features"]),
        build_logreg_run_spec("full_descriptive", processed_files["full_features"]),
        build_xgb_run_spec("start_only", processed_files["start_features"]),
        build_xgb_run_spec("early_first3", processed_files["early_features"]),
        build_xgb_run_spec("full_descriptive", processed_files["full_features"]),
    ]

    print("Benchmark training scaffold")
    for run_spec in run_specs:
        print(run_spec)
    print("TODO: wire feature tables into grouped training/evaluation flows.")


if __name__ == "__main__":
    main()
