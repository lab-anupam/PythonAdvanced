"""
main.py
-------
Entry point for the Configurable Data Ingestion & Processing Pipeline.

Runs:
- Async ingestion
- Composition-based processing pipeline
- Metrics generation

Author: Anupam Bhattacharyya
"""

import asyncio

from ingestion import ingest_all_sources
from processors import (
    Cleaner,
    Transformer,
    FeatureEngineer,
    MetricsCalculator
)
from pipeline import Pipeline


async def main():
    print("\n========== DATA INGESTION ==========\n")

    # 1️⃣ Ingest raw data asynchronously
    raw_data = await ingest_all_sources()
    print("Raw Data:")
    print(raw_data)

    print("\n========== PIPELINE EXECUTION ==========\n")

    # 2️⃣ Configure pipeline using composition
    pipeline = Pipeline(steps=[
        Cleaner(),
        Transformer(multiplier=2),
        FeatureEngineer(),
        MetricsCalculator()
    ])

    # 3️⃣ Run pipeline
    result = pipeline.run(raw_data)

    print("\n========== FINAL OUTPUT ==========\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
