import pytest
import os

@pytest.mark.it("You have to use the eye() method")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "eye(" in content

@pytest.mark.it('The output should be a matrix which values should be from 0 to 9')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]\n'