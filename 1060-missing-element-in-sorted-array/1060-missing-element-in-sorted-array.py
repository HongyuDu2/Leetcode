class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing_fun(i):
            return (nums[i] - nums[0]) -i
        n = len(nums)
        if k > missing_fun(n-1):
            return nums[n-1] + (k - missing_fun(n-1))
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if missing_fun(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left-1] + k - missing_fun(left-1)