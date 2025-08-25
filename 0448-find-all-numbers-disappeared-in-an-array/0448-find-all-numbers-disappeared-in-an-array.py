class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            obs = abs(num) - 1
            if nums[obs] >0:
                nums[obs] = -nums[obs]
        return[i + 1 for i in range(len(nums)) if nums[i] > 0]