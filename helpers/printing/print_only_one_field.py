"""
Parses through converted input, and prints only one field of each cell, specified by second input variable
"""

def print_only_one_field(input, field):
    rows = []
    row = ""

    for cell in input:
        if type(cell[field] == int):
            row = row + str(cell[field])
        else:
            row = row + cell[field]
            
        if len(row) == 9:
            rows.append(row)
            row = ""
    
    for r in rows:
        print(r)

