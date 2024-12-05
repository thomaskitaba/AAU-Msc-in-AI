#!/usr/bin/python3
""" Nqueens """

import sys

# accept size of board from user
board = []
solutions = []
n = 0

def check_position(n, row, col):
    """
     check if placing a queen at row, col  is valid
     both vertically and diagonally
    """
    for r in range(row):
        # means same column or diagonal
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def nqueens(row, board, solutions):
    """
    recursive function that uses backtracking
    """
    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        if check_position(n, row, col):
            # place queen on board denoted by placing col on row
            board[row] = col
            # recursively call nqueens to place queen on the next row
            nqueens(row + 1, board, solutions)
            # backtack and remove the queen from previous row
            board[row] = -1
    
    return solutions
    # print("solve n queens problem {}".format(n))
if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: Enter number of Queens")
    if (len(sys.argv) > 2):
        print("Usage: Invalid number of arguments")
    if (len(sys.argv) == 2):
        # convert argv[1] to integer
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Usage: Enter a valid integer")
        if (n < 4):
            print("Usage: Enter a number greater than 3")
    row = 0
    # fill the board with -1
    board = [-1] * n
    # print(board)
    
    solution = nqueens(row, board, solutions)
    print(solution)
    
    