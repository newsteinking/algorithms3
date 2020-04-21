import pprint
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_word = 0

    def __repr__(self):
        return str(self.children)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return str(self.root.children)

    def insert(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_word += 1

    def search(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        
        if current.end_word: return True
        else: return False
