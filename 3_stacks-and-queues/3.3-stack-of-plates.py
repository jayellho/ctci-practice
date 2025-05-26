'''
3.3 Stack of Plates:
Imagine a (literal) stack of plates.
If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
import unittest

class SetOfStacks:
    def __init__(self, threshold=5):
        self.masterStack = []
        self.threshold = threshold

    def push(self, elem):
        # push to new stack if masterStack empty OR previous stack in masterStack is full.
        if not self.masterStack or len(self.masterStack[-1]) == self.threshold:
            newStack = [elem]
            self.masterStack.append(newStack)

        # push to current stack.
        else:
            self.masterStack[-1].append(elem)

    def pop(self):
        # illegal if masterStack is empty. or if last stack is empty (not removed).
        assert self.masterStack
        assert self.masterStack[-1]

        # pop, then delete if stack is empty after pop.
        res = self.masterStack[-1].pop()

        if not self.masterStack[-1]:
            self.masterStack.pop()
        
        return res


# thank you chatgpt for the tests lol.
class TestSetOfStacks(unittest.TestCase):
    def test_push_and_pop_single_stack(self):
        ss = SetOfStacks(threshold=3)
        ss.push(1); ss.push(2); ss.push(3)
        self.assertEqual(ss.pop(), 3)
        self.assertEqual(ss.pop(), 2)
        self.assertEqual(ss.pop(), 1)
        with self.assertRaises(AssertionError):
            ss.pop()

    def test_multiple_stacks_creation_and_pop(self):
        ss = SetOfStacks(threshold=2)
        for elem in ['a', 'b', 'c', 'd']:
            ss.push(elem)
        # internal structure check
        self.assertEqual(ss.masterStack, [['a', 'b'], ['c', 'd']])
        # full LIFO across stacks
        self.assertEqual(ss.pop(), 'd')
        self.assertEqual(ss.pop(), 'c')
        self.assertEqual(ss.pop(), 'b')
        self.assertEqual(ss.pop(), 'a')
        with self.assertRaises(AssertionError):
            ss.pop()

    def test_pop_empty_raises(self):
        ss = SetOfStacks()
        with self.assertRaises(AssertionError):
            ss.pop()

    def test_threshold_one(self):
        ss = SetOfStacks(threshold=1)
        ss.push(10); ss.push(20); ss.push(30)
        # every push creates a new sub-stack
        self.assertEqual(len(ss.masterStack), 3)
        self.assertEqual(ss.pop(), 30)
        self.assertEqual(ss.pop(), 20)
        self.assertEqual(ss.pop(), 10)
        with self.assertRaises(AssertionError):
            ss.pop()

if __name__ == '__main__':
    unittest.main()
