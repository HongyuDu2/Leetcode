class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        room = 0
        end_time = 0

        for num in start:
            if num >= end[end_time]:
                end_time += 1
            else:
                room += 1
        return room