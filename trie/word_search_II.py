'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
 horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
'''

class TrieNode:

    def __init__(self):
        self.children = dict()
        self.end_word = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_word = True 

    def search(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        
        if current.end_word: return True
        else: return False

def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    def dfs(i, j, path, current):
        if current.is_end_word:
            result.append(path)
            current.end_word = False  

        temp = board[i][j]
        current = current.children.get(temp)
        if not current: return 

        board[i][j] = '#'
        directions = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
        for x, y in directions:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                dfs(x, y, path + temp, current)
        board[i][j] = temp 


    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, '', trie.root)

    return result 

