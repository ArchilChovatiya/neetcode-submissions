class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))
        minHeap = [(0, k)]
        time = 0
        visited = set()
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            visited.add(v1)
            time = max(time, w1)
            for (w2, v2) in edges[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, v2))
        return time if len(visited) == n else -1