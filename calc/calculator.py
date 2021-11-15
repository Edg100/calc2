""" Incremental function"""
#Importing all calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

class Calculator:
    """ Calculator class for all math operations"""
    @staticmethod
    def add_number(*args):
        """Add a list of numbers from result"""
        # Addition object
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_number(*args):
        """Subtract a list of numbers from result"""
        # Subtraction object
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """Multiply numbers from result"""
        #Multiplication object
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def divide_numbers(*args):
        """Divide numbers from result"""
        #Division object
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
