"""
Given a cell and all the input, look through other cells in its row and grab possible values
"""
from termcolor import cprint

possible_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_possible_line_values(cell, input, mode):

    if mode not in ["row", "col"]:
        cprint("get_possible_line_values: {} is not a supported mode".format(mode), "red")

    # Grab values within same row/col (depending on mode chosen) that are solved (numbers as value)
    solved_values = [x["value"] for x in input if x[mode] == cell[mode] and x["value"].isdigit()]

    #print(solved_values)

    """
    # Check if there are duplicate values in the line - which would be an error
    if len(solved_values) - len(set(solved_values)) == 0:
        cprint("get_possible_line_values: There are values on {} {}".format(mode, cell[mode]))
        error = True
    """

    #print(list(set(possible_values) - set(solved_values)))

    # No duplicates - return possible values (all possible values - solved values)
    return set(possible_values) - set(solved_values)
    

    