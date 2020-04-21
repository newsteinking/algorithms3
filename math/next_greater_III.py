'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same 
digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, 
you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1'''

def next_greater_three(n):
    n = [int(x) for x in str(n)]
    i = len(n) - 2
    while i > -1:
        if n[i] < n[i + 1]: break
        i -= 1

    if i < 0: return -1
    minx = n[i]
    smallest = i + 1
    for j in range(i + 1, len(n)):
        if n[j] > minx and n[j] < n[smallest]:
            smallest = j
    n[smallest], n[i] = n[i], n[smallest]
    n = n[:i + 1] + sorted(n[i + 1:])
    result = int(''.join(str(x) for x in n)) 
    return result if result < 2 ** 31 - 1 else -1