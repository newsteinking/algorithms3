'''
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, 
they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in 
the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
'''
from collections import defaultdict

def flower_planting(N, paths):
    graph = defaultdict(set)
    result = [0] * N 

    for u, v in paths: 
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)

    for i in range(N):
        result[i] = ({1,2,3,4} - {result[x] for x in graph[i]}).pop()

    return result 
