"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda x : x.start)
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr.end > intervals[i].start:
                return False
            curr = intervals[i]
        return True