'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character 
but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

def is_isomorphic(s, t):
    letter_map = {}
    used_t = set()

    for index, char in enumerate(s):
        if char in letter_map:
            if t[index] != letter_map[char]:
                return False 
        else:
            if t[index] not in used_t:
                letter_map[char] = t[index]
                used_t.add(t[index])
            else:
                return False 
    return True 
