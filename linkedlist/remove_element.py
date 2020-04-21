'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

def remove_elements(head, val):
    while head and head.val == val:
        head = head.next

    if not head: return
    prev, current = head, head.next
        

    while current:
        if current.val == val:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next

    return head
