"""Lightweight runner for feature-family ablation scaffolding."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.utils.io import load_yaml


def main() -> None:
    """Print the processed feature-family files expected for ablation studies."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    processed_files = paths_config["processed_files"]

    print("Ablation scaffold")
    print(f"Pressure features: {processed_files['pressure_features']}")
    print(f"Progression features: {processed_files['progression_features']}")
    print(f"360 features: {processed_files['features_360']}")
    print("TODO: define ablation matrix against the benchmark feature views.")


if __name__ == "__main__":
    main()
