"""
decorators.py
-------------
Reusable decorators for logging and timing.

Used across:
- ingestion
- pipeline
- processors

Author: Anupam Bhattacharyya
"""

import time
from functools import wraps


def log_execution(func):
    """
    Logs when a function starts and finishes.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Started: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result
    return wrapper


def timing(func):
    """
    Measures execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__}: {end - start:.2f}s")
        return result
    return wrapper
