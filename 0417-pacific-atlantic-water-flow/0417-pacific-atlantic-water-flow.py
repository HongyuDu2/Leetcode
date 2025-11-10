class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        R, C = len(heights), len(heights[0])
        dirs = ((0,-1), (0,1), (1,0), (-1,0))

        def dfs(r, c, vis):
            vis[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, vis)
        
        pac = [[False]*C for _ in range(R)]
        alt = [[False]*C for _ in range(R)]

        for c in range(C):
            dfs(0, c, pac)
        for r in range(R):
            dfs(r, 0, pac)
        for c in range(C):
            dfs(R-1, c, alt)
        for r in range(R):
            dfs(r, C-1, alt)
        
        return [[r,c] for r in range(R) for c in range(C) if pac[r][c] and alt[r][c]]