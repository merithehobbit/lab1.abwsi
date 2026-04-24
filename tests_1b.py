"""
tests_1b.py

Unit tests for simple_calculator from lab_1b.py using pytest.
"""

import pytest
from lab_1b import simple_calculator


def test_addition():
    assert simple_calculator("add", 5, 3) == 8
    assert simple_calculator("add", -2, 2) == 0
    assert simple_calculator("add", 0, 0) == 0


def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2
    assert simple_calculator("subtract", -2, -2) == 0
    assert simple_calculator("subtract", 0, 5) == -5


def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15
    assert simple_calculator("multiply", -2, 2) == -4
    assert simple_calculator("multiply", 0, 100) == 0


def test_division():
    assert simple_calculator("divide", 6, 3) == 2
    assert simple_calculator("divide", -4, 2) == -2
    assert simple_calculator("divide", 5, 2) == 2.5


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)


def test_invalid_operation():
    with pytest.raises(ValueError):
        simple_calculator("modulus", 5, 3)

    with pytest.raises(ValueError):
        simple_calculator("", 5, 3)
