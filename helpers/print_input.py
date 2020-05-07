"""
Used to print input in formatted 9x9 characters
"""


def print_input(input):

    if isinstance(input, str):
        input = input.split(" ")
        for i in input: 
            print(i)
    
    elif isinstance(input, list):
        counter = 0
        row = ""
        for cell in input:
            row = row + cell["value"]
            counter = counter + 1
            if counter % 9 == 0:
                print(row)
                row = ""
        



            


    
    
        

