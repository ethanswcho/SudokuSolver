"""
For each unresolved cell, update its possible values.
"""

from possible_values.get_possible_line_values import get_possible_line_values


def update_possible_values(input):

    for cell in input:
        
        # cell value is already determined. skip.
        if cell["value"] is not "x":
            continue
    
        # Grab possible values of this cell relative to its row, col and square. 
        possible_row_values = get_possible_line_values(cell, input, "row")
        possible_col_values = get_possible_line_values(cell, input, "col")
        possible_square_values = get_possible_square_values(cell, input)
        
        possible_values = get_possible_values(possible_row_values, possible_col_values, possible_square_values)

        if len(possible_values) == 0:
            print("Row: {} Col: {} does not have any possible values...".format(cell["row"], cell["col"]))
            
        elif len(possible_values) == 1:
            cell["value"] = possible_values[0]

        else: 
            continue
        
        
