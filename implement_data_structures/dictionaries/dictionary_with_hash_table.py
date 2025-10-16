# TODO: Implementation of dictionary with hash table.
from enum import Enum

class CollisionTypes(Enum):
    OPEN_ADDR = 1
    CHAINING = 2

class LinkedListNode:
    def __init__(self, val, next=None):
        self.hash = None
        self.key = val
        self.val = val
        self.next = next

class HashTableDictionary:
    def __init__(self, size=1000, collision=CollisionTypes.OPEN_ADDR):
        self.size = size
        self.dictionary = [None] * self.size # NOTE: for open addressing, each of these are just the elements; for chaining, each of these are unordered linked lists. 
        self.collision = collision

    def _collision_resolution(self, k, v):
        if self.collision == CollisionTypes.OPEN_ADDR:
            pass
        elif self.collision == CollisionTypes.CHAINING:
            pass
        pass

    def search(self, k):
        pass
        
    def insert(self, k, v):
        pass

    def delete(self, x):
        pass
        
    def max(self):
        pass

    def min(self):
        pass

    def predecessor(self, x):
        pass

    def successor(self, x):
        pass
