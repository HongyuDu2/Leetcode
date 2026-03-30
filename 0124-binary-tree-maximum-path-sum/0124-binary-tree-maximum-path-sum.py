# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxval = float('-inf')
        def maxnode(node):
            if not node:
                return 0
            left_root = max(maxnode(node.left), 0)
            right_root = max(maxnode(node.right), 0)

            curr = node.val + left_root + right_root
            self.maxval = max(self.maxval, curr)
            return node.val + max(left_root, right_root)
        maxnode(root)
        return self.maxval
