'''
Given a string containing only digits, restore it by returning all possible valid IP 
address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

def restore_ip_addresses(s):
    result = []

    def backtrack(s, index, path):
        if index == 4:
            if not s: result.append(path[:-1])
            return 
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    backtrack(s[i:], index + 1, path + s[:i] + '.')
                elif i == 2 and s[0] != '0':
                    backtrack(s[i:], index + 1, path + s[:i] + '.')
                elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                    backtrack(s[i:], index + 1, path + s[:i] + '.')

    backtrack(s, 0, '')
    return result