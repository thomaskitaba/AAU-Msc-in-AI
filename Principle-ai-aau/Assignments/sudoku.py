#!/usr/bin/python3
import math 
def is_valid(board, row, col, num):
    """ check if placing num on (row, col) is valid """
    # Check column
    for i in range(9):
        if board[i][col] == num or board[row][i] == num:
            return False
    # Check part of sudoku (3 x 3) grid
    start_col = 3 * math.floor(col / 3)   # 3 * (col // 3)
    start_row = 3 * (row // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False  # means the location is not empty
    return True # means the location has value
    
def find_empty_space(board):
    """ 
        return row, col if empty location 
        to place num is found 
    """
    for r in range(9):
        for c in range(9):
            # 0 means empty location on the board
            if board[r][c] == 0:
                return (r, c)
    return None
            
def solve_sudoku(board):
    """
        recursive function that uses backtracking
    """
    empty = find_empty_space(board)
    if empty:
        row, col = empty # destructure the returned values
    else:
        return True  # The board is full therefore it is solved
    # Place num 1 - 9  to this location
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False

def print_board(board):
    """
        print the sudoku board
    """
    for r in range(9):
        for c in range(9):
            if c != 9:
                print(board[r][c], end=" | ")
        print("")
        

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
    
