"""
python_decorators_from_zero_to_advanced.py
=========================================

Goal:
-----
Understand decorators from ZERO to ADVANCED level
using small, readable examples.

Read this file top-to-bottom.
Run sections one by one if needed.

Author: Anupam Bhattacharyya
"""

# ============================================================
# LEVEL 0 — FUNCTIONS ARE OBJECTS (THE FOUNDATION)
# ============================================================

def hello():
    print("Hello")

# Functions can be assigned to variables
x = hello
x()  # Output: Hello


# ============================================================
# LEVEL 1 — FUNCTIONS CAN BE PASSED AS ARGUMENTS
# ============================================================

def call_function(func):
    """
    func is a function passed as an argument
    """
    func()

def say_hi():
    print("Hi")

call_function(say_hi)  # Output: Hi


# ============================================================
# LEVEL 2 — FUNCTIONS CAN BE RETURNED FROM FUNCTIONS
# ============================================================

def outer():
    def inner():
        print("Inside inner")
    return inner

f = outer()
f()  # Output: Inside inner


# ============================================================
# LEVEL 3 — FIRST REAL DECORATOR (NO @ SYNTAX YET)
# ============================================================

def simple_decorator(func):
    """
    Takes a function and returns a new function
    """
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def greet():
    print("Hello")

# Manual decoration
greet = simple_decorator(greet)
greet()

"""
Output:
Before function
Hello
After function
"""


# ============================================================
# LEVEL 4 — DECORATOR USING @ SYNTAX (SYNTAX SUGAR)
# ============================================================

def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def welcome():
    print("Welcome!")

welcome()

"""
Equivalent to:
welcome = my_decorator(welcome)
"""


# ============================================================
# LEVEL 5 — DECORATORS WITH ARGUMENTS (*args, **kwargs)
# ============================================================

def log(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

@log
def greet_user(name):
    print("Hello", name)

greet_user("Anupam")

"""
Output:
Function started
Hello Anupam
Function finished
"""


# ============================================================
# LEVEL 6 — WHY *args AND **kwargs EXIST
# ============================================================

@log
def add(a, b):
    return a + b

print(add(2, 3))

"""
Decorator works for ANY function signature
"""


# ============================================================
# LEVEL 7 — PROBLEM: FUNCTION METADATA IS LOST
# ============================================================

print(greet_user.__name__)  # wrapper
print(greet_user.__doc__)   # None


# ============================================================
# LEVEL 8 — FIXING METADATA USING functools.wraps
# ============================================================

from functools import wraps

def log_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_with_wraps
def multiply(a, b):
    """Multiply two numbers"""
    return a * b

print(multiply(3, 4))
print(multiply.__name__)   # multiply
print(multiply.__doc__)    # Multiply two numbers


# ============================================================
# LEVEL 9 — TIMING DECORATOR (REAL-WORLD USE)
# ============================================================

import time

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__}: {end - start:.2f}s")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)

slow_function()


# ============================================================
# LEVEL 10 — DECORATORS WITH PARAMETERS
# ============================================================

def repeat(n):
    """
    Decorator factory:
    returns a decorator
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()


# ============================================================
# LEVEL 11 — STACKING DECORATORS (ORDER MATTERS)
# ============================================================

@log_with_wraps
@timing
def process_data():
    time.sleep(0.5)

process_data()

"""
Execution order:
1. log_with_wraps
2. timing
3. process_data
4. timing ends
5. log ends
"""


# ============================================================
# LEVEL 12 — DECORATORS IN CLASS METHODS
# ============================================================

class DataProcessor:

    @log_with_wraps
    def clean(self, data):
        return [x for x in data if isinstance(x, int)]

dp = DataProcessor()
print(dp.clean([1, None, "x", 2]))


# ============================================================
# LEVEL 13 — COMMON MISTAKES (DO NOT DO THIS)
# ============================================================

"""
❌ Forgetting *args, **kwargs
❌ Forgetting return value
❌ Forgetting @wraps
❌ Using decorators for complex logic
"""


# ============================================================
# LEVEL 14 — FINAL SUMMARY (READ THIS)
# ============================================================

"""
Key Takeaways:
--------------
1. Functions are objects
2. Decorators replace functions
3. wrapper() runs instead of original function
4. *args, **kwargs make decorators generic
5. @wraps preserves identity
6. Decorators add behavior without modifying code
"""

# ===================== END OF FILE ==========================
