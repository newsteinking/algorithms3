'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words 
do not share common letters. You may assume that each word will contain only lower case letters. If no such two 
words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
'''

def max_product_length(words):
    mask_map = {}
    for word in words:
        mask = 0
        for char in set(word):
            mask |= (1 << (ord(char) - ord('a')))
        mask_map[mask] = max(mask_map.get(mask, 0), len(word))

    max_len = 0
    for x in mask_map:
        for y in mask_map:
            if not x & y:
                max_len = max(max_len, mask_map[x] * mask_map[y])

    return max_len


def max_product_length_v2(words):
    max_len = 0
    words_set = [set(words[i]) for i in range(len(words))]
    
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if not (words_set[i] & words_set[j]):
                max_len = max(max_len, len(words[i] * len(words[j])))
    
    return max_len

def max_product_length_v3(words):
    mask = [0] * len(words)
    result = 0

    for i in range(len(words)):
        for char in words[i]:
            mask[i] |= 1 << (ord(char) - ord('a'))
        for j in range(i):
            if not (mask[i] & mask[j]):
                result = max(result, len(words[i]) * len(words[j]))

    return result 