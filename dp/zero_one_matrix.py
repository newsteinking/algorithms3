'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
'''

import sys
def zero_matrix(matrix):
    R, C = len(matrix), len(matrix[0])
    distances = [[sys.maxsize for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                distances[i][j] = 0
            else:
                if i > 0:
                    distances[i][j] = min(distances[i][j], distances[i-1][j] + 1)
                if j > 0: 
                    distances[i][j] = min(distances[i][j], distances[i][j-1] + 1)

    for i in reversed(range(R)):
        for j in reversed(range(C)):
            if i < R-1:
                distances[i][j] = min(distances[i][j], distances[i+1][j] + 1)
            if j < C-1: 
                distances[i][j] = min(distances[i][j], distances[i][j+1] + 1)

    return distances