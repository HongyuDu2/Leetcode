class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        total_count = 0
        def dfs (r, s):
            if r < 0 or s < 0 or r >= nrow or s >= ncol or grid[r][s] == '0':
                return
            grid[r][s] = '0'
            dfs(r+1, s)
            dfs(r-1, s)
            dfs(r, s+1)
            dfs(r, s-1)
        for i in range(0, nrow):
            for j in range(0, ncol):
                if grid[i][j] == '1':
                    total_count += 1
                dfs(i, j)
        return total_count
