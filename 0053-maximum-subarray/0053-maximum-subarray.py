class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
    
        for num in nums[1:]:
        # 决定是“加入”还是“重启”
        # 如果 current_sum 是负数，max(num, negative + num) 会直接选择 num
            current_sum = max(num, current_sum + num)
        
        # 更新全局最大值
            max_sum = max(max_sum, current_sum)
        
        return max_sum