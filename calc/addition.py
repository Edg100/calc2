"""Addition Calculation from values A and value B in the calculation class"""

from calc.calculation import Calculation

#This is the way for Addition class to extend with the Calculation class
class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        """Here the use of self is to reference the
        data in the object instance called encapsulation."""
        return self.num_a + self.num_b
