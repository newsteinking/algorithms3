'''
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);            // return true
circularDeque.insertLast(2);            // return true
circularDeque.insertFront(3);           // return true
circularDeque.insertFront(4);           // return false, the queue is full
circularDeque.getRear();            // return 2
circularDeque.isFull();             // return true
circularDeque.deleteLast();         // return true
circularDeque.insertFront(4);           // return true
circularDeque.getFront();           // return 4
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = self.rear = None
        self.capacity = k
        self.size = 0
                
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.rear = Node(value)
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.rear = Node(value) 
        else:
            new_rear = Node(value)
            new_rear.prev = self.rear
            self.rear.next = new_rear 
            self.rear = new_rear
        self.size += 1
        return True 

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): 
            return False
        elif self.size == 1:
            self.head = self.rear = None
        else: 
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1 
        return True 

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): 
            return False 
        elif self.size == 1:
            self.head = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None 
        self.size -= 1
        return True 
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()