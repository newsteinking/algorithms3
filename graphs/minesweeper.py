'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''

def minesweeper(board, click):

    def dfs(i, j):
        if board[i][j] == 'E':
            next_valid_points, count_mines = [], 0
            for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
                         (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    count_mines += board[x][y] == 'M'
                    next_valid_points.append((x, y))

            if count_mines == 0:
                board[i][j] = 'B'
                for x, y in next_valid_points: dfs(x, y)
            else: board[i][j] = str(count_mines)


    i, j = click[0], click[1] 
    m, n = len(board), len(board[0])

    if board[i][j] == 'M': board[i][j] = 'X'
    else: dfs(i, j)

    return board
