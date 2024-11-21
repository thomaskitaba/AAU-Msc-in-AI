#!/usr/bin/python3
import math
# steps to solve it
# get empty positions location
# loop 1 upto 10  to put fill the empty position
# if valid   then add it to the board and got to then next empty location (use recursion)
#  if recuresion succeds put return true   else.  if numbers are invalid at the end return false
# 

def validate(board, row, col, num):
    # Check column and row
    for r in range(9):
        if board[r][col] == num or board[row][r] == num:
            return False
    
    # Check (3 X 3) grid
    start_col = 3 * math.floor(col / 3)
    start_row = 3 * math.floor(row / 3)
    
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True
    
def emptyPosition(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                 return (r, c)
    return None

def print_board(board):
    for r in board:
        print(r)
        
def  solve_sudoku(board):
    empty = emptyPosition(board)
    if empty:
        row, col = empty
    else:
        return True
    for num in range(1, 10):
        if validate(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
    
    if (solve_sudoku(board)):
        print("Solved board")
        print_board(board)
    else:
        print("Board is unsolvable")
    
