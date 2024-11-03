'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def are_lists_equal(list1, list2):
            return Counter(list1) == Counter(list2)

        if nums == nums.sort(reverse=True):
            return nums.sort

        nums_str = ''.join(map(str, nums))
        nums_int = int(nums_str)

        while True:
            nums_int += 1
            nums_str = str(nums_str)
            if are_lists_equal(list(nums_str), nums):
                break
        
        return list(nums_str)
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the largest index i such that nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If such an index exists
            # Step 2: Find the largest index j greater than i such that nums[i] < nums[j]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap the value of nums[i] with that of nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the sequence from nums[i + 1] up to the last element
        nums[i + 1:] = reversed(nums[i + 1:])