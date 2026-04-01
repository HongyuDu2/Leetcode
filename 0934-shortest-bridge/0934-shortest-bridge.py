class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()

        def dfs(r, c):
            grid[r][c] = 2
            q.append((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr <n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found: break
        
        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            distance += 1
        return distance