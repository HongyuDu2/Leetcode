class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        a = set()
        for i in range(0, len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
        
        b = sorted(a)

        res1 = 1
        res2 = 1
        for i in range(0, len(b)-1):
            if b[i+1] == b[i] + 1:
                res2 += 1
                if res1 < res2:
                    res1 = res2
            else:
                res2 = 1

        return res1