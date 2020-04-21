'''
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off 
the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the 
grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
'''
def number_of_enclaves(A):

    def dfs(i, j):
        A[i][j] = 0
        directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for x, y in directions:
            if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y]:
                dfs(x, y)

    for i in range(len(A)):
        if A[i][0]: dfs(i, 0)
        if A[i][len(A[0]) - 1]: dfs(i, len(A[0]) - 1)

    for i in range(len(A[0])):
        if A[0][i]: dfs(0, i)
        if A[len(A) - 1][i]: dfs(len(A) - 1, i)

    return sum(sum(row) for row in A)
    
def number_of_enclaves(A):
    
    def neighbors(i, j):
        nei = []
        directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for x, y in directions:
            if 0 <= x < len(A) and 0 <= y < len(A[0]):
                nei.append((x, y))
        return nei
    
    def dfs(i, j):
        nonlocal enclave
        seen.add((i, j))
        nei = neighbors(i, j)
        if len(nei) < 4: 
            enclave = False
        for x, y in nei:
            if A[x][y] and (x, y) not in seen:
                dfs(x, y)

    seen, count = set(), 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] and (i, j) not in seen:
                c = len(seen)
                enclave = True 
                dfs(i, j)
                if enclave: count += len(seen) - c

    return count 
