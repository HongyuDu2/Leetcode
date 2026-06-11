class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for cur in nums2:
            while stack and stack[-1] < cur:
                next_greater[stack.pop()] = cur
            stack.append(cur)
        res = []
        for x in nums1:
            res.append(next_greater.get(x, -1))
        return res