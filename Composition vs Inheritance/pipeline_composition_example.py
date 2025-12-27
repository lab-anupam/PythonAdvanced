"""
pipeline_composition_example.py
--------------------------------
Topic: Composition over Inheritance
Use case: ML / Data Processing Pipeline
"""

# ============================================================
# PIPELINE STEPS
# ============================================================

class Cleaner:
    def run(self, data):
        """Remove None and invalid values"""
        return [x for x in data if isinstance(x, (int, float))]


class Validator:
    def run(self, data):
        """Ensure data is not empty"""
        if not data:
            raise ValueError("Data validation failed: empty dataset")
        return data


class Normalizer:
    def run(self, data):
        """Normalize values between 0 and 1"""
        max_val = max(data)
        return [x / max_val for x in data]


class Logger:
    def run(self, data):
        """Log data length (side-effect allowed here)"""
        print(f"[LOG] Records count: {len(data)}")
        return data


# ============================================================
# PIPELINE (COMPOSITION)
# ============================================================

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step.run(data)
        return data


# ============================================================
# USAGE
# ============================================================

if __name__ == "__main__":
    raw_data = [10, None, 20, "x", 30]

    pipeline = Pipeline([
        Cleaner(),
        Validator(),
        Logger(),
        Normalizer()
    ])

    result = pipeline.run(raw_data)
    print("Final Output:", result)
