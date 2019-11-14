def print_board(board):
    for row in board:
        print(row)

def is_valid_size(board):

    is_valid = True
    if len(board) != 3:
        is_valid = False 
    for row in board:
        if len(row) != 3:
            is_valid = False
    return is_valid

def move(board, location, player):
    if not is_valid_size(board): 
        raise Exception('Game board size is not valid!')

    row_number = location[0]
    col_number = location[1]
    
    board[row_number][col_number] = player
    return board

game_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player = 'O'
loc = (0, 0)
game_board = move(game_board, loc, player)

player = 'X'
loc = (0, 1)
game_board = move(game_board, loc, player)

print_board = game_board
