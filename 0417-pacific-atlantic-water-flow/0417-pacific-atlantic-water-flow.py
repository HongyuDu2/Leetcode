class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if not heights or not heights[0]:
        #     return []
        nrow, ncol = len(heights), len(heights[0])
        dir = ([1,0],[-1,0],[0,1],[0,-1])
        def dfs(n, r, vis):
            vis[n][r] = True
            for i, j in dir:
                dn, dr = n+i, r+j
                if 0<=dn<nrow and 0<=dr<ncol and not vis[dn][dr] and heights[dn][dr]>=heights[n][r]:
                    dfs(dn,dr,vis)
        
        pac = [[False]*ncol for _ in range(nrow)]
        atc = [[False]*ncol for _ in range(nrow)]

        for i in range(nrow):
            dfs(i,0,pac)
        for i in range(ncol):
            dfs(0,i,pac)
        for i in range(nrow):
            dfs(i,ncol-1,atc)
        for i in range(ncol):
            dfs(nrow-1,i,atc)
        
        return [[r,s] for r in range(nrow) for s in range(ncol) if pac[r][s] == atc[r][s] == True]

