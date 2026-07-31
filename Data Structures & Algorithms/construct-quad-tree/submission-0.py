class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isSame(x0, y0, length):
            val = grid[x0][y0]
            for i in range(x0, x0 + length):
                for j in range(y0, y0 + length):
                    if grid[i][j] != val:
                        return False
            return True

        def build(x0, y0, length):
            if isSame(x0, y0, length):
                return Node(grid[x0][y0] == 1, True)
            half = length // 2
            return Node(True, False,
                        build(x0, y0, half),
                        build(x0, y0 + half, half),
                        build(x0 + half, y0, half),
                        build(x0 + half, y0 + half, half))

        return build(0, 0, len(grid))
