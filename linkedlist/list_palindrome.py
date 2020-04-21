'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
'''

def list_palindrome(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    while prev:
        if prev.val != head.val:
            return False 
        prev = prev.next
        head = head.next

    return True 


def list_palindrome_v2(head):
    temp = []
    while head:
        temp.append(head.val)
        head = head.next

    l,r = 0, len(temp)-1
    while l < r:
        if temp[l] != temp[r]:
            return False 
        l += 1
        r -= 1
    return True
    