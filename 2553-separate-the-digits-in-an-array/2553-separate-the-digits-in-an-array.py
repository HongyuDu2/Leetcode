class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            s = str(nums[i])
            for ch in s:
                res.append(int(ch))
        return res