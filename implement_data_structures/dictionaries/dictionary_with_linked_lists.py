# Implementation of dictionary with unsorted linked list.
# NOTE: Sorted linked lists have limited advantages as the underlying data structure since we can't really do binary search, hence not implemented.
class SinglyLinkedNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class DoublyLinkedNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class SingleLLDictionary:
    def __init__(self):
        self.head = None
        self.min_key = None
        self.max_key = None

    def search(self, k):
        ptr = self.head

        while ptr:
            if ptr.key == k:
                return ptr
            ptr = ptr.next
        return None

    def insert(self, k, v):
        to_insert = SinglyLinkedNode(k, v)
        to_insert.next = self.head
        self.head = to_insert
        
        # update min and/or max.
        if self.min_key is None or k < self.min_key:
            self.min_key = k
        if self.max_key is None or k > self.max_key:
            self.max_key = k  

    def _update_min_max(self):
        if not self.head:
            self.min_key = None
            self.max_key = None
            return
        
        self.min_key = self.head.key
        self.max_key = self.head.key
        ptr = self.head.next
        
        while ptr:
            if ptr.key < self.min_key:
                self.min_key = ptr.key
            if ptr.key > self.max_key:
                self.max_key = ptr.key
            ptr = ptr.next

    def delete(self, k):
        ptr = self.head

        if not ptr:
            return
        

        # special treatment if deleting head of list.
        if self.head.key == k:
            self.head = self.head.next
        else:
            while ptr.next:
                if ptr.next.key == k:
                    ptr.next = ptr.next.next
                    break
                ptr = ptr.next
            
        # update min or max.
        if self.min_key == k or self.max_key == k:
            self._update_min_max()
        
    def max(self):
        return self.max_key

    def min(self):
        return self.min_key

    def predecessor(self, k):
        pred_node = None
        ptr = self.head
        
        while ptr:
            if ptr.key < k:
                if pred_node is None or ptr.key > pred_node.key:
                    pred_node = ptr
            ptr = ptr.next
        
        return pred_node

    def successor(self, k):
        succ_node = None
        ptr = self.head
        
        while ptr:
            if ptr.key > k:
                if succ_node is None or ptr.key < succ_node.key:
                    succ_node = ptr
            ptr = ptr.next
        
        return succ_node
    
    def print_list(self):
        """Helper to visualize the list."""
        if not self.head:
            print("  List is empty")
            return
        
        ptr = self.head
        items = []
        while ptr:
            items.append(f"({ptr.key}: {ptr.val})")
            ptr = ptr.next
        
        print("  " + " -> ".join(items))
        print(f"  [Cached: min={self.min_key}, max={self.max_key}]")


# TODO: Implement doubly linked list version of dictionary.
class DoubleLLDictionary:
    pass

# Driver code.
if __name__ == "__main__":

    # For singly linked list implementation of dictionary.
    singlell_dict = SingleLLDictionary()
    singlell_dict.insert(5, "five")
    singlell_dict.insert(2, "two")
    singlell_dict.insert(8, "eight")
    singlell_dict.insert(1, "one")
    singlell_dict.insert(9, "nine")
    singlell_dict.insert(4, "four")

    singlell_dict.print_list()

    node = singlell_dict.search(8)
    if node:
        print(f"Search for key 8: Found! Value = {node.val}")
    singlell_dict.delete(5)
    singlell_dict.print_list()

    singlell_dict.delete(9)
    singlell_dict.print_list()

    # For doubly linked list implementation of dictionary.
    # TODO: Implement doubly linked list version of dictionary.
