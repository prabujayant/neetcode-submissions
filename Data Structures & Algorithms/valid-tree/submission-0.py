class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=(n-1):
            return False

        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited=set()

        def dfs(node,prev):
            if node in visited:
                return 
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour==prev:
                    continue
                dfs(neighbour,node)

        dfs(0,-1)

        return len(visited)==n
