'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
from .singly_linked_list_implementation import Node as ListNode

def swap_pairs(head):
    def helper(head, k):
        count = 0
        prev, current, next = None, head, None
        
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        if next is not None:
            head.next = helper(next, k)
        
        return prev
    
    head = helper(head, 2)
    return head

def swap_pairs_v2(head):
    if head == None or head.next == None:
        return

    prev = head
    current = head.next
    head = current
    
    while True:
        next = current.next
        current.next = prev

        if next == None or next.next == None:
            prev.next = next
            break
        
        prev.next = next.next
        prev = next
        current = prev.next


    return head
