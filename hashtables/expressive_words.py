'''
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", 
"ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications 
of the following extension operation: choose a group consisting of characters c, and add some number of characters 
c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get 
"helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" 
to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two 
extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
''' 
def expressive_words(S, words):
        
    def compress(word):
        compressed, i = [], 0
        while i < len(word):
            j = i + 1
            while j < len(word) and word[j] == word[i]: j += 1
            compressed.append((j - i, word[i]))
            i = j
        return compressed

    def check(word):
        word = compress(word)
        if len(word) != len(S): return False 
        for a, b in zip(S, word):
            i, j = a
            x, y = b
            if j != y: return False 
            if i < x: return False 
            if i < 3 and i != x: return False 
        return True 

    count, S = 0, compress(S)
    for word in words:
        if check(word): count += 1
    return count   

def expressive_words_v2(S, words):

    def check(W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]: return False
            while i2 < n and S[i2] == S[i]: i2 += 1
            while j2 < m and W[j2] == W[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
    
        return i == n and j == m
    
    res, count = [], 0
    for word in W:
        if check(word): count += 1
    return count 


