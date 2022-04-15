import os
import pytest

@pytest.mark.it('The app.py file should exist on the root of the project')
def test_file_exists():
    assert os.path.exists("app.py") == True