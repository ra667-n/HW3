'''My Calculator Test''' 
from calculator.calculation import Calculation as cal

def test_addition():
    '''Test that addition function works '''    
    assert cal.add(5,2) == 7 

def test_subtraction():
    '''Test that subtraction function works '''    
    assert cal.subtract(9,9) == 0

def test_multiplication():
    '''Test that multiplication works'''
    assert cal.multiply(7,7) == 49

def test_division():
    '''Test division'''
    assert cal.divide(4,2) == 2

def test_divide_by_zero():
    '''Test division by zero raises an exception'''
    try:
        cal.divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False  # Should never reach here if exception is raised
