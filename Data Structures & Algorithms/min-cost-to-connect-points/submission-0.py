class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        minHeap = [(0, 0)]
        visited = set()
        total_cost = 0
        while minHeap and len(visited) < n:
            cost, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            for next_cost, v in adj[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (next_cost, v))
        return total_cost
