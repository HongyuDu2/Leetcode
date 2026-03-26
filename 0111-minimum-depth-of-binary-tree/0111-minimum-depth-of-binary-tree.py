# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # return 1+min(
        #     self.minDepth(root.left), self.minDepth(root.right)
        # )
        if not root:
            return 0
        self.ans = float('inf')
        def dfs(node, height):
            if not node:
                return
            if not node.left and not node.right:
                self.ans = min(self.ans, height)
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        dfs(root, 1)
        return self.ans