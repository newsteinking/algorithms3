'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed 
by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.
'''

import math

def dis(p1,p2):
    return math.sqrt((p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2) 
    
def area(a,b,c):
    h = (a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)
    try: return math.sqrt(h) / 4
    except: return 0


def largest_area(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    l = len(points)
    d = [[0 for i in range(l)] for j in range(l)]
    for i in range(l - 1):
        for j in range(i, l):
            d[i][j] = dis(points[i], points[j])
            
    maxarea = 0
    for i in range(l - 2):
        for j in range(i, l - 1):
            for k in range(j, l):
                maxarea = max(maxarea, area(d[i][j], d[i][k], d[j][k]))
                
    return maxarea 