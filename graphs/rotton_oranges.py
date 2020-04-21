'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.
'''
from collections import deque
def orange(grid):
    R, C = len(grid), len(grid[0])
    queue = deque()
    
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r, c))

    def neighbors(r, c):
        for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    d = 0
    while queue:
        node_count = len(queue)
        for _ in range(node_count):
            r, c = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
        d += 1

    if any(1 in row for row in grid):
        return -1
    return 0 if d == 0 else d - 1