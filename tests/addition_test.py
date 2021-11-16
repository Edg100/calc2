"""Test for the addition object"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """Testing static method for addition"""
    #Arrange
    my_numbers = (1.0,2.0)
    # Act
    addition = Addition(my_numbers)
    #Assert
    assert addition.get_result() == 3.0
