'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over 
every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
'''


def unique_paths_three(grid):
    remain = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: sr, sc = i, j 
            if grid[i][j] == 2: dr, dc = i, j
            if grid[i][j] != -1: remain += 1


    def neighbors(i, j):
        for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i -1, j)):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] % 2 == 0:
                yield x, y 

    def dfs(row, col, remain):
        nonlocal paths
        remain -= 1
        if remain < 0: return 
        if row == dr and col == dc:
            if remain == 0: paths += 1
            return 

        grid[row][col] = -1
        for x, y in neighbors(row, col):
            dfs(x, y, remain)
        grid[row][col] = 0

    paths = 0
    dfs(sr, sc, remain)
    return paths
