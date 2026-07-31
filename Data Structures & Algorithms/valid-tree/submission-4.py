class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # build graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dfs to check connectivity
        visit = [0] * n

        def dfs(node):
            visit[node] = 1
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
        dfs(0)
        # check all visited
        return all(visit)

# O(N + E) time
# O(N + E) space
