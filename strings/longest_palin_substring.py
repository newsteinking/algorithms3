'''
Given a string s, find the longest palindromic substring in s. You may assume that the 
maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

def longest_palin_substring(s:str) -> str:
    if s == None or len(s) == 0: return ''
    start, end = 0, 0
    
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        length = max(len1, len2)

        if length > end - start:
            start = i - (length-1)//2
            end = i + length//2

    return s[start:end+1]


