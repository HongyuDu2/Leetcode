class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start_val = nums[i]
            while i +1 < n and nums[i+1] == nums[i] + 1:
                i += 1
            end_val = nums[i]
            if start_val == end_val:
                res.append(str(start_val))
            else:
                res.append(f"{start_val}->{end_val}")
            i += 1
        return res