'''
According to the Wikipedia's article: "The Game of Life, also known simply as 
Life, is a cellular automaton devised by the British mathematician John Horton 
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead 
(0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by 
reproduction.
Write a function to compute the next state (after one update) of the board given 
its current state. The next state is created by applying the above rules 
simultaneously to every cell in the current state, where births and deaths 
occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is 
infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
'''

def game_of_life(board):

    def get_live_count(i, j):
        directions = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                      (i, j - 1), (i, j + 1), 
                      (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        alive = 0
        for m, n in directions:
            if 0 <= m < len(board) and 0 <= n < len(board[0]):
                if board[m][n] == 2: alive += 1
                if board[m][n] == 1: alive += 1

        return alive

    def update(i, j):
        alive = get_live_count(i, j)
        if board[i][j] == 0 or board[i][j] == 3:
            if alive == 3: board[i][j] = 3
        else:
            if alive < 2 or alive > 3: board[i][j] = 2
    
    def restore_board():
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == 2: board[i][j] = 0
                if col == 3: board[i][j] = 1

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            update(i, j)

    restore_board()
    return board
