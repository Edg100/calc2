"""Multiplication Class for two numbers"""

from calc.calculations.calculation import Calculation

#This is the way for Multiplication class to extend with the Calculation class

class Multiplication(Calculation):
    """The multiplication class from the calculation parent class"""
    def get_result(self):
        """This is to get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
