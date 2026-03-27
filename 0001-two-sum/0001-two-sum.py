class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        for i, pos in enumerate(nums):
            diff = target - pos
            if diff in set:
                return [set[diff], i]
            set[pos] = i
        

