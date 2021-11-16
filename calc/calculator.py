""" This is the increment function"""
from calc.history.calculations import Calculations

#Calculator class contains the methods to calculate
# division, addition, multiplication and subtraction
class Calculator:
    """ This is the Calculator class"""
    #Calculator class calls methods on Calculations class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # This to have more than one action per function
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    #Tuple passes in as many data values as we need
    def add_numbers(tuple_values: tuple):
        """ Add list of numbers from result"""
        Calculations.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ Subtract list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ Multiply list of numbers from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True
    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Divide list of numbers from result"""
        Calculations.add_division_calculation(tuple_values)
        return True
