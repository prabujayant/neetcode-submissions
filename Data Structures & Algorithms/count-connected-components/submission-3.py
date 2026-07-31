class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n

        def dfs(node):
            vis[node] = 1
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei)

        count = 0
        for i in range(n):
            if not vis[i]:
                count += 1
                dfs(i)

        return count

# O(N + E) time
# O(N + E) space
