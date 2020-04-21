'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

def pow_v1(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_v1(x, n//2) * pow_v1(x, int(n//2))
    else:
        return x * pow_v1(x, n//2) * pow_v1(x, int(n//2))


def pow_v2(x, n):
    if n == 0:
        return 1
    temp = pow_v2(x, n//2)
    if n%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

def pow_v3(x, n):
    if n == 0:
        return 1
    temp = pow_v3(x, int(n/2))
    if n%2 == 0:
        return temp*temp
    else:
        if n > 0: return x*temp*temp
        else: return (temp*temp) / x

def pow_v4(x, n):
    result = 1
    while n > 0:
        if n % 2 is not 0:
            result *= x
            if n == 1:
                break
         
        n //= 2
        x *= x    
    return result

def pow_v5(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res

