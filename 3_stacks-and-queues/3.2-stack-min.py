'''
3.2 Stack Min:
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
'''

'''
each element in stack has the minimum as at the stack.
<elem>, <current min>
minimum - just check if current element is smaller than the previous elem's min. if there is no prev elem, just set to current elem.
'''
class Stack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, elem):
        # push into minstack if elem is <= top of minstack.
        if not self.minstack or (self.minstack and elem <= self.minstack[-1]):
            self.minstack.append(elem)

        self.stack.append(elem)



    def pop(self):
        assert self.stack
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        
        return self.stack.pop()

    def min(self):
        assert self.stack

        return self.minstack[-1]

# test cases.
## 1
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(1)
stack.pop()
assert stack.min() == 1

## 2
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(1)
stack.pop()
assert stack.pop() == 2

## 3 - try to pop from empty stack.
stack = Stack()
try:
    stack.pop()
except AssertionError:
    pass


## 4
stack = Stack()
stack.push(2)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
assert stack.min() == 2

## 4
stack = Stack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
assert stack.min() == 1


## 5 - try to min from empty stack.
stack = Stack()
try:
    stack.min()
except AssertionError:
    pass