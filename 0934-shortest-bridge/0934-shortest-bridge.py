class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return
            q.append((i,j))
            grid[i][j] = 2
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        
        distance = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                r, l = q.popleft()
                for dr, dl in directions:
                    i, j = r+dr, l+dl
                    if 0<=i<n and 0<=j<n:
                        if grid[i][j] == 1:
                            return distance
                        if grid[i][j] == 0:
                            grid[i][j] = 2
                            q.append((i,j))
            distance += 1
        return distance


             