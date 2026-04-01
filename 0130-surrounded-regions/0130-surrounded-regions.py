class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if not board or not board[0]:
        #     return
        
        n, c = len(board), len(board[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= c or board[i][j] != "O":
                return
            board[i][j] = "S"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(n):
            dfs(i,0)
            dfs(i,c-1)
        for i in range(c):
            dfs(0,i)
            dfs(n-1,i)
        for i in range(n):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
        return board

                