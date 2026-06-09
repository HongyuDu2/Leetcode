class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            dp1, dp2 = nums[0], max(nums[1], nums[0])
            for i in range(2, n-1):
                dp1, dp2 = dp2, max(dp1 + nums[i], dp2)
            curr1 = dp2
            
            dp3, dp4 = nums[1], max(nums[2], nums[1])
            for i in range(3, n):
                dp3, dp4 = dp4, max(dp3 + nums[i], dp4)
            curr2 = dp4
        return max(curr1, curr2)
            