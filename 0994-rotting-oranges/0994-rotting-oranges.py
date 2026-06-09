class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, c = len(grid), len(grid[0])
        total = 0
        for i in range(n):
            for j in range(c):
                if grid[i][j] == 1:
                    total += 1
        
        time = 0
        while time >= 0:
            rotten = [(i, j) for i in range(n) for j in range(c) if grid[i][j] == 2]
            total_b = total
            for i in range(n):
                for j in range(c):
                    if grid[i][j] == 2 and (i, j) in rotten:
                        if 0 <= i - 1 and grid[i-1][j] == 1:
                            grid[i-1][j] = 2
                            total -= 1
                        if 0 <= j - 1 and grid[i][j-1] == 1:
                            grid[i][j-1] = 2
                            total -= 1
                        if n > i + 1 and grid[i+1][j] == 1:
                            grid[i+1][j] = 2
                            total -= 1
                        if c > j + 1 and grid[i][j+1] == 1:
                            grid[i][j+1] = 2
                            total -= 1
            if total == total_b:
                return -1 if total > 0 else time
            time += 1
            if total == 0:
                return time
            

