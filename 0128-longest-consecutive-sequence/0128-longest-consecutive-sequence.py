class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        longres = 0
        for num in num_set:
            if num-1 not in num_set:
                start = num
                coun = 1

                while start+1 in num_set:
                    start += 1
                    coun += 1
                longres = max(longres, coun)
        return longres