import heapq
from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Min-heap to track end times
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)

        return len(heap)
