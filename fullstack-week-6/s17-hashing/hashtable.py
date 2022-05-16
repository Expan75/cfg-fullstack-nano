# Let's try to implment one!


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
            self.buckets[index] = [(key, value)]
            return
        else:
            self.buckets[index].append((key, value))
        
    def find(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for stored_key, value in bucket:
            if key == stored_key:
                return value
        else:
            return None

hashtable = HashTable()
hashtable.insert("hello", 1)
hashtable.insert("world", 2)
value = hashtable.find("hello")
print(f"key=hello, value={value}")
