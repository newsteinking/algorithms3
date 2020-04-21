'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the 
source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive 
the signal? If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''

from heapq import heappush, heappop
from collections import defaultdict, deque

def network_delay_time(times, n, source):
    graph = defaultdict(set)
    for u, v, t in times:
        graph[u].add((v, t))

    def djikstra():    
        distances = [None] * (n + 1)
        que = [(0, source)]

        while que:
            path_len, v = heappop(que)
            if distances[v] is None:
                distances[v] = path_len
                for node, edge_len in graph[v]:
                    if distances[node] is None:
                        heappush(que, [path_len  + edge_len, node])

        return distances

    distances = djikstra()
    if None in distances[1:]: return -1
    else: return max(distances[1:])
