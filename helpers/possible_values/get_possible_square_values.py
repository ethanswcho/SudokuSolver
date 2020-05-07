"""
Given a cell, return possible values relative to the 3x3 square it is part of
"""

import math
possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_possible_square_values(cell, input):

    start_row = math.floor(cell["row"]/3) * 3 + 1
    end_row = start_row + 3
    start_col = math.floor(cell["col"]/3) * 3 + 1
    end_col = start_col + 3

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if input[]







    