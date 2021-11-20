"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_result_value() == 8.0
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_result_value() == -6.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_result_value() == 6.0

def test_calculator_division_static(clear_history_fixture):
    """Testing the division method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (3.0,3.0)
    Calculator.division_numbers(my_tuple)
    assert Calculator.get_result_value() == 1.0

def test_calculator_divisionZero_static(clear_history_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple


    #Trying stuff DELETE before commit
    """
    def get_result(self):
    test_size = 1000000
    sum_of_values = 0.0
    for n in test_size:
        t0 = time.time()
        for value in self.values:
            try:
                sum_of_values = value[0] / value[1]
                return sum_of_values
            # Try using a raise
            except ZeroDivisionError:
                print("Cannot divide by 0")
        t1 = time.time()
        total_time = t1-t0

    """