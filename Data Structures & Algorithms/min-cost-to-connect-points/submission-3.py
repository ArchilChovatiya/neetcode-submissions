class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        minHeap = [(0,points[0][0],points[0][1])] 
        visited = set()
        total = 0
        while minHeap:
            (dist, x1, y1) = heapq.heappop(minHeap)
            if (x1, y1) in visited:
                continue
            total += dist
            visited.add((x1,y1))
            points.remove([x1,y1])
            for (x2,y2) in points:
                if (x2,y2) not in visited:
                    heapq.heappush(minHeap,((abs(x1-x2)+abs(y1-y2), x2, y2)))
        return total