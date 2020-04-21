'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear 
in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''
from collections import Counter
def uncommon_words(A, B):
    A = Counter(A.split())
    B = Counter(B.split())

    result = []

    for word, count in A.items():
        if word not in B and count == 1:
            result.append(word)

    for word, count in B.items():
        if word not in A and count == 1:
            result.append(word)

    return sorted(result) 

