'''
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
'''

def shifting_letters(S, shifts):
    ans = []
    X = sum(shifts) % 26
    for i, c in enumerate(S):
        index = ord(c) - ord('a')
        ans.append(chr(ord('a') + (index + X) % 26))
        X = (X - shifts[i]) % 26

    return "".join(ans)

def shifting_letters_v2(S, shifts):
    shifts[-1] %= 26
    for i in range(len(shifts) - 2, -1, -1):
        shifts[i] += shifts[i + 1]
        shifts[i] %= 26

    S = [x for x in S]
    for i in range(len(S)):
        if ord(S[i]) + shifts[i] <= ord('z'):
            S[i] = chr(ord(S[i]) + shifts[i])
        else:
            S[i] = chr(ord(S[i]) + shifts[i] - ord('z') + ord('a') - 1)

    return ''.join(S)

