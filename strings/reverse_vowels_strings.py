'''
Write a function that takes a string as input and reverse only the vowels 
of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

def reverse_vowels(word):
    word = list(word)
    left, right = 0, len(word)-1
    vowels = ('a', 'e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    while left < right:
        while left < right and word[left] not in vowels:
            left += 1
        while right > left and word[right] not in vowels:
            right -= 1

        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return ''.join(word)

def reverse_vowels_v2(word: str) -> str:
    vowels = []
    for char in word:
        if char in ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U'):
            vowels.append(char)
    vowels.reverse()
    result = ''
    vowel_count = 0
    for i in range(len(word)):
        if word[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            result += vowels[vowel_count]
            vowel_count += 1
        else:
            result += word[i]
    return result
