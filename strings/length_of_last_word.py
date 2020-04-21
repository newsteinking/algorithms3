'''
Given a string s consists of upper/lower-case alphabets and empty space 
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

def length_of_last_word(s:str) -> int:
    s = s.lstrip()
    s = s.rstrip()
    i = len(s) - 1
    count = 0
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1

    return count
