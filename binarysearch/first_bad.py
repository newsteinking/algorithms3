'''
You are a product manager and currently leading a team to develop a new 
product. Unfortunately, the latest version of your product fails the 
quality check. Since each version is developed based on the previous 
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the 
first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether 
version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

def is_bad_version(version):
    versions = [True for x in range(100)] + [False for x in range(150)]
    return versions[version]

def first_bad(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if not is_bad_version(mid):
            right = mid
        else:
            left = mid + 1

    return left