#Python3
#Hash Table
class HashTable(object):
    """
    Implementing a hash table with list chaining
    """
    def __init__(self, m, p = 1000000007, x = 263):
        """
        m is the size of the hash table
        p is a large prime number for modulo division
        x is the smallest prime number greater than 256
        """
        self.m = m
        self.p = p
        self.x = x
        self.buckets = [[] for _ in range(m)]
   
    def _hash(self, string):
        """
        Polynomial hash function
        Used to generate more "random" hash values to preserve low collision probability
        Calculated as the sum of the ASCII values of the characters times some prime number
        exponentiated to the position of the character
        """
        return sum([(ord(char) * self.x ** i) for i, char in enumerate(string)])  % self.p % self.m
        
    def add(self, string):
        bucket = self._hash(string)
        if string not in self.buckets[bucket]:
            self.buckets[bucket].insert(0, string)
    
    def remove(self, string):
        bucket = self._hash(string)
        if string in self.buckets[bucket]:
            self.buckets[bucket].remove(string)
        
    def find(self, string):
        bucket = self._hash(string)
        if string in self.buckets[bucket]:
            return "yes"
        else:
            return "no"
    
    def check(self, bucket):
        return " ".join(self.buckets[bucket])


#%%
m = int(input())
lines = int(input())

ht = HashTable(m)

for _ in range(lines):
    command, value = input().split()
    if command == "add":
        ht.add(value)
    elif command == "del":
        ht.remove(value)
    elif command == "find":
        print(ht.find(value))
    elif command == "check":
        print(ht.check(int(value)))
    else:
        raise ValueError("SOMETHING HAS GONE HORRIBLY WRONG!")