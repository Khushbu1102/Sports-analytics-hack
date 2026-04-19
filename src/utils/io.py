"""Shared input/output helpers for configuration and file paths."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# TODO: Centralize artifact writers once data contracts stabilize.


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML file into a plain dictionary."""
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if it does not already exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def resolve_repo_path(path_value: str | Path, project_root: str | Path | None = None) -> Path:
    """Resolve a repo-relative path using an optional project root."""
    base = Path(project_root) if project_root is not None else Path(".")
    return (base / Path(path_value)).resolve()
