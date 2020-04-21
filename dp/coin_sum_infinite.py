'''
Coin Sum Infinite
You are given a set of coins S. In how many ways can you make sum N assuming
 you have infinite amount of each coin in the set. Note : Coins in set S will
  be unique. Expected space complexity of this problem is O(N). Example :
Input : 
    S = [1, 2, 3] 
    N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}    
Note that the answer can overflow. So, give us the answer % 1000007
'''

def coinchange2(coins, target):
    memo = {}
    
    def dp(remain, index):
        if remain < 0 or index == -1:
            return 0 
        if remain == 0:
            return 1
        if (remain, index) in memo:
            return memo[(remain, index)] 
        
        memo[(remain, index)] = (dp(remain - coins[index], index) + dp(remain, index - 1)) % 1000007
        return memo[(remain, index)] 
    
    return dp(target, len(coins) - 1) % 1000007