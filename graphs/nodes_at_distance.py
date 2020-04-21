'''
Given a binary tree of integers. All nodes in the binary tree have distinct values. You are given an integer B. You have to find all the nodes that are at a distance of exactly C from the node containing value B. Return an array of integers consisting all the nodes that are C distance from node containing value B. Note:
You may return the nodes in any order.
Your solution will run on multiple test cases, if you are using global variables make sure to clear every time .
Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= Node values <= 10^9 
0 <= B <= 10^9
0 <= C <= 100
For Example
Input 1:
            1
          /   \
         2    3
        /   / \
       4   5 6  7
      /
     8 

     B = 3
     C = 3
Output 1:
    [4, 5]

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
        B = 4
        C = 1
Output 2:
    [2, 5]
'''


from collections import deque, defaultdict

def nodes_at_distance(A, B, C):
    if C == 0: return [B]
        
    graph = defaultdict(list)
    
    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs_tree(root):
        que = deque([root])
        while que:
            current = que.popleft()
            if current.left:
                add_edge(current.val, current.left.val)
                que.append(current.left)
            if current.right:
                add_edge(current.val, current.right.val)
                que.append(current.right)

    def bfs(source, k):
        que = deque([source])
        seen = set()
        level = 0
        while que:
            count = len(que)
            for _ in range(count):
                current = que.popleft()
                seen.add(current)
            
                for node in graph[current]:
                    if node not in seen:
                        que.append(node)
                        seen.add(node)
            level += 1
            if level == k: break
        return list(que)
    
    bfs_tree(A)
    return bfs(B, C)
        
        