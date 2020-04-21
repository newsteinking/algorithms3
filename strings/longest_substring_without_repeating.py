'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence 
             and not a substring.
'''

def longest_unique_substring(s:str) -> int:
    max_total = 1
    max_current = 1
    if len(s) == 0: return 0
    visited = {s[0]:0}

    for i in range(1, len(s)):
        if s[i] not in visited or i - max_current > visited.get(s[i], -1):
            max_current += 1
        else:
            if max_current > max_total:
                max_total = max_current
            max_current = i - visited.get(s[i], -1)
        visited[s[i]] = i
    
    if max_current > max_total:
        max_total = max_current
    
    return max_total
