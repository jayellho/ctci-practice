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

    def push(self, elem):
        # check min
        if not self.stack:
            self.stack.append((elem, elem))
        else:
            if self.stack[-1][1] > elem:
                self.stack.append((elem, elem))
            else:
                self.stack.append((elem, self.stack[-1][1]))

    def pop(self):
        assert self.stack
        return self.stack.pop()[0]

    def min(self):
        assert self.stack

        return self.stack[-1][1]

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

    
