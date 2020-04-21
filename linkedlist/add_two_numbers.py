'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

from .singly_linked_list_implementation import *

def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    current = Node(0)
    newNode = current
    carry = 0
    while l1 or l2:
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0

        sumx = first + second + carry
        carry = sumx // 10
        sumx %= 10
        
        temp = Node(sumx)
        newNode.next = temp
        newNode = newNode.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    if carry:
        temp = Node(carry)
        newNode.next = temp
    
    return current.next
