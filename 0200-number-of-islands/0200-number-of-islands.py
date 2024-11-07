class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        count = 0
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                return
            
            grid[x][y] = '0'
            
            for dx, dy in directions:
                dfs(x + dx, y + dy)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                    
        return count