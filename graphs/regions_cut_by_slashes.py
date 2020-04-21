'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, '\', or blank space.  
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a '\' is represented as "\\".)

Return the number of regions.
'''

def region_count(grid):
    scaled_grid = [[0] * (len(grid) * 3) for _ in range(len(grid) * 3)]
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '\\':
                scaled_grid[i * 3][j * 3] = 1 
                scaled_grid[i * 3 + 1][j * 3 + 1] = 1 
                scaled_grid[i * 3 + 2][j * 3 + 2] = 1
            elif grid[i][j] == '/':
                scaled_grid[i * 3][j * 3 + 2] = 1
                scaled_grid[i * 3 + 1][j * 3 + 1] = 1
                scaled_grid[i * 3 + 2][j * 3] = 1

    def dfs(i, j):
        scaled_grid[i][j] = 1
        directions = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
        for x, y in directions:
            if 0 <= x < len(scaled_grid) and 0 <= y < len(scaled_grid) and scaled_grid[x][y] == 0:
                dfs(x, y)

    count = 0
    for i in range(len(scaled_grid)):
        for j in range(len(scaled_grid)):
            if scaled_grid[i][j] == 0:
                count += 1
                dfs(i, j)

    return count    



