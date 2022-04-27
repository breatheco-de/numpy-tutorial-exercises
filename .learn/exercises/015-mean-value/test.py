import pytest
import os
import numpy

@pytest.mark.it("You have to use the mean() method")
def test_random():
    f = open('app.py')
    content = f.read()
    assert "mean(" in content

@pytest.mark.it('The output should be a the mean value of the array')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == f'{app.arr.mean()}\n'

@pytest.mark.it('You should create a variable named arr')
def test_arr_exists():
    try:
        from app import arr
    except AttributeError:
        raise AttributeError("The variable 'arr' should exist on app.py")

@pytest.mark.it('The array should have ten random values')
def test_arr_value(capsys):
    from app import arr
    size = numpy.size(arr)
    assert size == 10