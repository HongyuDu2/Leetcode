class Solution:
    def maxProduct(self, nums) -> int:
        # if not nums:
        #     return 0
        res = max_so_far = min_so_far = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            test_max = max(curr, max_so_far*curr, min_so_far*curr)
            test_min = min(curr, max_so_far*curr, min_so_far*curr)
            max_so_far = test_max
            min_so_far = test_min
            res = max(res, max_so_far)
        return res


