"""Test Division"""
import pytest
from calculator.operations.division import Division


def test_division():
  """Testing Division"""
  #Arrange
  numbers = (10.0, 5.0)
  division = Division(numbers)
  #Act
  #Assert
  assert division.get_result()==2.0
  
  
def test_division_zero():
  """Testing ZeroDivision"""
  #Arrange
  numbers = (8.0, 0)
  division = Division(numbers)
  #Act
  #Assert
  with pytest.raises(ZeroDivisionError):
    division.get_result()
