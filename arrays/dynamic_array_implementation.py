import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0                               #Count of elements
        self.capacity = 1                        #Default capacity
        self.A = self.make_array(self.capacity)  #Make low level array
    
    def __len__(self):
        return self.n

    def __repr__(self):
        result = []
        for i in range(self.n):
            result.append(str(self.A[i]))
        return str(' '.join(result))

    def __getitem__(self, key):
        if not 0 <= key < self.n:
            raise IndexError('invalid index')
        return self.A[key]

    def make_array(self, c):
        return (c * ctypes.py_object)()

    def append(self, x):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        self.A[self.n] = x
        self.n += 1

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for j in range(self.n):
            new_array[j] = self.A[j]
        self.A = new_array
        self.capacity = new_capacity

    def pop(self):
        self.A[self.n-1] = None
        self.n -= 1

    def push_left(self, x):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        for i in range(self.n-1, -1, -1):
            self.A[i+1] = self.A[i]
        self.A[0] = x
        self.n += 1

    def insert_index(self, index, x):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        if not 0 <= index < self.n:
            raise IndexError
        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i]
        self.A[index] = x
        self.n += 1

    def find_key(self, x):
        '''
        Find x in array and return index. If not 
        found return -1 
        '''
        for i in range(self.n):
            if self.A[i] == x:
                return i
        return -1

    def remove_key(self, x):
        '''
        Remove all instances of x in Array
        '''
        while True:
            i = self.find_key(x)
            if i == -1:
                break
            for j in range(i+1, self.n):
                self.A[j-1] = self.A[j]
            self.A[self.n-1] = None
            self.n -= 1

    def delete_index(self, index):
        if not 0 <= index < self.n:
            raise IndexError
        for i in range(index, self.n):
            self.A[i] = self.A[i+1]
        self.A[self.n-1] = None
        self.n -= 1



