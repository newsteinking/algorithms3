'''

Given n points on a 2D plane, find the maximum number of points that lie on the same 
straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code 
definition to get new method signature.

'''

import math
from collections import Counter

def max_points(points):
    if len(points) < 3: return len(points)
    uniques = Counter(tuple(x) for x in points)
    points = list(uniques.keys())
    if len(points) == 1: return uniques[points[0]]
    max_count = 0
    for i in range(len(points) - 1):
        slopes = Counter()
        for j in range(i + 1, len(points)):
            dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
            if dx == 0: slope = '$'
            elif dy == 0: slope = 0
            else: slope = Decimal(dy) / dx

            slopes[slope] += uniques[points[j]]
        max_count = max(max_count, uniques[points[i]] + slopes.most_common(1)[0][1])

    return max_count