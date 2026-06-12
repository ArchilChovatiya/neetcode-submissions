class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        n , m  = len(grid), len(grid[0])
        def dfs(i , j):
            if i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited or grid[i][j]=="0":
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and(i,j) not in visited:
                    res+=1
                    dfs(i,j)
        return res

