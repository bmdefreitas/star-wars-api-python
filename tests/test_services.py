# content of test_sysexit.py
import pytest


def test_one():
    x = "this"
    assert "h" in x

def test_two():
    x = "hello"
    assert "h" in x

def test_three():
    x = "world"
    assert "w" in x