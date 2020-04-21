'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should 
be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

def combinations_three(k, n):
    numbers = [x for x in range(1,10)]
    result = []

    def backtrack(temp, start, remain, count):
        if remain == 0 and count == 0:
            result.append(temp[:])
        if remain < 0 or count < 0: return
        else:
            for i in range(start, len(numbers)):
                temp.append(numbers[i])
                backtrack(temp, i+1, remain-numbers[i], count-1)
                temp.pop()

    backtrack([], 0, n, k)
    return result


