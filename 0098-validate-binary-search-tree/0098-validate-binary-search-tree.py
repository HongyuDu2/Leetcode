# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= low or val >= upper:
                return False
            if not helper(node.left, low, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)