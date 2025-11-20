# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # 交换当前节点左右子树
        root.left, root.right = root.right, root.left

        # 递归地反转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root