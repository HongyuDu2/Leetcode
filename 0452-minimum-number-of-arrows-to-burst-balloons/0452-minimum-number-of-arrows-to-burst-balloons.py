class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        num, arrow = 1, points[0][1]
        for i in range(1, len(points)):
            if arrow < points[i][0]:
                num += 1
                arrow = points[i][1]
        return num