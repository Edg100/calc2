"""This is to test the Calculator Class"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """ This is a fixture that defines a function for testing"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#Adding the fixture function as a parameter to the test that you want to use it
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # With Tuple we can manage as much data as we need
    my_tuple = (4.0,5.0,1.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 10.0
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # With Tuple we can manage as much data as we need
    my_tuple = (10.0,5.0,1.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == -16.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # With Tuple we can manage as much data as we need
    my_tuple = (7.0,2.0,2.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 28.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # With Tuple we can manage as much data as we need
    my_tuple = (1.0,2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 0.5
