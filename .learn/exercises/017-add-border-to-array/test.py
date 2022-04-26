import pytest
import os
import numpy

@pytest.mark.it("You have to use the ones() method")
def test_random():
    f = open('app.py')
    content = f.read()
    assert "ones(" in content

@pytest.mark.it('The output should be a the expected matrix')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[0. 0. 0. 0. 0. 0. 0.]\n [0. 1. 1. 1. 1. 1. 0.]\n [0. 1. 1. 1. 1. 1. 0.]\n [0. 1. 1. 1. 1. 1. 0.]\n [0. 1. 1. 1. 1. 1. 0.]\n [0. 1. 1. 1. 1. 1. 0.]\n [0. 0. 0. 0. 0. 0. 0.]]\n'