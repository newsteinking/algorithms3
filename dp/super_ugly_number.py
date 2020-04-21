'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

def super_ugly_number(n, primes):
    prime_index = [0] * len(primes)
    ugly = [1]

    while n > 1:
        temp = [1] * len(primes)
        for i in range(len(temp)):
            temp[i] = primes[i] * ugly[prime_index[i]]
        umin = min(temp)
        ugly.append(umin)
        for index, val in enumerate(temp):
            if val == umin: prime_index[index] += 1
        n -= 1

    return ugly[-1]

