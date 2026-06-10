class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminder = {0:1}
        total = 0
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            r = prefix % k
            if r in reminder:
                reminder[r] += 1
            else:
                reminder[r] = 1
        for value in reminder.values():
            if value >= 2:
                total += math.comb(value, 2)
        return total
