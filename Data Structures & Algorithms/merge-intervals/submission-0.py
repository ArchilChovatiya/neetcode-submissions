class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for [x,y] in intervals:
            if not res:
                res.append([x,y])

            last = res[-1]
            if x <= last[1]:
                res[-1] = [last[0],max(last[1],y)]
            else:
                res.append([x,y])
        return res      