class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        total = 0
        for i in range(n):
            curr = min(height[left], height[right])*(right-left)
            total = max(curr, total)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return total
