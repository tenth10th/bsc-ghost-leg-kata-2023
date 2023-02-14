from typing import List
# How might we implement a Ghost Leg function?

# How should we represent the "legs" or "rungs"?

# What tests should we write to prove that it's working correctly?
# elements : list of columns - ['A', 'B', 'C', 'D']
# legs : list of connections - [['A', 'B'], ['C', 'D']]
# return reordered elements - ['B', 'A', 'C', 'D']

"""
[A, B, C]

[[A, B], [B, C]]

first loop - A (current column)
first leg
[A, B]: A is in [A, B] A -> B
second leg (at this point, current_column = B)
[B, C]: B is in [B, C] B -> C, current_column = C

[C]

second loop - B (current column)
first leg
[A, B]: B is in [A, B] B -> A
second leg (at this point, current_column = B)
[B, C]: A is not in [B, C] current_column = A

[C, A]

third loop - C (current column)
first leg
[A, B]: C is not in [A, B] C -> C
second leg (at this point, current_column = B)
[B, C]: C is in [B, C] C -> B

[C, A, B]
"""

"""
Chuba suggested:

    We could try modeling the legs as a graph with an
    adjacency matrix that also stores the order, e.g.:
    {
    A: [B,D]
    ...
    }
    means we swap A with B on the first pass and swap
    with D the next time.
"""

    # Would the tests not be messed up as the columns are passed by reference?
    # you should probably use copy.deepcopy https://docs.python.org/3/library/copy.html



#
def check_leg(element_leg_array: List[str], current_column: str) -> str:
    if current_column in element_leg_array:
        current_column_idx = element_leg_array.index(current_column)
        if current_column_idx == 0:
            return element_leg_array[1]
        else:
            return element_leg_array[0]
    else:
        return current_column

def ghost_leg(elements: List[str], legs: List[List[str]]) -> List[str]:
    output_list = ['' for element in elements]
    for element in elements:
        new_column = element
        for leg in legs:
            new_column = check_leg(leg, new_column) 
        output_list_idx = elements.index(new_column)
        
        output_list[output_list_idx] = element

    return output_list #check_leg(legs[0], elements)
