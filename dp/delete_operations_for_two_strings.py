'''Given two words word1 and word2, find the minimum number of steps 
required to make word1 and word2 the same, where in each step you can 
delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to 
make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

def min_distance_strings(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[None for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return m+n - 2*dp[m][n]