import heapq
import collections
import unittest

# Given a set of directed, positive-weighted edges and nodes labelled from 1 to n, and a starting vertex s and a target vertex t: 
# Find the min cost path to reach t.

def dijkstra(n, s, t, edges):

    # build adjacency list.
    adj = collections.defaultdict(list)
    for src, dst, wt in edges:
        adj[src].append((wt, dst))

    # initial state.
    dist = [float('inf')] * (n + 1) # extra var to keep indices consistent with node labels.
    parent = [-1] * (n + 1) # for tracing path if needed.

    dist[s] = 0
    parent[s] = s

    heap = []
    heapq.heappush(heap, (0, s)) # (dist, u)

    # iterate.
    while heap:
        d, u = heapq.heappop(heap)

        # get outgoing edges if any.
        for wt, v in adj[u]:
            newDist = dist[u] + wt

            if newDist < dist[v]:
                dist[v] = newDist
                heapq.heappush(heap, (newDist, v))
                parent[v] = u

    # get path and also return dist if valid.
    if dist[t] != float('inf'):
        # get path by from s to t.
        curr = t
        path = []
        while True:
            path.append(curr)
            if curr == s:
                break
            curr = parent[curr]
        
        path = path[::-1]
        
        print(f"path from s to t: {path}")

        return dist[t], path
    return -1, []


# test suite generated from chatgpt.
# Define the test suite
class TestDijkstra(unittest.TestCase):

    def test_simple_triangle(self):
        cost, path = dijkstra(3, 1, 3, [(1, 2, 1), (2, 3, 1), (1, 3, 10)])
        self.assertEqual(cost, 2)
        self.assertEqual(path, [1, 2, 3])

    def test_unreachable(self):
        cost, path = dijkstra(4, 1, 4, [(1, 2, 1), (2, 3, 1)])
        self.assertEqual(cost, -1)
        self.assertEqual(path, [])

    def test_cycle(self):
        cost, path = dijkstra(3, 1, 3, [(1, 2, 2), (2, 3, 2), (3, 1, 2)])
        self.assertEqual(cost, 4)
        self.assertEqual(path, [1, 2, 3])

    def test_zero_weight(self):
        cost, path = dijkstra(3, 1, 3, [(1, 2, 0), (2, 3, 0)])
        self.assertEqual(cost, 0)
        self.assertEqual(path, [1, 2, 3])

    def test_multiple_edges(self):
        cost, path = dijkstra(2, 1, 2, [(1, 2, 10), (1, 2, 3)])
        self.assertEqual(cost, 3)
        self.assertEqual(path, [1, 2])

    def test_self_loop(self):
        cost, path = dijkstra(2, 1, 2, [(1, 1, 5), (1, 2, 1)])
        self.assertEqual(cost, 1)
        self.assertEqual(path, [1, 2])

    def test_start_equals_target(self):
        cost, path = dijkstra(3, 2, 2, [(1, 2, 1), (2, 3, 1)])
        self.assertEqual(cost, 0)
        self.assertEqual(path, [2])

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDijkstra))
