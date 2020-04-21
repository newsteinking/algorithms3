'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such 
that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers 
are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

def four_sum_count(A, B, C, D):
    hashmap = {}
    for a in A:
        for b in B:
            hashmap[a + b] = hashmap.get(a + b, 0) + 1

    count = 0
    for c in C: 
        for d in D:
            if -c - d in hashmap:
                count += hashmap[-c - d]

    return count

def four_sum_count(A, B, C, D):
    A_dict, B_dict, C_dict, D_dict = {}, {}, {}, {}
        
    for i in A: A_dict[i] = A_dict.get(i, 0) + 1
    for i in B: B_dict[i] = B_dict.get(i, 0) + 1
    for i in C: C_dict[i] = C_dict.get(i, 0) + 1
    for i in D: D_dict[i] = D_dict.get(i, 0) + 1
    
    AB = {}
    for i in A_dict:
        for j in B_dict:
            if i+j in AB:
                AB[i+j] += A_dict[i] * B_dict[j]
            else:
                AB[i+j] = A_dict[i] * B_dict[j]
                
    count = 0
    for i in C_dict:
        for j in D_dict:
            if -i-j in AB:
                count += C_dict[i] * D_dict[j] * AB[-i-j]
                
    return count