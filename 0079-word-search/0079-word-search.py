class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])  # 获取行和列的数量

        def dfs(r, c, index):
            # 如果所有字符都匹配，则返回 True
            if index == len(word):
                return True
            # 边界条件和字符不匹配时返回 False
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False
            
            # 暂时标记当前单元格为已访问
            temp = board[r][c]
            board[r][c] = '#'
            
            # 递归探索四个方向
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # 恢复单元格的原始值
            board[r][c] = temp
            return found

        # 遍历每个单元格作为起始点
        for i in range(rows):
            for j in range(cols):
                # 如果找到匹配的路径则返回 True
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        # 如果没有找到匹配的路径则返回 False
        return False
        
        
        