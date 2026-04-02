class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for s in nums:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return[keys for keys,_ in sorted(d.items(), key=lambda x:x[1], reverse=True)[:k]]
