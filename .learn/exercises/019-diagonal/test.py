import pytest
import os
import numpy

@pytest.mark.it("You have to use the diag() method")
def test_random():
    f = open('app.py')
    content = f.read()
    assert "diag(" in content

@pytest.mark.it('The output should be a the diagonal of the matrix')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[0 4 8]\n'