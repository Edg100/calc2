"""Division Class for two numbers"""

from calc.calculations.calculation import Calculation

#This is the way for Division class to extend with the Calculation class

class Division(Calculation):
    """The division class from the calculation parent class"""
    def get_result(self):
        """This is to get the division results"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result

    @classmethod
    def create(cls, values):
        pass
