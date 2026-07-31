from typing import List
import heapq

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)

        # Min-heap to track meeting end times
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            # If the current meeting starts after the earliest meeting ends, reuse the room
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            
            # Add current meeting's end time
            heapq.heappush(heap, intervals[i].end)

        return len(heap)
