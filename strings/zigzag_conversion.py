'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

def zigzag_conversion(S:str, rows:int) -> str:
    # direction 1 means down and 0 means up
    direction = True
    count = 0
    result = [[] for i in range(rows)]
    for i in range(len(S)):
        if direction:
            if count < rows:
                result[count].append(S[i])
                count += 1
            else:
                direction = 0
                count -= 2
                result[count].append(S[i])
                count -= 1
        else:
            if count >= 0:
                result[count].append(S[i])
                count -= 1
            else:
                direction = 1
                count += 2
                result[count].append(S[i])
                count += 1
    return ''.join(sum(result, []))

def zigzag_v2(S, rows):
    down = True
    count = 0
    result = [[] for x in range(rows)]

    for char in S:
        result[count].append(char)
        if down: count += 1
        else: count -= 1
        if count == 0 or count == rows-1:
            down = not down
    return ''.join(sum(result, []))
