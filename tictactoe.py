
# from typing import List

# def printBoard(moves_X: List[int], moves_O: List[int]) -> List[List[int]]:
#     board = [['_'] * 3 for _ in range(3)]
#     for i in moves_X: board[i // 3][i % 3] = 'X'
#     for i in moves_O: board[i // 3][i % 3] = 'O'
#     for r in board: print(r)

def checkWin(board):
    if (board[0] == board[1] == board[2] or \
        board[3] == board[4] == board[5] or \
        board[6] == board[7] == board[8] or \
        board[0] == board[3] == board[6] or \
        board[1] == board[4] == board[7] or \
        board[2] == board[5] == board[8] or \
        board[0] == board[4] == board[8] or \
        board[2] == board[4] == board[6]):
        return True
    return False

def printBoard(board):
    for row in board: print(row)

def printHelper():
    print("\nEnter a number between 1 through 9 to place your tile:")
    for row in [[1,2,3],[4,5,6],[7,8,9]]: print(row)

def main():

    user_X = True
    board = [['_'] * 3 for _ in range(3)]
    marked = set()

    # Continuously read user input until board is filled or winner is declared
    while True:

        # Player 1's turn
        if user_X:
            move = int(input("\nPlayer 1, enter your square: ")) - 1
            if move in marked:
                print("Tile has already been filled, please select another tile")
                continue
            board[move // 3][move % 3] = 'X'
            if checkWin(board):
                print('Player 1 is winner!')
                return
            marked.add(move)
            printBoard(board)
            user_X = False

        # Player 2's turn
        else:
            move = int(input("\nPlayer 2, enter your square: ")) - 1
            if move in marked:
                print("Tile has already been filled, please select another tile")
                continue
            board[move // 3][move % 3] = 'O'
            if checkWin(board):
                print('Player 1 is winner!')
                return
            marked.add(move)
            printBoard(board)
            user_X = True

        # If board is completely filled and no winner was declared, result is a draw
        if len(marked) == 9:
            print('Draw!')
            return
        # if user_X:
        # if user_input.lower() == 'exit':
        #     print("Exiting the loop. Goodbye!")
        #     break  # Exit the loop when the user types 'exit'
        
        # # Process the input
        # print(f"You entered: {user_input}")

printHelper()
main()
printBoard()
