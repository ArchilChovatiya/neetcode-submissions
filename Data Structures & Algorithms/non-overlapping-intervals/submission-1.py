class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        curr = intervals[0]
        removed = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curr[1]:
                curr = intervals[i]
            else:
                if curr[1] > intervals[i][1]:
                    curr = intervals[i]
                removed+=1
        return removed
