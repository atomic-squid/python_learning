# assignment from edube.org
from random import randrange

# initialize board and create dictionary of positions for choice selection
board, board_positions = [], {}

for x in range(3):
    board.append([]) # create row
    for y in range(3):
        coord = (x, y)
        num = 1 + 3 * x + y
        board[x].append(num)
        board_positions[num] = coord

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    b1 = "+---+---+---+"
    for row in board:
        print(b1, f'| {row[0]} | {row[1]} | {row[2]} |', sep="\n")
    print(b1)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move_choice = int(input("Enter your move (1-9): "))
        except ValueError:
            print("An integer value is expected")
            continue

        try:
            move_choice = board_positions[move_choice]
            if move_choice not in make_list_of_free_fields(board):
                print("That is not available")
                continue
            break
        except KeyError:
                print("That is not a valid choice")
                continue
    
    x, y = move_choice
    board[x][y] = 'O'

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    available = []
    for pos, (x, y) in board_positions.items():
        if pos == board[x][y]:
            available.append((x, y))
    return available


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == board[0][1] == board[0][2] == sign: return True
    if board[1][0] == board[1][1] == board[1][2] == sign: return True
    if board[2][0] == board[2][1] == board[2][2] == sign: return True
    if board[0][0] == board[1][0] == board[2][0] == sign: return True
    if board[0][1] == board[1][1] == board[2][1] == sign: return True
    if board[0][2] == board[1][2] == board[2][2] == sign: return True
    if board[0][0] == board[1][1] == board[2][2] == sign: return True
    if board[0][2] == board[1][1] == board[2][0] == sign: return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)

    if board_positions[5] in free_fields:
        x, y = board_positions[5]
    else:
        x, y = free_fields[randrange(len(free_fields))]

    board[x][y] = 'X'
    display_board(board)


# board_1 = board[:]
# board_2 = [[1,2,3],[4,'X','O'],[7,8,9]]
# board_3 = [['O','X','X'],['O','X',6],['O',8,9]]
# board_4 = [[1,2,'X'],[4,'X','O'],['X','O',9]]
# print(board_positions)

# print(victory_for(board_4, 'X'))

# main loop
while True:
    draw_move(board)
    if victory_for(board, 'X'):
        print("X has won!")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("O has won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("The game is a tie.")
        break
