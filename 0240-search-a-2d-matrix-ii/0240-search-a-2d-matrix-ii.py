class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][n-1] >= target:
                l, r = 0, n-1
                while l <= r:
                    mid = (l + r)//2
                    if matrix[i][mid] > target:
                        r -= 1
                    elif matrix[i][mid] < target:
                        l += 1
                    else:
                        return True
        return False