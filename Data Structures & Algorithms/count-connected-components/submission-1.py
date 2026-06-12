class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgs = {}
        for [x,y] in edges:
            if x not in edgs: edgs[x] = []
            if y not in edgs: edgs[y] = []
            edgs[x].append(y)
            edgs[y].append(x)
        
        visited = set()
        def helper(i , prev):
            if i in visited: return
            visited.add(i)
            for j in edgs.get(i,[]):
                if j != prev:
                    helper(j , i)
        count = 0
        for i in range(n):
            if i not in visited:
                helper(i,-1)
                count+=1
        return count
