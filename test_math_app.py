import pytest
from math_app import diviser

def test_division_positive():
    assert diviser(10, 2) == 5

def test_division_negative():
    assert diviser(-10, 2) == -5

def test_division_zero():
    with pytest.raises(ValueError):
        diviser(10, 0)
