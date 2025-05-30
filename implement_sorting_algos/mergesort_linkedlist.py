# define linked list node.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



def mergeSort(node):
    # base case - if None or single node.
    if not node or not node.next:
        return node

    # get mid pointer.
    mid = node
    fast = node.next

    while fast and fast.next:
        mid = mid.next
        fast = fast.next.next
    right_head = mid.next # save mid.next before we set it to None. this will be the right sublist.
    mid.next = None # set the left sublist to be half.
    
    # recursive mergeSort calls.
    l1 = mergeSort(node)
    l2 = mergeSort(right_head)
    return merge(l1, l2)

def merge(l1, l2): # each list has to be sorted.
    newNode = Node(0) # dummy node
    ptr = newNode

    while l1 or l2:
        if not l1:
            ptr.next = l2
            l2 = l2.next

        elif not l2:
            ptr.next = l1
            l1 = l1.next
        else:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next

        ptr = ptr.next
    
    return newNode.next

def printList(node):

    print(f"linked list: ")
    while node:
        print(node.val, end=" ")
        node = node.next
    print("\n")


l1 = Node(7, next=Node(5, next=Node(7, next=Node(1, next=Node(6)))))
printList(mergeSort(l1))


l1 = Node(1, next=Node(5, next=Node(7, next=Node(1, next=Node(1)))))
printList(mergeSort(l1))
