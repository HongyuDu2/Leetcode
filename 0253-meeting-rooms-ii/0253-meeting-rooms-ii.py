class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        max_val = 0
        curr = 0
        star = 0
        endd = 0

        while star < len(intervals):
            if starts[star] < ends[endd]:
                curr += 1
                star += 1
            else:
                curr -= 1
                endd += 1
            
            max_val = max(max_val, curr)
        return max_val