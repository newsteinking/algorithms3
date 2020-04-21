'''
Given two integers representing the numerator and denominator of a fraction, return 
the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

def fraction_to_decimal(numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''
    numerator, denominator = abs(numerator), abs(denominator)
    
    integer_part, decimal = divmod(numerator, denominator)
    if decimal == 0: return sign + str(integer_part)
    
    seen, index, fraction_part = dict(), 0, list()
    while decimal:
        if decimal in seen: break
        seen[decimal] = index
        quotient, decimal = divmod(decimal * 10, denominator)
        fraction_part.append(str(quotient))
        index += 1
    else:
        return sign + str(integer_part) + '.' + ''.join(fraction_part)
    
    index = seen[decimal]
    return sign + str(integer_part) + '.' + ''.join(fraction_part[:index]) + '(' + ''.join(fraction_part[index:]) + ')'
