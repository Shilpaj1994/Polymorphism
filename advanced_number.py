#! /usr/bin/env python3
"""
Script to create a Python class named `AdvancedNumber` that models a custom numerical type with rich functionality using Python's special methods.
Author: Shilpaj Bhalerao
Date: 2024-11-28
"""
# Standard Library Imports
from typing import Union


class AdvancedNumber:
    """
    Class to model a custom numerical type with rich functionality using Python's special methods.
    """
    def __init__(self, value: Union[int, float]) -> None:
        """
        Constructor for the `AdvancedNumber` class.
        """
        self.value = value

    # ----------------------------- String Representation -----------------------------
    def __str__(self) -> str:
        """
        String representation of the `AdvancedNumber` object.
        """
        return f"Value: {self.value}"

    def __repr__(self) -> str:
        """
        String representation of the `AdvancedNumber` object.
        """
        return f"AdvancedNumber({self.value})"

    # ----------------------------- Arithmetic Operations -----------------------------
    def __add__(self, other) -> "AdvancedNumber":
        """
        Addition operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        return AdvancedNumber(self.value + other)

    def __sub__(self, other) -> "AdvancedNumber":
        """
        Subtraction operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        return AdvancedNumber(self.value - other)

    def __mul__(self, other) -> "AdvancedNumber":
        """
        Multiplication operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        return AdvancedNumber(self.value * other)

    def __truediv__(self, other) -> "AdvancedNumber":
        """
        True division operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        return AdvancedNumber(self.value / other)

    def __mod__(self, other) -> "AdvancedNumber":
        """
        Modulo operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        return AdvancedNumber(self.value % other)

    # ----------------------------- Comparison Operations -----------------------------
    def __eq__(self, other) -> bool:
        """
        Equality operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        return self.value == other

    def __gt__(self, other) -> bool:
        """
        Greater than operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other) -> bool:
        """
        Greater than or equal to operation for the `AdvancedNumber` object.
        """
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        return self.value >= other

    # ----------------------------- Hashing -----------------------------
    def __hash__(self) -> int:
        """
        Hash value for the `AdvancedNumber` object.
        """
        return hash(self.value)
    
    # ----------------------------- Boolean Conversion -----------------------------
    def __bool__(self) -> bool:
        """
        Boolean conversion for the `AdvancedNumber` object.
        """
        if self.value != 0:
            return True
        return False

    # ----------------------------- Callable -----------------------------
    def __call__(self) -> int:
        """
        Callable operation for the `AdvancedNumber` object.
        """
        return self.value ** 2

    # ----------------------------- Formatting -----------------------------
    def __format__(self, format_spec: str) -> str:
        """
        Formatting operation for the `AdvancedNumber` object.
        """
        if format_spec == ".2f":
            return f"{self.value:.2f}"
        elif format_spec == "#x":
            return f"{self.value:#x}"
        return f"{self.value}"
    
    # ----------------------------- Destructor -----------------------------
    def __del__(self):
        """
        Destructor
        """
        print(f"AdvancedNumber with value {self.value} is being destroyed")
        self.value = None
        self = None