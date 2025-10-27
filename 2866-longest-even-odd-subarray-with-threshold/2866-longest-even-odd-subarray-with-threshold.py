class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            if sum == 0:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    sum = 1
            else:
                if nums[i] <= threshold and nums[i-1] % 2 != nums[i] % 2:
                    sum += 1
                else:
                    max_len = max(max_len, sum)
                    if nums[i] % 2 == 0 and nums[i] <= threshold:
                        sum = 1
                    else:
                        sum = 0
        max_len = max(max_len, sum)
        return max_len


