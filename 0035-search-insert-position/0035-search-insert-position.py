class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if i ==0 and nums[i] > target:
                return 0
            if i == len(nums)-1 and nums[i] < target:
                return len(nums)
            if nums[i] == target:
                return i
            if nums[i] < target and target < nums[i+1]:
                return i+1
            