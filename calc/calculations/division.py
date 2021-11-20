"""Division class"""
from calc.calculations.calculation import Calculation

class Division(Calculation): # pylint: disable=too-few-public-methods
    
    """ calculation addition class"""
    def get_result(self):
        """get the addition results"""
        divide_values = self.values[0]
        for value in self.values:
            if value == 0:
                raise Exception('ZeroDivisionError')
            divide_values = divide_values / value
            return divide_values
