class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        result = ''
        if self.head == None:
            return ''
        current = self.head
        while current.next:
            result += str(current.val) + '->'
            current = current.next
        result += str(current.val)
        return result

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, key):
        if self.head == None:
            return None
        if key > len(self):
            return None
        current = self.head
        while key > 0:
            current = current.next
            key -= 1
        return current.val


    def push_front(self, x):
        newNode = Node(x)
        if self.head != None:
            newNode.next = self.head
    
        self.head = newNode

    def push_end(self, x):
        if self.head == None:
            self.head = Node(x)
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(x)

    def is_empty(self):
        return self.head == None

    def pop_front(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.val

    def pop_back(self):
        if self.head == None:
            return None
        if self.head.next == None:
            temp = self.head.val
            self.head = None
            return temp
        
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next.val
        current.next = None
        return temp

    def front_list(self):
        if self.head == None:
            return None
        return self.head.val

    def back_list(self):
        if self.head == None:
            return None
        current = self.head

        while current.next:
            current = current.next
        return current.val

    def insert_list(self, index, value):
        newNode = Node(value)
        if index > len(self):
            return
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while index > 1:
                current = current.next
            tempnode = current.next
            current.next = newNode
            newNode.next = tempnode

    def erase_list(self, index):
        if self.head == None:
            return None

        if index == 0:
            self.head = self.head.next
        current = self.head
        while index > 1:
            current = current.next
            if current is None:
                break
            index -= 1
        if current == None:
            return 
        
        current.next = None
        return self.head

    def reverse_list(self):
        prev, current, next = None, self.head, None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def remove_value(self, value):
        current, prev = self.head, self.head
        while current:
            if current.val == value:
                break
            prev = current
            current = current.next

        if current == None:
            return 
        if current == self.head:
            self.head = self.head.next
            return self.head
        prev.next = prev.next.next
        return self.head







