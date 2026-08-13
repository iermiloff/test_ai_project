import pytest
from math_utils import divide

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5.0

def test_divide_mixed_numbers():
    assert divide(10, -2) == -5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
