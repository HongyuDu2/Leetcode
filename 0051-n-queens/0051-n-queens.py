class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]

        cols = set()
        left_diag = set()
        right_diag = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (c+r) in left_diag or (r-c) in right_diag:
                    continue
                cols.add(c)
                left_diag.add(c+r)
                right_diag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                left_diag.remove(r+c)
                right_diag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res