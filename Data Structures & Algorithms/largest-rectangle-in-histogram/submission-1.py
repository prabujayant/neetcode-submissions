from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n + 1):  # Include a dummy bar at the end
            curr_height = 0 if i == n else heights[i]

            # Pop bars while the current bar is shorter than the bar at stack top
            while stack and curr_height < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]

                # Width is current index if stack is empty, else between current and new top
                width = i if not stack else i - stack[-1] - 1

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
