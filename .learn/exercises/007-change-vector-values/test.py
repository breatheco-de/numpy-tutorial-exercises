import pytest
import os

@pytest.mark.it("Use the zeros() function")
def test_output():
    f = open(os.path.dirname(os.path.abspath('app.py'))+'/app.py')
    content = f.read()
    assert content.find("zeros(") > 0

@pytest.mark.it('The output should be a null vector of size 10 and the fifth value should be 1')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]\n'