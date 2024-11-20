#!/usr/bin/python3

def is_valid(board, row, col, num):
    return False

def find_empty_space(board):
    row = col = 0
    return (row, col)

def solve_sudoku(board):
    empty = find_empty_space(board)
    # place num 1 - 9  to this location
    board[row] = col
    num = 1
    if is_valid(board, row, col, num):
        return True
    else:
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
    else:
        print("Board is unsolvable")
    
