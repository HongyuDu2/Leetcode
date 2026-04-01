class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dist = {}
        for i, x in enumerate(s):
            dist[x] = i
        res = []
        start = 0
        end = 0
        for i, x in enumerate(s):
            end = max(end, dist[x])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res