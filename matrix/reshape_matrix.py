'''
In MATLAB, there is a very useful function called 'reshape', which can 
reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two 
positive integers r and c representing the row number and column number of 
the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original
 matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output
 the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 
matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the 
riginal matrix.
'''

def reshape_matrix(matrix, rows, cols):
    if len(matrix)*len(matrix[0]) != rows*cols:
        return matrix 
    
    matrix = [item for innerlist in matrix for item in innerlist]
    new_matrix = [[None for _ in range(cols)] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[index]
            index += 1
    return new_matrix