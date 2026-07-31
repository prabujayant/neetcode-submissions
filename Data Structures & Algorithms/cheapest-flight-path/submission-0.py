class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        minHeap = [(0, src, 0)]  # (total cost, current city, stops so far)
        
        while minHeap:
            cost, city, stops = heapq.heappop(minHeap)
            
            if city == dst:
                return cost
            
            if stops <= k:
                for nei, price in graph[city]:
                    heapq.heappush(minHeap, (cost + price, nei, stops + 1))
        
        return -1
