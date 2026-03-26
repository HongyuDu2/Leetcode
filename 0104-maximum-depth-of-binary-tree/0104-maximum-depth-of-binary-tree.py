# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, height):
            if not node:
                return
            self.ans = max(self.ans, height)
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        dfs(root, 1)
        return self.ans
    
    # if root is None:
    #     return 0
    # return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
