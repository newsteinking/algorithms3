def lcs(word1, word2):
    '''
    Using recursion without memo
    '''
    def helper(i, j):
        if i == len(word1) or j == len(word2):
            return 0
        elif word1[i] == word2[j]:
            return 1 + helper(i+1, j+1)
        else:
            return max(helper(i+1, j), helper(i, j+1))

    return helper(0, 0)

def lcs_dp(word1, word2):
    '''
    Using dynamic programming
    '''
    m, n = len(word1), len(word2)
    cache = [[None for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    return cache[m][n]
