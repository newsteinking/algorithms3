'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number 
that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 
and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to 
ny other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
'''

def rotated_digits(N: int) -> int:
    count = 0
    for n in range(1,N+1):
        ok = False
        for c in str(n):
            if c in "2569":
                ok = True
            elif c in "347":
                ok = False
                break
        if ok:
            count += 1
    return count

def rotated_digits_v2(N):
    rotated_map = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6}
    result = 0

    for number in range(1, N+1):
        number = str(number)
        rotated_number, valid = 0, True
        for digit in number:
            if int(digit) not in rotated_map:
                valid = False
                break
            rotated_number *= 10
            rotated_number += rotated_map[int(digit)]

        if valid and rotated_number != int(number):
            result += 1

    return result