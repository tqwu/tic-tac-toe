
# from typing import List
from helper import checkWin, printBoard, printHelper

printHelper()

user_X = True
board = ['_'] * 9
marked = set()

# Continuously read user input until board is filled or winner is declared
while True:

    # Player 1's turn
    if user_X:
        move = int(input("\nPlayer 1, enter your square: "))
        if not (1 <= move <= 9):
            print('Invalid entry, please try again')
            continue
        if move in marked:
            print("Tile has already been filled, please select another tile")
            continue
        board[move - 1] = 'X'
        if checkWin(board):
            print('\nPlayer 1 is winner!')
            break
        marked.add(move)
        printBoard(board)
        user_X = False

    # Player 2's turn
    else:
        move = int(input("\nPlayer 2, enter your square: "))
        if not (1 <= move <= 9):
            print('Invalid entry, please try again')
            continue
        if move in marked:
            print("Tile has already been filled, please select another tile")
            continue
        board[move - 1] = 'O'
        if checkWin(board):
            print('\nPlayer 2 is winner!')
            break
        marked.add(move)
        printBoard(board)
        user_X = True

    # If board is completely filled and no winner was declared, result is a draw
    if len(marked) == 9:
        print('Draw!')
        break

printBoard(board)
