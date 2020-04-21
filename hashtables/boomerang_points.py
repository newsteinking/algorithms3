'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all 
in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
import math

def boomerang(points):
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            f = p[0]-q[0]
            s = p[1]-q[1]
            cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
        for k in cmap:
            res += cmap[k] * (cmap[k] -1)
    return res


def boomerang_v2(points):
    count = 0

    def distance(i, j):
        return math.sqrt(math.pow((points[i][0] - points[j][0]), 2) + math.pow((points[i][1] - points[j][1]), 2))

    for i in range(len(points)):
        for j in range(len(points)):
            for k in range(len(points)):
                if len(set({i, j, k})) == 3 and distance(i, j) == distance(i, k):
                    count += 1

    return count

def boomerangs_v3(points):
    count = 0
        
    def distance(i, j):
        x = points[i][0] - points[j][0]
        y = points[i][1] - points[j][1]
        return x*x + y*y
    
    n = len(points)
    distances = [[None] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = distances[j][i] = distance(i, j)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if len(set({i, j, k})) == 3 and distances[i][j] == distances[i][k]:
                    count += 1
    
    return count