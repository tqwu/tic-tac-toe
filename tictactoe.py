
from helper import checkWin, printBoard, printHelper, invalidEntry

printHelper()

user_X = True
board = ['_'] * 9
marked = set()

# Set up board
while True:

    board_pref = input("\nBoard preference: ").upper()

    if board_pref == 'N':
        board = [str(i + 1) for i in range(9)]
        break
    elif board_pref == 'B':
        break
    else:
        invalidEntry()

printBoard(board)

# Continuously read user input until board is filled or winner is declared
while True:

    player = 1 if user_X else 2
    tile = 'X' if user_X else 'O'

    move = input(f"\nPlayer {player}, enter a number from 1-9 to place your '{tile}' tile: ")

    if not move.isdigit() or not (1 <= int(move) <= 9):
        invalidEntry()
        continue

    if move in marked:
        print("Tile has already been filled, please select another tile")
        continue

    board[int(move) - 1] = tile
    marked.add(move)
    printBoard(board)

    if checkWin(board):
        print(f"\nCONGRATULATIONS!!! Player {player} is the winner!")
        break

    # If board is completely filled and no winner was declared, result is a draw
    if len(marked) == 9:
        print('\nDRAW! How about another game?')
        break

    user_X = not user_X
