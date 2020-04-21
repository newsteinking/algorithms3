'''On the first row, we write a 0. Now in every subsequent row, we look at the previous 
row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. 
(The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
'''

def kth_grammar(n, k):
    row = [0]
    for _ in range(n):
        temp = []
        for number in row:
            if number == 0:
                temp.append(0)
                temp.append(1)
            else:
                temp.append(1)
                temp.append(0)
        row = temp
    return row[k-1]
