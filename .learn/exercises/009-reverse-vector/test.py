import pytest
import os

@pytest.mark.it("You have to reverse the vector values")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("[::-1]") > 0

@pytest.mark.it('The output should be a vector with all the integers from 10 to 1')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[9 8 7 6 5 4 3 2 1 0]\n'