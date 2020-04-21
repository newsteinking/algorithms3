'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

def surround(board):
    if not board: return 
    M = len(board)
    N = len(board[0])
    
    for i in range(M):
        for j in range(N):
            if board[i][j] == 'O':
                board[i][j] = '$'

    def fill(i, j):
        if i < 0 or i >= M or j < 0 or j >= N or board[i][j] != '$':
            return

        board[i][j] = 'O'

        fill(i+1, j)
        fill(i-1, j)
        fill(i, j+1)
        fill(i, j-1)

    for i in range(M):
        for j in range(N):
            if (i in [0, M-1] or j in [0, N-1]) and board[i][j] == '$':
                fill(i, j)
    
    for i in range(M):
        for j in range(N):
            if board[i][j] == '$':
                board[i][j] = 'X'

    return board

