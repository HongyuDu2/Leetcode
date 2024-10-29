class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summit = 0
        n=len(nums)

        if n == 1:
            summit = 0
        elif nums[1] < nums[0]:
            summit = 0
        elif nums[n-1] > nums [n-2]:
            summit = n-1
        else:
            for i in range(0, len(nums)):
                if i > 0 and i < len(nums) - 1:  # 确保 i 不是第一个或最后一个元素
                    if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                        summit = i
                        break
        
        return summit

        