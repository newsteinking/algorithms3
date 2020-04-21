def reverse1(s):
    if len(s) == 0:
        return s
    else:
        return reverse1(s[1:]) + s[0]

def reverse2(s):
    s = list(s)
    def helper(start, end, s):
        if start >= end:
            return
        s[start], s[end] = s[end], s[start]
        return helper(start+1, end-1, s)
    helper(0, len(s)-1, s)
    return ''.join(s)

def reverse3(s):
    s = list(s)
    start = 0
    end = len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

def reverse4(s):
    return s[::-1]

def reverse5(s):
    result = ''
    for char in s[::-1]:
        result += char
    return result


