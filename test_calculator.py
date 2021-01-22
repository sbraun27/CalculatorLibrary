"""
Unit tests for calculator.py
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 8 == calculator.multiplication(4, 2)

    def test_division(self):
        assert 10 == calculator.division(100, 10)
