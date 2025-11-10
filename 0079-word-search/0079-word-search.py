class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            # k: 当前要匹配的 word[k]
            if k == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if board[r][c] != word[k]:
                return False

            # 标记已访问（原地修改），避免重复使用同一格
            tmp = board[r][c]
            board[r][c] = "#"  # 任意占位符，表示已用

            found = (
                dfs(r-1, c, k+1) or
                dfs(r+1, c, k+1) or
                dfs(r, c-1, k+1) or
                dfs(r, c+1, k+1)
            )

            board[r][c] = tmp   # 回溯：恢复
            return found

        # 小剪枝：字符频次不满足直接失败
        from collections import Counter
        wc = Counter(word)
        bc = Counter(ch for row in board for ch in row)
        for ch, cnt in wc.items():
            if bc[ch] < cnt:
                return False

        # 再剪枝：如果首尾字符在全局里更稀少，倒序可降低分支（可选）
        # if bc[word[0]] > bc[word[-1]]:
        #     word = word[::-1]

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False