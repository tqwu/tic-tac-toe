
from helper import checkWin, printBoard, printBoardHelper, printModeHelper, invalidEntry

user_X = True
robot = False
board = ['_'] * 9
marked = set()


# set up board
printBoardHelper()
while True:

    board_pref = input("\nBoard preference: ").upper()

    if board_pref == 'D':
        board = [str(i + 1) for i in range(9)]
        break
    elif board_pref == 'B':
        break
    else:
        invalidEntry()

printBoard(board)


# choose game mode: robot vs. multiplayer
printModeHelper()
while True:

    mode_pref = input("\nGame mode preference: ").upper()

    if mode_pref == 'R':
        robot = True
        print("You've selected to play against a robot!")
        break
    elif mode_pref == 'M':
        print("You've selected to play against another player on the command line!")
        break
    else:
        invalidEntry()


# continuously read user input until board is filled or winner is declared
while True:

    tile = 'X' if user_X else 'O'
    player = 1 if user_X else 2
    move = None

    # robot makes move
    if robot and not user_X:
        for i in range(1, 10):
            if str(i) not in marked:
                move = str(i)
                break
        print(f"\nThe robot has chosen tile {move}")

    # player(s) makes move
    else:
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
        if robot:
            if user_X: print("\nCONGRATULATIONS!!! You've won against the robot.")
            else: print("\nSorry, game over: the robot won. Try again?")
        else: print(f"\nCONGRATULATIONS!!! Player {player} is the winner!")
        break

    # if board is completely filled and no winner was declared, result is a draw
    if len(marked) == 9:
        print('\nDRAW! How about another game?')
        break

    user_X = not user_X
