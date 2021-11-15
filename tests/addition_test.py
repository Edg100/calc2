"""Test for the addition object"""
from calc.calculations.addition import Addition

def test_cal_add():
    """testing static method for addition"""
    #Arrange
    my_numbers = (5.0,9.0)
    # Act
    addition = Addition(my_numbers)
    #Assert
    assert addition.get_result() == 14.0