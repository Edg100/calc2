"""Test for the division object"""
from calc.calculations.division import Division

def test_calculation_division():
    """Testing static method for division"""
    #Arrange
    my_numbers = (1.0,4.0)
    # Act
    division = Division(my_numbers)
    #Assert
    assert division.get_result() == 0.25
