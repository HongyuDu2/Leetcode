# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (self.countFrom(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))
    def countFrom(self, node, target):
        if not node:
            return 0
        cnt = 1 if node.val == target else 0
        cnt += self.countFrom(node.left, target-node.val)
        cnt += self.countFrom(node.right, target-node.val)
        return cnt