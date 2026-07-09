class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        total = 0
        curr = 1
        l, r = 0, 0
        n = len(nums)
        while r <= n-1:
            curr = curr * nums[r]
            while curr >= k:
                curr = curr // nums[l]
                l += 1
            total += r - l + 1
            r += 1
        return total
            
