'''
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 
1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
'''
from collections import deque 

def shortest_bridge(A):
    components1 = set()
    components2 = set()

    def get_one():
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]: return (i, j)

    def neighbors(i, j):
        directions = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
        for x, y in directions:
            if 0 <= x < len(A) and 0 <= y < len(A[0]):
                yield x, y

    def dfs(i, j, c_id):
        A[i][j] = 0
        if c_id == 1: components1.add((i, j))
        if c_id == 2: components2.add((i, j))

        for x, y in neighbors(i, j):
            if A[x][y]: dfs(x, y, c_id)

    dfs(*get_one(), 1)
    dfs(*get_one(), 2)

    def bfs():
        distance = 0
        que = deque([x for x in components1])
        seen = set(x for x in components1)
        while que:
            node_count = len(que)
            for _ in range(node_count):
                i, j = que.popleft()
                if (i, j) in components2: return distance - 1
                seen.add((i, j))
                for x, y in neighbors(i, j):
                    if (x, y) not in seen:
                        que.append((x, y))
                        seen.add((x, y))
            distance += 1

    return bfs()









