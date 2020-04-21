'''
In English, we have a concept called root, which can be followed by some other words to form another longer 
word - let's call this word successor. For example, the root an, followed by other, which can form another word
 another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the
 sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the
  shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
'''

class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_word = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root 
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_word += 1

    def search(self, key):
        current = self.root
        for index, char in enumerate(key):
            if char not in current.children or current.end_word:
                break
            current = current.children[char]
        
        if index == 0: return key
        return key[:index] if current.end_word else key

def replace_words(words, sentence):
    trie = Trie()
    for word in words: trie.insert(word)

    result = []
    for word in sentence.split():
        result.append(trie.search(word))
    return ' '.join(result)


