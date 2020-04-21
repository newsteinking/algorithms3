'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed 
by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.
'''
from math import sqrt

def largest_area(points):
    area = 0

    def distance(x, y):
        return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

    def t_area(i, j, k):
        a = distance(i, j)
        b = distance(j, k)
        c = distance(k, i)
        return 0.25 * sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))         

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                area = max(area, t_area(i, j, k))

    return area