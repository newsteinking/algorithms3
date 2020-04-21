'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending 
positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
'''

def position_large_groups(S):
    result, i, j = [], 0, 0

    for j in range(len(S) - 1):
        if j == len(S) - 1 or S[j] != S[j + 1]:
            if j - i + 1 >= 3:
                result.append([i, j])
            i = j + 1
    
    return result 



def position_large_groups_v2(S):
    left, right = 0, 0 

    result = []
    while right + 1 < len(S):
        while right + 1 < len(S) and S[right] == S[right + 1]:
            right += 1

        if right - left + 1 >= 3:
            result.append([left, right])

        left = right + 1
        right += 1 

    return result 