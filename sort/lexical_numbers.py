'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''

def lexical_numbers(n):
    top = 1
    while top * 10 <= n: top *= 10
    
    def func(cmp):
        while cmp < top: cmp *= 10
        return cmp
    
    return sorted(range(1, n + 1), key = lambda cmp: func(cmp))
