'''
4.1 Route Between Nodes:
Given a directed graph, design an algorithm  to find out whether there is a route between two nodes.
'''

'''
- run BFS or DFS from start node.
- DFS - might go through a lot of paths and get far away before getting the path between two nodes.
- BFS - we keep as close to the original node as possible, so would be better to find the path between two nodes.

'''
import collections

# code ==============================================================
def routeBetweenNodes(dir_graph: dict, start: int, end: int) -> bool:
    '''
    we want to find the path from a to b.
    dir_graph in the format: <source nodes> : [<dest_1, dest_2, ...>]
    assume that node values are unique.
    '''

    q = collections.deque()
    visited = set()

    q.append(start)
    
    while q:

        curr = q.popleft()
        print(f"curr = {curr}")
        if curr in dir_graph:
            for neighbor in dir_graph[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

                if neighbor == end:
                    print(f"result = {True}")
                    return True
    print(f"result = {False}")
    return False
        
            

# test cases ==============================================================

## 1 - path exists.
a, b = 1, 5
dir_graph = {
    1 : [3, 4],
    2 : [1, 3],
    4 : [3, 5],
}

routeBetweenNodes(dir_graph, a, b)

## 2 - path does not exist.
a, b = 2, 5
dir_graph = {
    1 : [3, 4],
    2 : [1, 3],
    4 : [3, 5],
}

routeBetweenNodes(dir_graph, a, b)








