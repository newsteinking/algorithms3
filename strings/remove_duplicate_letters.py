'''
Given a string which contains only lowercase letters, remove duplicate letters so that 
every letter appear once and only once. You must make sure your result is the smallest 
in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
'''

from collections import Counter

def remove_duplicate_letters(s):
    stack, seen, counter = [], set(), Counter(s)
    for char in s:
        counter[char] -= 1
        if char in seen: continue

        while stack and stack[-1] > char and counter[stack[-1]] != 0:
            seen.discard(stack[-1])
            stack.pop()

        stack.append(char)
        seen.add(char)

    return ''.join(stack)

