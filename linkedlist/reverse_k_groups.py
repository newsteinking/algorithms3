'''
Given a linked list, reverse the nodes of a linked list k at a time and return its
 modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain 
as it is.

Example:

Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
'''

from .singly_linked_list_implementation import Node as ListNode

def reverse_k_group(head, k):
    jump = dummy = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:
            r = r.next
            count += 1

        if count == k:
            prev, current = r, l
            for _ in range(k):
                current.next, current, prev = prev, current.next, current
            jump.next, jump, l = prev, l, r
        else:
            return dummy.next



