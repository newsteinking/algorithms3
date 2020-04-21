'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

from .singly_linked_list_implementation import Node as ListNode

def remove_nth_end(head: ListNode, n: int) -> ListNode:
    slow = head
    fast = head
    while n > 0:
        fast = fast.next
        n -= 1
    if not fast: return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
