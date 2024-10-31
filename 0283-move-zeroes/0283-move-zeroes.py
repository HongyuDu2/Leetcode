class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = '&'
                k = k + 1
        
        #nums = [item for item in nums if item != '&']
        while '&' in nums:
            nums.remove('&')
        nums.extend([0] * k)

        return nums