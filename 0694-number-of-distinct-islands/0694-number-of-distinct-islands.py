class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        def dfs(i,j,direction):
            if i<0 or j<0 or i>=nrow or j>=ncol or grid[i][j] ==0:
                return ""
            grid[i][j] = 0
            path = direction
            path += dfs(i+1,j,'D')
            path += dfs(i-1,j,'U')
            path += dfs(i,j+1,'L')
            path += dfs(i,j-1,'R')
            path += 'B'
            return path
        shape = set()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    shape.add(dfs(i,j,'S'))
        return len(shape)