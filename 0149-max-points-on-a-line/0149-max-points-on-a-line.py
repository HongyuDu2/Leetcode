class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 2
        for i in range(n):
            slope_count = defaultdict(int)
            for j in range(i + 1, n):
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                if dy == 0:
                    slope = (0, 1)
                else:
                    g = gcd(abs(dy), abs(dx))
                    slope = (dy//g, dx//g)
                slope_count[slope] += 1
                ans = max(ans, slope_count[slope] + 1)
        return ans

        