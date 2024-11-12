'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums) - 1
        while l >= 0:
            for i in range(l - 1, -1, -1):
                if i == 0 and nums[i] < len(nums[:l]) - 1:
                    return False
                elif nums[i] >= len(nums[:l]) - len(nums[:i]) and i > 0:
                    l = nums.index(nums[i])
                    break
                elif nums[i] >= len(nums[:l]) - len(nums[:i]) and i == 0:
                    return True
                else:
                    continue
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0  # 记录能到达的最远位置
        for i in range(len(nums)):
            # 如果当前位置超过能到达的最远位置，返回 False
            if i > farthest:
                return False
            # 更新最远可达位置
            farthest = max(farthest, i + nums[i])
            # 如果最远可达位置已经覆盖到最后一个索引，返回 True
            if farthest >= len(nums) - 1:
                return True
        # 如果循环结束后仍未到达最后一个位置，返回 False
        return False

        
        