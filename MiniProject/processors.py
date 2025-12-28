"""
processors.py
-------------
Data processing steps for the pipeline.

Each processor:
- Is a class
- Has a single responsibility
- Exposes a run(data) method

Author: Anupam Bhattacharyya
"""

from copy import deepcopy
from decorators import log_execution


# ============================================================
# 1. CLEANER — MUTABILITY BUG (FOR LEARNING)
# ============================================================

class BuggyCleaner:
    """
    ❌ Demonstrates a MUTABILITY bug.
    Mutates input data directly.
    """

    @log_execution
    def run(self, data):
        for item in data:
            if item["value"] is None:
                data.remove(item)   # ❌ modifying list while iterating
        return data


# ============================================================
# 2. CLEANER — SAFE VERSION (CORRECT)
# ============================================================

class Cleaner:
    """
    ✅ Correct cleaner.
    Does NOT mutate input data.
    """

    @log_execution
    def run(self, data):
        # Create a NEW list (safe copy)
        cleaned = [
            item for item in data
            if item.get("value") is not None
        ]
        return cleaned


# ============================================================
# 3. TRANSFORMER
# ============================================================

class Transformer:
    """
    Applies transformations to data values.
    """

    def __init__(self, multiplier=1):
        self.multiplier = multiplier

    @log_execution
    def run(self, data):
        return [
            {
                **item,
                "value": item["value"] * self.multiplier
            }
            for item in data
        ]


# ============================================================
# 4. FEATURE ENGINEER
# ============================================================

class FeatureEngineer:
    """
    Creates derived features (ML-style).
    """

    @log_execution
    def run(self, data):
        max_value = max(item["value"] for item in data)

        return [
            {
                **item,
                "normalized_value": item["value"] / max_value
            }
            for item in data
        ]


# ============================================================
# 5. METRICS CALCULATOR
# ============================================================

class MetricsCalculator:
    """
    Produces summary metrics from processed data.
    """

    @log_execution
    def run(self, data):
        values = [item["value"] for item in data]

        return {
            "count": len(values),
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values)
        }
