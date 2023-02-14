from ghost_leg import ghost_leg, check_leg

# You can call "pytest" in the terminal to run tests!

# By default, PyTest looks for files, containing classes or functions
# whose names start with test_*

def test_return_maintains_length():
    columns = ['A', 'B', 'C', 'D']
    legs = []

    reordered = ghost_leg(columns, legs)
    assert len(reordered) == len(columns)

def test_return_original_order_when_there_are_no_legs():
    columns = ['A', 'B', 'C', 'D']
    legs = []

    reordered = ghost_leg(columns, legs)
    assert reordered == columns

def test_leg_from_current_column_is_followed():
    leg = ['A', 'B']
    current_column = 'A'
    
    new_column = check_leg(leg, current_column)
    assert new_column == 'B'


def test_order_changes_when_there_are_legs():
    columns = ['A', 'B']
    legs = [['A', 'B']]

    reordered = ghost_leg(columns, legs)
    assert reordered == ['B', 'A']

def test_order_changes_when_there_are_legs():
    columns = ['A', 'B', 'C']
    legs = [['A', 'B'], ['B', 'C']]

    reordered = ghost_leg(columns, legs)
    assert reordered == ['B', 'C', 'A']

def test_complex_case():
    columns = ['A', 'B', 'C', 'D']
    legs = [['A', 'B'],  ['C', 'D'],  ['B', 'C'],  ['C', 'D'],  ['B', 'C'],  ['A', 'B']]
    reordered = ghost_leg(columns, legs)
    assert reordered == ['C', 'B', 'D', 'A']

# def test_that_passes():
#     """
#     If an assertion fails, or an exception occurs, a test will Fail...
#     If not, it passes. This test always passes.
#     """
#     assert True


# def test_that_fails():
#     """
#     This test fails, because 1 does not equal 0
#     """
#     x = 1
#     assert x == 0
