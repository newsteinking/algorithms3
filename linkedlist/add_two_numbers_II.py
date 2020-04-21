'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two 
numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

def add_two_numbers_list(l1, l2):
    stack1, stack2, new_head = list(), list(), None
    while l1: stack1.append(l1.val); l1 = l1.next 
    while l2: stack2.append(l2.val); l2 = l2.next 

    def insert_head(x):
        nonlocal new_head
        temp = ListNode(x)
        temp.next = new_head
        new_head = temp

    carry = 0
    while stack1 or stack2:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0

        sumx = val1 + val2 + carry
        carry = sumx // 10
        sumx %= 10

        insert_head(sumx)

    if carry: insert_head(carry)
    return new_head

