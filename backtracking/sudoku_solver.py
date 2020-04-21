'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''

def solve_sudoku(board):

    def find_unassigned():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j 
        return -1, -1

    def check_row(row, num):
        for char in board[row]:
            if char == num: return False 
        return True 

    def check_col(col, num):
        for row in board:
            if row[col] == num: return False
        return True

    def check_square(box_row, box_col, num):
        for row in range(box_row, box_row + 3):
            for col in range(box_col, box_col + 3):
                if board[row][col] == num:
                    return False 
        return True

    def is_safe(row, col, num):
        box_row = row - row % 3
        box_col = col - col % 3
        if check_row(row, num) and check_col(col, num) and check_square(box_row, box_col, num):
            return True 
        return False 

    def solve():
        row, col = find_unassigned()
        if row == -1 and col == -1:
            return True 
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if is_safe(row, col, num):
                board[row][col] = num 
                if solve(): return True 
                board[row][col] = '.'

        return False
    
    solve()
    return board 

    
