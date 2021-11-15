"""Test for the subtraction object"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
        """testing static method for subtraction"""
        #Arrange
        my_numbers = (8.0,6.0)
        # Act
        subtraction = Subtraction(my_numbers)
        #Assert
        assert subtraction.get_result() == 2.0
