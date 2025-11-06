class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in cache:
                return [cache[num2], i]
            cache[num1] = i
        return []