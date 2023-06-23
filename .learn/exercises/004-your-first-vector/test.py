import pytest
import os, re

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

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[0\. 0\. 0\. 0\. 0\. 0\. 0\. 0\. 0\. 0\.\]")
        assert bool(regex.search(content)) == False