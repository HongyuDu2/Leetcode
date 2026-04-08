class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        total = 0
        for i in range(0, len(nums)-2):
            dp1 = nums[i]
            dp2 = nums[i+1]
            for j in range(i+2, len(nums)):
                if nums[j] - dp2 == dp2 - dp1:
                    total += 1
                    dp1 = dp2
                    dp2 = nums[j]
                else:
                    break
        return total