class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        output = []
        for i in range(0, len(intervals)):
            if not output or output[-1][1] < intervals[i][0]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(intervals[i][1], output[-1][1])
        return output
