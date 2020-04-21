#class to implement hash tables using linear probing

class HashTable:
    def __init__(self):
        self._length = 0
        self._capacity = 10
        self._load_factor = 0.5
        self._table = [None]*self._capacity

    def __len__(self):
        return self._length

    def __setitem__(self, key, value):
        self._length += 1
        hashed_key = self._hash(key)
        while self._table[hashed_key] not in (None, '$'):
            if self._table[hashed_key][0] == key:
                self._length -= 1
                break
            hashed_key = self._increment_key(hashed_key)
        pair = (key, value)
        self._table[hashed_key] = pair
        if self._length / self._capacity >= self._load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._find_item(key)
        return self._table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self._table[index] = '$'

    def __repr__(self):
        result = ''
        for x in self._table:
            if x not in (None, '$'):
                result += str(x) + ' '
        return result

    def _hash(self, key):
        return hash(key) % self._capacity
    
    def _increment_key(self, key):
        return (key+1) % self._capacity         

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self._table[hashed_key] is None:
            raise KeyError
        original_key = hashed_key
        while self._table[hashed_key][0] != key:
            hashed_key = self._increment_key(key)
            if self._table[hashed_key] == None:
                raise KeyError
            if hashed_key == original_key:
                raise KeyError
        return hashed_key

    def _resize(self):
        self._capacity *= 2
        self._length = 0
        old_table = self._table
        self._table = [None]*self._capacity
        for x in old_table:
            if x not in (None, '$'):
                self[x[0]] = x[1]


