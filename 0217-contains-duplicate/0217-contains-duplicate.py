class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        for key in nums:
            if key not in set:
                set[key] = 1
            else:
                return True
        return False