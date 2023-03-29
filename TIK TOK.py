import random
# SYED ABDULLAH ASHAR    200901074      SEC B 
# The board is represented as a list of strings, where each string
# represents a row on the board. A blank space is represented by ' '.
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# The player is represented by 'X' and the computer is represented by 'O'.
player = 'X'
computer = 'O'

# Returns a list of all possible moves on the board.
def get_possible_moves(board):
    moves = []
    for i in range(9):
        if board[i] == ' ':
            moves.append(i)
    return moves

# Returns the score of the current board state for the player.
def get_score(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return 1
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return 1
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return 1
    if board[2] == board[4] == board[6] == player:
        return 1
    # No winner yet
    return 0

# Returns the result of applying the move to the board.
def make_move(board, move, player):
    board[move] = player
    return board

# Returns the result of undoing the move on the board.
def undo_move(board, move):
    board[move] = ' '
    return board

# Returns the optimal move for the computer using the Minimax algorithm.
def get_best_move(board, player):
    if player == computer:
        # Maximizing player (computer)
        best_score = -float('inf')
    else:
        # Minimizing player (user)
        best_score = float('inf')
    possible_moves = get_possible_moves(board)
    best_move = possible_moves[0]
    for move in possible_moves:
        board = make_move(board, move, player)
        if get_score(board, player) == 1:
            # If the move results in a win, return it immediately
            undo_move(board, move)
            return move
        if len(get_possible_moves(board)) == 0:
            # If the move results in a tie, score it as 0
            score = 0
        else:
            # Recursively call the function with the opposite player
            score = get_best_move(board, player=computer if player==player else player)
        undo_move(board, move)
        if player == computer:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    return best_move

# Prints the current board state.
def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

# The main game loop.
while True:
    # The user goes first.
    print_board(board)
    # Check if the game is over.
    if get_score(board, player) == 1:
        print(f'{player} wins!')
        break
    if len(get_possible_moves(board)) == 0:
        print('Tie game!')
        break

    # Get the user's move.
    while True:
        move = int(input('Enter your move (0-8): '))
        if move in get_possible_moves(board):
            board = make_move(board, move, player)
            break
        else:
            print('Invalid move. Try again.')

    # Check if the game is over.
    if get_score(board, player) == 1:
        print_board(board)
        print(f'{player} wins!')
        break
    if len(get_possible_moves(board)) == 0:
        print_board(board)
        print('Tie game!')
        break

    # Get the computer's move.
    print('Thinking...')
    move = get_best_move(board, computer)
    board = make_move(board, move, computer)

    # Print the board and the computer's move.
    print_board(board)
    print(f'Computer chooses {move}.')

