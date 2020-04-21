'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent 
to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''

from collections import Counter
import heapq

def reorganize_string(S):
    heap, result = [], []
    
    for count in Counter(S).items():
        if count[1] > (len(S) + 1) // 2: return '' 
        heap.append((-count[1], count[0]))
    heapq.heapify(heap)
    
    while len(heap) >= 2:
        count1, val1 = heapq.heappop(heap)
        count2, val2 = heapq.heappop(heap)
        result.extend([val1, val2])

        if count1 + 1: heapq.heappush(heap, (count1 + 1, val1))
        if count2 + 1: heapq.heappush(heap, (count2 + 1, val2))

    if heap: result.append(heap[0][1])
    return ''.join(result)

