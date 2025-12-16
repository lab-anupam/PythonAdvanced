"""
python_comprehensions_notes.py
--------------------------------
Author: Anupam Bhattacharyya
Topic: List, Dict, Set & Generator Comprehensions (Advanced)
Use case: Interviews, Data Engineering, AI/ML pipelines
"""

# ============================================================
# 1. LIST COMPREHENSIONS
# ============================================================

# Basic mapping
nums = [1, 2, 3, 4]
squares = [n ** 2 for n in nums]

# Filtering
evens = [n for n in range(10) if n % 2 == 0]

# if–else (ternary inside comprehension)
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]

# Nested loops
pairs = [(i, j) for i in range(2) for j in range(3)]

# Flattening a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]

# Flatten + filter
even_flat = [x for row in matrix for x in row if x % 2 == 0]


# ============================================================
# 2. DICT COMPREHENSIONS
# ============================================================

# Basic dict comprehension
square_map = {n: n ** 2 for n in range(5)}

# Filtering values
scores = {"A": 80, "B": 55, "C": 90}
passed = {k: v for k, v in scores.items() if v >= 60}

# Key transformation
data = {"Name": "Anupam", "Age": 30}
lower_keys = {k.lower(): v for k, v in data.items()}

# Swapping keys and values (values must be unique & hashable)
rev = {v: k for k, v in {"a": 1, "b": 2}.items()}


# ============================================================
# 3. SET COMPREHENSIONS
# ============================================================

nums = [1, 2, 2, 3, 3]
unique_squares = {n ** 2 for n in nums}


# ============================================================
# 4. GENERATOR COMPREHENSIONS
# ============================================================

# Lazy evaluation (memory efficient)
gen = (n * 2 for n in range(10))

# Consume generator
for val in gen:
    pass


# ============================================================
# 5. COMMON PITFALLS (IMPORTANT)
# ============================================================

# ❌ Late binding issue
funcs = [lambda: i for i in range(3)]
# All functions return 2

# ✅ Correct way
funcs_fixed = [lambda i=i: i for i in range(3)]

# ❌ Do NOT use comprehensions for side effects
# [lst.append(x) for x in range(5)]  # Bad practice

# ❌ Duplicate keys overwrite silently
data = ["ab", "cd", "ef"]
bad_dict = {len(x): x for x in data}  # Only last value survives


# ============================================================
# 6. WHEN TO USE / NOT USE
# ============================================================

"""
USE comprehensions when:
- Simple mapping or filtering
- Readable in one line
- No side effects

AVOID comprehensions when:
- Complex branching logic
- Nested conditions hurting readability
- Logging / printing / API calls
"""

# ============================================================
# END OF FILE
# ============================================================
