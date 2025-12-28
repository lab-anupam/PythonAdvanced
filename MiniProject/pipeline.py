"""
pipeline.py
-----------
Pipeline orchestration using composition.

The pipeline:
- Accepts processing steps
- Executes them sequentially
- Is independent of step implementation

Author: Anupam Bhattacharyya
"""

from decorators import log_execution, timing


class Pipeline:
    """
    Orchestrates execution of processing steps.
    """

    def __init__(self, steps):
        """
        steps: list of processor objects
        """
        self.steps = steps

    @log_execution
    @timing
    def run(self, data):
        """
        Run data through all pipeline steps.
        """
        current_data = data

        for step in self.steps:
            step_name = step.__class__.__name__
            print(f"[PIPELINE] Executing step: {step_name}")

            # call a semantic method instead of run
            current_data = step.run(current_data)

        return current_data

