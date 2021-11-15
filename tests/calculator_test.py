"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def cl_his_fixture():
    """Function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.cl_his()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(cl_his_fixture):
    """This is to test the add method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(7.0,2.0,3.0) == 12.0

def test_calculator_subtract_static(cl_his_fixture):
    """This to test the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(8.0,2.0,7.0) == -1.0

def test_calculator_multiply_static(cl_his_fixture):
    """This to test the multiply method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(4.0,6.0,2.0) == 48.0

def test_calculator_divide_static(cl_his_fixture):
    """This to test the divide method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(24.0,6.0) == 4.0
