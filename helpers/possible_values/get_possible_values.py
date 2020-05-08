"""
For the given cell, get possible values
"""

from .get_possible_line_values import get_possible_line_values
from .get_possible_square_values import get_possible_square_values


def get_possible_values(cell, input):

    #Get 3 sets of possible row/col/square values relative to this cell's position
    possible_row_values = get_possible_line_values(cell, input, "row")
    possible_col_values = get_possible_line_values(cell, input, "col")
    possible_square_values = get_possible_square_values(cell, input)
    
    print(possible_row_values)
    print(possible_col_values)
    print(possible_square_values)
    

    return list(possible_square_values.intersection(possible_row_values.intersection(possible_col_values)))


    