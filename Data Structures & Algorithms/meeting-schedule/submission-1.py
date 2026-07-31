class Solution:
    def canAttendMeetings(self, intervals: List['Interval']) -> bool:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x.start)

        # Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        
        return True
