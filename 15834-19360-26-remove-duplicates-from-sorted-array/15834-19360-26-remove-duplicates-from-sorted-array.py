class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            t = 0
            if nums[i] == nums[i-1]:
                t += 1
            if t == 0:
                nums[k] = nums[i]
                k += 1
        
        return k
             