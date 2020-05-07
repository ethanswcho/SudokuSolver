"""
print the input and all the information included.
Prints one cell's worth of information at a time.
"""

def print_all_fields(input):
    for cell in input:
        print("value: " + cell["value"])
        print("row: " + cell["row"])
        print("col: " + cell["col"])
        print("square: " + cell["square"])
        print()
    