"""
For the given cell, get possible values
"""

from .get_possible_line_values import get_possible_line_values
from .get_possible_square_values import get_possible_square_values


def get_possible_values(cell, input):

    possible_row_values = set(get_possible_line_values(cell, input, "row"))
    possible_col_values = set(get_possible_line_values(cell, input, "col"))
    possible_square_values = set(get_possible_square_values(cell, input))

    return list(possible_square_values.intersection(possible_row_values.intersection(possible_col_values)))


    