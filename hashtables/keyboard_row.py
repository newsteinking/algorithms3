'''
Given a List of words, return the words that can be 
typed using letters of alphabet on only one row's of American keyboard like the image below.


Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

def find_word_rows(words):
    levels = ['qwertyuiopQWERTYUIOP',
              'asdfghjklASDFGHJKL',
              'zxcvbnmZXCVBNM']

    result = []
    for word in words:
        for level in levels:
            found = True
            for char in word:
                if char not in level:
                    found = False
                    break
            if found: 
                result.append(word)
                break
    

    return result

def find_words_v2(words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
        w = set(word.lower())
        if w <= line1 or w <= line2 or w <= line3:
            ret.append(word)
    return ret