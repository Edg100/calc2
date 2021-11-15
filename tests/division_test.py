"""Test for the division object"""
from calc.calculations.division import Division

def test_calculation_subtraction():
        """testing static method for multiplication"""
        #Arrange
        my_numbers = (12.0,2.0)
        # Act
        division = Division(my_numbers)
        #Assert
        assert division.get_result() == 6.0
