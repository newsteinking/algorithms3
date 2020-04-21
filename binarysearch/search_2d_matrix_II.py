'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the 
following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''

def search_matrix_sorted(matrix, target):
    if not matrix: return False
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1

    return False

def search_matrix_sorted_v2(matrix, target):
    
    def search(row):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1

        return False 

    if not matrix: return False
    for row in matrix:
        if search(row): return True
    return False