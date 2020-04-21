'''
Given a string S and a string T, find the minimum window in S which will contain all the characters 
in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''
from collections import Counter
def min_window(s, t):
    pattern_count = Counter(t)
    window_count = Counter()

    unique, formed = len(pattern_count), 0

    left, right = 0, 0
    min_size = (float('inf'), 0, 0)
    while right < len(s):
        char = s[right]
        window_count[char] += 1
        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1

        while left <= right and unique == formed:
            char = s[left]
            if  right - left + 1 < min_size[0]:
                min_size = (right - left + 1, left, right)

            window_count[char] -= 1
            if char in pattern_count and window_count[char] < pattern_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1

    return '' if min_size[0] == float('inf') else s[min_size[1]:min_size[2] + 1]

