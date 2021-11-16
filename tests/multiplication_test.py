"""Test for the multiplication object"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """Testing static method for multiplication"""
    #Arrange
    my_numbers = (5.0,4.0)
    # Act
    multiplication = Multiplication(my_numbers)
    #Assert
    assert multiplication.get_result() == 20.0
