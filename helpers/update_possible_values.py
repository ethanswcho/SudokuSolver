"""
For each unresolved cell, update its possible values.
"""
from .possible_values.get_possible_values import get_possible_values

def update_possible_values(input):

    for cell in input:
        
        # cell value is already determined. skip.
        if cell["value"] != "x":
            continue

        #Get a list of all possible values
        possible_values = get_possible_values(cell, input)
        print("row: {} col: {} square: {} possible values: ".format(cell["row"], cell["col"], cell["square"]))
        print(*possible_values, sep= ", ")

        if len(possible_values) == 0:
            print("Row: {} Col: {} does not have any possible values...".format(cell["row"], cell["col"]))
            
        elif len(possible_values) == 1:
            cell["value"] = possible_values[0]

        else: 
            continue
        
        
