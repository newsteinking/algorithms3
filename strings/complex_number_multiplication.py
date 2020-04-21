'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of 
[-100, 100]. And the output should be also in this form.
'''

def complex_numbers_multiply(a, b):
    a_number, a_complex = a.split('+')
    b_number, b_complex = b.split('+')

    a_complex = int(a_complex[:-1])
    b_complex = int(b_complex[:-1])
    a_number = int(a_number)
    b_number = int(b_number)

    return (str(a_number * b_number - (a_complex * b_complex)) + '+' + 
            str(a_complex * b_number + b_complex * a_number) + 'i')

