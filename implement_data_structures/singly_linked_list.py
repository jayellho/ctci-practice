# NOTE: This implementation matches by the first value of each node.

from __future__ import annotations

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):

        self.head = None


    def search(self, x: Node) -> Node:

        ptr = self.head
        while ptr:
            if ptr.val == x.val:
                return ptr
            ptr = ptr.next
        return None
            

    def insert(self,x: Node) -> None:

        if not x:
            print(f"Please insert a Node() object.")
            return
        # insert to front of list.
        ptr = x

        # in case node is not a node by itself, forward pointer to the end.
        while x.next:
            x = x.next
        
        x.next = self.head
        self.head = ptr

    def _get_pred(self, x: Node):
        ptr = self.head

        while ptr and ptr.next:
            if ptr.next.val == x.val:
                return ptr
            ptr = ptr.next
        
        return None


    def delete(self, x: Node):
        if not self.head:
            return

        pred = self._get_pred(x)
        
        if not pred:
            if self.head.val == x.val:
                self.head = self.head.next
        else:
            pred.next = pred.next.next




# driver code.
if __name__ == "__main__":

    my_list = SinglyLinkedList()

    my_list.insert(Node(1))
    my_list.insert(Node(3))
    my_list.insert(Node(2))

    print(f"search and found: {my_list.search(Node(1)).val}")
    my_list.delete(Node(2))

    ptr = my_list.head

    while ptr:
        print(ptr.val)
        ptr = ptr.next