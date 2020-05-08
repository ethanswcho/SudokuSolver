"""
Parses through cells (list of dicts), and if it encounters a cell with a None as value immediately terminate and return True
"""

def has_none(input):

    for cell in input:
        if cell["value"] is "x":
            return True
    
    return False
        