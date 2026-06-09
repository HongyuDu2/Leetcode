class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            dp1 = nums[0]
            dp2 = max(nums[0], nums[1])
            for i in range(2, n):
                curr = max(dp1 + nums[i], dp2)
                dp1 = dp2
                dp2 = curr
        return curr