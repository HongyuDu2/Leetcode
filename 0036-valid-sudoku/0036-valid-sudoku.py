class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])

        for i in range(0, m):
            list_test = []
            for j in range(0, n):
                if board[i][j] not in list_test and board[i][j] != ".":
                    list_test.append(board[i][j])
                elif board[i][j] in list_test:
                    return False
        
        for j in range(0, n):
            list_test = []
            for i in range(0, m):
                if board[i][j] not in list_test and board[i][j] != ".":
                    list_test.append(board[i][j])
                elif board[i][j] in list_test:
                    return False
        
        for k1 in range(0,3):
            for k2 in range(0,3):
                list_test = []
                for i in range(3*k1, 3*k1+3):
                    for j in range(3*k2, 3*k2+3):
                        if board[i][j] not in list_test and board[i][j] != ".":
                            list_test.append(board[i][j])
                        elif board[i][j] in list_test:
                            return False
        return True
