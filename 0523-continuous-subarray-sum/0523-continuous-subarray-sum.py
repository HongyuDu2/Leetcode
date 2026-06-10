class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # for length in range(2, n+1):
        #     for j in range(0, n-length+1):
        #         if sum(nums[j:j+length]) % k == 0:
        #             return True
        # return False

        reminder = {0:-1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            r = prefix % k
            if r in reminder:
                if i - reminder[r] >= 2:
                    return True
            else:
                reminder[r] = i
        return False