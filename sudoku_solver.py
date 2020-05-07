
from helpers.convert_input import convert_input
from helpers.print_input import print_input
from helpers.has_none import has_none
from helpers.update_possible_values import update_possible_values
from helpers.printing.print_all_fields import print_all_fields
from helpers.printing.print_only_numbers import print_only_numbers

input = "xx28x769x 8x4x9xxxx xx62xx1x5 94xxxx2xx 6xxxxxxx9 xx1xxxx37 1x7xx34xx xxxx7x8x3 x296x87xx"

def sudoku_solver(input):

    print_input(input)
    input, error = convert_input(input)
    
    print("Conversion success.")
    print("Only Numbers:")
    print_only_numbers(input)

    """
    if error:
        #Exit condition
        print("Error: Please check your input")
    
    while has_none(input):
        
        update_possible_values(input)
        error = set_values(input)
        if error:
            print("This sudoku cannot be solved!")
            break
    
    return input
    """


if __name__=="__main__":
    sudoku_solver(input)

