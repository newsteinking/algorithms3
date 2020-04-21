'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, 
including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''

def self_dividing_numbers(left, right):
    result = []

    for num in range(left, right + 1):
        self_dividing = True 
        num_str = str(num)
        for digit in num_str:
            if digit == '0' or num % int(digit) != 0:
                self_dividing = False
                break

        if self_dividing: result.append(num)

    return result  
