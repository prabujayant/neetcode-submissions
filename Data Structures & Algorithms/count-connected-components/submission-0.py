class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count=0
        visited=set()

        def bfs(start):
            queue=deque([start])
            while queue:
                node=queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
                count+=1
        return count