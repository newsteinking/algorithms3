'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

def count_primes(n):
    primes = [True for i in range(n+1)]
    p = 2

    while p*p <= n:
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    count = 0
    for i in range(2,len(primes)):
        if primes[i] == True:
            count += 1

    return count
    
