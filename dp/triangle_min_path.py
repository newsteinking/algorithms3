'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to 
adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

def triangle_min_path(triangle):
    dp = [x for x in triangle[-1]]
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(i+1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

    return dp[0]
