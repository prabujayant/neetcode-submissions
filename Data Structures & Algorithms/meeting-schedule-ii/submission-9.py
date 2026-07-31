import heapq
from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Time:  O(n log n)  (sort + heap ops)
        Space: O(n)        (heap of end times)
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []

        for it in intervals:
            if heap and heap[0] <= it.start:
                heapq.heappop(heap)
            heapq.heappush(heap, it.end)

        return len(heap)
