class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        max_height = grid[0][0]

        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            max_height = max(max_height, height)
            if r == n - 1 and c == n - 1:
                return max_height
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < n and 0 <= col < n and (row, col) not in visited:
                    visited.add((row, col))
                    heapq.heappush(minHeap, (grid[row][col], row, col))
        return -1
