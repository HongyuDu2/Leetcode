class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        for key in nums:
            if key in set:
                return True
            else:
                set[key] = 1
        return False