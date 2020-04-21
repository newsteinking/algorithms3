'''
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
from collections import deque

def num_squares(n):
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    queue = deque([(0, 0)])
    visited = set()
    while queue:
        i, step = queue.popleft()
        step += 1
        for square in squares:
            k = i + square
            if k > n: break
            if k == n: return step
            if k not in visited:
                visited.add(k)
                queue.append((k, step))
    
    return 0

def num_squares_v2(n):
    if n < 2: return n
    squares = []
    i = 1
    while i * i < n:
        squares.append(i * i)
        i += 1
    que, level = deque([n]), 0
    while que:
        level += 1
        node_count = len(que)
        for _ in range(node_count):
            x = que.popleft()
            for y in squares:
                if x == y: return level
                if x < y: break
                que.append(x - y)

    return level 


def numSquares(n):
    choices = [x ** 2 for x in range(1, int(math.sqrt(n)) + 1)]
    memo = {}

    def dp(remain):
        if remain <= 0: return 0
        if remain in memo: return memo[remain]

        val = float('inf')
        for value in choices:
            if value <= remain:
                val = min(val, dp(remain - value))
            else:
                break

        val += 1
        memo[remain] = val 
        return memo[remain] 

    return dp(n)