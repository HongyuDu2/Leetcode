class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        output = [[0] * n for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                sum = 0
                for k1 in range(i-1, i+2):
                    for k2 in range(j-1, j+2):
                        if 0 <= k1 <= m-1 and 0 <= k2 <= n-1:
                            sum += board[k1][k2]
                sum -= board[i][j]
                if board[i][j] == 1:
                    if sum < 2:
                        output[i][j] = 0
                    elif sum == 2 or sum == 3:
                        output[i][j] = 1
                    else:
                        output[i][j] = 0
                else:
                    if sum == 3:
                        output[i][j] = 1
                    else:
                        output[i][j] = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = output[i][j]
        return board
