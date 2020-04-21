'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to 
be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight
 Hundred Ninety One"
'''

def number_to_words(num):
    if num == 0: return 'Zero'
    ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', 
        ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', 
        ' Seventeen', ' Eighteen', ' Nineteen'] 
    threes = ['', '', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
    fours = ['', ' Thousand', ' Million', ' Billion']

    num = list(str(num))
    front = len(num) % 3
    position = []
    if front: position.append(str(int(''.join(num[:front]))))
    
    for i in range(front, len(num), 3):
        position.append(str(int(''.join(num[i: i + 3]))))

    position = position[::-1]
    temp = position[:]
    for i, x in enumerate(position):
        number = int(x)
        if number < 20:
            position[i] = ones[number]
        elif 20 <= number < 100: 
            string = threes[int(x[0])]
            string += ones[int(x[1])]
            position[i] = string
        elif number >= 100:
            string = ones[int(x[0])] + ' ' + 'Hundred'
            if int(x[1]) == 1: 
                string += ones[int(''.join(x[1:]))]
                position[i] = string
                continue 
            string += threes[int(x[1])] 
            string += ones[int(x[2])]
            position[i] = string

    for i in range(1, len(position)):
        if int(temp[i]): position[i] += fours[i]

    return ''.join(position[::-1]).rstrip().lstrip()