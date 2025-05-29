'''
3.6 Animal Shelter:
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. 
You may use the built-in Linked list data structure.
'''

'''
- use 2 separate linked lists - one for cat and one for dog.
- for enqueue, append to whichever animal's linked list.
- for dequeue any, check timestamp for head and pick the earlier one.
- for dequeue dog and dequeue cat, pick the head.
- how to track?
    - each animal will be (<timestamp>, <identity>, <animal_type>)
- timestamp will be global.

'''


# helper functions and classes.
class Node:
    def __init__(self, val, next=None):
        self.val = val # assume (<identifier>, <animal type>, <dequeuedBool>)
        self.next = next

# main function.
class AnimalShelter:
    def __init__(self):
        self.headCat = self.tailCat = None
        self.headDog = self.tailDog = None
        self.timestamp = 0


    def enqueue(self, x): # val of x will look like [<timestamp>, (<identity>, <animal_type>)]

        self.timestamp += 1
        newNode = Node([self.timestamp, x])
        # CATS
        if newNode.val[1][1] == 'cat':
            # if cat is empty.
            if not self.headCat and not self.tailCat:
                self.headCat = self.tailCat = newNode
            # else, expand current linked list.
            else:
                self.tailCat.next = newNode
                self.tailCat = self.tailCat.next

        # DOGS
        else:
            # if dog is empty.
            if not self.headDog and not self.tailDog:
                self.headDog = self.tailDog = newNode
            # else, expand current linked list.
            else:
                self.tailDog.next = newNode
                self.tailDog = self.tailDog.next
        self.printQueue()

    def dequeueAny(self):
        # edge case: both cat and dog are empty.
        if not self.headCat and not self.headDog:
            return None
        
        # dequeue the head with the earlier timestamp.
        if not self.headCat or (self.headCat and self.headDog and self.headCat.val[0] > self.headDog.val[0]):
            # pick the dog, and move pointer ahead.
            res = self.headDog
            self.headDog = self.headDog.next

        else:
            res = self.headCat
            self.headCat = self.headCat.next
        print(f"dequeued a {res.val[1]}")
        # self.printQueue()    
        return res
    


    def dequeueDog(self):
        # edge case: dog is empty.
        if not self.headDog:
            return None
        
        # return current, and move pointer to next.
        res = self.headDog
        self.headDog = self.headDog.next
        print(f"dequeued a {res.val[1]}")
        # self.printQueue()
        return res

        

    def dequeueCat(self):
        # edge case: cat is empty.
        if not self.headCat:
            return None
        
        # return current, and move to next pointer.
        res = self.headCat
        self.headCat = self.headCat.next
        print(f"\ndequeued a {res.val[1]}")
        # self.printQueue()
        return res


    def printQueue(self):
        currCat = self.headCat
        currDog = self.headDog

        print("curr Cat = ", end = " ")
        while currCat:
            print(currCat.val, end = " ")
            currCat = currCat.next
        print("\n")
        print("curr Dog = ")
        while currDog:
            print(currDog.val, end = " ")
            currDog = currDog.next
        print("\n")


# test cases:
def testDriver(testList, expectedAns):
    test = AnimalShelter()
    result = []
    for i in testList:
        if i == "dqa":
            tmp = test.dequeueAny()
            result.append(tmp.val[1][0] if tmp else None)
        elif i == "dqc":
            tmp = test.dequeueCat()
            result.append(tmp.val[1][0] if tmp else None)
        elif i == "dqd":
            tmp = test.dequeueDog()
            result.append(tmp.val[1][0] if tmp else None)
        else:
            test.enqueue(i)
    print(result)
    
    n = len(expectedAns)
    for j in range(n):
        assert expectedAns[j] == result[j]

# 1 - build interleaving dogs and cats. remove legally and check what was removed.
## build.
testList = [
            (12, 'cat'), 
            (13, 'dog'), 
            (14, 'cat'), 
            (15, 'dog'), 
            (16, 'cat'), 
            (17, 'dog'),
            "dqa", # 12
            "dqc", # 14
            "dqd", # 13
            "dqc", # 16
            "dqa", # 15
            (18, 'dog'),
            (19, 'dog'),
            "dqa",
            "dqa"
            ]
expectedAns = [12, 14, 13, 16, 15, 17, 18]
testDriver(testList, expectedAns)

# 2 - build cats then dogs. remove legally and check what was removed.
testList = [
            (12, 'cat'), 
            (13, 'cat'), 
            (14, 'cat'), 
            (15, 'dog'), 
            (16, 'dog'), 
            (17, 'dog'),
            "dqa", # 12
            "dqc", # 13
            "dqd", # 15
            "dqc", # 14
            "dqa", # 16
            (18, 'dog'),
            (19, 'dog'),
            "dqa", # 17
            "dqa" # 18
            ]
expectedAns = [12, 13, 15, 14, 16, 17, 18]
testDriver(testList, expectedAns)

# 3 - build cats. try to remove dogs.
testList = [
            (12, 'cat'), 
            (13, 'cat'), 
            (14, 'cat'), 
            "dqd",
            "dqd"
            ]
expectedAns = [None, None]
testDriver(testList, expectedAns)

# 4 - build dogs. try to remove cats.
testList = [
            (12, 'dog'), 
            (13, 'dog'), 
            (14, 'dog'), 
            "dqc",
            ]
expectedAns = [None]
testDriver(testList, expectedAns)


# 6 - empty list. remove dog.
testList = [
            "dqd",
            ]
expectedAns = [None]
testDriver(testList, expectedAns)

# 7 - empty list. remove cat.
testList = [
            "dqc",
            ]
expectedAns = [None]
testDriver(testList, expectedAns)

print(f"All test cases passed!")
