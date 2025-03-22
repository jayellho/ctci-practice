'''
4.7 Build Order:
You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.
EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
'''

'''
- <independent> ==> <dependent> e.g. (a, d) means a is a prereq to d.

- not valid:
    - dependencies cannot be built.
    - cycles - e.g. a depends on d and d depends on a.
    -



Solution #1 : remove incoming edges

- build two dicts:
    - incoming = <node> : <num of incoming edges for that node>
    - outgoing = <node> : <nodes that rely on this node as a prereq>

- queue for what to process next
    - populate with difference between all nodes and set(incoming)

- while q:
    - pop from q, push into res.
    - find in outgoing dict and minus 1 in incoming dict
    - if 0 after minusing, append to q.

- if len(res) < len(projects): return error
- else: return res


Solution #2: dfs.
- build
'''
import collections

## SOLUTION 2 - DFS.

def buildOrder(projects_list, dependencies_list):

    # build adjacency list.
    adj_list = {}
    for fro, to in dependencies_list:
        if fro not in adj_list:
            adj_list[fro] = [to]
        else:
            adj_list[fro].append(to)
        
    # do dfs.
    # res = []
    partial_visited = set()
    fully_visited = set()
    def dfs(node, res):
        # print(f"partial_visited = {partial_visited}, fully_visited = {fully_visited}")
        if node in partial_visited:
            return False
        
        if node not in fully_visited:
            partial_visited.add(node)
            if node in adj_list:
                for child in adj_list[node]:
                    if not dfs(child, res):
                        return False
            fully_visited.add(node)
            partial_visited.remove(node)
            res.append(node)
        return True
        
    # print(res, partial_visited, fully_visited)
    res = []
    for i in projects_list:
        # if i not in fully_visited:
        dfs(i, res)
    
    res.reverse()
    print(res)
    return res if len(res) == len(projects_list) else "error"
    
        
# ## SOLUTION 1 - remove incoming edges etc.
# # define functions.
# def buildOrder(projects_list, dependencies_list):
#     # build incoming and outgoing dicts.
#     incoming = collections.defaultdict(int)
#     outgoing = collections.defaultdict(list)

#     for in_node, out_node in dependencies_list:
#         incoming[out_node] += 1
#         outgoing[in_node].append(out_node)
    
#     # build queue.
#     start = set(projects_list) - set(incoming.keys())
#     q = collections.deque(start)

#     # iterate.
#     res = []
#     while q:
#         curr = q.popleft()
#         res.append(curr)
        
#         for node in outgoing[curr]:
#             incoming[node] -= 1
            
#             if incoming[node] == 0:
#                 q.append(node)
#     return res if len(res) == len(projects_list) else "error"



# test cases.
## 1 - valid order possible.
projects_list = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies_list = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
res = buildOrder(projects_list, dependencies_list)
print(res)

## 2 - invalid order.
projects_list = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies_list = [('a', 'd'), ('d', 'a'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
res = buildOrder(projects_list, dependencies_list)
print(res)

