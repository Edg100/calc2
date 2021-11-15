"""Addition Class for two numbers"""

from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """The addition class from the calculation parent class"""
    def get_result(self):
        """This is to get the addition results"""
# Here sum_values is for the summation of two or group of values
        sum_values = 0.0
        for value in self.values:
            sum_values = value + sum_values
        return sum_values

