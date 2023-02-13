# You can call "pytest" in the terminal to run tests!

# By default, PyTest looks for files, containing classes or functions
# whose names start with test_*


def test_that_passes():
    """
    If an assertion fails, or an exception occurs, a test will Fail...
    If not, it passes. This test always passes.
    """
    assert True


def test_that_fails():
    """
    This test fails, because 1 does not equal 0
    """
    x = 1
    assert x == 0
