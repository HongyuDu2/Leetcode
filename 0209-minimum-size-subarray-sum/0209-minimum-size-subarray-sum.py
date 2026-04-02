class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                min_len = min(min_len, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
