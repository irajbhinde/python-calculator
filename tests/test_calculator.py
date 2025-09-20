import pytest
from src.calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0.5, 0.25, 0.75),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (2, 5, -3),
    (0.5, 0.25, 0.25),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (0.5, 0.2, 0.1),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_raises_on_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_add_negative_numbers():
    assert add(-3, -7) == -10

