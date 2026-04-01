class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if not heights or not heights[0]:
        #     return []
        nrow, ncol = len(heights), len(heights[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(r, c, vis):
            vis[r][c] = True
            for i, j in dirs:
                nr, nc = r+i, c+j
                if 0 <= nr < nrow and 0 <= nc < ncol and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, vis)
        
        pac = [[False]*ncol for _ in range(nrow)]
        atc = [[False]*ncol for _ in range(nrow)]

        for k in range(ncol):
            dfs(0, k, pac)
        for k in range(nrow):
            dfs(k, 0, pac)
        for k in range(ncol):
            dfs(nrow-1, k, atc)
        for k in range(nrow):
            dfs(k, ncol-1, atc)
        
        return [[r, s] for r in range(nrow) for s in range(ncol) if pac[r][s] and atc[r][s]]
