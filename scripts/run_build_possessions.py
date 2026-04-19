"""Lightweight runner for the possession-building scaffold."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.build_possessions import build_possession_job
from src.utils.io import load_yaml


def main() -> None:
    """Print the possession-building contract for the current repo config."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    job = build_possession_job(paths_config)

    print("Possession stage scaffold")
    print(f"Cleaned input: {job['cleaned_events']}")
    print(f"Possession output: {job['possessions_base']}")
    print("TODO: wire cleaned_events.parquet into build_possessions_base.")


if __name__ == "__main__":
    main()
