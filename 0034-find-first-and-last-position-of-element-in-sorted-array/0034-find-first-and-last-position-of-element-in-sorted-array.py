class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        if target not in nums_set:
            return [-1, -1]
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                l += 1
            else:
                r -= 1
        left = l

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] <= target:
                l += 1
            else:
                r -= 1
        right = r
        return [left, right]
    