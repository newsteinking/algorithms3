class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def enque(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def deque(self):
        temp = self.front
        if self.front == None:
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return temp.data

    def front_que(self):
        if self.front == None:
            return None
        else: return self.front.data


