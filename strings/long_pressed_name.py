'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long 
pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, 
with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''

def long_pressed_name(name, typed):
    if len(name) > len(typed): return False 
    
    i, j = 0, 0
    while i < len(typed) and j < len(name):
        if typed[i] != name[j]: return False
        if j + 1 < len(name) and name[j] != name[j + 1]:
            while i < len(typed) - 1 and typed[i] == typed[i + 1]:
                i += 1
        i += 1
        j += 1
    
    while i < len(typed) - 1 and typed[i] == typed[i + 1]:
        i += 1
    if i < len(typed) and typed[i] == typed[i - 1]: i += 1

    return i == len(typed) and j == len(name)
