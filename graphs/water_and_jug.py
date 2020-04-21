'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply 
available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets 
by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

'''
from collections import deque

def can_measure_water(x, y, z):
    que = deque([(0, 0)])
    visited = set()
    if x + y < z: return False
    while que:
        i, j = que.popleft()
        visited.add((i, j))
        states = set()
        if i + j == z: return True

        states.add((x, j))
        states.add((i, y))
        states.add((0, j))
        states.add((i, 0))
        states.add((min(i + j, x), (i + j) - min(i + j, x)))
        states.add(((i + j) - min(i + j, y), min(i + j, y)))

        que.extend(states - visited)

    return False 
