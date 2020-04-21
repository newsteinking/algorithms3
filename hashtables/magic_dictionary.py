'''
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character 
into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient 
algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables 
are persisted across multiple test cases. Please see here for more details.
'''

from collections import Counter
class MagicDictionary:        
    
    def neighbors(self, word):
        for index in range(len(word)):
            yield word[:index] + '*' + word[index + 1:]

    def buildDict(self, dictionary) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(dictionary)
        self.count = Counter(nei for word in dictionary for nei in self.neighbors(word))

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after 
        modifying exactly one character
        """
        for neighbor in self.neighbors(word):
            if self.count[neighbor] > 1 or self.count[neighbor] == 1 and word not in self.words:
                return True
        return False 