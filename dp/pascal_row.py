'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's 
triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
'''


def pascal_row(n:int) -> list:
    triangle = []
    for i in range(n):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1

        for j in range(1, i):
            row[j] = triangle[j-1] + triangle[j]
        triangle = row
    return triangle
