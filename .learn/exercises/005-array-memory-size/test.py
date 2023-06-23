import pytest
import os,re

@pytest.mark.it("You have to use the itemsize property")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("itemsize") > 0

@pytest.mark.it("You have to use the size property")
def test_size_used():
    f = open('app.py')
    content = f.read()
    assert content.find("size") > 0

@pytest.mark.it('The output should be the memory size of a null vector of size 10')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert '80\n' in captured.out


@pytest.mark.it("Do not hardcode the expected output")
def test_harcoded_output():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\((\s*80)")
        assert bool(regex.search(content)) == False