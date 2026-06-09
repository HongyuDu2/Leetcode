class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        target = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                target = max(target, count)
            else:
                count = 0
        return target
            
                 