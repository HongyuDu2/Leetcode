class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = 0
        dp2 = 0
        for i in range(0, len(nums)):
            cur = max(dp1, dp2 + nums[i])
            dp2 = dp1
            dp1 = cur
        return cur