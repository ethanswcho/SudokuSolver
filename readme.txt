Input data structure:

The very initial input will be a long string representing 9x9 sudoku board of values.
The string will will divide each row by a space (" "), and any unknown values (empty cells) will be repesented as a "x".
Do not enter space at the end. If inputted correctly, the input string should contain 81 characters and 8 spaces (" ").
ex)
"xx28x769x 8x4x9xxxx xx62xx1x5 94xxxx2xx 6xxxxxxx9 xx1xxxx37 1x7xx34xx xxxx7x8x3 x296x87xx"

Then, the sudokusolver will take the above string input and will convert it into a list of dictionaries that contain necessary information.
Each dict will contain value, row and col. Any unknown values ("x" in string) will stay as x as value.
Note that row and col values are 1-based.
ex (using above string)):
[
    {
        "value": "x",
        "row": 1,
        "col": 1
    },
    {
        "value": "x",
        "row": 1,
        "col": 2
    },
    {
        "value": 2,
        "row": 1,
        "col": 3
    }
    ...
]


