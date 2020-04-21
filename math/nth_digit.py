'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of 
the number 10.
'''

def nth_digit(n):
    start, size, step = 1, 1, 9

    while n > size * step:
        n, start, size, step = n - size * step, start * 10, size + 1, step * 10

    return int(str(start + (n - 1) // size)[(n - 1) % size])

def nth_digit_v2(n):
    start, size = 1, 1

    while n > size:
        n, start = n - size, start + 1
        size = len(str(start))

    return int(str(start)[n-1])

