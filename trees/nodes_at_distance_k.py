'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node. 
 The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
'''
from collections import defaultdict, deque

def distance_k(root, target, k):
    graph = defaultdict(list)
    parents = {root:None}
    
    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    que = deque([root])
    while que:
        current = que.popleft()
        if parents[current]: 
            add_edge(current, parents[current])
        if current.left:
            parents[current.left] = current
            que.append(current.left)
            add_edge(current, current.left)
        if current.right:
            parents[current.right] = current
            que.append(current.right)
            add_edge(current, current.right)

    que, seen = deque([target]), set()
    while k:
        node_count = len(que)
        for _ in range(node_count):
            current = que.popleft()
            seen.add(current)
            for node in graph[current]:
                if node not in seen:
                    que.append(node)
                    seen.add(node)
        k -= 1
        
    return sorted(x.val for x in que)


