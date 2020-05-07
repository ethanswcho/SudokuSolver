"""
Parses through converted input, and prints only numbers
"""

def print_only_numbers(input):
    rows = []
    row = ""

    for cell in input:
        row = row + cell["value"]
        if len(row) == 9:
            rows.append(row)
            row = ""
    
    for r in rows:
        print(r)
