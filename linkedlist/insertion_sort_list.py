'''
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output 
list.
At each iteration, insertion sort removes one element from the input data, finds the location it 
belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

class ListNodeSort:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertion_sort_list(head):
    if head is None or head.next is None:
        return head 

    dummy = ListNodeSort(None)
    dummy.next, tail = head, head.next
    dummy.next.next = None

    while tail:
        prev, current, next = dummy, dummy.next, tail.next
        while current:
            if tail.val <= current.val:
                prev.next, tail.next = tail, current
                break
            prev, current =  current, current.next
        else:
            prev.next, tail.next = tail, None
        tail = next 

    return dummy.next 