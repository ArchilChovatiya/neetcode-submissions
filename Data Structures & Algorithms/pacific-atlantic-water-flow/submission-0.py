class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n , m = len(heights) , len(heights[0])
        
        def dfs(i , j , visited , prevHeight):
            if i < 0 or j < 0 or i >=n or j >=m or (i , j ) in visited: return
            if prevHeight <= heights[i][j]:
                visited.add((i, j))
                dfs(i+1 , j, visited, heights[i][j]) 
                dfs(i , j+1, visited, heights[i][j]) 
                dfs(i-1 , j, visited, heights[i][j]) 
                dfs(i , j-1, visited, heights[i][j])
        pacific  = set()
        for i in range(n):
            dfs(i, 0 ,pacific, 0)
        for j in range(m):
            dfs(0, j , pacific, 0)
        atlantic = set()
        for i in range(n):
            dfs(i, m-1 , atlantic, 0)
        for j in range(m):
            dfs(n-1, j , atlantic, 0)

        res = []
        for block in pacific:
            if block in atlantic:
                res.append(block)
        return res