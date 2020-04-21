'''
As it is Tushar's Birthday on March 1st, he decided to throw a party to 
all his friends at TGI Fridays in Pune. Given are the eating capacity of 
each friend, filling capacity of each dish and cost of each dish. 
A friend is satisfied if the sum of the filling capacity of dishes he 
ate is equal to his capacity. Find the minimum cost such that all of 
Tushar's friends are satisfied (reached their eating capacity). NOTE:
Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution 
always exists.
Input Format
Friends : List of integers denoting eating capacity of friends separated by space.
Capacity: List of integers denoting filling capacity of each type of dish.
Cost :    List of integers denoting cost of each type of dish.
'''

def birthday(A, B, C):
    n, m = len(B) + 1, max(A) + 1
    dp = [[i and float('inf') or 0] * (n) for i in range(m)]

    for i in range(m):
        for j in range(1, n):
            if i - B[j - 1] >= 0:
                dp[i][j] = min(dp[i][j - 1], dp[i - B[j - 1]][j] + C[j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
    ans = 0
    for a in A:
        ans += dp[a][-1]
    return ans