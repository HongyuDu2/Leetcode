class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            if nums[i] != i+1:
                return False
        if nums[n-1] == n-1:
            return True
        else:
            return False