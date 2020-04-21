'''
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, 
and it is guaranteed an answer exists. 

Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''

from collections import Counter
def rearrange_barcodes(barcodes):
    i, n = 0, len(barcodes)
    result = [0] * len(barcodes)

    for val, count in Counter(barcodes).most_common():
        for _ in range(count):
            result[i] = val 
            i += 2
            if i >= n: i = 1

    return result 
