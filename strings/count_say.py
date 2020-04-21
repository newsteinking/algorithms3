'''
The count-and-say sequence is the sequence of integers with the first five terms as 
following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

def count_say(n):
    n = str(n)
    result = ['1', '11']
    for i in range(2, int(n)):
        temp = result[-1] + '$'
        ans = ''
        count = 1
        for i in range(1, len(temp)):
            if temp[i] != temp[i-1]:
                ans += str(count) + temp[i-1]
                count = 1
            else:
                count += 1
        result.append(ans)
    return int(result[-1])




