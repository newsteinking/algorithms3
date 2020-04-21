'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom 
represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on, return all 
possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not 
valid, it should be "10:02".
'''

def binary_watch(num):
    nums = [str(0)]*(10-num) + [str(1)]*num 
    perm = []
    times = []

    def generate_permutations(temp):
        if len(temp) == len(nums):
            perm.append(temp[:])
        else:
            for i in range(len(nums)):
                if i in used or i > 0 and nums[i] == nums[i-1] and i-1 not in used:
                    continue
                used.add(i)
                temp.append(nums[i])
                generate_permutations(temp)
                temp.pop()
                used.remove(i)

    def convert_to_time():
        for permutation in perm:
            hours, minutes = ''.join(permutation[:4]), ''.join(permutation[4:])
            hours, minutes = str(int(hours, 2)), str(int(minutes, 2))

            if int(hours) > 11 or int(minutes) > 59:
                continue
            
            time = hours + ':' + minutes
            if len(minutes) < 2:
                minutes = '0' + minutes
            times.append(time)

    used = set()
    generate_permutations([])
    convert_to_time()
    return times 

