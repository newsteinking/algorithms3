'''
A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it 
equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and 
only if queries[i] matches the pattern.

 

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
'''

def camel_match(queries, pattern):
    
    def match(query, pattern):
        i, j = 0, 0
        while i < len(query) and j < len(pattern):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if query[i].isupper():
                    return False
                i += 1
        if j == len(pattern):
            return query[i:].lower() == query[i:]
        return False
    
    res = []
    for query in queries:
        res.append(match(query, pattern))
    return res


def camel_match_v2(queries, pattern):

    def helper(query):
        q = [val for val in query if val.isupper()]
        p = [val for val in pattern if val.isupper()]
        if q != p: return False
        q = [x for x, val in enumerate(query) if val.isupper()]
        p = [x for x, val in enumerate(pattern) if val.isupper()]
        
        p_start, q_start = 0, 0
        for index, end in enumerate(p):
            for char in pattern[p_start:end]:
                if char not in query[q_start:q[index]]:
                    return False
                p_start += 1
                q_start += 1
            p_start = end
            q_start = q[index]
        
        return True 

    return [helper(query) for query in queries]






