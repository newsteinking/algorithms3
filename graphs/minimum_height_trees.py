'''
For an undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum 
height are called minimum height trees (MHTs). Given such a graph, write a function to find 
all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n 
and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

from collections import defaultdict, deque

def find_min_height_trees(n, edges):
    graph, parents = defaultdict(set), {}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    def bfs(source):
        seen = set()
        que = deque([source])
        while que:
            longest = que[0]
            for _ in range(len(que)):
                current = que.popleft()
                seen.add(current)
                for node in graph[current]:
                    if node not in seen:
                        parents[node] = current
                        que.append(node)
                        seen.add(node)
        return longest

    start = bfs(0)
    end = bfs(start)
    
    path = []
    while end != start:
        path.append(end)
        end = parents[end]
    path.append(end)
    
    mid = len(path) // 2
    
    return [path[mid - 1], path[mid]] if len(path) % 2 == 0 else [path[mid]]


