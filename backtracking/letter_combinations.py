'''
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

def letter_combinations(digits:str) -> list:
    phone = {2:'abc', 3:'def', 4:'ghi', 5:'jkl',
              6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

    result = []
    def combine(combination, digits):
        if len(digits) == 0:
            result.append(combination)
        else:
            for letter in phone[int(digits[0])]:
                combine(combination+letter, digits[1:])
    
    if digits == None:
        return []
    combine('', digits)
    return result