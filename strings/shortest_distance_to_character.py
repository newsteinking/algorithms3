'''
Given a string S and a character C, return an array of integers representing the shortest 
distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''

def shortest_distance_character(s, c):
    position = list()
    for index, char in enumerate(s):
        if char == c: position.append(index)

    def binary_search(x):
        left, right = 0, len(position) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if position[mid] == x:
                return mid 
            elif position[mid] < x:
                left = mid 
            else:
                right = mid 

        if abs(position[left] - index) < abs(position[right] - index):
            return left 
        else: return right

    result = []
    for index, char in enumerate(s):
        result.append(abs(position[binary_search(index)] - index))

    return result


