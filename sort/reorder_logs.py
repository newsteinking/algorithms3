'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''

def reorder_logs(logs):
    letter_logs, digit_logs = [], []
    for index, log in enumerate(logs):
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            log = log.split()
            letter_logs.append((log[1:], log[0], index))

    letter_logs.sort()
    result = []
    for i in range(len(letter_logs)):
        result.append(logs[letter_logs[i][2]])

    result += digit_logs
    return result 

def reorder(logs):

    def f(log):
        id_, rest = log.split(' ', 1)
        return (0, rest, id_) if rest[0].isalpha() else (1, )

    return sorted(logs, key = f)