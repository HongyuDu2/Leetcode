class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        pre = {0:1}
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in pre:
                count += pre[target]
            if current_sum in pre:
                pre[current_sum] += 1
            else:
                pre[current_sum] = 1
        return count