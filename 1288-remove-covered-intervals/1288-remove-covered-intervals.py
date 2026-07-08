class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        count = 0
        prev_end = 0
        for i in range(0, len(intervals)):
            if intervals[i][1] > prev_end:
                count += 1
                prev_end = intervals[i][1]
        return count