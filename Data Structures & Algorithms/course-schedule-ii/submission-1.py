from collections import deque

class Solution:
    def findOrder(self, V: int, prerequisites: list[list[int]]) -> list[int]:
        # build graph
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        for u, v in prerequisites:   # u depends on v
            adj[v].append(u)
            indegree[u] += 1

        # queue for indegree 0
        q = deque([i for i in range(V) if indegree[i] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        # if topo sort has all nodes → valid order, else cycle → []
        return topo if len(topo) == V else []

# O(N + E) time 
# O(N + E) space
