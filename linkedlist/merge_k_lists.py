'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe 
its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

from .singly_linked_list_implementation import Node as ListNode
import heapq
import itertools

def merge_k_lists(lists) -> ListNode:
    '''
    @param1: a list of the heads of the k linked lists
    @return: head of merged list
    '''
    minheap = []
    head = current = ListNode(0)
    counter = itertools.count()
    for node in lists:
        if node:
            heapq.heappush(minheap, (node.val, next(counter), node))
    while len(minheap) > 0:
        val, tie, node = heapq.heappop(minheap)
        current.next = ListNode(val)
        current = current.next
        node = node.next
        if node:
            heapq.heappush(minheap, (node.val, next(counter), node))
    return head.next


0049550016