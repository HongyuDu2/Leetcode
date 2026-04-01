class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow, ncol = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i<0 or j<0 or i>=nrow or j>=ncol or board[i][j]!=word[k]:
                return False
            tmp=board[i][j]
            board[i][j] = "#"
            test = (dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1))
            board[i][j]=tmp
            return test
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
                    
