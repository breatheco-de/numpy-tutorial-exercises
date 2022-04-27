import pytest
import os

@pytest.mark.it("You have to use the itemsize property")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("itemsize") > 0

@pytest.mark.it("You have to use the itemsize property")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("size") > 0

@pytest.mark.it('The output should be the memory size of a null vector of size 10')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '80\n'