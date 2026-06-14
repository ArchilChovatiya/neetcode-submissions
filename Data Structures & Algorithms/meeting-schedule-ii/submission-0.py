"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end   = sorted([i.end   for i in intervals])
        c = res = 0
        i = j = 0 
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                i+=1
                c +=1
            else:
                j+=1
                c-=1
            res = max(res , c)
        return res
