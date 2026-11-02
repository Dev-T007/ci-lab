from calc import add,sub
import pytest

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(1,-1) == 2


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
    (-1.5, -2.5, -4.0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
