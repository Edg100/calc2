"""Test for the subtraction object"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """Testing static method for subtraction"""
    #Arrange
    my_numbers = (1.0,2.0)
    # Act
    subtraction = Subtraction(my_numbers)
    #Assert
    assert subtraction.get_result() == -3
