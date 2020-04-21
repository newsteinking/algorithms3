'''pri
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown 
'''

def nqueens(n):
    board = [['.'] * n for _ in range(n)]

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q': return False 

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q': return False 

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q': return False 

        return True 

    def solve(board, col):
        if col == n:               
            result.append([''.join(x) for x in board])

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                if solve(board, col + 1): return True 
                board[i][col] = '.'

        return False

    result = []
    solve(board, 0)
    return result
