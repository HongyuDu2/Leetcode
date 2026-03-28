class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        set = {}
        for i, num in enumerate(s):
            set[num] = i
        res = []
        start = 0
        end = 0
        for i, num  in enumerate(s):
            end = max(end, set[num])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res