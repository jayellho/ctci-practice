# Implementation of union-find by component size.
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n)) # assumption is that nodes are labelled from 0 to n-1.
        self.componentSize = [1] * n # initial component size is self.

    # find root of node x.
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
                
        self.parent[x] = self.find(self.parent[x]) # sets parent recursively until root.
        return self.parent[x]

    # merge two sets - the smaller set should be subsumed under the other.
    def union(self, s1: int, s2: int) -> bool:

        # check if same component.
        rootS1 = self.find(s1)
        rootS2 = self.find(s2)
        if rootS1 == rootS2:
            return False

        # set larger component to be parent of smaller. update component size.
        if self.componentSize[rootS1] >= self.componentSize[rootS2]:
            self.parent[rootS2] = rootS1
            self.componentSize[rootS1] += self.componentSize[rootS2]
        else:
            self.parent[rootS1] = rootS2
            self.componentSize[rootS2] += self.componentSize[rootS1]
        
        return True
            



