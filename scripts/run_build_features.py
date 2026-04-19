"""Lightweight runner for benchmark feature-table scaffolding."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.features.build_early_features import early_features_output_path
from src.features.build_full_features import full_features_output_path
from src.features.build_start_features import start_features_output_path
from src.utils.io import load_yaml


def main() -> None:
    """Print canonical output locations for the three benchmark feature views."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    processed_dir = paths_config["data"]["processed_dir"]

    print("Feature stage scaffold")
    print(f"Start-only features: {start_features_output_path(processed_dir)}")
    print(f"Early first-3-events features: {early_features_output_path(processed_dir)}")
    print(f"Full descriptive features: {full_features_output_path(processed_dir)}")
    print("TODO: wire possessions_base.parquet and cleaned_events.parquet into feature builders.")


if __name__ == "__main__":
    main()
