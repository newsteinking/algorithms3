'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such 
that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
'''

from collections import deque
from functools import lru_cache

@lru_cache()
def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def fibonacci_dynamic(n):
    if n == 0: return 0
    cache = deque([0, 1, 1])
    for i in range(2, n):
        cache.append(cache[1] + cache[2])
        cache.popleft()
    return cache[-1]

def fibonacci_dynamic_v2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1, f2 = 0, 1
    i = 1
    while i < n:
        result = f1 + f2
        f1 = f2
        f2 = result
        i += 1
    return result

def fibonacci_formula(n):
    root5 = 5**0.5
    fib = (((1+root5)/2)**(n+1)) - (((1-root5)/2)**(n+1))
    result = fib/root5
    return int(result)

