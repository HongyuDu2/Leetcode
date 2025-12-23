class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0]*n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        matrix[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    if i > 0:
                        matrix[i][j] += matrix[i-1][j]
                    if j > 0:
                        matrix[i][j] += matrix[i][j-1]
        return matrix[m-1][n-1]