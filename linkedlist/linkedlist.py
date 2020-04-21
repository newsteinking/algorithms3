class Node:
    def __init__(self, x):
        self.val = x
        self.next = None 

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size: return -1

        current = self.head 
        for _ in range(index):
            current = current.next 

        return current.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, 
        the new node will be the first node of the linked list.
        """
        temp = self.head 
        self.head = Node(val)
        self.head.next = temp 
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None: 
            self.addAtHead(val)
            return
        current = self.head 
        while current.next:
            current = current.next 
        current.next = Node(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the 
        length of linked list, the node will be appended to the end of linked list. If index is 
        greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size: return
        
        if index == self.size:
            self.addAtTail(val)
        else:
            current = self.head 
            for _ in range(index - 1):
                current = current.next

            temp = current.next 
            current.next = Node(val)
            current.next.next = temp
            self.size += 1



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size: return 
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head 
            for _ in range(index - 1):
                current = current.next

            current.next = current.next.next 

        self.size -= 1 



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)