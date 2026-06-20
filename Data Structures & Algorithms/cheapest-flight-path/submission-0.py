class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [sys.maxsize for i in range(n)]
        res[src] = 0
        for i in range(k+1):
            res_copy = res[:]
            for [u, v, cost] in flights:
                res_copy[v] = min(res_copy[v], res[u] + cost)
            res = res_copy[:]
        return res[dst] if res[dst]!=sys.maxsize else -1 
