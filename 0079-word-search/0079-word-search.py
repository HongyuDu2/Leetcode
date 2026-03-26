class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow, ncol = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r<0 or c<0 or r>=nrow or c>=ncol or board[r][c] != word[k]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            test = (dfs(r-1,c,k+1) or dfs(r+1,c,k+1) or dfs(r,c-1,k+1) or dfs(r,c+1,k+1))
            board[r][c] = tmp
            return test
        
        for i in range(0, nrow):
            for j in range(0, ncol):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
                    
