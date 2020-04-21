'''
Given two words (beginWord and endWord), and a dictionary's word list, find all 
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a 
transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible 
transformation.
'''

from collections import defaultdict, deque
import string
def generateNeighbors(word, wordList):
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in wordList:
                yield candidate

def createAllPaths(parentDict, word, beginWord):
    if word == beginWord:
        return [[beginWord]]
    output = []
    for w in parentDict[word]:
       x = createAllPaths(parentDict, w, beginWord)
       for l in x:
           l.append(word)
           output.append(l)
    return output

def word_ladder_two(beginWord, endWord, wordList):
    q = deque([beginWord ])
    seen = set([beginWord])
    wordList = set(wordList)
    parents = defaultdict(set)
    while q:
        num_in_level = len(q)
        finished = False
        seen_this_level = set()
        for i in range(num_in_level):
            q_item = q.popleft()
            for i in range(len(beginWord)):
                for letter in string.ascii_lowercase:
                    candidate = q_item[:i] + letter + q_item[i+1:]
                    if candidate in wordList:
                        if candidate == endWord:
                            finished = True
                        elif candidate in seen:
                            continue
                        if candidate not in seen_this_level:
                            q.append(candidate)
                        seen_this_level.add(candidate)
                        parents[candidate].add(q_item)
        if finished:
            break
        seen |= seen_this_level
    return createAllPaths(parents, endWord, beginWord)
