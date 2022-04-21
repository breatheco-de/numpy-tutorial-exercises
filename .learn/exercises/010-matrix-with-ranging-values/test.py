import pytest
import os

@pytest.mark.it("You have to use the reshape() method")
def test_output():
    f = open(os.path.dirname(os.path.abspath('app.py'))+'/app.py')
    content = f.read()
    assert content.find("reshape(") > 0

@pytest.mark.it('The output should be a matrix which values should be from 0 to 9')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[0 1 2]\n [3 4 5]\n [6 7 8]]\n'