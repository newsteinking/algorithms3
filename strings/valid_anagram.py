'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

def valid_anagram(s, t):
    s_hash, t_hash = 0, 0
    i, j = 0, 0

    while i < len(s) or j < len(t):
        if i < len(s):
            s_hash += hash(s[i])
            i += 1
        if j < len(t):
            t_hash += hash(t[j])
            j += 1

    return s_hash == t_hash