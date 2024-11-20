#!/usr/bin/bash
def is_valid(board, row,col, num):
    
# def is_valid(board, row, col, num): 
    # Check the row and col
    for c in range(9):
        if board[row][c] == num or  if board[r][col] == num:
            return False
    

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def find_empty(board):
    """
    Find the next empty cell in the board (a cell with 0).
    Return (row, col) if found, or None if the board is full.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                return (row, col)
    return None

def solve_sudoku(board):
    """
    Solve the Sudoku board using backtracking.
    Return True if solved, False otherwise.
    """
    empty = find_empty(board)  # Find the next empty cell
    if not empty:
        return True  # No empty cells left, board is solved

    row, col = empty

    # Try placing numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Place the number
            if solve_sudoku(board):  # Recurse
                return True
            # Backtrack
            board[row][col] = 0
    
    return False  # No solution found

# Example usage
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


