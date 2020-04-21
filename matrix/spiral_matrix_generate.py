'''
Given a positive integer n, generate a square matrix filled with elements 
from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def generate_spiral_matrix(N):
    top, bottom, left, right = 0, N-1, 0, N-1
    direction = 0
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    number = 1
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right+1):
                matrix[top][i] = number
                number += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom+1):
                matrix[i][right] = number
                number += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = number
                number += 1
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = number
                number += 1
            left += 1
        direction = (direction + 1) % 4
    return matrix
