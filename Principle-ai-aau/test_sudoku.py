import unittest
from sudoku import is_valid, find_empty_space, solve_sudoku

class TestSudoku(unittest.TestCase):
    
    def setUp(self):
        # A sample Sudoku board with some empty cells
        self.board = [
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
        
    def test_is_valid(self):
        # Test the validity of placing numbers on the board
        # For example, placing 1 in position (0,2) is invalid because 1 already exists in row 0
        self.assertFalse(is_valid(self.board, 0, 2, 1))
        # Placing 4 in position (0, 2) should be valid as it does not conflict with any number in the row, column, or 3x3 grid
        self.assertTrue(is_valid(self.board, 0, 2, 4))

    def test_find_empty_space(self):
        # Test the function that finds an empty space
        self.assertEqual(find_empty_space(self.board), (0, 2))  # the first empty cell is at (0, 2)
    
    def test_solve_sudoku(self):
        # Test if the Sudoku solver can solve the given board
        solved_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        
        self.assertTrue(solve_sudoku(self.board))  # This should return True, meaning it is solvable
        self.assertEqual(self.board, solved_board)  # The board should match the solved board
    
    def test_unsolvable_board(self):
        # Create an unsolvable board where there's a conflict
        unsolvable_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 0, 9]
        ]
        
        self.assertFalse(solve_sudoku(unsolvable_board))  # This should return False as the board is unsolvable

if __name__ == "__main__":
    unittest.main()
