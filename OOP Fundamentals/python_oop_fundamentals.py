"""
python_oop_fundamentals.py
-------------------------
Author: Anupam Bhattacharyya
Topic: Python OOP Fundamentals
Purpose: Interviews + Real-world backend / data engineering usage
"""

# ============================================================
# 1. BASIC CLASS & OBJECT
# ============================================================

class Person:
    species = "Human"  # class variable

    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}"


# ============================================================
# 2. CLASS METHOD vs STATIC METHOD
# ============================================================

class User:
    role = "guest"

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_admin(cls, name):
        """Alternative constructor"""
        user = cls(name)
        user.role = "admin"
        return user

    @staticmethod
    def is_valid_username(name):
        """Utility method"""
        return isinstance(name, str) and len(name) >= 3


# ============================================================
# 3. __str__ vs __repr__
# ============================================================

class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Account Balance: {self.balance}"

    def __repr__(self):
        return f"Account(balance={self.balance})"


# ============================================================
# 4. ENCAPSULATION
# ============================================================

class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


# ============================================================
# 5. SIMPLE DATA PROCESSOR (REAL-WORLD STYLE)
# ============================================================

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def clean(self):
        self.data = [x for x in self.data if x is not None]

    def normalize(self):
        max_val = max(self.data)
        self.data = [x / max_val for x in self.data]

    def summary(self):
        return {
            "count": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "avg": sum(self.data) / len(self.data)
        }


# ============================================================
# END OF FILE
# ============================================================
