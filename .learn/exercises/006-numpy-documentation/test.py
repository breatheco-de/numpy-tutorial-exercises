import pytest
import os

@pytest.mark.it("You have to use the info() function")
def test_output():
    f = open(os.path.dirname(os.path.abspath('app.py'))+'/app.py')
    content = f.read()
    assert content.find("info(") > 0