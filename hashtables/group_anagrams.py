'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from collections import defaultdict
def group_anagrams(words:list) -> list:
    word_map = defaultdict(list)
    for word in words:
        hash_word = 0
        for char in word:
            hash_word += hash(char)
        word_map[hash_word].append(word)
    return [x for x in word_map.values()]

