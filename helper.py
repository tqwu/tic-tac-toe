
def checkWin(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for (i, j, k) in winning_combinations:
        if board[i] == board[j] == board[k] and board[i] in {'X', 'O'}:
            return True
    return False

def printBoard(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def printHelper():
    print("\nEnter a number between 1 through 9 to place your tile:")
    for row in [[1,2,3],[4,5,6],[7,8,9]]: print(row)
