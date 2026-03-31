class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        def dfs(r, c, direction):
            if r<0 or c<0 or r>=nrow or c >= ncol or grid[r][c]==0:
                return ""
            grid[r][c] = 0
            path = direction
            path += dfs(r-1, c, "D")
            path += dfs(r+1, c, "U")
            path += dfs(r, c+1, "L")
            path += dfs(r, c-1, "R")
            path += 'B'
            return path
        shape = set()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    path = dfs(i,j,'S')
                    shape.add(path)
        return len(shape)