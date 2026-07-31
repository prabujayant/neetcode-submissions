class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        # Build adjacency list and sort destinations
        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()
        
        result = []
        
        def dfs(node):
            while graph[node]:
                next_dest = graph[node].pop(0)
                dfs(next_dest)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]