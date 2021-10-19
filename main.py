""" content of calculator.py#"""
# disabling:
# C0304: Trailing newlines (Trailing-newlines)
# pylint: disable=C0304

def inc(x_value):
    """ Increment Function adds one to the x_value"""

    return x_value + 1
def test_answer():
    """This Tests the function"""

    assert inc(4) == 5



