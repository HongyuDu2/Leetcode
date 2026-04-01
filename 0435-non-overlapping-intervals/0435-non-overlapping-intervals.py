class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        remove = 0
        begin = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < begin:
                remove += 1
            else:
                begin = intervals[i][1]
        return remove