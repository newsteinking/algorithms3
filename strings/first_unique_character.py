'''
Given a string, find the first non-repeating character in it and
 return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

from collections import Counter
def first_unique(word):
    count = Counter(word)
    for i in range(len(word)):
        if count[word[i]] == 1:
            return i 
    return -1


