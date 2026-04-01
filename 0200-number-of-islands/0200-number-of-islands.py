class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0
        nrow, ncol = len(grid), len(grid[0])
        total = 0
        def dfs(r, c):
            if r<0 or c<0 or r >= nrow or c >= ncol or grid[r][c]=='0':
                return 0
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for i in range(0, nrow):
            for j in range(0, ncol):
                if grid[i][j] == '1':
                    total += 1
                    dfs(i, j)
        return total

