#!/usr/bin/python3
import sys

def validate(board, row, col):
    for r in range(row):
        if board[r] == col or (abs(r - row) == abs(board[r] - col)):
            return False
    return True
def nqueens(board, row, solutions):
    if row == n:
        solutions.append(board[:])
        return solutions
    
    for col in range(n):
        if validate(board, row, col):
            board[row] = col
            nqueens(board, row + 1, solutions)
            board[row] = -1
            
    return solutions

if __name__ == "__main__":
    n = int(sys.argv[1])
    solutions = []
    board = [-1] * n
    row = 0
    result = nqueens(board, row, solutions)
    print(result)













