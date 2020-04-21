'''
Given two strings s1 and s2, write a function to return true if s2 contains 
the permutation of s1. In other words, one of the first string's permutations 
is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

def permutations_string(small, big):
    if len(small) > len(big): return False
    small_hash = 0
    for char in small:
        small_hash += hash(char)

    big_hash = 0
    for i in range(len(small)):
        big_hash += hash(big[i])

    if small_hash == big_hash:
        return True

    start = 0
    for i in range(len(small), len(big)):
        big_hash -= hash(big[start])
        big_hash += hash(big[i])
        
        if small_hash == big_hash:
            return True
        i += 1
        start += 1
    return False

