'''
Given a string S, return the "reversed" string where all characters 
that are not a letter stay in the same place, and all letters reverse 
their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''

def reverse_only_letters(word):
    start, end = 0, len(word)-1
    word = list(word)
    while start < end:
        while start < end and not word[start].isalpha():
            start += 1

        while end > start and not word[end].isalpha():
            end -= 1

        word[start], word[end] = word[end], word[start]
        
        start += 1
        end -= 1

    return ''.join(word)

