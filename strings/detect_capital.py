'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
'''

def detect_capital(word):
    count_title = 0
    for char in word: 
        if char.istitle(): count_title += 1

    if count_title == len(word): return True
    if count_title == 0: return True 
    if count_title == 1 and word[0].istitle(): return True

    return False 
