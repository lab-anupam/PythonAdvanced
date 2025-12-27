"""
python_decorators_real_life_examples.py
======================================

Purpose:
--------
Understand WHY decorators are used through REAL-LIFE examples.

Each example solves a real production problem:
- Logging
- Timing
- Validation
- Authorization
- Retry
- Caching

Author: Anupam Bhattacharyya
"""

from functools import wraps
import time
import random


# ============================================================
# EXAMPLE 1 — LOGGING (MOST COMMON USE CASE)
# ============================================================

def log_execution(func):
    """
    Logs start and end of function execution
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Started {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result
    return wrapper


@log_execution
def load_data():
    print("Loading data from source...")


@log_execution
def clean_data():
    print("Cleaning data...")


# ============================================================
# EXAMPLE 2 — TIMING (PERFORMANCE MONITORING)
# ============================================================

def timing(func):
    """
    Measures execution time
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__}: {end - start:.2f}s")
        return result
    return wrapper


@timing
def heavy_computation():
    time.sleep(1.2)


# ============================================================
# EXAMPLE 3 — INPUT VALIDATION
# ============================================================

def validate_numbers(func):
    """
    Ensures all arguments are numbers
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise ValueError("Only numbers are allowed")
        return func(*args, **kwargs)
    return wrapper


@validate_numbers
def add(a, b):
    return a + b


# ============================================================
# EXAMPLE 4 — AUTHORIZATION (VERY COMMON IN BACKEND)
# ============================================================

def require_admin(func):
    """
    Simple authorization check
    """
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            raise PermissionError("Admin access required")
        return func(user_role, *args, **kwargs)
    return wrapper


@require_admin
def delete_user(user_role, user_id):
    print(f"User {user_id} deleted")


# ============================================================
# EXAMPLE 5 — RETRY ON FAILURE (DATA / API CALLS)
# ============================================================

def retry(max_attempts):
    """
    Retries function execution on failure
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator


@retry(3)
def fetch_remote_data():
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    print("Data fetched successfully")


# ============================================================
# EXAMPLE 6 — CACHING (PERFORMANCE OPTIMIZATION)
# ============================================================

def simple_cache(func):
    """
    Simple in-memory cache
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("[CACHE] Returning cached result")
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@simple_cache
def expensive_calculation(x):
    print("Performing expensive calculation...")
    time.sleep(1)
    return x * x


# ============================================================
# MAIN EXECUTION (RUN STEP BY STEP)
# ============================================================

if __name__ == "__main__":

    print("\n--- LOGGING ---")
    load_data()
    clean_data()

    print("\n--- TIMING ---")
    heavy_computation()

    print("\n--- VALIDATION ---")
    print(add(2, 3))
    # add(2, "x")  # Uncomment to see validation error

    print("\n--- AUTHORIZATION ---")
    # delete_user("user", 101)  # Uncomment to see permission error
    delete_user("admin", 101)

    print("\n--- RETRY ---")
    try:
        fetch_remote_data()
    except Exception:
        print("All retries failed")

    print("\n--- CACHING ---")
    print(expensive_calculation(5))
    print(expensive_calculation(5))  # Cached result
