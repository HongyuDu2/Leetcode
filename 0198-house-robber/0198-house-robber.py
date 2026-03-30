class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp1 = 0
        dp2 = 0
        for x in nums:
            curr = max(dp1, dp2 + x)
            dp2 = dp1
            dp1 = curr
        return curr