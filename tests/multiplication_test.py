"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """Testing that our calculator has a static method for Multiplication"""
    #Arrange
    myNumbers = (2.0,5.0)
    multiplication = Multiplication(myNumbers)
    #Act
    """Not needed in this version for now"""
    #Assert
    assert multiplication.get_result()==10.0
