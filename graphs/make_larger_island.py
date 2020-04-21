'''

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
'''
from collections import deque 
def largest_island(grid):
    components_id, components_area = {}, {}

    def neighbors(m, n):
        for x, y in ((m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                yield x, y

    def bfs(i, j, ID):
        que, count = deque([(i, j)]), 0
        while que:
            m, n = que.popleft()
            seen.add((m, n))
            components_id[(m, n)] = ID
            count += 1
            for x, y in neighbors(m, n):
                if (x, y) not in seen:
                    que.append((x, y))
                    seen.add((x, y))
        components_area[ID] = count            

    ID, seen = 0, set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in seen:
                bfs(i, j, ID)
                ID += 1
    
    if len(components_area) == 1 and components_area[0] == len(grid) * len(grid[0]):
        return len(grid) * len(grid[0])
    
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                id_set = set()
                for x, y in neighbors(i, j):
                    id_set.add(components_id[(x, y)])
                max_area = max(max_area, sum([components_area[ID] for ID in id_set]) + 1)        
    
    return max_area

