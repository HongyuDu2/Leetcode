class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        set = {0:1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            target = curr_sum - k
            if target in set:
                count += set[target]
            if curr_sum in set:
                set[curr_sum] += 1
            else:
                set[curr_sum] = 1
        return count