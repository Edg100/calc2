"""Subtraction Class for two numbers"""

import pprint

from calc.calculations.calculation import Calculation

#This is the way for Subtraction class to extend with the Calculation class
class Subtraction(Calculation):
    """The subtraction class from the calculation parent class"""
    def get_result(self):
        """This is to get the subtraction results"""
# Here diff_value is for the different of two values
        diff_values = 0.0
        for value in self.values:
            diff_values = diff_values - value
            pprint.pprint(value)
        return diff_values

