import pytest
import os

@pytest.mark.it("Use the zeros() function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("zeros(") > 0

@pytest.mark.it('The output should be a null vector of size 10')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert '[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n' in captured.out
