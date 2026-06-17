class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >=len(grid) or j >=len(grid[0]) or (i,j) in visited or grid[i][j]==0:
                return 0
            visited.add((i,j))
            return dfs(i, j+1) + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + 1


        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea,dfs(i,j))
        return maxArea