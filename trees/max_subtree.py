from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
import itertools

class PQ:
    
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed>'
        self.counter = itertools.count()    

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return [priority, task]
        raise KeyError('pop from an empty priority queue')

def max_subtree(A, B, C, D):
    graph = defaultdict(set)
    
    for i in range(len(B)):
        graph[B[i]].add(C[i])
        graph[C[i]].add(B[i])

    def bfs(source, counter):
        que = deque([source])
        count = 0
        seen = set()
        while que:
            current = que.popleft()
            component_id[current] = counter
            count += 1
            seen.add(current)
            for vertex in graph[current]:
                if vertex not in seen:
                    que.append(vertex)
                    seen.add(vertex)

        return count 

    result, component_id, pq = [], {}, PQ()
    counter = itertools.count()

    for i in range(len(D)):
        source = B[D[i] - 1]
        dest = C[D[i] - 1]
        graph[source].remove(dest)
        graph[dest].remove(source)

        count = next(counter)
        if source not in component_id: component_id[source] = next(counter)
        if dest not in component_id: component_id[dest] = next(counter)

        comp_1 = component_id[source]
        comp_2 = component_id[dest]
        if comp_1 == comp_2: comp_2 = next(counter)

        count1 = bfs(source, comp_1)
        count2 = bfs(dest, comp_2)
        pq.add_task(comp_1, -count1)
        pq.add_task(comp_2, -count2)
        priority, task = pq.pop_task()
        result.append(-priority)
        pq.add_task(task, priority)

    return result 
