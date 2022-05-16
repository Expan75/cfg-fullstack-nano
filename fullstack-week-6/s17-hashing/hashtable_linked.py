# Let's try to implment one using a linked list!


class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __repr__(self):
        return f"node(key={self.key},value={self.value})"

    def append(self, key, value):
        current_node = self

        while current_node.next is not None:
            current_node = current_node.next

        # we now have reached the tail and insert our new value
        self.next = Node(key, value)

    def search(self, key=None, value=None):
        if (self.value == value) or (self.key == key):
            return self
        # if we haven't found anything, we proceed to the next node
        # this is done via recursion (more on this maybe later)
        if self.next == None:
            return None
        else:
            return self.search(self.next)

class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        hashsum = 0

        for index, character in enumerate(key):
            # we define our custom hash value as (index + length of key) ^ (character code)
            hashsum += (index + len(key)) ** ord(character)
            
            # ensure we stay within range(0, self.capacity - 1)
            hashsum = hashsum % self.capacity

        return hashsum

    def insert(self, key, value):
        
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        
        # insert using append in bucket if not first value (linear probing-ish)
        if node is None:
            self.buckets[index] = Node(key,value)
            return
        else:
            self.buckets[index].append(key,value)
        
    def find(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        return bucket.search(key)

hashtable = HashTable()
hashtable.insert("hello", 1)
hashtable.insert("world", 2)
value = hashtable.find("hello")
print(f"key=hello, value={value}")
