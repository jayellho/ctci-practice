'''
3.5 Sort Stack:
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
'''

'''
- unsortedStack, sortedStack
- while len of sorted < len of unsorted:
    # conditions to move from unsorted to sorted:
        - unsorted is not empty and (top of unsorted > top of sorted OR sorted is empty)
    
    # store top of unsorted in tmp

    # while sorted and top of sorted >  tmp, pop into unsorted

    # add tmp into sorted.


'''

def sortStack(unsortedStack):

    sortedStack = []

    n = len(unsortedStack)

    while len(sortedStack) < n:
        # print(f"unsorted = {unsortedStack}, sorted = {sortedStack}")

        # move unsorted to sorted
        while unsortedStack and (not sortedStack or unsortedStack[-1] > sortedStack[-1]):
            sortedStack.append(unsortedStack.pop())
        
        # store top of unsorted in tmp
        if unsortedStack:
            tmp = unsortedStack.pop()
        else:
            tmp = None
        
        # move sorted to unsorted
        while sortedStack and tmp and sortedStack[-1] > tmp:
            unsortedStack.append(sortedStack.pop())
        
        # append tmp on top of sorted.
        if tmp:
            sortedStack.append(tmp)

    return sortedStack


# test cases
unsorted = [2, 5, 3, 4, 1]
res = sortStack(unsorted)
print(res)

unsorted = [3, 1, 4, 2, 5]
res = sortStack(unsorted)
print(res)

unsorted = [6, 6, 1, 5, 2, 4, 3, 7]
res = sortStack(unsorted)
print(res)