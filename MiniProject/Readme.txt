📦 Configurable Data Ingestion & Processing Pipeline
📌 Overview

This project is a real-world, end-to-end backend data pipeline that ingests data from multiple sources, processes it through a configurable pipeline, and produces metrics.

It demonstrates advanced Python fundamentals commonly used in:

Data Engineering

ML Feature Pipelines

Backend & Microservices

Async Systems

🎯 Key Objectives

Fetch data concurrently from multiple sources using async/await

Process data using a composition-based pipeline

Apply logging and timing decorators without modifying business logic

Avoid mutable shared state bugs

Use Pythonic comprehensions for transformations

Build a system that is easy to extend and interview-ready

🧠 Concepts Demonstrated
Topic	How it’s Used
Python Internals & Mutability	Demonstrates mutation bugs and safe copy patterns
List & Dict Comprehensions	Data filtering, feature engineering, metrics
OOP Fundamentals	Clean classes, __init__, single responsibility
Composition over Inheritance	Pipeline accepts pluggable processing steps
Decorators	Logging and timing as cross-cutting concerns
Async Programming	Concurrent ingestion using asyncio.gather
🏗️ Project Structure
data_pipeline_project/
│
├── decorators.py      # Logging & timing decorators
├── ingestion.py       # Async data ingestion layer
├── processors.py      # Data cleaning, transformation & features
├── pipeline.py        # Composition-based pipeline orchestration
├── main.py            # Entry point (end-to-end execution)
└── README.md          # Project documentation

🧩 Architecture Diagram
┌────────────────────┐
│ External Data APIs │
│ (Source A, B, ...) │
└─────────┬──────────┘
          │   async / await
          ▼
┌────────────────────┐
│  Ingestion Layer   │
│  (asyncio.gather)  │
└─────────┬──────────┘
          │   raw data (list of dicts)
          ▼
┌────────────────────┐
│      Pipeline      │
│ (Composition-based)│
└─────────┬──────────┘
          │
          ▼
 ┌──────────────────────────────┐
 │   Processing Steps (Order)   │
 │                              │
 │  1. Cleaner                  │
 │  2. Transformer              │
 │  3. FeatureEngineer          │
 │  4. MetricsCalculator        │
 └─────────┬────────────────────┘
           │
           ▼
┌────────────────────┐
│  Final Output      │
│  (Metrics / Data)  │
└────────────────────┘

🔄 Execution Flow

Async ingestion

Multiple data sources are fetched concurrently

Reduces total latency (I/O-bound optimization)

Pipeline execution

Data flows through each processor step

Each step:

Receives data

Returns new data

Does not mutate shared state

Decorators

Logging and timing applied transparently

No clutter inside business logic

🧪 Example Data Flow
Raw Data (Ingested)
[
  {"id": 1, "value": 10},
  {"id": 2, "value": None},
  {"id": 3, "value": 30}
]

After Cleaning
[
  {"id": 1, "value": 10},
  {"id": 3, "value": 30}
]

After Feature Engineering
[
  {"id": 1, "value": 20, "normalized_value": 0.33},
  {"id": 3, "value": 60, "normalized_value": 1.0}
]

Final Metrics
{
  "count": 2,
  "min": 20,
  "max": 60,
  "avg": 40.0
}

🧠 Design Decisions (Important)
Why Composition?

Steps can be added, removed, or reordered

No fragile inheritance hierarchies

Pipeline logic never changes

Inheritance models identity; composition models behavior

Why Decorators?

Logging and timing are cross-cutting concerns

Avoids duplicated code

Keeps business logic clean

Why Async?

External APIs and databases are slow

Async allows concurrent waiting

Improves throughput without threads

▶️ How to Run
python main.py


Requirements:

Python 3.9+

No external dependencies

🎯 Interview-Ready Explanation (Use This)

I built a configurable async data ingestion and processing pipeline using composition over inheritance. Data is fetched concurrently using async/await, processed through independent pipeline steps, and instrumented with decorators for logging and timing. The design avoids shared mutable state, uses Pythonic comprehensions, and is easily extensible.