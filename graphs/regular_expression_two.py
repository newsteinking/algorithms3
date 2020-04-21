'''
Implement regular expression matching with support for '.' and '*'. '.' 
Matches any single character. '*' Matches zero or more of the preceding element. 
The matching should cover the entire input string (not partial). 
The function prototype should be:
int isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

def isMatch(self, text, pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == -1:
                ans = i == -1
            else:
                first_match = i > -1 and pattern[j] in {text[i], '.'}
                if j > 0 and pattern[j - 1] == '*':
                    ans = dp(i, j - 2) or first_match and dp(i - 1, j)
                else:
                    ans = first_match and dp(i - 1, j - 1)

            memo[i, j] = ans
        return memo[i, j]

    return int(dp(len(text) - 1, len(pattern) - 1))

