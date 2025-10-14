from __future__ import annotations
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert(self, x):
        if not self.head:
            self.head = x
        else:
            ptr = self.head
            self.head = x
            self.head.next = ptr
            ptr.prev = self.head

    def delete(self, x):
        found = self.search(x)

        if not found:
            return
        
        if found == self.head:
            self.head = found.next
            if self.head:
                self.head.prev = None
        else:
            if found.prev:
                found.prev.next = found.next
            if found.next:
                found.next.prev = found.prev
        

    def search(self, x):
        ptr = self.head
        while ptr:
            if ptr.val == x.val:
                return ptr
            ptr = ptr.next

        return None


if __name__=="__main__":
    double_ll = DoublyLinkedList()

    double_ll.insert(Node(1))
    double_ll.insert(Node(2))
    double_ll.insert(Node(3))
    double_ll.insert(Node(4))
    double_ll.insert(Node(5))

    double_ll.delete(Node(4))
    double_ll.delete(Node(5))

    # print forward.
    ptr = double_ll.head
    while ptr:
        print(ptr.val)
        ptr = ptr.next
    
    # print backwards.
    ptr = double_ll.head
    while ptr.next:
        ptr = ptr.next
    while ptr:
        print(ptr.val)
        ptr = ptr.prev
    
