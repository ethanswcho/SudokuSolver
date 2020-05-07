"""
Given text input, convert it to a list of dictionary containing the value, row, and column information
If a part of the input includes unexpected character, error flag will be set to True.
row and column are 1-based (1-9)
"""

from termcolor import cprint
import math

def convert_input(input):
    output = []
    row = 1
    col = 1
    error = False
    
    for char in input:
        if char == " ":
            continue
            
        # Expected chars (numbers or "x")
        if char.isdigit() or char == "x":
            output.append(make_cell_dict(char, row, col))

        # Unexpected behavior
        else:
            output.append(make_cell_dict("?", row, col))
            error = True
        
        if row < 9:
            row = row + 1
        elif col < 9:
            row = 1
            col = col +1
    
    if row != 9 and col != 9:
        print("row: {} col: {}".format(row, col))
        cprint("convert_input: there are not enough input!", "red")
    
    return output, error

def get_square(row, col):
    row_val = math.floor(row/3) * 3
    col_val = math.floor(col/3) + 1
    return row_val + col_val

def make_cell_dict(value, row, col):
    return {
        "value": value,
        "row": row,
        "col": col,
        "square": get_square(row, col)
    }