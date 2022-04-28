import pytest
import os
import numpy

@pytest.mark.it("You have to use the max() method")
def test_random():
    f = open('app.py')
    content = f.read()
    assert "max(" in content

@pytest.mark.it('You should create a variable named arr')
def test_arr_exists():
    try:
        from app import arr
    except AttributeError:
        raise AttributeError("The variable 'arr' should exist on app.py")

@pytest.mark.it('The array should have three random values')
def test_arr_value(capsys):
    from app import arr
    size = numpy.size(arr)
    assert size == 10