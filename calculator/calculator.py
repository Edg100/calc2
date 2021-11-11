""" Incremental function"""
#Importing all calculations

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class where cl_history is the clear history"""
    #Calculator static property
    history = []
    @staticmethod
    def get_first_cal_add_hist():
        """This is to get the first added calculation history"""
        return Calculator.history[0].get_result()
    @staticmethod
    def cl_hist():
        """This clears history of the calculator"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """This controls the history count"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """Add calaculation history to calculator"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_last_cal_add_hist():
        """Get last added calculation history"""
        return Calculator.history[-1].get_result()
    @staticmethod
    def add_number(num_a, num_b):
        """Add numbers to result"""
        #Addition object
        addition = Addition.create(num_a,num_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_cal_add_hist()
    @staticmethod
    #Calling method
    def subtract_number(num_a, num_b):
        """Substract numbers from result"""
        # Subtraction object
        subtraction = Subtraction.create(num_a, num_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_cal_add_hist()
    @staticmethod
    def multiply_numbers(num_a, num_b):
        """Multiply two numbers and store the result"""
        #Multiplication object
        Calculator.add_calculation_to_history(Multiplication.create(num_a, num_b))
        return Calculator.get_last_cal_add_hist()
    @staticmethod
    def divide_numbers(num_a, num_b):
        """Divide two numbers and store the result"""
        #Division object
        Calculator.add_calculation_to_history(Division.create(num_a, num_b))
        return Calculator.get_last_cal_add_hist()
