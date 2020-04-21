'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p 
will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

def find_anagrams(string, pattern):
    hash_pattern = hash_string = 0
    result = []

    for char in pattern: hash_pattern += hash(char)
    for i in range(len(pattern)): hash_string += hash(string[i])

    if hash_pattern == hash_string: result.append(0)

    for i in range(len(pattern), len(string)):
        hash_string -= hash(string[i-len(pattern)])
        hash_string += hash(string[i])
        if hash_string == hash_pattern:
            result.append(i-len(pattern)+1)

    return result

