'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

import heapq
def kth_smallest_matrix(matrix, k):
    row = []
    for index, val in enumerate(matrix[0]):
        heapq.heappush(row, (val, index, 0))
                
    for _ in range(k - 1):
        val, index, position = heapq.heappop(row)
        if position + 1 < len(matrix):
            heapq.heappush(row, (matrix[position + 1][index], index, position + 1))
    
    return heapq.heappop(row)[0]

