class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        intervals.sort(key=lambda x: x[0])
        #output = []
        while i <= len(intervals)-2:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][0] <= intervals[i+1][1]:
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            elif intervals[i][0] > intervals[i+1][1]:
                intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
            else:
                i += 1
        return intervals
        