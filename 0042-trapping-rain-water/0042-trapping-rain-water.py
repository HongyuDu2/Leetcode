class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0
        n = len(height)
        left_height = [0]*n
        right_height = [0]*n

        left_height[0] = height[0]
        for i in range(1, n):
            left_height[i] = max(left_height[i-1], height[i])
        
        right_height[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_height[i] = max(right_height[i+1], height[i])
        
        res = 0
        for i in range(0, n):
            res += min(left_height[i], right_height[i]) - height[i]
        return res