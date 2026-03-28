class Solution:
    def jump(self, nums: List[int]) -> int:
        fast = 0
        end = 0
        jump = 0
        for i in range(len(nums)-1):
            fast = max(fast, i+ nums[i])
            if i == end:
                jump += 1
                end = fast
                if end > len(nums)-2:
                    break
        return jump


