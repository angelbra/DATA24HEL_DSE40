# test.py
import pytest 

def add_one(x):
    return x + 1

def test_add_one():
    assert add_one(4) == 5

def test_add_one_fail():
    assert add_one(4) == 7

def test_add_one_with_str():
    with pytest.raises(TypeError):
        add_one('4')