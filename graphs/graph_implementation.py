from collections import defaultdict, deque
import sys

class GraphMatrix:

    def __init__(self):
        self.graph = []

    def add_edge(self, u, v):
        if v < u: u, v = v, u
        if v >= len(self.graph):
            temp = self.graph
            self.graph = [[-1 for x in range(2*v)] for x in range(2*v)]
            for i in range(len(temp)):
                for j in range(len(temp)):
                    self.graph[i][j] = temp[i][j]

        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def bfs(self, root):
        que = deque([root])
        visited = set()
        result = []

        while que:
            current = que.popleft()
            result.append(current)
            visited.add(root)

            for index, vertex in enumerate(self.graph[current]):
                if index not in visited and vertex != -1:
                    que.append(index)
                    visited.add(index)

        return result

    def dfs(self, root):
        visited, result = set(), list()

        def helper(root, visited):
            visited.add(root)
            result.append(root)

            for index, vertex in enumerate(self.graph[root]):
                if index not in visited and vertex != -1:
                    helper(index, visited)

        helper(root, visited)
        return result

    def count(self):
        return len(self.bfs(0))

    def dijkstra(self, root):
        V = self.count()
        distances = [sys.maxsize]*V
        distances[root] = 0
        spt = set()
        parents = [None]*V

        def find_min(distances, spt, V):
            minx = sys.maxsize

            for v in range(V):
                if distances[v] < minx and v not in spt:
                    minx = distances[v]
                    min_index = v

            return min_index

        for _ in range(V):
            u = find_min(distances, spt, V)
            spt.add(u)

            for v in range(V):
                if (self.graph[u][v] > 0 and 
                        v not in spt and 
                        distances[v] > distances[u] + self.graph[u][v]):
                    distances[v] = distances[u] + self.graph[u][v]
                    parents[v] = u

        
        return parents

    def print_shortest_paths(self, source):
        result = []
        parents = self.dijkstra(source)
        
        for i in range(1, len(parents)):
            temp = []
            j = i
            while j:
                temp.insert(0, j)
                j = parents[j]
            temp.insert(0, 0)
            result.append(temp)
        return result



class GraphList:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, root):
        que, visited, result = deque([root]), set(), list()

        while que:
            current = que.popleft()
            visited.add(current)
            result.append(current)

            for vertex in self.graph[current]:
                if vertex not in visited:
                    visited.add(vertex)
                    que.append(vertex)

        return result

    def dfs(self, root):
        visited, result = set(), list()

        def helper(root, visited):
            visited.add(root)
            result.append(root)

            for vertex in self.graph[root]:
                if vertex not in visited:
                    helper(vertex, visited)

        helper(root, visited)
        return result

    def dfs_iterative(self, root):
        visited, stack, result = set(), list([root]), list()

        while stack:
            current = stack.pop()
            if current not in visited:
                result.append(current)
                visited.add(current)

            for vertex in self.graph[current]:
                if vertex not in visited:
                    stack.append(vertex)

        return result

    def cycle(self):
        visited = set()
        
        def cycleUtil(current, visited, parent):
            visited.add(current)
            for vertex in self.graph[current]:
                if vertex not in visited:
                    if cycleUtil(vertex, visited, current):
                        return True
                elif parent != vertex:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if cycleUtil(vertex, visited, -1):
                    return True
        return False

    def count_connected(self):
        visited = set()
        count = 0

        def bfs(source):
            que = deque([source])
            while que:
                current = que.popleft()
                visited.add(current)

                for vertex in self.graph[current]:
                    if vertex not in visited:
                        que.append(vertex)
                        visited.add(vertex)
            
        count = 0
        for vertex in self.graph:
            if vertex not in visited:
                bfs(vertex)
                count += 1
        return count

    def list_connected(self):
        visited = set()
        result = []

        def bfs(source):
            temp = []
            que = deque([source])
            while que:
                current = que.popleft()
                visited.add(current)
                temp.append(current)

                for vertex in self.graph[current]:
                    if vertex not in visited:
                        que.append(vertex)
                        visited.add(vertex)
            result.append(sorted(temp))
        
        for vertex in self.graph:
            if vertex not in visited:
                bfs(vertex)

        return result

    def bipartite(self):
        color = 0
        colors = {0:0}
        que = deque([0])

        while que:
            current = que.popleft()

            for vertex in self.graph[current]:
                if vertex not in colors:
                    que.append(vertex)
                    colors[vertex] = 1 - colors[current]
                elif colors[vertex] == colors[current]:
                    return False
        return True





