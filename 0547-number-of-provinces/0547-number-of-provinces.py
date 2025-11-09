class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(isConnected, i, visited):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(isConnected, j, visited)
        count = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(isConnected, i, visited)
                count += 1
        return count