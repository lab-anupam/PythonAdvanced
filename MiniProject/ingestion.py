"""
ingestion.py
------------
Async data ingestion layer.

Simulates fetching data from multiple external APIs.
Uses async/await to run requests concurrently.

Author: Anupam Bhattacharyya
"""

import asyncio
from decorators import log_execution, timing


# ============================================================
# SIMULATED ASYNC DATA SOURCES
# ============================================================

@log_execution
@timing
async def fetch_source_a():
    """
    Simulates API call to Source A
    """
    await asyncio.sleep(1)  # simulate network delay
    return [
        {"id": 1, "value": 10},
        {"id": 2, "value": None}
    ]


@log_execution
@timing
async def fetch_source_b():
    """
    Simulates API call to Source B
    """
    await asyncio.sleep(1.5)  # simulate slower API
    return [
        {"id": 3, "value": 30},
        {"id": 4, "value": 0}
    ]


# ============================================================
# INGESTION ORCHESTRATOR
# ============================================================

@log_execution
@timing
async def ingest_all_sources():
    """
    Fetch data from all sources concurrently.
    """
    data_sets = await asyncio.gather(
        fetch_source_a(),
        fetch_source_b()
    )

    # Flatten list of lists (comprehension)
    combined_data = [item for dataset in data_sets for item in dataset]

    return combined_data
