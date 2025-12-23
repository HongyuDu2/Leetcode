class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        matrix2 = [[0]*n for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix2[i][j] = 1
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix2[i][j] == 1:
                    matrix[i] = [0]*n
                    for r in range(0, m):
                        matrix[r][j] = 0

        

        return matrix
