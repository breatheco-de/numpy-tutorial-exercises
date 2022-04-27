import pytest
import os

@pytest.mark.it("You have to use the nonzero() method")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "nonzero(" in content

@pytest.mark.it('The output should be a tuple of arrays with the indices of non zero values')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '(array([0, 1, 4]),)\n'