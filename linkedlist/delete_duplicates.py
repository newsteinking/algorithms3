'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

def delete_duplicates(head):
    current = head    
    while current:
        prev = current
        while prev.next and prev.val == prev.next.val:
            prev = prev.next
        current.next = prev.next
        current = current.next
    return head

