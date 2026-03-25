class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        for i in range(0, len(nums)):
            if i > max_distance:
                return False
            max_distance = max(max_distance, i + nums[i])
            if max_distance >= len(nums) - 1:
                return True