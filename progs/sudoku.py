# from LAB: https://edube.org/learn/pe-2/lab-sudoku-4

"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill
the board in a very specific way:

* each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
* each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
* each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits
  from 0 to 9.

If you need more details, you can find them [https://en.wikipedia.org/wiki/Sudoku](here).

Your task is to write a program which:

* reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
* outputs Yes if the Sudoku is valid, and No otherwise.
"""

def check_sudoku(test_board):
    # define valid list of values
    _DIGITS = list(n for n in range(1, 10))

    # dice input board into grid of integers.
    try:
        grid = list(list(int(n) for n in line) for line in test_board)
    except ValueError: return False

    # if more than 9 rows, fail
    if len(grid) != 9: return False

    # validate rows
    for row in grid:
        sort_group = sorted(row)
        if sort_group != _DIGITS:
            return False

    # validate columns
    for col in range(9):
        sort_group = sorted(grid[row][col] for row in range(9))
        if sort_group != _DIGITS:
            return False

    # validate tiles
    for x_tile in range(0,9,3):
        for y_tile in range(0,9,3):
            sort_group = sorted(grid[x][y] for x in range(x_tile, x_tile + 3) for y in range(y_tile, y_tile + 3))
            if sort_group != _DIGITS:
                return False

    # if the above tests don't return, pass
    return True

# enter in the lines for the board
board = []
for num in range(1,10):
    while True:
        line = input(f"Enter row {num}: ")
        if len(line) == 9 and line.isnumeric() and line.find('.') == -1 and line.find(',') == -1:
            board.append(line)
            break
        else:
            print("Invalid line, try again!")

if check_sudoku(board):
    print("Yes")
else:
    print("No")