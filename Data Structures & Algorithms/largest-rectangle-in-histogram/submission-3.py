class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []        # stack stores indices of bars
        max_area = 0      # variable to track the maximum area

        # Add a zero at the end to flush out remaining bars in the stack
        for i, h in enumerate(heights + [0]):
            # While the current bar is smaller than the bar at the top of the stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # height of the bar to process
                # If the stack is empty, width is i (entire width up to i)
                # Else, width is distance between current index and index after popping
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)  # update max area if needed
            stack.append(i)  # push current index to stack

        return max_area

