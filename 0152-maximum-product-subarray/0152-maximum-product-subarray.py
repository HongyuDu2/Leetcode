class Solution:
    def maxProduct(self, nums) -> int:
        # if not nums:
        #     return 0
        res = max_so_far = min_so_far = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            tem_max = max(nums[i], nums[i]*max_so_far, nums[i]*min_so_far)
            tem_min = min(nums[i], nums[i]*max_so_far, nums[i]*min_so_far)
            max_so_far = tem_max
            min_so_far = tem_min
            res = max(res, max_so_far)
        return res
