'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to
 make the gray scale of 
each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a 
cell has less than 8 
surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''

def image_smoother(M):
    new_matrix = [[None for _ in range(len(M[0]))] for _ in range(len(M))]
        
    def get_neighbors(i, j):
        neighbors = []
        directions = [(i-1, j-1), (i-1, j), (i-1, j+1), 
                      (i, j-1), (i, j), (i, j+1), 
                      (i+1, j-1), (i+1, j), (i+1, j+1)]
        
        for direction in directions:
            if 0 <= direction[0] < len(M) and 0 <= direction[1] < len(M[0]):
                neighbors.append(direction)
        
        return neighbors
    
    def grey(i, j):
        directions = get_neighbors(i, j)
        sumx = sum([M[direction[0]][direction[1]] for direction in directions])
        new_matrix[i][j] = sumx // len(directions)
        
    
    for i in range(len(M)):
        for j in range(len(M[0])):
            grey(i, j)
    
    return new_matrix