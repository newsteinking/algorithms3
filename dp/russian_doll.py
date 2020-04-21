'''
Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope. Find the maximum number of envelopes you can put one inside other. 
Input Format
The only argument given is the integer matrix A.
Output Format
Return the maximum number of envelopes you can put one inside other.
Constraints
1 <= N <= 1000
1 <= A[i][0], A[i][1] <= 10^9
For Example
Input 1:
    A = [   [5, 4]
            [6, 4]
            [6, 7]
            [2, 3]   ]
Output 1:
    3
    Explanation 1:
        Step 1: put [2, 3] inside [5, 4]
        Step 2: put [5, 4] inside [6, 7]

Input 2:
    A = A : [   [8, 9]
                [8, 18] ]
Output 2:
    1
    Explanation 2:
        No envelopes can be put inside any other so answer is 1.
'''


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key = lambda x: (x[0], -x[1]))
 
        def CeilIndex(A, l, r, key): 
  
            while (r - l > 1): 
              
                m = l + (r - l)//2
                if (A[m] >= key): 
                    r = m 
                else: 
                    l = m 
            return r 
           
        def LongestIncreasingSubsequenceLength(A, size): 
          
            # Add boundary case, 
            # when array size is one 
           
            tailTable = [0 for i in range(size + 1)] 
            len = 0 # always points empty slot 
           
            tailTable[0] = A[0] 
            len = 1
            for i in range(1, size): 
              
                if (A[i] < tailTable[0]): 
          
                    # new smallest value 
                    tailTable[0] = A[i] 
           
                elif (A[i] > tailTable[len-1]): 
          
                    # A[i] wants to extend 
                    # largest subsequence 
                    tailTable[len] = A[i] 
                    len+= 1
           
                else: 
                    # A[i] wants to be current 
                    # end candidate of an existing 
                    # subsequence. It will replace 
                    # ceil value in tailTable 
                    tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i] 
                  
           
            return len
        
        return LongestIncreasingSubsequenceLength([x for y, x in A], len(A))
                