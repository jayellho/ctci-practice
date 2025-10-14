class SinglyLinkedNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class DoublyLinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Queue with singly linked list.
class SingleLLQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        if not self.tail:
            self.tail = x
            self.head = x
        else:
            self.tail.next = x
            self.tail = self.tail.next
        

    def dequeue(self):
        # no items in queue.
        if not self.head:
            return

        ptr = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return ptr

    def print_q(self):
        curr = self.head

        while curr:
            print(curr.val)
            curr = curr.next

# Queue with doubly linked list - only has benefits if double-ended I think.
class DoubleLLQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        if not self.tail:
            self.tail = x
            self.head = x
        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = self.tail.next

    def appendleft(self, x):
        if not self.head:
            self.head = x
            self.tail = x
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x

    def pop(self):
        # no items in queue.
        if not self.tail:
            return
        ptr = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return ptr


    def popleft(self):
        # no items in queue.
        if not self.head:
            return

        ptr = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return ptr
    
    def print_q(self):
        curr = self.head

        while curr:
            print(curr.val)
            curr = curr.next



# driver code.
if __name__ == "__main__":
    # run queue implemented with single linked list.
# run queue implemented with single linked list.
    print("=== Single Linked List Queue ===")
    q = SingleLLQueue()
    q.enqueue(SinglyLinkedNode(1))
    q.enqueue(SinglyLinkedNode(2))
    q.enqueue(SinglyLinkedNode(3))
    q.print_q()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(SinglyLinkedNode(4))
    q.print_q()
    
    # run deque implemented with doubly linked list.
    print("\n=== Doubly Linked List Deque ===")
    dq = DoubleLLQueue()
    
    # Add to rear
    dq.append(DoublyLinkedNode(1))
    dq.append(DoublyLinkedNode(2))
    dq.append(DoublyLinkedNode(3))
    print("After appending 1, 2, 3:")
    dq.print_q()
    
    # Add to front
    dq.appendleft(DoublyLinkedNode(0))
    print("\nAfter appendleft(0):")
    dq.print_q()
    
    # Remove from rear
    removed = dq.pop()
    print(f"\nPopped from rear: {removed.val}")
    dq.print_q()
    
    # Remove from front
    removed = dq.popleft()
    print(f"\nPopped from front: {removed.val}")
    dq.print_q()
    
    # Mix operations
    dq.append(DoublyLinkedNode(5))
    dq.appendleft(DoublyLinkedNode(-1))
    print("\nAfter append(5) and appendleft(-1):")
    dq.print_q()