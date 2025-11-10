class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if board[r][c] != word[k]:
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r-1, c, k+1) or
                dfs(r+1, c, k+1) or
                dfs(r, c+1, k+1) or
                dfs(r, c-1, k+1)
            )

            board[r][c] = tmp
            return found

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False