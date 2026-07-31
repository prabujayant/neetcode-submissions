class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import collections, heapq

        # Build graph: node -> list of (neighbor, weight)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # Min-heap: (current_total_weight, node)
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue

            visited.add(n1)
            time = max(time, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return time if len(visited) == n else -1
