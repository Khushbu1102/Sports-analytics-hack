"""Lightweight runner for the cleaning stage scaffold."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.clean_events import build_cleaning_job
from src.data.load_data import build_raw_data_manifest, summarize_available_raw_inputs
from src.utils.io import load_yaml


def main() -> None:
    """Print the cleaning-stage contract and current raw-data availability."""
    paths_config = load_yaml(ROOT / "config" / "paths.yaml")
    manifest = build_raw_data_manifest(paths_config)
    availability = summarize_available_raw_inputs(manifest)
    job = build_cleaning_job(paths_config)

    print("Cleaning stage scaffold")
    print(f"Events CSV: {job['events_csv']}")
    print(f"360 CSV: {job['frames_360_csv']}")
    print(f"Cleaned output: {job['cleaned_events']}")
    print(f"Raw files available: {availability}")
    print("TODO: wire load_events_csv/load_frames_360_csv into clean_events_table.")


if __name__ == "__main__":
    main()
