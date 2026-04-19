"""Parsing helpers for StatsBomb-style nested fields."""

from __future__ import annotations

import ast
from typing import Any

# TODO: Add stricter typed parsers once raw field formats are confirmed.


def parse_literal_list(value: Any) -> list[Any]:
    """Parse a Python-literal list stored as text."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return list(ast.literal_eval(str(value)))


def parse_location(value: Any) -> list[float]:
    """Parse a two-value or three-value StatsBomb location field."""
    parsed = parse_literal_list(value)
    return [float(item) for item in parsed]


def parse_visible_area(value: Any) -> list[float]:
    """Parse a flattened visible-area polygon field."""
    parsed = parse_literal_list(value)
    return [float(item) for item in parsed]
