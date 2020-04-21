'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is 
composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are 
different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  
If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]
Output: 2
Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

from collections import deque 

def shortest_path_binary_matrix(grid) -> int:
    if grid[0][0] or grid[-1][-1]: return -1
    que = deque([(0, 0)])
    
    def neighbors(i, j):
        for dx, dy in zip((1, 1, 1, 0, 0, -1, -1, -1), (-1, 0, 1, -1, 1, -1, 0, 1)):
            x, y = i + dx, j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                yield x, y
    
    level = 1
    seen = set()
    while que:
        node_count = len(que)
        for _ in range(node_count):
            i, j = que.popleft()
            seen.add((i, j))
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return level
            
            for x, y in neighbors(i, j):
                if (x, y) not in seen:
                    que.append((x, y))
                    seen.add((x, y))
        level += 1
    
    return -1