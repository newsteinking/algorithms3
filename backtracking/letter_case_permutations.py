'''Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''

def letter_case_permutations(S):
    res = ['']

    for ch in S:
        if ch.isalpha():
            res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i + ch for i in res]

    return res

def letter_case_permutations_v2(S):
    if not S: return ['']
    S = [x for x in S]
    que = deque([S])
    for i in range(len(S)):
        if S[i].isdigit(): continue
        node_count = len(que)
        for j in range(node_count):
            current = que.popleft()
            current[i] = current[i].upper()
            que.append(current.copy())
            current[i] = current[i].lower()
            que.append(current.copy())
    
    return [''.join(x) for x in que]