"""Multiplication Calculation from values A and value B in the calculation class"""

from calc.calculation import Calculation

#This is the way for Multiplication class to extend with the Calculation class
class Multiplication(Calculation):
    """The addition class has one method to get the result of the the calculation
     A and B come from the calculation parent class"""
    def get_result(self):
        """self is to reference the data in the object instance called encapsulation."""

        return self.num_a * self.num_b
