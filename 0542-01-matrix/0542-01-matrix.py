class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n =len(mat), len(mat[0])
        dist = [[-1]*n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dir:
                nr, nc = dr+r, dc+c
                if 0<=nr<m and 0<=nc<n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist 
