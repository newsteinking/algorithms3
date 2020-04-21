'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two 
queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

def total_queens(n):
    board = [[0] * n for _ in range(n)]
    count = 0

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i]: return False 

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]: return False 

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j]: return False 

        return True 

    def solve(board, col):
        nonlocal count 
        if col == n: count += 1
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1): return True 
                board[i][col] = 0
        
        return False 

    solve(board, 0)
    return count 

