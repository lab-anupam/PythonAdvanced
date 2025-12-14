"""
python_mutability_notes.py
Author: Anupam Bhattacharyya

Topic: Python Internals & Mutability
"""

import copy

# -------------------------------
# 1. Variables are references
# -------------------------------
a = [1, 2, 3]
b = a
b.append(4)

print("Shared reference:", a)  # [1, 2, 3, 4]


# -------------------------------
# 2. Creating independent copy
# -------------------------------
a = [1, 2, 3]
b = a.copy()
b.append(4)

print("After copy:", a)  # [1, 2, 3]


# -------------------------------
# 3. Shallow copy bug
# -------------------------------
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0].append(99)

print("Shallow copy issue:", a)  # inner list modified


# -------------------------------
# 4. Deep copy fix
# -------------------------------
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print("Deep copy safe:", a)  # unchanged


# -------------------------------
# 5. Mutable argument bug
# -------------------------------
def buggy_add(x, lst=[]):
    lst.append(x)
    return lst

print("Buggy:", buggy_add(1))
print("Buggy:", buggy_add(2))


# -------------------------------
# 6. Correct mutable argument fix
# -------------------------------
def safe_add(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print("Safe:", safe_add(1))
print("Safe:", safe_add(2))


# -------------------------------
# 7. Immutable behavior
# -------------------------------
x = 10
y = x
x += 1

print("Immutable safe:", y)  # 10
