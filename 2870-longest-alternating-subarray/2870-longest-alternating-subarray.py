class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        index = 0
        sum = 1
        max_len = -1
        for i in range(len(nums)-1):
            if sum == 1:
                if nums[i+1] - nums[i] == 1:
                    index = 1
                    sum += 1
                    max_len = max(max_len, sum)
            else:
                if index == 1 and nums[i+1] - nums[i] == -1:
                    index = -1
                    sum += 1
                    max_len = max(max_len, sum)
                elif index == -1 and nums[i+1] - nums[i] == 1:
                    index = 1
                    sum += 1
                    max_len = max(max_len, sum)
                else:
                    if nums[i+1] - nums[i] == 1:
                        index = 1
                        sum = 2
                        max_len = max(max_len, sum)
                    else:
                        index = 0
                        sum = 1
        return max_len



