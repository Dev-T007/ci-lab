from calc.py import add,sub

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(1,-1) == 0