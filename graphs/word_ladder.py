'''
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a 
transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is 
"hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict, deque
import string

def word_ladder(begin_word, end_word, word_list):
    transformations = defaultdict(list)
    for word in word_list:
        for i in range(len(begin_word)):
            transformations[word[:i] + '*' + word[i+1:]].append(word)

    que = deque([(begin_word, 1)])
    visited = set()
    visited.add(begin_word)

    while que:
        current_word, level = que.popleft()
        for i in range(len(begin_word)):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            for word in transformations[intermediate_word]:
                if word == end_word:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    que.append((word, level+1))
            transformations[intermediate_word] = []
    return 0

def word_ladder_v2(start, end, words):
    que = deque([(start, 1)])
    words = set(words)

    while que:
        current, level = que.popleft()

        if current == end:
            return level

        for i in range(len(start)):
            for letter in string.ascii_lowercase:
                candidate = current[:i] + letter + current[i+1:]
                if candidate in words:
                    que.append((candidate, level+1))
                    words.remove(candidate)
    return 0

