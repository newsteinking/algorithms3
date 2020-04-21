'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

def multiply_strings(num1, num2):
    result = 0
    position_total = 1
    for i in num1[::-1]:
        sumx = 0
        carry = 0
        position = 1
        #print(num2[i])
        for j in num2[::-1]:
            #print(num1[i])
            temp = (int(i) * int(j)) + carry
            sumx += (temp % 10) * position
            carry = temp // 10
            position *= 10
        if carry:
            sumx += carry*position
        result += sumx*position_total
        position_total *= 10

    return str(result)

if __name__ == '__main__':
    print(multiply_strings('20', '3'))


