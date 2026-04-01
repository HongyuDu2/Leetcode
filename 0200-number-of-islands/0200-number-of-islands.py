class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0
        n, c = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= c or grid[i][j] == "0":
                return "0"
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        total = 0
        for i in range(n):
            for j in range(c):
                if grid[i][j] == '1':
                    total += 1
                    dfs(i, j)
        return total


