class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0
        num_set = set(nums)
        total = 0
        for num in num_set:
            if num -1 not in num_set:
                count = 1
                start = num
                while start + 1 in num_set:
                    count += 1
                    start += 1
                total = max(total, count)
        return total