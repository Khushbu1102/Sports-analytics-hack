"""Canonical schemas and filenames shared across the project."""

from __future__ import annotations

# TODO: Expand these references into richer schema objects once column-level
# validation rules are agreed across preprocessing and modeling.

POSSESSION_KEY_COLUMNS = ["match_id", "possession", "possession_team"]
TARGET_COLUMN = "shot_label"
MATCH_GROUP_COLUMN = "match_id"

CANONICAL_INTERMEDIATE_FILENAMES = {
    "cleaned_events": "cleaned_events.parquet",
    "possessions_base": "possessions_base.parquet",
}

CANONICAL_PROCESSED_FEATURE_FILENAMES = {
    "start_features": "features_start.parquet",
    "early_features": "features_early_first3.parquet",
    "full_features": "features_full.parquet",
    "pressure_features": "features_pressure.parquet",
    "progression_features": "features_progression.parquet",
    "features_360": "features_360.parquet",
}

LEAKAGE_BLOCKLIST = [
    "shot_*",
    "pass_shot_assist",
    "pass_goal_assist",
    "shot_derived_fields",
]
