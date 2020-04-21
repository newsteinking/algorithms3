'''
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, 
with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
'''

def min_area_rectangle(points):
    seen = set()
    min_area = float('inf')

    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
        seen.add((x1, y1))

    return min_area if min_area != float('inf') else 0

def min_area_rectangle_v2(points):
    unique = set(map(tuple, points))

    min_area = float('inf')
    for i in range(len(points) - 1):
        for j in range(i):
            x1, y1 = points[i]
            x2, y2 = points[j]
             
            if x1 != x2 and y1 != y2 and (x1, y2) in unique and (x2, y1) in unique:
                min_area = min(min_area, abs(x2 - x1) * abs(y2 - y1))

    return 0 if min_area == float('inf') else min_area

