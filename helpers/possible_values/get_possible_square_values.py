"""
Given a cell, return possible values relative to the 3x3 square it is part of
"""

import math
possible_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_possible_square_values(cell, input):

    #  Grab values within same row/col (depending on mode chosen) that are solved (numbers as value)
    solved_values = [x["value"] for x in input if x["square"] == cell["square"] and x["value"] != "x"]

    
    return set(possible_values) - set(solved_values)
    