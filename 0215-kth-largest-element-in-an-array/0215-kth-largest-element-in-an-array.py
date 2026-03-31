import heapq
from typing import List



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot_val = random.choice(nums)
        large, medium, small = [], [], []
        for num in nums:
            if num > pivot_val:
                large.append(num)
            elif num < pivot_val:
                small.append(num)
            else:
                medium.append(num)
        if k <= len(large):
            return self.findKthLargest(large, k)
        if k > len(large) + len(medium):
            return self.findKthLargest(small, k-len(large)-len(medium))
        return pivot_val
