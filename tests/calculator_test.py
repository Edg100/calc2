"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def cl_his_fixture():
    """Function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(cl_his_fixture):
    """This is to test the add method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # with Tuple we can have more data than args
    my_tuple = (1.0, 2.0, 5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0

def test_calculator_subtract_static(cl_his_fixture):
    """This to test the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # with Tuple we can have more data than args
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == -6.0

def test_calculator_multiply_static(cl_his_fixture):
    """This to test the multiply method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # with Tuple we can have more data than args
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 6.0

def test_calculator_divide_static(cl_his_fixture):
    """This to test the divide method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # with Tuple we can have more data than args
    my_tuple = (6.0,2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 3.0
