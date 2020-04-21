'''
Given an unsorted array of integers, find the length of longest increasing 
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to 
return the length.
Your algorithm should run in O(n2) complexity.
'''

def longest_inc(word):
    cache = [1]*len(word)

    for i in range(1, len(word)):
        for j in range(i):
            if word[i] > word[j]:
                cache[i] = max(cache[i], 1+cache[j])

    return max(cache)


def lis(A):
    memo = {}
    
    def dp(prev_index, n):
        if n == len(A):
            return 0 
        if prev_index in memo:
            return memo[prev_index] 
        
        chose, skip = 0, 0
        if prev_index < 0 or A[prev_index] < A[n]:
            chose = 1 + dp(n, n + 1)
        skip = dp(prev_index, n + 1)
        memo[prev_index] = max(chose, skip)
        return memo[prev_index] 
    
    dp(-1, 0)
    return max(memo.values())
            