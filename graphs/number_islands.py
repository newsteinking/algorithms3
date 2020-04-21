'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by 
water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


def number_islands(grid) -> int:

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        if grid[i][j] != '1':
            return

        grid[i][j] = '0'

        rows = [i+1, i-1, i, i]
        cols = [j, j, j-1, j+1]
        for k in range(4):
            dfs(rows[k], cols[k])

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count
