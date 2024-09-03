
from helper import checkWin, printBoard, printHelper

printHelper()

user_X = True
board = ['_'] * 9
marked = set()

# Continuously read user input until board is filled or winner is declared
while True:

    player = 1 if user_X else 2

    move = input(f"\nPlayer {player}, enter your selection: ")

    if not move.isdigit() or not (1 <= int(move) <= 9):
        print('Invalid entry, please try again')
        continue

    if move in marked:
        print("Tile has already been filled, please select another tile")
        continue

    board[int(move) - 1] = 'X' if user_X else 'O'

    if checkWin(board):
        print(f"CONGRATULATIONS!!! Player {player} is winner!")
        break

    marked.add(move)
    printBoard(board)
    user_X = not user_X

    # If board is completely filled and no winner was declared, result is a draw
    if len(marked) == 9:
        print('Draw!')
        break

printBoard(board)
