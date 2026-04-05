class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for s in nums:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        d1 = sorted(d.items(), key = lambda x : x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(d1[i][0])
        return res
