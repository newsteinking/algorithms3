'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by 
deleting some characters of the given string. If there are more than one possible results, return the 
longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

def longest_word_dict(s, d):

    def subsequence(word1, word2):
        first, second = 0, 0
        while first < len(word1) and second < len(word2):
            if word1[first] == word2[second]:
                second += 1
                first += 1
            else:
                first += 1

        return True if second == len(word2) else False

    max_len = float('-inf')
    max_word = ''
    for index, word in enumerate(d):
        if subsequence(s, word):
            if len(word) > max_len or len(word) == max_len and word < max_word:
                max_len = len(word)
                max_word = word

    return max_word





