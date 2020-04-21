'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such 
that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  
(Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
'''

def magic_squares(grid):

    def is_magic(row, col):
        numbers = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                if grid[i][j] in numbers or grid[i][j] > 9 or grid[i][j] < 1: return False
                numbers.add(grid[i][j])

        target = sum(grid[row][col:col+3])

        for i in range(3):
            sumx = sum(grid[row][col:col+3])
            if sumx != target: return False

        for i in range(3):
            sumx = 0
            for j in range(3):
                sumx += grid[row + j][col + i]
            if sumx != target: return False 

        diagonal1 = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
        diagonal2 = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]
        return diagonal1 == diagonal2 == target



    total_magic_grids = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            if is_magic(i, j):
                total_magic_grids += 1

    return total_magic_grids