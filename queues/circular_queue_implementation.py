class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.que = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        position = (self.rear + 1) % self.capacity
        self.que[position] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.que[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True 

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.que[self.front] if self.que[self.front] is not None else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.que[self.rear] if self.que[self.rear] is not None else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.que[self.rear] is None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()