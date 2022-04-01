import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correct(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division_calculate_correct(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_substraction_calculate_correct(self):
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_adding_calculate_correct(self):
        assert self.calc.adding(self, 5, 7) == 12
