'''
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, 
formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
'''
from heapq import heappush, heappop, heapify

def largest_perimeter_triangle(sides):

    def valid(triangle):
        a, b, c = triangle
        a, b, c = -a, -b, -c
        return a + b > c and a + c > b and b + c > a

    sides = [-x for x in sides]
    heapify(sides)
    triangle = [heappop(sides), heappop(sides), heappop(sides)]
    heapify(triangle)

    if valid(triangle): return -sum(triangle)
    count = len(sides)
    for i in range(count):
        heappop(triangle)
        heappush(triangle, heappop(sides))
        if valid(triangle): return -sum(triangle)

    return 0

